import sys

FILE = "data/sentences_for_tagging.txt"
out = "annotated_sentences_for_tagging.txt"


def process_line(line, outf):
    print(line)
    doc = input("Give a score or skip")
    if doc == "skip":
        print("\n")
    else:
        outf.write(line.strip() + "\t{}\n".format(doc))
    print('\n')


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 0:
        if len(args) == 1:
            FILE = args[0]
        else:
            FILE = args[0]
            out = args[1]

    index = 0
    outf = open(out, "w")
    try:
        with open(FILE) as file:
            for line in file:
                process_line(line, outf)
                index += 1

    except BaseException:
        outf.write(str(index))
        outf.flush()
        outf.close()
        print("\n")
        print(index)
