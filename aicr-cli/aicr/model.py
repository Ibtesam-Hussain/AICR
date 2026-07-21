"""
Model loading for AICR.

Downloads the base model (Qwen2.5-Coder-3B-Instruct) and your fine-tuned
DPO adapter from the HuggingFace Hub, and loads them together in 4-bit
(QLoRA) for local inference. Everything runs on the user's own machine —
no server, no hosted API.
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

BASE_MODEL_NAME = "Qwen/Qwen2.5-Coder-3B-Instruct"

# Update this once you've pushed your adapter to the HF Hub, e.g.:
# "your-username/aicr-dpo-v2"
ADAPTER_REPO = "ibti101/aicr-v1"

SYSTEM_MESSAGE = (
    "You are a code reviewer. Follow this exact structure: "
    "1) Briefly validate what works (1-2 sentences), "
    "2) Use 'However' to transition to specific failures, "
    "3) Reference specific test cases (Test 3, Test 5, etc.), "
    "4) Provide concrete fixes. Do NOT provide generic code descriptions or explanations."
)

_model = None
_tokenizer = None


def load_model(adapter_repo: str = ADAPTER_REPO, use_gpu: bool = True):
    """Loads (and caches) the base model + AICR adapter. Downloads on first run,
    then uses the local HuggingFace cache on subsequent runs."""
    global _model, _tokenizer

    if _model is not None:
        return _model, _tokenizer

    print(f"Loading base model ({BASE_MODEL_NAME})...")

    quantization_kwargs = {}
    if use_gpu and torch.cuda.is_available():
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
        )
        quantization_kwargs = {"quantization_config": bnb_config, "device_map": "auto"}
    else:
        print("No GPU detected — running in CPU mode (slower).")
        quantization_kwargs = {"torch_dtype": torch.float32, "device_map": "cpu"}

    base_model = AutoModelForCausalLM.from_pretrained(BASE_MODEL_NAME, **quantization_kwargs)

    print(f"Loading AICR adapter ({adapter_repo})...")
    model = PeftModel.from_pretrained(base_model, adapter_repo)
    model.eval()

    tokenizer = AutoTokenizer.from_pretrained(adapter_repo)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    _model, _tokenizer = model, tokenizer
    return model, tokenizer


def generate_review(code: str, adapter_repo: str = ADAPTER_REPO, max_new_tokens: int = 400) -> str:
    """Runs AICR's fine-tuned review on a snippet of code. The system message
    is a hard requirement for this model — do not omit it."""
    model, tokenizer = load_model(adapter_repo)

    prompt_text = f"Review this code:\n\n{code}"
    messages = [
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": prompt_text},
    ]
    input_text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated = output_ids[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(generated, skip_special_tokens=True)