def convert_dylan_to_unicode(legacy_text: str) -> str:
   
    dylan_to_unicode_map = {
       
        "لإ": "ڵا", "لأ": "ڵا", "لآ": "ڵا",
        "وَ": "ۆ",
        
        "ؤ": "ۆ",
        "ة": "ە",
        "ض": "ڤ",
        "ص": "ڵ",
        "ث": "ێ",
        "ه": "ھ",
        "ك": "ک",
        "ي": "ی",
        "ى": "ی",
        "ذ": "ڕ",
    }

    modern_text = legacy_text
    
    for legacy_char, modern_char in dylan_to_unicode_map.items():
        modern_text = modern_text.replace(legacy_char, modern_char)
        
    return modern_text

# --- Example Usage ---
if __name__ == "__main__":
    legacy_text_example = """
سلآو، ئةمة نموونةيةكى نويَية بؤ تاقيكردنةوةي ضةند ثةيظيَك.
ئةمة ذؤذنامةيةكى كوردى ية.
ضيديوَكة زؤر جوانة.
ئةو صَيوانةى دةبيني، ئةوة بؤ ئيَمةية.
سوپاسى هةموو لايةك دةكةم.
"""

    print("--- Original (Dylan Legacy) ---")
    print(legacy_text_example)
    print("\n" + "="*70 + "\n")
    
    converted_text = convert_dylan_to_unicode(legacy_text_example)
    
    print("--- Converted (Modern Unicode) ---")
    print(converted_text)