import sys

sys.path.append("./commom")

from Formater import Formater

if len(sys.argv) == 2:
    f = open(sys.argv[1])
    string = f.read()

else:
    print("Path for txt file must be given as argument")
    sys.exit()

formater = Formater()

w1 = open("./data/output/not_justified.txt", "w")
not_justified_text = formater.format(string, 40, False)
w1.write(not_justified_text)

w2 = open("./data/output/justified.txt", "w")
justified_text = formater.format(string, 40, True)
w2.write(justified_text)

f.close()
w1.close()
w2.close()

