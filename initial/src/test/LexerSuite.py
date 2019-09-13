import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
        # self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
        # self.assertTrue(TestLexer.checkLexeme("aAsVN","aAsVN,<EOF>",103))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme('''int main(){FLOAT a; "abc" = 1.0;}''','''"abc",<EOF>''',104))

    # 105 -> 110
    def test_comment_line_1 (self):
        self.assertTrue(TestLexer.checkLexeme("int a; // abcxyz", "int,a,;,<EOF>",105))
    def test_comment_line_2 (self):
        self.assertTrue(TestLexer.checkLexeme("/* ab // cb \n */", "<EOF>",106))
    def test_comment_line_3 (self):
        self.assertTrue(TestLexer.checkLexeme('''"abc" /* abc /* // cb \n */''', '''"<EOF>"''', 107))
    # def test_comment_line_4 (self):
        # self.assertTrue(TestLexer.checkLexeme(,,108))

    # 111 -> 120
    # def test_stringlit_(self):
        # self.assertTrue(TestLexer.checkLexeme(,,110))

    # 121 -> 130
    def test_unclosestring(self):
        self.assertTrue(TestLexer.checkLexeme('''string "abc" "xyz''','''string, abc, "xyz, "EOF"''',121))