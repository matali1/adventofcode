import click
# --- Day 8: I Heard You Like Registers ---
#
# You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.
#
# Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:
#
# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10
#
# These instructions would be processed as follows:
#
#     Because a starts at 0, it is not greater than 1, and so b is not modified.
#     a is increased by 1 (to 1) because b is less than 5 (it is 0).
#     c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
#     c is increased by -20 (to -10) because c is equal to 10.
#
# After this process, the largest value in any register is 1.
#
# You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.
#
# What is the largest value in any register after completing the instructions in your puzzle input?
#
# Your puzzle answer was 5966.
# --- Part Two ---
#
# To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).


@click.command()
@click.option('--file', help='File to read the lines')
def compute_register_instructions_from_file(file):
    if file:
        with open(file) as myfile:
            registers,hightest_value_ever = compute_register_instructions(myfile)
            print registers
            max_value = -99999
            for key in registers:
                if registers[key] > max_value:
                    max_value = registers[key]
        print 'MAX value is',max_value
        print 'HIGHEST value ever WAS', hightest_value_ever

    else:
        print "Provide input file --file"

def parse_line(line):
    'd dec 461 if oiy <= 1'
    tokens = line.split(" ")
    return tokens
def compute_register_instructions(lines):
    print 'compute_register_instructions'
    highest_value_ever = 0
    registers = {}
    for line in lines:
        print line
        reg,operation,value_str,if_token,cond_reg,cond_oper,cond_value_str = parse_line(line)
        print reg
        value = int(value_str)
        if operation == 'dec':
            #decrease will be adding a negative
            value = -value

        cond_value = int(cond_value_str)
        if not reg in registers:
            registers[reg] = 0
        if not cond_reg in registers:
            registers[cond_reg] = 0

        val_register_to_change = registers[reg]
        val_register_in_condition = registers[cond_reg]

        if cond_oper == '==':
            if val_register_in_condition == cond_value:
                #sign already changed
                registers[reg] = val_register_to_change + value
        elif cond_oper == '>':
            if val_register_in_condition > cond_value:
                registers[reg] = val_register_to_change + value
        elif cond_oper == '<':
            if val_register_in_condition < cond_value:
                registers[reg] = val_register_to_change + value
        elif cond_oper == '>=':
            if val_register_in_condition >= cond_value:
                registers[reg] = val_register_to_change + value
        elif cond_oper == '==':
            if val_register_in_condition == cond_value:
                registers[reg] = val_register_to_change + value
        elif cond_oper == '<=':
            if val_register_in_condition <= cond_value:
                registers[reg] = val_register_to_change + value
        elif cond_oper == '!=':
            if val_register_in_condition != cond_value:
                registers[reg] = val_register_to_change + value
        else:
            raise Exception("Not implemented" ,cond_oper)

        for key in registers:
            if registers[key] > highest_value_ever:
                highest_value_ever = registers[key]

    return registers,highest_value_ever

if __name__ == '__main__':
    max_value = compute_register_instructions_from_file()
    print 'MAX is',max_value