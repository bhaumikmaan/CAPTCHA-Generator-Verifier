##    KNOWLEDGE IS POWER    ##

import random
def generate_captcha(n = 9):
    lower_case = []
    upper_case = []
    digits = []

    #Fill up with A-Z
    for x in range(65, 91):
        upper_case.append(chr(x))
    #Fill up with a-z
    for x in range(97, 123):
        lower_case.append(chr(x))
    #Fill up with 0-9
    for x in range(48, 58):
        digits.append(chr(x))

    random.shuffle(lower_case)
    random.shuffle(upper_case)
    random.shuffle(digits)

    data = [lower_case, digits, upper_case ] #Nested List

    captcha = ''
    for i in range(n):
        q = random.randint(0,2) #0 or 1 or 2
        captcha = captcha + random.choice(data[q])

    return captcha

def main():
    print('Your CAPTCHA Code Is: ' , end = '')
    cpt = generate_captcha()
    print(cpt)

main()
