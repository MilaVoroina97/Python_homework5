# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

def delete_letter(text):
    delete_text = 'абв'
    res = [i for i in text.split() if delete_text not in i]
    return ' '.join(res)

text = 'Удалите все всеабв абв словаабв слова, где есть абв"'
print(delete_letter(text))