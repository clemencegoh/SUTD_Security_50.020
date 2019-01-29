import string
from collections import Counter

# upper and lower alphabets, for use later
lower_alpha = map(chr, range(97, 123))
upper_alpha = map(chr, range(65, 91))


def encrypt_caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


encrypted = encrypt_caesar('hello there!', 3)
print('encrypted text:', encrypted)


def decrypt_caesar(ciphertext):
    freq_map = Counter(ciphertext)
    most_freq_letter = freq_map.most_common()
    return most_freq_letter[0][0]


print(decrypt_caesar(encrypted))



