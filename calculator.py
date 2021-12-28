import argparse
import random

# chunk a list into pre-defined chunks n long
def chunk(l: list, n: int) -> list:
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

# create a card n in sequence (0-indexed) for a total of nrbits bits
def create_card(n: int, nrbits: int) -> list:
    whole_list = list(range(0, 2 ** nrbits))
    return chunk([x for x in whole_list if x & (1 << n) != 0], 8 if nrbits < 9 else 16)

# format a card created with create_card into a single string suitable for printing
def format_card(card: list) -> str:
    strcard = [[str(y) for y in x] for x in card]
    maxlen = max([len(x) for x in sum(strcard, [])])

    return '\n'.join([' '.join([y.rjust(maxlen, ' ') for y in x]) for x in strcard])

def main(args):
    print('The mystery calculator!!!\n')

    # protect against inadvertent bad things happening
    if not args.i_know_what_im_doing and args.nrbits > 10:
        print('That\'s likely a terrible idea (it will be enormous and slow)')
        return

    maxnum = 2 ** args.nrbits - 1
    print(f'Pick a number between 1 and {maxnum} (but don\'t tell me)\n')

    # go through each card (essentially a card with all the numbers having that bit set)
    # and print them out, asking the user each turn whether their number is present.
    # if it is, then that bit is set, and we continue on.
    # at the end, nr will have their number (if they've answered correctly)
    nr = 0
    bits = list(range(0, args.nrbits))

    if args.random:
        random.shuffle(bits)

    for i in bits:
        if args.ruin:
            print(f'* current bit:        {i}')
            print(f'* bits currently set: {nr:0{args.nrbits}b} ({nr})')

        print(format_card(create_card(i, args.nrbits)))
        answer = input('Is your number on this card? [y/N]: ')
        if len(answer) > 0 and answer.lower()[0] == 'y':
            nr |= 1 << i

        if args.ruin:
            print(f'* bits now set:       {nr:0{args.nrbits}b} ({nr})')
        
        print('\n')

    print(f'🪄 Your number was: {nr}. Magic!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python implementation of "the mystery calculator"')
    parser.add_argument('--ruin', '-v', action='store_true', help='Ruin the magic by showing some behind-the-scenes info (verbose mode)')
    parser.add_argument('--nrbits', '-b', type=int, default=6, help='Number of bits in the number to guess')
    parser.add_argument('--i-know-what-im-doing', action='store_true', help='Ignore good ideas')
    parser.add_argument('--random', '-r', action='store_true', help='Go through the cards in a random order')

    args = parser.parse_args()
    main(args)
