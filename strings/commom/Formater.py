from random import randrange
import re

class Formater:

    def __fill_line_with_spaces(self, line, max_size):
        while len(line) < max_size:
            line = self.add_random_whitespace(line)

        return line

    def __justify_lines(self, list_of_lines):
        max_size = max([
            len(line) for line in list_of_lines
        ])

        return [
            self.__fill_line_with_spaces(
                line, 
                max_size
            ) for line in list_of_lines
        ]

    def __get_list_of_lines(self, text, max_chars):
        words_list = re.split(' |\n', text)
        text_lines = []
        line = ""

        for word in words_list:
            line += "{} ".format(word)

            if len(line[:-1]) > (max_chars):
                line = line[:-1]
                line_words = line.split(" ")
                line = line[:-len(line_words[-1])]
                line += "\n"
                text_lines.append(line)
                line = "{} ".format(line_words[-1])

        text_lines.append(line)

        return text_lines

    def add_random_whitespace(self, string):
        words = string.split(" ")
        words.insert(
            randrange(1, len(words)-1), ""
        )
        return " ".join(words)

    def format(self, text, max_chars, justify=False):
        formated_lines = self.__get_list_of_lines(
            text, 
            max_chars
        )

        if justify:
            formated_lines = self.__justify_lines(
                formated_lines
            )

        return "".join(formated_lines)



        


        

