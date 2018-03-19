import click


@click.command()
@click.option('--file', help='File to get the checksum')
def provide_checksum(file):
    if file:
        matrix = []
        with open(file) as myfile:
            for line in myfile:
                row = [int(val) for val in line.split("\t")]
                matrix.append(row)
            # print matrix
            value = checksum(matrix)
            print "********* Checksum is %d" % value
            value = checksum_evenly_distribute(matrix)
            print "********* Checksum  evenly distribute is %d" % value


def checksum(matrix):
    checksum = 0
    for row in matrix:
        value = max(row) - min(row)
        checksum += value
    return checksum


def find_evenly_distribute(row):
    sorted_list = sorted(row)
    for idx, num in enumerate(sorted_list):
        for val in sorted_list[idx + 1:]:
            #if modulo is 0, so they divide by each other
            if (val % num) == 0:
                return (num, val)
    return (0, 1)


def checksum_evenly_distribute(matrix):
    checksum = 0
    for row in matrix:
        print row
        (val1, val2) = find_evenly_distribute(row)
        print val1, val2
        checksum += (val2 / val1)
    return checksum


if __name__ == '__main__':
    value = provide_checksum()

