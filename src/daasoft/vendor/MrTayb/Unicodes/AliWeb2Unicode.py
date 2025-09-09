def convert_aliweb_to_unicode(legacy_text: str) -> str:

    temp_placeholder = "§"  
    modern_text = legacy_text.replace("ط", temp_placeholder)  # Step 1: ط -> §
    modern_text = modern_text.replace("گ", "ط")             # Step 2: گ -> ط
    modern_text = modern_text.replace("ڭ", "گ")             # Step 3: ڭ -> گ
    modern_text = modern_text.replace(temp_placeholder, "ڭ") # Step 4: § -> ڭ
    
    
    aliweb_to_unicode_map = {
        # Multi-character first
        "لاَ": "ڵا", "لآ": "ڵا", "لاً": "ڵا",
        "لَ": "ڵ", "پ": "ڵ",
        "رِ": "ڕ", "أ": "ڕ",
        "ؤ": "ۆ", "وَ": "ۆ",
        "يَ": "ێ", "یَ": "ێ", "ص": "ێ",
        
        "ة": "ە",
        "ه": "ھ",
        "ي": "ی",
        "ض": "چ",
        "ث": "پ",
        "ظ": "ڤ",
        "ْ": "", "ُ": "",
        "ى": "*",
        "ك": "ک",
        "ذ": "ژ",
    }

    for legacy_char, modern_char in aliweb_to_unicode_map.items():
        modern_text = modern_text.replace(legacy_char, modern_char)
        
    return modern_text

# --- Example Usage ---
if __name__ == "__main__":
    legacy_text_example = """
ئەم طةكستة بؤ تاقيكردنةوةي طؤأينةكانة.
سلآو، ضؤني؟ ئةمة ثةيظيَكة بؤ نموونة.
ئةو كابراية كوردة.
ئةم طولة زؤر جوانة.
ئةمة طةورةترين ثةرتووكة.
من ثارةم ثيَية.
ئةمة هةمووي بؤ تؤية.
ئةو كضة زؤر ضالاكة، وةك ضؤلةكة واية.
ئةم كارة زؤر طرانة، من ناتوانم بيكةم.
ئةو زؤر حةزي لة طوَيَز و طةنمة.
ئةو دةرطاية داخراوة.
"""

    print("--- Original (AliWeb Legacy) ---")
    print(legacy_text_example)
    print("\n" + "="*70 + "\n")
    
    converted_text = convert_aliweb_to_unicode(legacy_text_example)
    
    print("--- Converted (Modern Unicode) ---")
    print(converted_text)