import sys

codebook = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    '!',
    ' ',
    '"',
    '#',
    '$',
    '%',
    '&',
    '\'',
    '(',
    ')',
    '*',
    '+',
    ',',
    '-',
    '.',
    '/',
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    ':',
    ';',
    '<',
    '=',
    '>',
    '?',
    '@',
    '[',
    '\\',
    ']',
    '^',
    '_',
    '`',
    '{',
    '|',
    '}',
]

EMOJI_BASE = 0x1F600
#EMOJI_BASE = 0x1F400


def emoji_encode(input: str) -> str:
    r = ""
    for c in input:
        offset = codebook.index(c)
        emojiset = int(EMOJI_BASE + offset)
        r += chr(int(emojiset))
    return r


def emoji_decode(input: str) -> str:
    r = ""
    for c in input:
        codechar = codebook[(ord(c)-EMOJI_BASE)]
        r += codechar
    return r


if __name__ == '__main__':
    print(emoji_encode(sys.argv[1]))
    # print(emoji_decode(sys.argv[1]))
