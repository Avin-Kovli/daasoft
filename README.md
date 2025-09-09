# DAAsoft

DAAsoft is a Kurdish Badinî text normalization library built around your `Normalization_Avin` code (provided by you).  
This package re-exports and wraps the original Avin modules (placed under `daasoft.vendor`) and exposes a friendly API similar to AsoSoft's structure.

## Quick install (local)
```bash
pip install -e path/to/DAAsoft
```

## Example
```python
from daasoft import normalize_text, Words2Numbers, AliK2Unicode

txt = "رامـــانیت ناڤێت کــوردی"
print(normalize_text(txt))

print(Words2Numbers("هەژدە"))
```

## Notes
- The original Avin modules are included in `daasoft.vendor` unmodified for provenance.
- This scaffold focuses on normalization; other modules (G2P, Transliteration, Sort) are intentionally not included so you can add them later.
