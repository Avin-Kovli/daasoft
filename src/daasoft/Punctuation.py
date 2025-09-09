# Thin wrapper for punctuation normalizer
from .vendor.MrTayb import Punctuations

def normalize_multiline_text(text: str) -> str:
    if hasattr(Punctuations, 'NormalizePunctuations'):
        return Punctuations.NormalizePunctuations(text)
    if hasattr(Punctuations, 'normalize'):
        return Punctuations.normalize(text)
    # default fallback: strip extra spaces
    import regex as re
    return re.sub(r'[ \t\u00A0]+', ' ', text).strip()
