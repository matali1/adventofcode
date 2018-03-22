import click
@click.command()
@click.option('--file', help='File to read the lines')
def get_valid_passphrases_from_file(file):
    if file:
        with open(file) as myfile:
            valid_lines=get_valid_passhprases(myfile)

    print valid_lines
    print 'THERE ARE %d valid_lines' % len(valid_lines)



def check_if_valid(tokens):
    tokens_set = list(set(tokens))
    if len(tokens)!= len(tokens_set):
        return False
    return True

def check_if_valid_no_anagrams(tokens):
    sorted_letters_tokens = set()
    #sort letters in the word
    for word in tokens:
        letters = []
        for letter in word:
            letters.append(letter)
        sorted_letters_tokens.add(''.join(sorted(letters)))
    if len(tokens) != len(sorted_letters_tokens):
        print sorted_letters_tokens
        print tokens
        return False
    return True


def get_valid_passhprases(lines):
    valid_lines = []
    for line in lines:
        print line.replace("\n", "")
        tokens = line.replace("\n", "").split(" ")
        if check_if_valid(tokens) and check_if_valid_no_anagrams(tokens):
            valid_lines.append(line)
            print '\tVALID'
        else:
            print '\tNOT VALID'

    return valid_lines


if __name__ == '__main__':
    valid_lines = get_valid_passphrases_from_file()
    print 'VALID LINES',
    print valid_lines
    print len(valid_lines)

