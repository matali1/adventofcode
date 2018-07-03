# --- Day 10: Knot Hash ---
#
# You come across some programs that are trying to implement a software emulation of a hash based on knot-tying. The hash these programs are implementing isn't very strong, but you decide to help them anyway. You make a mental note to remind the Elves later not to invent their own cryptographic functions.
#
# This hash function simulates tying a knot in a circle of string with 256 marks on it. Based on the input to be hashed, the function repeatedly selects a span of string, brings the ends together, and gives the span a half-twist to reverse the order of the marks within it. After doing this many times, the order of the marks is used to build the resulting hash.
#
#   4--5   pinch   4  5           4   1
#  /    \  5,0,1  / \/ \  twist  / \ / \
# 3      0  -->  3      0  -->  3   X   0
#  \    /         \ /\ /         \ / \ /
#   2--1           2  1           2   5
#
# To achieve this, begin with a list of numbers from 0 to 255, a current position which begins at 0 (the first element in the list), a skip size (which starts at 0), and a sequence of lengths (your puzzle input). Then, for each length:
#
#     Reverse the order of that length of elements in the list, starting with the element at the current position.
#     Move the current position forward by that length plus the skip size.
#     Increase the skip size by one.
#
# The list is circular; if the current position and the length try to reverse elements beyond the end of the list, the operation reverses using as many extra elements as it needs from the front of the list. If the current position moves past the end of the list, it wraps around to the front. Lengths larger than the size of the list are invalid.
#
# Here's an example using a smaller list:
#
# Suppose we instead only had a circular list containing five elements, 0, 1, 2, 3, 4, and were given input lengths of 3, 4, 1, 5.
#
#     The list begins as [0] 1 2 3 4 (where square brackets indicate the current position).
#     The first length, 3, selects ([0] 1 2) 3 4 (where parentheses indicate the sublist to be reversed).
#     After reversing that section (0 1 2 into 2 1 0), we get ([2] 1 0) 3 4.
#     Then, the current position moves forward by the length, 3, plus the skip size, 0: 2 1 0 [3] 4. Finally, the skip size increases to 1.
#
#     The second length, 4, selects a section which wraps: 2 1) 0 ([3] 4.
#     The sublist 3 4 2 1 is reversed to form 1 2 4 3: 4 3) 0 ([1] 2.
#     The current position moves forward by the length plus the skip size, a total of 5, causing it not to move because it wraps around: 4 3 0 [1] 2. The skip size increases to 2.
#
#     The third length, 1, selects a sublist of a single element, and so reversing it has no effect.
#     The current position moves forward by the length (1) plus the skip size (2): 4 [3] 0 1 2. The skip size increases to 3.
#
#     The fourth length, 5, selects every element starting with the second: 4) ([3] 0 1 2. Reversing this sublist (3 0 1 2 4 into 4 2 1 0 3) produces: 3) ([4] 2 1 0.
#     Finally, the current position moves forward by 8: 3 4 2 1 [0]. The skip size increases to 4.
#
# In this example, the first two numbers in the list end up being 3 and 4; to check the process, you can multiply them together to produce 12.
#
# However, you should instead use the standard list size of 256 (with values 0 to 255) and the sequence of lengths in your puzzle input. Once this process is complete, what is the result of multiplying the first two numbers in the list?

def convert_to_ascii_list(input_string):
    ascii_list = [ord(character) for character in input_string]
    return ascii_list


def get_sublist(circular_list, start_idx, sublist_length):
    sublist = []
    list_length = len(circular_list)
    for value in range(sublist_length):
        sublist.append(circular_list[(start_idx + value) % list_length])
    return sublist


def knot_hash_ascii(circular_list, hash_list):
    skip_size = 0
    idx = 0
    for round in range(64):
        print '###ROUND ', round
        circular_list, skip_size, idx = knot_hash(circular_list, hash_list, skip_size, idx)

    print circular_list
    return circular_list


def knot_hash(circular_list, hash_list, initial_skip_size=0, initial_idx=0):
    skip_size = initial_skip_size
    list_length = len(circular_list)
    original_list = circular_list
    print original_list
    new_idx = initial_idx

    for input in hash_list:
        print '-----------------------'
        print input

        start_idx = new_idx
        print 'Start index: ', start_idx, ' value: [', circular_list[start_idx], ']'
        sublist_length = input
        sublist = get_sublist(circular_list, start_idx, sublist_length)
        print sublist
        reverse_sublist = sublist[::-1]
        print reverse_sublist
        # replace values
        for value in range(len(reverse_sublist)):
            cur_idx = (start_idx + value) % list_length
            # replace that value with reverse_sublist
            circular_list[cur_idx] = reverse_sublist[value]
        # recalculate the indexes
        print "Rearranged circular_list"
        print circular_list
        new_idx = (start_idx + input + skip_size) % list_length
        skip_size += 1
        print 'new idx ', new_idx
        print 'new skip size ', skip_size

    return circular_list, skip_size, new_idx


def result_produce(new_list):
    return new_list[0] * new_list[1]


def dense_hash(sparse_hash):
    print '**', (len(sparse_hash) % 16)
    if (len(sparse_hash) % 16):
        raise Exception("should be a power of 16")

    dense_hash_list = []
    for batch in range(len(sparse_hash) / 16):
        print '**', batch
        idx_shift = batch * 16
        value = sparse_hash[0 + idx_shift]
        for next_val in sparse_hash[(1 + idx_shift):(batch + 1) * 16]:
            value = value ^ next_val
        dense_hash_list.append(value)
    return dense_hash_list


def hex_signature(values_list):
    signature = ''
    for value in values_list:
        # with leading 0
        hex = '{:02x}'.format(value)
        signature += hex
    return signature


if __name__ == '__main__':
    # compute_total_score_from_file()
    circular_list = range(0, 256)
    extra_hash = [17, 31, 73, 47, 23]
    hash_str = '189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62'
    hash = convert_to_ascii_list(hash_str)
    hash.extend(extra_hash)
    print hash
    # new_list,new_idx,skip_size = knot_hash(circular_list, hash)
    # result = new_list[0]*new_list[1]

    sparse_hash = knot_hash_ascii(circular_list, hash)
    dense_hash_list = dense_hash(sparse_hash)
    print dense_hash_list
    print hex_signature(dense_hash_list)
    # print 'PRODUCE', result
