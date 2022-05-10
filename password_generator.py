# Written by CJ Teas

import random

password_count = 0

while password_count < 1:

    lletter_count = 0
    uletter_count = 0
    digit_count = 0
    special_count = 0

    # 2 uppercase letters
    # 2 lowercase letters
    # 2 digits
    # 2 special characters

    letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    digits_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    special_list = ['!', '@', '$', '%', '^', '&', '*']

    password_list = []
    shuffled_password = []

    while lletter_count < 2:
        random_digit = random.randrange(0, 26)
        lletter = letters_list[random_digit]
        password_list.append(lletter)
        lletter_count += 1

    while uletter_count < 2:
        random_digit = random.randrange(0, 26)
        uletter = letters_list[random_digit].upper()
        password_list.append(uletter)
        uletter_count += 1

    while digit_count < 2:
        random_digit = random.randrange(0, 9)
        pw_digit = (digits_list[random_digit])
        password_list.append(pw_digit)
        digit_count += 1

    while special_count < 2:
        random_digit = random.randrange(0, 7)
        pw_special = (special_list[random_digit])
        password_list.append(pw_special)
        special_count += 1

    for i in password_list: 
        password_random = random.randrange(0, 6)
        pw_placement = password_list[password_random]
        shuffled_password.append(pw_placement)
    
    password_count += 1

user_guess = str(input('Guess a password. 8 Characters, 2 Uppercase Letters, 2 Lowercase, 2 digits, and 2 special characters:'))

if user_guess != shuffled_password:
    print('You Lose!')

elif user_guess == shuffled_password:
    print('You Win! (Impossible)')

print(*shuffled_password)













