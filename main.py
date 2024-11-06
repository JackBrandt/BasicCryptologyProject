'''main.py
author: Jack Brandt
date: 11/04/2024'''

# Imports
from affine_cipher import affine_encrypt
from affine_cipher import affine_decrypt
from affine_cipher import affine_attack

while True:

    cipher = input('What cipher are you using (or quit)? ')
    match cipher:
        case 'viginere':
            raise NotImplementedError
        case 'affine':
            en_or_de_crypt = input('encrypt or decrypt or attack? ')
            match en_or_de_crypt:
                case 'encrypt':
                    alpha = input('parameter alpha: ')
                    beta = input('parameter beta: ')
                    plain_text = input('Input plaintext message: ').lower()
                    affine_encrypt(plain_text,alpha,beta)
                case 'decrypt':
                    alpha = input('parameter alpha: ')
                    beta = input('parameter beta: ')
                    encrypted_text = input('Input encrypted text: ').lower()
                    affine_decrypt(encrypted_text,alpha,beta)
                case 'attack':
                    encrypted_text = input('Input encrypted text: ').lower()
                    affine_attack(encrypted_text)
                case _:
                    print('Error, please enter encrypt or decrypt')
        case 'quit':
            break
        case _:
            print("Cipher not in system...")
