# DAAsoft Normalize wrapper - integrates Avin's normalization modules
# This file wraps vendor code in a friendly API for the package.
from .vendor import NumbersAvin, boldR_and_Tatweel
from .vendor.MrTayb import Punctuations, Unicodes
import regex as re

# Expose key functions from vendor pieces with normalized names
# 1) Unicode conversion utilities (from Unicodes/*)
def convert_alik_to_unicode(text: str) -> str:
    """Convert AliK legacy fonts to modern Unicode using vendor converter if available."""
    try:
        return Unicodes.AliK2unicode.convert(text)
    except Exception:
        # fallback: try function names commonly used (AliK2Unicode)
        if hasattr(Unicodes, 'AliK2Unicode'):
            return Unicodes.AliK2Unicode(text)
        return text

def convert_aliweb_to_unicode(text: str) -> str:
    try:
        return Unicodes.AliWeb2Unicode.convert(text)
    except Exception:
        if hasattr(Unicodes, 'AliWeb2Unicode'):
            return Unicodes.AliWeb2Unicode(text)
        return text

def convert_dylan_to_unicode(text: str) -> str:
    try:
        return Unicodes.Dylan2Unicode.convert(text)
    except Exception:
        if hasattr(Unicodes, 'Dylan2Unicode'):
            return Unicodes.Dylan2Unicode(text)
        return text

def convert_zarnegar_to_unicode(text: str) -> str:
    try:
        return Unicodes.Zarnegar2Unicode.convert(text)
    except Exception:
        if hasattr(Unicodes, 'Zarnegar2Unicode'):
            return Unicodes.Zarnegar2Unicode(text)
        return text

# 2) Bold-R and Tatweel (from boldR_and_Tatweel)
def fix_bold_r(text: str) -> str:
    """Apply bold-R fixes from vendor code (if function exists)."""
    if hasattr(boldR_and_Tatweel, 'startWithBoldR'):
        return boldR_and_Tatweel.startWithBoldR(text)
    if hasattr(boldR_and_Tatweel, 'fix_bold_r'):
        return boldR_and_Tatweel.fix_bold_r(text)
    return text

def remove_tatweel(text: str) -> str:
    if hasattr(boldR_and_Tatweel, 'removeTatweel'):
        return boldR_and_Tatweel.removeTatweel(text)
    if hasattr(boldR_and_Tatweel, 'remove_tatweel'):
        return boldR_and_Tatweel.remove_tatweel(text)
    # generic tatweel removal:
    return re.sub(r'ـ+', '', text)

# 3) Punctuation normalization (from MrTayb.Punctuations)
def normalize_punctuations(text: str) -> str:
    try:
        if hasattr(Punctuations, 'NormalizePunctuations'):
            return Punctuations.NormalizePunctuations(text)
        elif hasattr(Punctuations, 'normalize_punctuation'):
            return Punctuations.normalize_punctuation(text)
    except Exception:
        pass
    # fallback: collapse multiple punctuation marks and normalize spaces
    text = re.sub(r'[؟?]{2,}', '؟', text)
    text = re.sub(r'[.!]{2,}', '.', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# High-level pipeline
def normalize_text(text: str) -> str:
    x = text
    # Use unicode converters if text looks like legacy encodings (heuristic: many non-standard chars)
    # We'll attempt all four converters gracefully.
    for conv in (convert_alik_to_unicode, convert_aliweb_to_unicode, convert_dylan_to_unicode, convert_zarnegar_to_unicode):
        try:
            new = conv(x)
            if new and new != x:
                x = new
        except Exception:
            continue
    x = fix_bold_r(x)
    x = remove_tatweel(x)
    x = normalize_punctuations(x)
    # final whitespace normalization
    x = re.sub(r'[\u200B\u200C\u200D\uFEFF]+', '', x)
    x = re.sub(r'[ \t\u00A0]+', ' ', x).strip()
    return x
