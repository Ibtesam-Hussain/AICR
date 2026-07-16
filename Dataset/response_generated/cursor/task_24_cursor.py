def parse_price(price: str) -> float:
    cleaned = price.replace("$", "").replace(",", "").strip()
    return float(cleaned)
