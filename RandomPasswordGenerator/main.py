import random

uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))
digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))
punctuationSign1 = random.choice(chr(random.randint(33, 47)) + chr(random.randint(58, 64)) + chr(random.randint(91, 96))
                                 + "{|}~")
punctuationSign2 = random.choice(chr(random.randint(33, 47)) + chr(random.randint(58, 64)) + chr(random.randint(91, 96))
                                 + "{|}~")

password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 \
           + punctuationSign1 + punctuationSign2


def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


password = shuffle(password)
print(f"Password: {password}")
