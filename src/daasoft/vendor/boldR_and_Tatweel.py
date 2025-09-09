import re

def startWithBoldR(text):
    words=text.split()
    for j in range(len(words)):
        if re.search(r"\bر\w*\b", words[j]):
            words[j] = re.sub(r"ر",r"ڕ", words[j])    
    text=' '.join(words)
    return text
#-----------------------------------------------------------------------------
def removeTatweel(text):
    z=text.split()    
    for j in range(len(z)):
        if not(z[j].endswith('هـ')):
            z[j]=z[j].replace('ـ','')
    text=' '.join(z)
    return text
text='''
رامـــانیت ناڤێت کــوردی
روژ و شەڤ
زەرزەوات
گوهـ
گوهــدار
گونەهـ
رەهەند
رەوشەنبیر
'''
print(startWithBoldR(text))
print('-'*30,'\n',removeTatweel(text))