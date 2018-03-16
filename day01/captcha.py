import click
@click.command()
@click.option('--text', help='Provide text to get captcha')
@click.option('--file', help='File to read the text from')
def inverse_captcha(text, file):
    """Provide captcha either from text or file"""
    if text:
        print "Captcha is %d" % captcha(text)
        print "Halfway Captcha is %d" % captcha_halway(text)
    if file:
        with open(file) as myfile:
            text = myfile.read().replace('\n', '')
            value = captcha(text)
            print "********* Captcha is %d" % value
            halfway = captcha_halway(text)
            print "********** Halfway Captcha is %d" % halfway

def reduce(text):
    '''
    Reduces text by returning only these letters for which the next letter is the same (circular list)
    :param text: input text
    :return: reduced text
    '''
    prev_letter = text[len(text)-1]
    clusters = ""
    for letter in text:
        if letter == prev_letter:
            clusters += letter
        prev_letter = letter

    print "%s -> %s" % (text,clusters)
    return clusters


def reduce_halfway(text):
    '''
    Reduces text by returning only these letters for which the next digit halfway arround the circular list ist the same
    :param text: input text
    :return: reduced text
    '''

    text_length = len(text)
    if text_length %2 == 1:
        print "ODD NUMBERS"
        return ""
    steps = text_length/2

    clusters = ""
    for idx,letter in enumerate(text):
        halfway_letter = text[(idx+steps)%text_length]
        if letter == halfway_letter :
            clusters += letter

    print "%s -> %s" % (text,clusters)
    return clusters


def captcha(text):
    if not text:
        return 0

    clusters = reduce(text)
    value = 0
    for letter in clusters:
        try:
            value += int(letter)
        except ValueError:
            print "\tIgnoring ", letter
            continue
    return value


def captcha_halway(text):
    if not text:
        return 0

    clusters = reduce_halfway(text)
    value = 0
    for letter in clusters:
        try:
            value += int(letter)
        except ValueError:
            print "\tIgnoring ", letter
            continue
    return value

if __name__ == '__main__':
    inverse_captcha()
    print captcha("11122")
