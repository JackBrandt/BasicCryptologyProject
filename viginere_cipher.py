'''
-Jack

 I had a separate project for viginere,
 if I get around to it I'll reimplement

Here is it's code:

int_key=[]
for c in list(str_key):
    int_key.append(alphabet[c])
#print(int_key)
#print(len(int_key))

int_plaintext_message=[]
for c in list(plaintext_message):
    int_plaintext_message.append(alphabet[c])
#print(int_plaintext_message)

int_encoded_message=[]

for i in range(len(int_plaintext_message)):
    int_encoded_message.append((int_plaintext_message[i] + int_key[i%len(int_key)])%26)

#print(int_encoded_message)
str_encoded_message=""
for i in int_encoded_message:
    str_encoded_message=str_encoded_message+int_to_char[i]
print(str_encoded_message)
'''