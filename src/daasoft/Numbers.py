# DAAsoft Numbers wrapper around Avin's NumbersAvin
from .vendor import NumbersAvin

def Words2Numbers(text: str):
    """Convert Kurdish Badinî number words to integer (wrapper)."""
    if hasattr(NumbersAvin, 'Words2Numbers'):
        return NumbersAvin.Words2Numbers(text)
    # fallback simple attempt
    try:
        return int(text)
    except Exception:
        raise ValueError("Unable to convert to number: " + repr(text))

def Numbers2Words(n: int) -> str:
    """If the vendor exposes a numbers->words function, wrap it; otherwise simple English fallback."""
    if hasattr(NumbersAvin, 'Numbers2Words'):
        return NumbersAvin.Numbers2Words(n)
    # very simple fallback (not localized)
    return str(n)
