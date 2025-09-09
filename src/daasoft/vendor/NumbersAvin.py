# -*- coding: utf-8 -*-
import regex as re

def Words2Numbers(text):
    word_to_num = {
        'سفر': 0, 'ئێک': 1,'دوو': 2,'سێ': 3, 'چار': 4,'پێنج': 5,'شەش': 6,'هەفت': 7,
        'هەشت': 8,'نەهـ': 9,'دەهـ': 10,'یازدە': 11,'دوازدە': 12,'سێزدە': 13,'چاردە': 14,
        'پازدە': 15,'شازدە': 16,'هەڤدە': 17,'هەژدە': 18,'نۆزدە': 19,'بیست': 20,'سیهـ': 30,
        'چل': 40,'پێنجی': 50,'شێست': 60,'هەفتێ': 70,'هەشتێ': 80,'نۆت': 90,'سەد': 100,
  'دووسەد':200,'سێسەد':300,'چارسەد':400,'پێنجسەد':500,'شەشسەد':600,'هەفتسەد':700,
  'هەشتسەد':800,'نەهسەد':900,'هزار': 1000,'ملیون': 1000000,'ملیار': 1000000000
    }
    finalresult=[]
    for lines in text.split('\n'):
        result = []
        current = 0
        total = 0
        compl=''
        word=lines.replace(' و ', ' ').split()
        for i in range(len(word)) :
            if word[i] in word_to_num: compl=''
            elif word[i][:-1] in word_to_num:word[i]=word[i][:-1]; compl='ێ'
            elif word[i][:-2] in word_to_num:word[i]=word[i][:-2]; compl='یێ'
            
            if word[i] in word_to_num:                
                value = word_to_num[word[i]]
                if word[0]=='هزار': current+= value
                elif value < 1000: current += value
                elif value==1000 and word[i-1] not in word_to_num : current += value
                else:
                    current *= value
                    total += current
                    current = 0
            else:
                if current != 0 or total != 0:
                    result.append(str(total + current)+compl)
                    current = 0
                    total = 0
                result.append(word[i])
        
        if current != 0 or total != 0:
            result.append(str(total + current)+compl)
        lines=' '.join(result)
        
        if re.search('پوینت',lines):lines = re.sub(r' پوینت ', r'.', lines)
        if re.search(' دۆلار',lines):lines = re.sub(' دۆلار', '$', lines)
        # if  re.search(' ژ سەدێ',lines):
        #     lines = re.sub(' ژ سەدێ', '%', lines)
        if  re.search(' ژ 100ێ',lines):lines = re.sub(' ژ 100ێ', '%', lines)
        if  re.search('سالب ',lines):lines = re.sub('سالب ', r'-', lines)
        if re.search(r'(-?\d+)(\s*)(ل سەر)(\s*)(\d+)(ێ?)',lines):# problem with 8 and 7 it convert it to 80 and 70
            lines=re.sub(r'(-?\d+)(\s*)(ل سەر)(\s*)(\d+)(ێ?)',r'\1/\5' , lines) 
        finalresult.append(lines)
    return '\n'.join(finalresult)


# --- Data Dictionaries ---
_numb = {
    0: "سفر", 1: "ئێک", 2: "دوو", 3: "سێ", 4: "چار",
    5: "پێنج", 6: "شەش", 7: "هەفت", 8: "هەشت", 9: "نەهـ",

    11: "یازدە", 12: "دوازدە", 13: "سێزدە", 14: "چاردە", 15: "پازدە",
    16: "شازدە", 17: "هەڤدە", 18: "هەژدە", 19: "نۆزدە",

    10: "دەهـ", 20: "بیست", 30: "سیهـ", 40: "چل", 50: "پێنجی",
    60: "شێست", 70: "هەفتێ", 80: "هەشتێ", 90: "نۆت",
100:'سەد',200:'دووسەد',300:'سێسەد',400:'چارسەد',500:'پێنجسەد',
600:'شەشسەد',700:'هەفتسەد',800:'هەشتسەد',900:'نەهسەد',
1000:"هزار",1000000:"ملیون",1000000000:"ملیار"
}
_scales = {
    1: "هزار", 2: "ملیون", 3: "ملیار", 4: "ترلیۆن",
}
_hundred = "سەد"
_negative = "سالب"
_connector = "و"
_point = "پوینت"

kurdishMonths={
    'ئادارا':3,
    'نیسانا':4,
    'گولانا':5,
    'خزیرانا':6,
    'تیرمەها':7,
    'تەباخا':8,
    'ئەیلوولا':9,
    'چرییا ئێکێیا':10,
    'چرییا دوویێیا':11,
    'کانوونا ئێکێیا':12,
    'کانوونا دوویێیا':1,
    'شوباتا':2
    }

# --- Core Conversion Functions ---
def _convert_less_than_thousand(number):
    if number == 0: return ""
    parts = []
    if number >= 100:
        hundreds_digit = number // 100
        if 1<= hundreds_digit <=9: 
            parts.append(_numb[hundreds_digit*100])   
        number %= 100
    if number > 0 and len(parts) > 0: parts.append(_connector)
    if number >= 20:
        tens_digit = number // 10
        ones_digit = number % 10
        parts.append(_numb[tens_digit * 10])
        if ones_digit > 0: parts.append(_connector); parts.append(_numb[ones_digit])
    else:
        parts.append(_numb[number])
    return " ".join(parts)

def convert_to_kurdish_text(number, convert_negatives=False):
    if not isinstance(number, int): raise ValueError("Input must be an integer.")
    if number < 0 and not convert_negatives: return str(number)
    if number == 0: return _numb[0]
    
    prefix = ""
    if number < 0 and convert_negatives:
        prefix = _negative + " "
        number = abs(number)
        
    chunks, result_parts = [], []
    while number > 0: chunks.append(number % 1000); number //= 1000
    if not chunks: return ""
    for i in range(len(chunks) - 1, -1, -1):
        chunk = chunks[i]
        if chunk == 0: continue
        chunk_text = _convert_less_than_thousand(chunk)
        if i > 0:
            scale_name = _scales[i]
            #result_parts.append(chunk_text+' '+scale_name if chunk == 1 else f"{chunk_text} {scale_name}")
            result_parts.append(f"{chunk_text} {scale_name}")
        else:
            result_parts.append(chunk_text)
    return prefix + f" {_connector} ".join(result_parts)

# --- Line-by-Line Processing Logic ---
def process_text_by_line(text, convert_negatives=False, convert_decimals=False):
    eastern_to_western = str.maketrans('٠١٢٣٤٥٦٧٨٩٫', '0123456789.')
    normalized_text = text.translate(eastern_to_western)
    
    lines = normalized_text.splitlines()
    processed_lines = [_convert_numbers_in_line(line, convert_negatives, convert_decimals) for line in lines]
    return "\n".join(processed_lines)

def _convert_numbers_in_line(line, convert_negatives, convert_decimals):
    if re.search(r'(\d+)(/)(\d+)(/)(\d+)',line):
        for key, value in kurdishMonths.items():
            matches = re.findall(r'/(\d+)/', line)
            if len(matches)>0:
                if value == int(matches[0]):
                    line = re.sub(r'(\d+)(/)(\d+)(/)(\d+)',rf'\1یێ {key} سالا \5ێ' , line)
    elif re.search(r'/',line):
        line = re.sub(r'(-?\d+)(/)(\d+)',r'\1 ل سەر \3ێ' , line) 
        
    if re.search(r'(\d+)(:)(\d+)(:)(\d+)',line): 
        line = re.sub(r'(\d+)(:)(\d+)(:)(\d+)',r'دەمژمێر \1 و \3 خولەک و \5 چرکە' , line) 
    elif re.search(r'(\d+)(:)(\d+)',line): 
        line = re.sub(r'(\d+)(:)(\d+)',r'دەمژمێر \1 و \3 خولەک ' , line) 
    if convert_decimals:
        line = re.sub("([0-9]{1,3})[,،](?=[0-9]{3})", r"\1", line)  # remove thousand separator 12,345,678 => 12345678
        line = re.sub(r'(-?\d+)\.(\d+)\s*([$%])?', lambda m: _replace_decimal(m, convert_negatives), line)
    
    
    line = re.sub(r'(-?\d+)(\p{L}+)', lambda m: _replace_with_suffix(m, convert_negatives), line)
    
    line = re.sub(r'(-?\d+)\s*([$%])', lambda m: _replace_with_symbol(m, convert_negatives), line)
    line = re.sub(r'(-?\d+)', lambda m: _replace_standalone(m, convert_negatives), line)

    return re.sub(r'\s+', ' ', line).strip()

# --- Helper functions for replacement logic ---
def _replace_decimal(match, convert_negatives):
    int_part_str, dec_part_str, symbol = match.groups()  
    int_text = convert_to_kurdish_text(int(int_part_str), convert_negatives)
    dec_text = convert_to_kurdish_text(int(dec_part_str), False)
    result = f" {int_text} {_point} {dec_text} "
    if symbol == '$': result += "دۆلار "
    elif symbol == '%': result += "ژ سەدێ "
    return result

def _replace_with_suffix(match, convert_negatives):
    number_str, suffix = match.groups()
    kurdish_text = convert_to_kurdish_text(int(number_str), convert_negatives)
    return f" {kurdish_text}{suffix} "

def _replace_with_symbol(match, convert_negatives):
    number_str, symbol = match.groups()
    kurdish_text = convert_to_kurdish_text(int(number_str), convert_negatives)
    if symbol == '$': return f" {kurdish_text} دۆلار "
    if symbol == '%': return f" {kurdish_text} ژ سەدێ "
    return match.group(0)

def _replace_standalone(match, convert_negatives):
    number_str = match.group(1)
    kurdish_text = convert_to_kurdish_text(int(number_str), convert_negatives)
    return f" {kurdish_text} "

# --- Main Execution Block ---
if __name__ == "__main__":
    # print("--- Kurdish Number to Text Converter (Line-by-Line) ---")
    
    sample_paragraph = """ل سالا 2024ێ، بهایێ 12.5$ بوو. 56.9
نرخێ داشکاندنێ 25% بوو.
ئەڤ کەسە ٣٤ سالە
٣٥٫٨ دهوک شول نەکر
65.8 دينار
98.8دينار
2123456909
1,234,234
1100
309
110%
٣/٨٠
67/886
١٥/١/١٩٩١
15/01/1991
12:4:05
03:6
ژمارا بەشداربویان -365 کەس بوون."""
    

    sample_paragraph1='''
    ٣/٨
    6/9
    '''
    print(f"\nOriginal Paragraph:\n{sample_paragraph}")

    print("\n--- All Options Enabled ---")
   # converted_paragraph = process_text_by_line(sample_paragraph, True, True)
   # print(converted_paragraph)
    
    text = '''
    پروژەک هاتە ڤەکرن ب کوژمێ چار ملیون و هەفتسەد و سیهـ و پێنج هزار و دووسەد و هەشتێ و سێ ل پارێزگەها دهوکێ 
    سەد hsjk
     هزار و ئێک
    ئێک ملیون و سەد هزار و سەد
    نۆزدە
    هەشتێ و شەش ژ سەدێ ل کوردستانێ بهارە
    بیست و پێنج دۆلار
    بیست
    سێ هزار و سەد و دەهـ
    سێ پوینت یازدە دۆلار
    شازدە هزار و هەفتسەد پوینت چل و ئێک ژ سەدێ ژمارەکا خەیالی یە

    '''
    print("\n--- Words to Numbers ---")
   # converted = Words2Numbers(converted_paragraph)
    #print(converted)
