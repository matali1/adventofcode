import click
@click.command()
@click.option('--file', help='File to read the lines')
def leave_the_maze(file):
    steps = 0
    if file:
        with open(file) as myfile:
            steps = calculate_steps(myfile)

    print steps
    print 'THERE ARE %d steps to leave the maze' % steps


def calculate_steps(myfile):
    instructions = [int(line) for line in myfile if line != ""]

    steps = 0
    start = instructions[0]
    current_idx = 0
    step_further = True
    while step_further:
        print '\nCurrent_idx ',current_idx
        if current_idx>len(instructions)-1:
            break
        move = instructions[current_idx]
        print 'Move to',move
        previous_idx = current_idx
        previous_value = instructions[current_idx]
        current_idx = current_idx + move
        steps+=1
        #part2
        if move >=3:
            instructions[previous_idx] = previous_value + -1
        else:
            instructions[previous_idx] = previous_value+1
        print 'steps =',steps
        

    print "STEPS is",steps
    return steps

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
    leave_the_maze()

