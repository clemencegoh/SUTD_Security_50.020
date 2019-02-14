import hashlib


def createHash(_item):
    hashed_val = hashlib.md5(_item).hexdigest()
    return hashed_val, len(hashed_val)


def analyzeHash(_items):
    item_lengths = []
    for i in _items:
        print(i)
        item_lengths.append(i[1])
    c = item_lengths[0]
    for l in item_lengths:
        if l != c:
            return False
    return True


def bruteForce():
    pass


def dictionaryAttack():
    pass


if __name__ == '__main__':
    tryout = [b'helloworld', b'longer_output_hello_world', b'short']
    print(analyzeHash(tryout))