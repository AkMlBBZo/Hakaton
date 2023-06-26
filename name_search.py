import re
from difflib import SequenceMatcher
import difflib
import pdf_reader

def find_matches_with_typos(pattern, text):
    matches = []
    pattern_length = len(pattern)

    # Поиск точных вхождений строки
    exact_matches = [m.start() for m in re.finditer(pattern, text, re.IGNORECASE | re.UNICODE)]
    matches.extend(exact_matches)
    # Поиск вхождений с опечатками
    bl=False
    sim=1
    for i in range(len(text) - pattern_length + 1):
        substring = text[i:i + pattern_length]

        # Вычисление сходства между строкой и подстрокой
        similarity = SequenceMatcher(None, pattern, substring).ratio()

        # Если сходство превышает 80% (изменено не более 20%), считаем это вхождением с опечатками
        if similarity >= 0.8 and bl == False:
            matches.append(i)
            bl=True
            sim=similarity
        elif bl==True and similarity < 0.8:
            bl = False
        elif similarity>sim:
            matches.pop()
            matches.append(i)
            sim=similarity


    return matches,sim


def main(pdf_name,search_name):
    search_name.replace(' \n',' ')
    search_name.replace('\n',' ')
    pages = pdf_reader.main(pdf_name)
    num_page=1
    result_string = ""
    for i in range(len(pages)):
        input_text=pages[i]
        input_text.replace(' \n',' ')
        input_text.replace('\n',' ')
        input_text.replace('  ',' ')


        matches,sim = find_matches_with_typos(search_name, input_text)
        bl=0
        # Формирование строки с результатами
        for match in matches:
            matched_text = input_text[match:match + len(search_name)]
            result_string += matched_text + "\n Страница:" + str(num_page) + "\n Схожесть с наименованием ОКС:" + str(int(sim*100))+"%\n\n\n"
        num_page+=1

    return result_string
