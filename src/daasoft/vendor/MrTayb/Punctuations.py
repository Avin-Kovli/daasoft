import re

def normalize_kurdish_punctuation(text: str, join_punctuation: bool = False) -> str:
    if not text.strip(): return ""
    opening_punct = r"«<“\(\[\{"
    closing_punct = r"»>”\)\]\}،؛؟.,!"
    all_punct = opening_punct + closing_punct
    if not join_punctuation:
        processed_text = text.replace('((', '«').replace('))', '»')
        processed_text = re.sub(rf'\s+([{re.escape(closing_punct)}])', r'\1', processed_text)
        processed_text = re.sub(rf'([{re.escape(opening_punct)}])\s+', r'\1', processed_text)
        processed_text = re.sub(rf'([{re.escape(closing_punct)}])([{re.escape(opening_punct)}])', r'\1 \2', processed_text)
        processed_text = re.sub(rf'([{re.escape(closing_punct)}])([^\s{re.escape(all_punct)}])', r'\1 \2', processed_text)
        processed_text = re.sub(rf'([^\s{re.escape(all_punct)}])([{re.escape(opening_punct)}])', r'\1 \2', processed_text)
        return re.sub(r'\s+', ' ', processed_text).strip()
    else:
        cleaned_text = normalize_kurdish_punctuation(text, join_punctuation=False)
        separated_text = re.sub(rf'([{re.escape(all_punct)}])', r' \1 ', cleaned_text)
        return re.sub(r'\s+', ' ', separated_text).strip()

def normalize_multiline_text(full_text: str, join_punctuation: bool = False) -> str:
    "Normalizes a multi-line string, preserving line breaks."
    if not full_text.strip(): return ""
    text = full_text.replace('\r\n', '\n')
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    lines = text.split('\n')
    processed_lines = [normalize_kurdish_punctuation(line, join_punctuation) for line in lines]
    return '\n'.join(processed_lines)

# --- --- --- EXAMPLES --- --- ---
if __name__ == "__main__":
    messy_text ='''
    ئەڤین هات .ئەز چوم ،تو هاتی .
  بهایێ (دولاری)د نوکە دا دبیتە سەد <هزار > دینار
    '''
    print("--- Normalized Multi-line Text (Joined) ---")
    #print(normalize_multiline_text(messy_text, join_punctuation=False)) #True -> Join punctuation, false -> Separate punctuation
    print("--- Normalized Multi-line Text (Separated) ---")
    #print(normalize_multiline_text(messy_text, join_punctuation=True)) #True -> Join punctuation, false -> Separate punctuation