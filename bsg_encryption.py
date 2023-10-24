import random


def encryption(text):
    char_number = []
    char_value = []
    for char in text:
        char_number.append(ord(char))
    for char in char_number:
        value = ''
        for i in range(char):
            value += str(random.randint(0,1))
        char_value.append(value)
    return '0'.join(char_value)


def decryption(text):
    char_value = text.split('o')
    result = ''
    for i in char_value:
        try:
            result += chr(int(len(i)))
        except:
            result += i
    return result


text = 'hello world'
print("encryption text : ",encryption(text))
print("decryption text :",decryption(encryption(text)))


