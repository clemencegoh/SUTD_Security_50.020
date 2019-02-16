import hashlib
import random
import string
import time
import itertools


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
    
    combi = ''
    for a in alphanum:
        for b in alphanum:
            for c in alphanum:
                for d in alphanum:
                    for e in alphanum:
                        combi = a + b + c + d + e
                        val, _ = createHash(bytes(combi.encode()))
                        if val in hash_values:
                            found.append(combi)
    
    endtime = time.time()
    
    return found, (endtime - starttime)


# todo: do this shit
def dictionaryAttack():

    starttime = time.time()
    # create list of hashes
    hash_values = []
    with open('hash5.txt') as h:
        for l in h.readlines():
            hash_values.append(l.strip())

    found = []
    with open('words5.txt') as f:
        for l in f.readlines():
            l = l.strip()
            letters = list(l)

            # create possible permutations
            perms = itertools.permutations(letters)

            # replace with numbers
            # for p in perms:
            #     for i in set(letters):
            #         for j in range(4) # 0-3

            #         for k in range(10):  # 0-9
            #             p.replace(i, )
            p = list(perms)
            print(p)
            print(len(p))
            exit(1)

            val, _ = createHash(bytes(l.encode()))           
            if val in hash_values:
                found.append(l)

    endtime = time.time()

    return found, (endtime - starttime) 


if __name__ == '__main__':
    tryout = [b'helloworld', b'longer_output_hello_world', b'short']
    # print(analyzeHash(tryout))
    # word_list, time_taken = bruteForce()
    # print(word_list, time_taken)
    word_list, time_taken = dictionaryAttack()
    # print(word_list, time_taken)
    
