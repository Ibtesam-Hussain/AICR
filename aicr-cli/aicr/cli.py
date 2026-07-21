"""
AICR command-line interface.

Usage:
    aicr review path/to/file.py
    aicr review path/to/file.py --adapter your-username/aicr-dpo-v2
    cat file.py | aicr review -
"""

import argparse
import sys
from pathlib import Path

from aicr.model import generate_review, ADAPTER_REPO


def _read_code(path_arg: str) -> str:
    if path_arg == "-":
        return sys.stdin.read()
    path = Path(path_arg)
    if not path.exists():
        print(f"Error: file not found: {path_arg}", file=sys.stderr)
        sys.exit(1)
    return path.read_text(encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        prog="aicr",
        description="AICR — review AI-generated code with a fine-tuned LLM.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    review_parser = subparsers.add_parser("review", help="Review a code file")
    review_parser.add_argument(
        "path", help="Path to the file to review, or '-' to read from stdin"
    )
    review_parser.add_argument(
        "--adapter", default=ADAPTER_REPO,
        help=f"HF Hub repo for the AICR adapter (default: {ADAPTER_REPO})",
    )
    review_parser.add_argument(
        "--max-tokens", type=int, default=400,
        help="Max tokens to generate for the review (default: 400)",
    )

    args = parser.parse_args()

    if args.command == "review":
        code = _read_code(args.path)
        if not code.strip():
            print("Error: no code to review (file/input is empty).", file=sys.stderr)
            sys.exit(1)

        print(f"\nReviewing {args.path}...\n")
        review = generate_review(code, adapter_repo=args.adapter, max_new_tokens=args.max_tokens)

        print("=" * 70)
        print("AICR REVIEW")
        print("=" * 70)
        print(review)
        print("=" * 70)


if __name__ == "__main__":
    main()