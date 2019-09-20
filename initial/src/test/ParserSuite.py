import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    # test define variable
    def test_variable_successful_204(self):
        input = """ int a,b,c,d; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))
    def test_variable_successful_205(self):
        input = """ float abcd;
            int thang;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))
    def test_variable_miss_right_square_bracket_206(self):
        input = """ int a[;
            int thang;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 206))
    #  ??????
    def test_variable_miss_left_square_bracket_207(self):
        input = """ int bk5];
                    int thang;"""
        expect = "Error on line 1 col 8: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 207))
    def test_variable_miss_right_square_bracket_208(self):
        input = """ int bku[123;
                    int thang;"""
        expect = "Error on line 1 col 12: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 208))
    def test_variable_successful_209(self):
        input = """ int bku [3], thang [1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))
    def test_variable_miss_intlit_210(self):
        input = """ string bku[]"""
        expect = "Error on line 1 col 12: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 210))
    def test_variable_wrong_intlit_211(self):
        input = """ string ppl[-1]"""
        expect = "Error on line 1 col 12: -"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    #test function
    def test_funcdeclaration_nonblock_212(self):
        input = """ int sum(int a, int b){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))
    def test_funcdeclaration_nonprameter_nonblock_213(self):
        input = """ int println(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))
    def test_funcdeclaration_nonprameter_nonblock_214(self):
        input = """ int sum(int a, int b{}"""
        expect = "Error on line 1 col 21: {"
        self.assertTrue(TestParser.checkParser(input, expect, 214))
