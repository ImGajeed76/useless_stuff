import random

import numba

lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

lorem_ipsum_sentences = [
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    'Quisque vitae varius ex, eu volutpat orci.',
    'Aenean ullamcorper orci et vulputate fermentum.',
    'Cras erat dui, finibus vel lectus ac, pharetra dictum odio.',
    'Nullam tempus scelerisque purus, sed mattis elit condimentum nec.',
    'Etiam risus sapien, auctor eu volutpat sit amet, porta in nunc.',
    'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.',
    'Proin ipsum purus, laoreet quis dictum a, laoreet sed ligula.',
    'Integer ultricies malesuada quam.',
    'Cras vel elit sed mi placerat pharetra eget vel odio.',
    'Duis ac nulla varius diam ultrices rutrum.'
]


@numba.jit(nopython=True)
def random_string(length: int):
    result = ""
    for i in range(length):
        rand = random.randint(97, 97 + 26)
        result += chr(rand)
    return result


@numba.jit(nopython=True)
def is_letter(char: str):
    if char.isalpha():
        return True
    return False


@numba.jit(nopython=True)
def shift(string: str, d: int):
    result = ""

    for i in range(len(string)):
        result += string[(i + len(string) + d) % len(string)]

    return result


@numba.jit(nopython=True)
def get_words(string: str, ignore_single_chars: bool = False):
    new_string = ""
    for c in string:
        if c.isalpha():
            new_string += c
        else:
            new_string += " " + c + " "

    all_words = []
    words = new_string.split()

    for word in words:
        if word.isalpha():
            if not (ignore_single_chars and len(word) == 1):
                all_words.append(word)

    return all_words


@numba.jit(nopython=True)
def word_count(string: str, ignore_single_chars: bool = False):
    words = get_words(string, ignore_single_chars)
    return len(words)


@numba.jit(nopython=True)
def longest_word(string: str, ignore_single_chars: bool = False, allow_multiple: bool = False):
    words = get_words(string, ignore_single_chars)
    max_len = 0
    max_word = ""

    for word in words:
        length = len(word)
        if length > max_len:
            max_len = length
            max_word = word

    return max_word


def count_letters(string: str):
    letter_counter = {}

    for c in string.lower():
        if c.isalpha():
            if c in letter_counter.keys():
                count = letter_counter[c]
                letter_counter.update({c: count + 1})
            else:
                letter_counter.update({c: 1})

    return dict(reversed(sorted(letter_counter.items(), key=lambda x: x[1])))


@numba.jit(nopython=True)
def reverse(string: str):
    result = ""

    for i in range(len(string)):
        result += string[len(string) - 1 - i]

    return result


def lorem_ipsum(n_sentences: int):
    result = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '

    for i in range(n_sentences - 1):
        result += random.choice(lorem_ipsum_sentences)

    return result
