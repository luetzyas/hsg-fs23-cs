# imports
from code_collection import *

#read inputfile
print("Exercise 5::")
parsed_values = read_input_bytes("input/aux_4.txt")

#get Message/Ciphertext
M11 = parsed_values.get('M11')
C11 = parsed_values.get('C11')
C21 = parsed_values.get('C21')
C22 = parsed_values.get('C22')
C31 = parsed_values.get('C31')
C33 = parsed_values.get('C33')

#prepare attributes for decryption
iv = get_iv()

#get secretkey from first block M11 & C11
k2 = xor(M11[:16], C11[:16])
M21 = decrypt_aes_ctr(k2, C21, iv.get('C21'))
M22 = decrypt_aes_ctr(k2, C22, iv.get('C22'))

#get secretkey from second block
k3 = xor(M21[16:32], C21[16:32])
M31 = decrypt_aes_ctr(k3, C31, iv.get('C31'))
M33 = decrypt_aes_ctr(k3, C33, iv.get('C33'))

print('\nKeys:')
print('k2: ', k2)
print('k3: ', k3)

print('\nMessages:')
print('M11: ', hex_to_text(M11.decode()))
print('M21: ', M21)
print('M22: ', M22)
print('M31: ', M31)
print('M33: ', M33)

"""
    Exercise 5::

    Keys:
    k2:  b'6\tLZo\xae\x1a\xe4\xe7\xc6s\x93\xef\xbf\xdf$'
    k3:  b'\xd4\xee\xe9\xea\xd0-\x083x\xef\xde\x18\xc4C\xf8+'
    
    Messages:
    M11:  Error converting hex to text: non-hexadecimal number found in fromhex() arg at position 1
    M21:  b'Infomration is physical, said Rolf Landauer... Weird.'
    M22:  b'Computer programming is an art form, like the creation of poetry or music.'
    M31:  b'There are infinitely many infinities?!'
    M33:  b'Why is the bitcoin price so volatile?'
"""