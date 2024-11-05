'''Contains encryption and decryption functions for affine ciphers
author: Jack Brandt
date: 11/04/24
'''
# Imports
from dictionaries import alpha_to_int_dict
from dictionaries import int_to_alpha_dict

def affine_encrypt(plain_text,alpha,beta):
    '''Encrypts a plain text message using an affine cipher (ax+b where x
    is the plaintext character to be shifted).
    Args:
        plain_text (str): The message you want encrypted (must be only
        lowercase letters)
        alpha (int or str): The alpha parameter
        beta (int or str): The beta parameter
    '''
    # Step 1: Convert everything to ints
    plaintext_int = []
    for char in plain_text:
        plaintext_int.append(alpha_to_int_dict[char])
    try:
        alpha = alpha_to_int_dict[alpha]
    except KeyError:
        alpha = int(alpha)
    try:
        beta = alpha_to_int_dict[beta]
    except KeyError:
        beta = int(beta)

    # Safety Check: GCD with 26 has to be 1
    if alpha % 2 == 0 or alpha % 13 == 0:
        raise ValueError('GCD(alpha,26) must be 1!')

    # Step 2: Apply affine_cipher to every character
    encrypted_int = []
    for integer in plaintext_int:
        encrypted_int.append(alpha*integer+beta)

    # Step 3: Convert back to string
    encrypted_string = ''
    for integer in encrypted_int:
        encrypted_string+=int_to_alpha_dict[integer]

    # Step 4: Print
    print(f'Your message encrypted with affine cipher (with parameters alpha={alpha}, beta={beta}) is:')
    print(encrypted_string)

def affine_decrypt(plain_text,alpha,beta):
    '''Decrypts a plain text message using an affine cipher (ax+b where x
    is the plaintext character to be shifted).
    Args:
        plain_text (str): The message you want encrypted (must be only
        lowercase letters)
        alpha (int or str): The alpha parameter
        beta (int or str): The beta parameter
    '''