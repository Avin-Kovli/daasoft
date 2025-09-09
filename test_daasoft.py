from daasoft import normalize_text, Words2Numbers, AliK2Unicode
s = "هاوڕێکان ــ و خاتوو"
print("Normalized:", normalize_text(s))
print("Words2Numbers('هەژدە') ->", Words2Numbers("هەژدە"))
