# You come across an experimental new kind of memory stored on an infinite two-dimensional grid.
#
# Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:
#
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...
#
# While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.
#
# For example:
#
#     Data from square 1 is carried 0 steps, since it's at the access port.
#     Data from square 12 is carried 3 steps, such as: down, left, left.
#     Data from square 23 is carried only 2 steps: up twice.
#     Data from square 1024 must be carried 31 steps.
#
# How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?


#The grid can be build as powers of odd values
powers = [odd_number**2 for odd_number in range(1,595,2)]
print powers

def find_steps(input):
    print 'Analyzing steps to ',input
    if input == 1:
        return 0

    cycle = 0
    for idx,value in enumerate(powers):
        if input <= value:
            cycle = idx
            break

    print '\tChecking cycle number ',cycle
    min_steps = cycle
    max_steps = min_steps*2
    print '\tMinimum steps ',min_steps
    print '\tMaximum steps ', max_steps

    first_number = powers[cycle-1] +1
    print first_number
    min_steps_first_number = first_number+cycle-1
    print input-first_number
    steps = (input - min_steps_first_number)%(cycle*2) + min_steps


    return steps



examples = [1,4,12,23,1024,347991]

for i in examples:
    print '\n===',i
    value = find_steps(i)
    print '=== STEPS are ',value
