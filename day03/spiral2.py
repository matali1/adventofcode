# --- Part Two ---
# As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.
#
# So, the first few squares' values are chosen as follows:
#
# Square 1 starts with the value 1.
# Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
# Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
# Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
# Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
# Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:
#
# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...
# What is the first value written that is larger than your puzzle input?
#
# Your puzzle input is still 347991.
#
# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26  1968
# 362  747  806   880  931 957
powers = [odd_number ** 2 for odd_number in range(3, 100, 2)]
print powers


def find_neighbours(position):
    lst = []
    for x1 in [-1, 0, 1]:
        for y1 in [-1, 0, 1]:
            lst.append((position[0] + x1, position[1] + y1))

    lst.remove(position)

    return lst


class SpiralMemory:
    # list of Cell
    memory = {}
    latest = ()

    def __init__(self):
        self.memory[0, 0] = 1
        self.latest = (0, 0)
        self.current_circle = 0

    def find_next_move(self):
        if self.latest == (0, 0):
            self.max_x = 1
            return (1,0)
        elif self.latest == (1, 0):
            return (1, 1)
        elif self.latest == (1, 1):
            return (0, 1)
        elif self.latest == (0, 1):
            return (-1, 1)
        elif self.latest == (-1, 1):
            return (-1, 0)
        elif self.latest == (-1, 0):
            return (-1, -1)
        elif self.latest == (-1, -1):
            return (0, -1)
        elif self.latest == (0, -1):
            return (1, -1)

        current_keys = len(self.memory.keys())
        print current_keys
        if current_keys in powers:
            self.current_circle = current_keys

        idx = powers.index(self.current_circle)
        max = idx + 2
        min = -(max)
        print 'min and max', min, max
        print self.latest
        # right

        new_move = (self.latest[0] + 1, self.latest[1])
        if new_move[0] <= max and new_move not in self.memory:
            print 'right'
            return new_move

        new_move = (self.latest[0], self.latest[1] + 1)
        # try up
        if new_move[1] <= max and new_move not in self.memory:
            print 'up'
            return new_move

        new_move = (self.latest[0] - 1, self.latest[1])
        if new_move[0] >= min and new_move not in self.memory:
            print 'left'
            return new_move

        new_move = (self.latest[0], self.latest[1] - 1)
        if new_move[1] >= min and new_move not in self.memory:
            print 'down'
            return new_move

    def next(self):
        neighbours = []
        new_value = 0
        next_move = self.find_next_move()
        print self.latest, '->', next_move
        neighbours = find_neighbours(next_move)
        # print neighbours

        for n in neighbours:
            if n in self.memory:
                new_value += self.memory[n]

        self.memory[next_move] = new_value
        self.latest = next_move

        return new_value


if __name__ == '__main__':
    memory = SpiralMemory()
    value = 0
    while value < 347991:
        # for i in range(0,27):
        # print '---- step number ',i
        value = memory.next()
        print '* ', value

    print '\nFINAL dictionary'
    print memory.memory
