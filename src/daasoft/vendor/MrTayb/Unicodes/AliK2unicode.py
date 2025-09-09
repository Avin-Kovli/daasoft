def convert_kurdish_legacy_to_modern(legacy_text: str) -> str:

    legacy_to_modern_map = {
      
       
        "لاَ": "ڵا",  
        "لآ": "ڵا",  
        "لاً": "ڵا",   
        "لَ": "ڵ",   
        "لً": "ڵ",   
        "لأ": "ڵ",   
        "رِ": "ڕ",   
        "يَ": "ێ",   
        "ىَ": "ێ",   
        "وَ": "ۆ",   
        "ي": "ی",   
        "ى": "ی",   
        "ؤ": "ۆ",   
        "ذ": "ژ",   
        "ض": "چ",   
        "ط": "گ",   
        "ظ": "ڤ",   
        "ث": "پ",   
        "ة": "ه‌",   
    }

    modern_text = legacy_text

    for legacy_char, modern_char in legacy_to_modern_map.items():
        modern_text = modern_text.replace(legacy_char, modern_char)
        
    return modern_text

# --- Example Usage with new comprehensive test cases ---

legacy_unicode_text = """سلآو، ئةمة نموونةيةكى نويَية.
ئةو گولَة جوانة.
رِوَليَ خوَ ببينن.
منداألاني كوردستان جوانن.
"""

#converted_text = convert_kurdish_legacy_to_modern(legacy_unicode_text)

# # Print the results for comparison
# print("Original (Legacy Unicode):")
# print(legacy_unicode_text)
# print("-" * 70)
print("Converted (Modern Unicode)")
#print(converted_text)
print("-" * 70)
