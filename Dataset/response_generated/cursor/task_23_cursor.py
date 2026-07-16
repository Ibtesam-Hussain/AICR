from collections import Counter
from typing import Any, List


def top_k_frequent(nums: List[Any], k: int) -> List[Any]:
    return [item for item, _ in Counter(nums).most_common(k)]
