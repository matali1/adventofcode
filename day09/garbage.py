import click

# A large stream blocks your path. According to the locals, it's not safe to cross the stream at the moment because it's full of garbage. You look down at the stream; rather than water, you discover that it's a stream of characters.
#
# You sit for a while and record part of the stream (your puzzle input). The characters represent groups - sequences that begin with { and end with }. Within a group, there are zero or more other things, separated by commas: either another group or garbage. Since groups can contain other groups, a } only closes the most-recently-opened unclosed group - that is, they are nestable. Your puzzle input represents a single, large group which itself contains many smaller ones.
#
# Sometimes, instead of a group, you will find garbage. Garbage begins with < and ends with >. Between those angle brackets, almost any character can appear, including { and }. Within garbage, < has no special meaning.
#
# In a futile attempt to clean up the garbage, some program has canceled some of the characters within it using !: inside garbage, any character that comes after ! should be ignored, including <, >, and even another !.
#
# You don't see any characters that deviate from these rules. Outside garbage, you only find well-formed groups, and garbage always terminates according to the rules above.
#
# Here are some self-contained pieces of garbage:
#
#     <>, empty garbage.
#     <random characters>, garbage containing random characters.
#     <<<<>, because the extra < are ignored.
#     <{!>}>, because the first > is canceled.
#     <!!>, because the second ! is canceled, allowing the > to terminate the garbage.
#     <!!!>>, because the second ! and the first > are canceled.
#     <{o"i!a,<{i<a>, which ends at the first >.


@click.command()
@click.option('--file', help='File to read the lines')
def compute_total_score_from_file(file):
    if file:
        with open(file) as myfile:
            line = myfile.readline()
            parse_string(line)
    else:
        print "Provide input file --file"
    return 0


def parse_string(line):
    print line
    nesting_group_level = 0
    score = 0
    is_garbage = False
    skip_character = False
    garbage_char_cnt = 0

    for char in line:
        if skip_character:
            skip_character = False
            continue

        if char == '{':
            if not is_garbage:
                nesting_group_level = nesting_group_level + 1
                score += nesting_group_level
            else:
                garbage_char_cnt += 1
        elif char == '}':
            if not is_garbage:
                nesting_group_level -= 1
            else:
                garbage_char_cnt += 1
        elif char == '<':
            if is_garbage:
                garbage_char_cnt += 1
            is_garbage = True
        elif char == '!':
            skip_character = True
        elif char == '>':
            is_garbage = False
        elif is_garbage:
            garbage_char_cnt += 1
        # print (char, garbage_char_cnt)

    print "Score: ",score
    print "Garbage charcters: ", garbage_char_cnt
    return score, garbage_char_cnt


if __name__ == '__main__':
    compute_total_score_from_file()

