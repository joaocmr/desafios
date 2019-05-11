import sys

sys.path.append("./commom")

from Formater import Formater

if len(sys.argv) == 4:
    f = open(sys.argv[1])
    string = f.read()
    MAX_WORDS = int(sys.argv[2])
    JUSTIFY = bool(int(sys.argv[3]))

else:
    print("Wrong number of arguments\n")
    print("Script must be executed like:\n")
    print("python scripts/format_text.py <path_to_txt> <max_words_per_line> <booleand_justified>:\n")
    sys.exit()

formater = Formater()

w = open("./data/output/formated_text.txt", "w")
output_text = formater.format(string, MAX_WORDS, JUSTIFY)
w.write(output_text)

f.close()
w.close()

