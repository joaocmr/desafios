import sys

sys.path.append("./commom")

from Formater import Formater

f = open("./data/input/text.txt")
string = f.read()

formater = Formater()

w1 = open("./data/output/not_justified.txt", "w")
not_justified_text = formater.format(string, 40, False)
w1.write(not_justified_text)

w2 = open("./data/output/justified.txt", "w")
justified_text = formater.format(string, 40, True)
w2.write(justified_text)

