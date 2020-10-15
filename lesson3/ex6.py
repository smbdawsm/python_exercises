''' Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
 и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но
 каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
'''
def int_func(word,good_word=[]):
    for letter in word:
        if ord(letter) >= 97 and ord(letter) <= 122:
            good_word.append(letter)
    if len(word) == len(good_word): 
        return ''.join(good_word).title()
    else: return ""

def string_parse(string,finish_string=[]):
    list_of_words = string.split()
    for word in list_of_words:
        finish_string.append(int_func(word))
    return print(f'Ахалай махалай, я наколдовал и получилось: {" ".join(finish_string)}')


string_parse(input('Введите предложение:  '))