"""
Brute force and Dictionary attack in python
Done by:
Clemence Goh (1002075)

Timings are estimated (depending on device):
Bruteforce: 65.07s (after optimizing)
Dictionary: 58.46s
"""

import hashlib
import random
import string
import time
import itertools
import argparse


def createHash(_item):
    hashed_val = hashlib.md5(_item).hexdigest()
    # print(hashed_val)
    return hashed_val, len(hashed_val)


def analyzeHash(_items):
    item_lengths = []
    for i in _items:
        val, l = createHash(i)
        item_lengths.append(l)
    c = item_lengths[0]
    for l in item_lengths:
        if l != c:
            return False
    return True


def bruteForce():
    starttime = time.time()
    # create list of hashes
    hash_values = []
    with open('hash5.txt') as h:
        for l in h.readlines():
            hash_values.append(l.strip())
    # print(hash_values)

    found = []
    alphanum = string.ascii_lowercase + string.digits

    all_found = False
    combi = ''
    for a in alphanum:
        if all_found:
            break
        for b in alphanum:
            if all_found:
                break
            for c in alphanum:
                if all_found:
                    break
                for d in alphanum:
                    if all_found:
                        break
                    for e in alphanum:
                        combi = a + b + c + d + e
                        val, _ = createHash(bytes(combi.encode()))
                        if val in hash_values:
                            found.append(combi)
                            if len(found) == len(hash_values):
                                all_found = True
    
    endtime = time.time()
    
    return found, (endtime - starttime)


def dictionaryAttack():
    starttime = time.time()
    # create list of hashes
    hash_values = []
    with open('hash5.txt') as h:
        for l in h.readlines():
            hash_values.append(l.strip())

    tried_dict = {}
    found = []
    with open('words5.txt') as f:
        """
        Assumptions made here: 
        - No single common word can be used more than once to hash to a value within the given
        - There are at most 2 numbers within the string
        - There are total of 5 characters in the alphanum string
        - There are at most 2 repeated characters
        """
        for l in f.readlines():
            # early cut off
            if len(found) == len(hash_values):
                break

            l = l.strip()
            letters = list(l)

            # create possible permutations
            perms = itertools.permutations(letters)
            p_list = list(perms)

            # do checks for each permutation
            word_exhausted = False

            for p in p_list:
                if len(found) == len(hash_values):
                    break

                if word_exhausted:
                    break

                # check vanilla word permutation
                word = ''.join(p)
                # print('[DEBUG] checking for:', word)

                # put into memory
                if word in tried_dict:
                    # print('[DEBUG][WARNING] whole perm tried before')
                    word_exhausted = True
                    break
                tried_dict[word] = 1

                h, _ = createHash(word.encode())
                if h in hash_values:
                    # print('appended:', word)
                    found.append((h, word))
                    word_exhausted = True
                else:
                    """
                    Replace one position only with number
                    """

                    # loop through once to replace
                    for i in range(len(p)):
                        # early cut off
                        if len(found) == len(hash_values):
                            break

                        # breaks once word is exhausted
                        if word_exhausted:
                            break

                        p_token = list(p)
                        p_token[i] = '.'
                        p_token = ''.join(p_token)

                        if p_token in tried_dict:
                            continue

                        for j in range(10):
                            if word_exhausted:
                                break
                            # create
                            replacing_p = list(p)
                            replacing_p[i] = str(j)
                            word = ''.join(replacing_p)

                            h, _ = createHash(word.encode())
                            if h in hash_values:
                                found.append((h, word))
                                word_exhausted = True

                        tried_dict[p_token] = 1

                """
                Replace two positions with numbers
                total: 10 possible combinations of 99
                """
                for i in range(4):  # 0 - 3
                    # early cut off
                    if len(found) == len(hash_values):
                        break
                    if word_exhausted:
                        break

                    for j in range(i + 1, 5):  # i - 4

                        if len(found) == len(hash_values):
                            break
                        if word_exhausted:
                            break

                        p_token = list(p)
                        p_token[i] = '.'
                        p_token[j] = '.'
                        p_token = ''.join(p_token)

                        if p_token in tried_dict:
                            continue

                        for a in range(10):
                            if len(found) == len(hash_values):
                                break
                            if word_exhausted:
                                break

                            first_replace = list(letters)
                            first_replace[i] = str(a)
                            for b in range(10):
                                if len(found) == len(hash_values):
                                    break
                                if word_exhausted:
                                    break
                                first_replace[j] = str(b)
                                word = ''.join(first_replace)

                                h, _ = createHash(word.encode())
                                if h in hash_values:
                                    found.append((h, word))
                                    # print('appended:', word)
                                    word_exhausted = True

                        tried_dict[p_token] = 1

    endtime = time.time()
    return found, (endtime - starttime)


def doBruteforce():
    print('executing bruteforce...')
    word_list, time_taken = bruteForce()
    print("found:")
    print(word_list)
    print('time taken:')
    print(time_taken)


def doDictionaryAttack():
    print('executing dictionary attack...')
    word_list, time_taken = dictionaryAttack()
    print('found:')
    word_list = [x[1] for x in word_list]
    print(word_list)
    print('time taken:')
    print(time_taken)
    return word_list


lower_alpha = string.ascii_lowercase


def saltedHash(_text):
    new_salted = _text + random.choice(lower_alpha)
    v, _ = createHash(new_salted.encode())
    return new_salted, v


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-part',
                        dest='part',
                        help='activate part, '
                             'should be:\n'
                             '0 for bruteforce,\n'
                             '1 for dictionary attack,\n'
                             '2 for dictionary + save passwords\n'
                             '3 for generation of salted passwords based on passwords from 2\n')

    # parse our arguments
    args = parser.parse_args()
    part = args.part

    if part == '0':
        doBruteforce()
    if part == '1':
        doDictionaryAttack()
    if part == '2':
        word_list = doDictionaryAttack()
        with open('saved_passwords.txt', 'w') as f:
            for w in word_list:
                f.write(w)
                f.write('\n')
    if part == '3':
        with open('salted6.txt', 'w') as s1:
            with open('pass6.txt', 'w') as s2:
                with open('saved_passwords.txt') as f:
                    for l in f.readlines():
                        salted_text, salted_hash = saltedHash(l.strip())
                        s1.write(salted_hash + '\n')
                        s2.write(salted_text + '\n')



