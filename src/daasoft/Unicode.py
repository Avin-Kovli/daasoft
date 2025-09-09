# Simple module exposing the vendor Unicode converters
from .vendor.MrTayb.Unicodes import AliK2unicode, AliWeb2Unicode, Dylan2Unicode, Zarnegar2Unicode

# Provide consistent function names if vendor modules define functions or classes
def AliK2Unicode(text: str) -> str:
    if hasattr(AliK2unicode, 'convert'):
        return AliK2unicode.convert(text)
    try:
        return AliK2unicode(text)
    except Exception:
        return text

def AliWeb2Unicode(text: str) -> str:
    if hasattr(AliWeb2Unicode, 'convert'):
        return AliWeb2Unicode.convert(text)
    try:
        return AliWeb2Unicode(text)
    except Exception:
        return text

def Dylan2Unicode(text: str) -> str:
    if hasattr(Dylan2Unicode, 'convert'):
        return Dylan2Unicode.convert(text)
    try:
        return Dylan2Unicode(text)
    except Exception:
        return text

def Zarnegar2Unicode(text: str) -> str:
    if hasattr(Zarnegar2Unicode, 'convert'):
        return Zarnegar2Unicode.convert(text)
    try:
        return Zarnegar2Unicode(text)
    except Exception:
        return text
