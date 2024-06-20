import re


def clean_html_tags(text):
    text = re.sub(r'<br\s*/*>', '\n', text)
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def check_quran_phrases_and_hadeeth(text):
    clues = ['سورة', 'سورة', 'آية', 'حديث', 'الحديث', 'الحديث', 'اية', 'ايه', 'تعالى']
    for clue in clues:
        if clue in text:
            return True
        
    return False

def detect_language(text):
    from langdetect import detect
    return detect(text)