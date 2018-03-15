
def reduce(text):
    prev_letter = text[0]
    clusters = ""
    current_cluster=""
    if text[0] == text[len(text)-1]:
        current_cluster = text[0]

    for letter in text[1:]:
        if prev_letter == letter:
            current_cluster = letter

        else:
            if current_cluster:
                clusters += current_cluster
                current_cluster = ""
        prev_letter = letter

    if current_cluster:
        clusters += current_cluster

    print "%s -> %s" % (text,clusters)
    return clusters

def captcha(text):
    if not text:
        return 0

    clusters = reduce(text)
    value = 0
    for letter in clusters:
        value += int(letter)
    return value




if __name__ == '__main__':
    print captcha("11122")
