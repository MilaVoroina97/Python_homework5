# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

text = input('Введите текст:')
with open('file_before_coding.txt','w', encoding='UTF-8') as data:
    data.write(text)

with open('file_before_coding.txt','r') as data:
    input_text = data.readline()

def encode_text(text):
    encoded_text = ''
    letter  = text[0]
    counter = 0
    if not text:
        return ''
    for i in range(len(text)):
        if text[i] == letter:
            counter += 1
        else:
            encoded_text = encoded_text + str(counter) + letter
            letter = text[i]
            counter = 1
    else:
        encoded_text = encoded_text + str(counter) + letter  
    return encoded_text

def decode_text(text2):
    decode_text = ''
    sum = ''
    for i in range(len(text2)):
        if text2[i].isdigit():
            sum += text2[i]
        else:
            decode_text = decode_text + text2[i] * int(sum)
            sum = ''
    return decode_text

with open('file_before_coding.txt','r') as file:
    decoding_text = file.read()

with open('file_after_coding.txt','w',encoding='UTF-8') as file:
    encodint_text = encode_text(decoding_text)
    file.write(encodint_text)

            
