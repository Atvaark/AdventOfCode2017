def is_anagram(word, other):
    if len(word) != len(other):
        return False

    word_ordered = ''.join(sorted(word))
    other_ordered = ''.join(sorted(other))
    return word_ordered == other_ordered


def check(passphrase, check_anagrams):
    words = passphrase.split(' ')
    word_dict = {}
    for word in words:
        if check_anagrams:
            for other_word in word_dict:
                if is_anagram(word, other_word):
                    return False

        if word in word_dict:
            return False
        word_dict[word] = 1
    return True

def get_valid_count(input_path, check_anagrams=False):    
    with open(input_path) as f:
        passphrases = f.read().splitlines()

    c = 0
    for phrase in passphrases:
        valid = check(phrase, check_anagrams)
        if valid:
            c += 1
    return c

def get_output(out_path):
    with open(out_path) as f:
        lines = f.read().splitlines()

    output_values = []
    for line in lines:
        output_values.append(int(line))
    
    return output_values

def main():
    output = get_output('day04.output')

    expected1 = output[0]
    actual1 = get_valid_count('day04.input')

    if actual1 == expected1:
        print(actual1, 'OK')
    else:
        print(f'{actual1} != {expected1} ERROR')

    expected2 = output[1]
    actual2 = get_valid_count('day04.input', check_anagrams=True)
    if actual2 == expected2:
        print(actual2, 'OK')
    else:
        print(f'{actual2} != {expected2} ERROR')

if __name__ == '__main__':
    main()