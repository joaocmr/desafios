import sys
import unittest

sys.path.append("./commom")

from Formater import Formater

class TestFormater(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.formater = Formater()
        f = open("./tests/data/input/text.txt")
        r1 = open("./tests/data/output/not_justified.txt")
        r2 = open("./tests/data/output/justified.txt")
        
        self.text = f.read()
        self.unjustified_output = r1.read()
        self.justified_output = r2.read()

        f.close()
        r1.close()
        r2.close()

    def test_add_random_whitespace(self):
        initial_text = "Text de Teste"
        initial_len = len(initial_text)

        final_text = self.formater.add_random_whitespace(
            initial_text
        )
        final_len = len(final_text)

        self.assertEqual(initial_len+1, final_len)

    def test_format_unjustified(self):
        expected_output = self.unjustified_output
        output = self.formater.format(self.text, 40, False)
        self.assertEqual(expected_output, output)

    def test_format_justified(self):
        expected_output = self.justified_output
        output = self.formater.format(self.text, 40, True)
        self.assertEqual(len(expected_output), len(output))


if __name__ == '__main__':
    unittest.main()