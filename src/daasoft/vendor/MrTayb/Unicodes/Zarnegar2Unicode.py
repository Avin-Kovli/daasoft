def convert_zarnegar_to_unicode(legacy_text: str) -> str:
   
    zarnegar_to_unicode_map = {
       
        "لاٌ": "ڵا",
        "يٌ": "ێ",  
        "یٌ": "ێ",  
        "ىٌ": "ێ",  
        "ه‏": "ە",  
        "لٌ": "ڵ",
        "رٍ": "ڕ",
        "وٌ": "ۆ",
    
        "ى": "ی",
        "ي": "ی",
    }

    modern_text = legacy_text
    
    for legacy_char, modern_char in zarnegar_to_unicode_map.items():
        modern_text = modern_text.replace(legacy_char, modern_char)
        
    return modern_text

# --- Example Usage ---
if __name__ == "__main__":
    legacy_text_example = "بلٌيٌين و بگه‏رٍيٌين بوٌ هه‏لاٌلٌه‏ى سىٌيه‏مى فه‏لسه‏فه"

    print("--- Original (Zarnegar Legacy) ---")
    print(legacy_text_example)
    print("\n" + "="*70 + "\n")
    
    converted_text = convert_zarnegar_to_unicode(legacy_text_example)
    
    print("--- Converted (Modern Unicode) ---")
    print(converted_text)
    