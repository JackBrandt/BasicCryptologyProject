'''main.py
author: Jack Brandt
date: 11/04/2024'''

# Imports
from affine_cipher import affine_encrypt
from affine_cipher import affine_decrypt

while True:

    cipher = input('What cipher are you using (or quit)? ')
    match cipher:
        case 'viginere':
            raise NotImplementedError
        case 'affine':
            alpha = input('parameter alpha: ')
            beta = input('parameter beta: ')
            en_or_de_crypt = input('encrypt or decrypt? ')
            match en_or_de_crypt:
                case 'encrypt':
                    plain_text = input('Input plaintext message: ')
                    affine_encrypt(plain_text,alpha,beta)
                case 'decrypt':
                    encrypted_text = input('Input encrypted text: ')
                    affine_decrypt(encrypted_text,alpha,beta)
                case _:
                    print('Error, please enter encrypt or decrypt')
        case 'quit':
            break
        case _:
            print("Cipher not in system...")
