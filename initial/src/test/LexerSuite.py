import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
        # self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
        # self.assertTrue(TestLexer.checkLexeme("aAsVN","aAsVN,<EOF>",103))
    # def test_integer_1(self):
    #     """test integers"""
        # self.assertTrue(TestLexer.checkLexeme('''int main(){FLOAT a; "abc" = 1.0;}''','''abc,<EOF>''',104))


    # 105 -> 110
    def test_comment_line_1 (self):
        self.assertTrue(TestLexer.checkLexeme("int a; // abcxyz", "int,a,;,<EOF>",105))
    def test_comment_line_2 (self):
        self.assertTrue(TestLexer.checkLexeme("/* ab // cb \n */", "<EOF>",106))
    def test_comment_line_3 (self):
        self.assertTrue(TestLexer.checkLexeme('''"abc" /* abc /* // cb \n */''', '''<EOF>''', 107))
    # def test_comment_line_4 (self):
        # self.assertTrue(TestLexer.checkLexeme(,108))

    # 111 -> 120
    def test_stringlit_1 (self):
        self.assertTrue(TestLexer.checkLexeme(''' "x y z \\b" 123''',''' "x y z \\b", 123, <EOF>''' ,110))
    def test_stringlit_2 (self):
        self.assertTrue(TestLexer.checkLexeme(''' abc "xyz"''', '''abc, xyz, <EOF>''', 111))
    def test_stringlit_3 (self):
        self.assertTrue(TestLexer.checkLexeme(''' 123 "ab    c"''','''123,ab   c,<EOF>''',112))
    def test_stringlit_4 (self):
	    self.assertTrue(TestLexer.checkLexeme(''' "Thang" / Thang''', ''' Thang, /, Thang, <EOF>''', 113))
    def test_stringlit_5(self):
        self.assertTrue(TestLexer.checkLexeme(''' "do\b minh   thang" ''','''do\b minh   thang, <EOF>''',114))
    def test_stringlit_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\abc" """, """abc\\abc, <EOF> """,115))
    def test_stringlit_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123" ""","""123a\\n123,<EOF>""", 116))
    def test_stringlit_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\\\123" ""","""123,123a\\\\123,<EOF>""",117))
    def test_stringlit_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "chan\\n qua " ""","""chan\\n qua,<EOF>""", 118))
    def test_stringlit_10(self):
        input = """ "1234a\\n123" """
        expect = "1234a\\n123, <EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect,119))
    def test_stringlit_120(self):
        input = """ "1234a\\n123" """
        expect = "1234a\\n123, <EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect,120))

    # 121 -> 130
    def test_unclosestring(self):
        self.assertTrue(TestLexer.checkLexeme('''string "abc" "xyz''', '''string, abc, "xyz, "EOF"''',121))