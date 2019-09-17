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
        self.assertTrue(TestLexer.checkLexeme("/* ab // cb \\n */", "<EOF>",106))
    def test_comment_line_3 (self):
        self.assertTrue(TestLexer.checkLexeme(''' "abc" /* abc /* // cb \\n */ ''', ''' abc,<EOF>''', 107))
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
        self.assertTrue(TestLexer.checkLexeme(''' "do\\b minh   thang" ''','''do\\b minh   thang, <EOF>''',114))
    def test_stringlit_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\nabc" """, """abc\\nabc, <EOF> """,115))
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
    def test_uncloses_tring_121(self):
        self.assertTrue(TestLexer.checkLexeme('''string "abc" "xyz''', '''STRINGTYPE, abc, Unclosed String: xyz''',121))
    def test_unclose_string_122(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme(""" "doanh\\n1243 """, """Unclosed String: doanh\\n1243 """, 122))

    #131 -> 140
    def test_illegal_escape_131(self):
        input = """ thang "123a\\m123" """
        expect = """thang,Illegal Escape In String: 123a\\m"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 131))
    def test_illegal_escape_132(self):
        input = """ chan "thiet\\chu" """
        expect = """ chan,Illegal Escape In String: thiet\\chu"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 132))

    # 141 -> 150
    def test_wrong_token_141(self):
        input = """ thang?dominh """
        expect = "thang,Error Token ?"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 141))
    def test_wrong_token_142(self):
        input = """ dominh#thang """
        expect = "dominh,Error Token #"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 142))
    def test_wrong_token_143(self):
        input = """ do~thang """
        expect = "do,Error Token ~"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 143))
    def test_wrong_token_144(self):
        input = """ bku&123 """
        expect = "bku,Error Token &"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 144))
    def test_wrong_token_145(self):
        input = """ $dominhthang """
        expect = "Error Token $"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 145))
    def test_wrong_token_146(self):
        input = """ cuong $ 123 """
        expect = "cuong,Error Token $"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 146))
    def test_wrong_token_147(self):
        input = """ minhthang`1999 """
        expect = "dominhthang,Error Token `"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 147))
    def test_wrong_token_148(self):
        input = """ xyz?123"1999 """
        expect = "xyz,Error Token ?"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))
    def test_wrong_token_149(self):
        input = """ dominhthang@1999 """
        expect = "dominhthang,Error Token @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 149))
    def test_wrong_token_150(self):
        input = """ qwe'123 """
        expect = "qwe,Error Token '"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 150))