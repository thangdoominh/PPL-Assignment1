import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
        # self.assertTrue(TestLexer.checkLexeme("aAsVN","aAsVN,<EOF>",103))
    def test_identifier_102(self):
        input = """aCBbdc"""
        expect = "aCBbdc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 102))
    def test_identifier_103(self):
        input = """aCBbdc"""
        expect = "aCBbdc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 103))
    def test_integer_1(self):
    #     """test integers"""
        self.assertTrue(TestLexer.checkLexeme('''123a123''','''123,a123,<EOF>''',104))


    # 105 -> 110
    def test_comment_line_105 (self):
        self.assertTrue(TestLexer.checkLexeme("int a; // abcxyz", "int,a,;,<EOF>",105))
    def test_comment_line_106 (self):
        self.assertTrue(TestLexer.checkLexeme("/* ab // cb \\n */", "<EOF>",106))
    def test_comment_line_107 (self):
        self.assertTrue(TestLexer.checkLexeme(''' "abc" /* abc /* // cb \\n */ ''', '''abc,<EOF>''', 107))
    def test_WS_108(self):
        input = "Alo\r lan 1\t Alo lan 2 \n"
        expect = "Alo,lan,1,Alo,lan,2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 108))
    def test_comment_line_109(self):
        input = "Alo lan 1 //abc \n\n xuong dong \n"
        expect = "Alo,lan,1,xuong,dong,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 109))


    # 111 -> 120
    def test_stringlit_1 (self):
        self.assertTrue(TestLexer.checkLexeme(''' "x y z \\b" 123''','''x y z \\b,123,<EOF>''' ,110))
    def test_stringlit_2 (self):
        self.assertTrue(TestLexer.checkLexeme(''' abc "xyz"''', '''abc,xyz,<EOF>''', 111))
    def test_stringlit_3 (self):
        self.assertTrue(TestLexer.checkLexeme(''' 123 "ab    c"''','''123,ab    c,<EOF>''',112))
    def test_stringlit_4 (self):
	    self.assertTrue(TestLexer.checkLexeme(''' "Thang" / Thang''', '''Thang,/,Thang,<EOF>''', 113))
    def test_stringlit_5(self):
        self.assertTrue(TestLexer.checkLexeme(''' "do\\b minh   thang" ''','''do\\b minh   thang,<EOF>''',114))
    def test_stringlit_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\nabc" """, """abc\\nabc,<EOF>""",115))
    def test_stringlit_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123" ""","""123a\\n123,<EOF>""", 116))
    def test_stringlit_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\\\123" ""","""123,123a\\\\123,<EOF>""",117))
    def test_stringlit_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "chan\\n qua " ""","""chan\\n qua ,<EOF>""", 118))
    def test_stringlit_10(self):
        input = """ "1234a\\n123" """
        expect = "1234a\\n123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect,119))
    def test_stringlit_120(self):
        input = """ "12 \\b 34a\\n123" """
        expect = "12 \\b 34a\\n123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect,120))

    # 121 -> 130
    def test_uncloses_tring_121(self):
        self.assertTrue(TestLexer.checkLexeme('''string "abc" "xyz''','''string,abc,Unclosed String: xyz''',121))
    def test_unclose_string_122(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme(""" "doanh\\n1243 ""","""Unclosed String: doanh\\n1243 """, 122))
    def test_wrong_token_123(self):
        input = """ "thang\\ " """
        expect = "Illegal Escape In String: thang\ "
        self.assertTrue(TestLexer.checkLexeme(input, expect, 123))
    def test_stringlit_124(self):
        input = """ "test case" \n "abc \\td" """
        expect = "test case,abc \\td,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 124))
    def test_unclose_string_125(self):
        input = """ abcd "abcd\\" """
        expect ="""abcd,Unclosed String: abcd\\" """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 125))
    def test_unclose_string_126(self):
        input = """ __int__ "abcd\\"a """
        expect ="""__int__,Unclosed String: abcd\\"a """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 126))
    def test_unclose_string_127(self):
        input = """ abcd "abcd\\" """
        expect ="""abcd,Unclosed String: abcd\\" """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 127))
    def test_string_128(self):
        input = """ zxvc \t 321\n"" """
        expect ="""zxvc,321,,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 128))
    def test_string_129(self):
        input = """ 123 \n 321 abcd\n"het biet test gi lun """
        expect ="""123,321,abcd,Unclosed String: het biet test gi lun """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 129))
    def test_unclose_string_130(self):
        input = """ 123 \n 321 abcd\n" """
        expect ="""123,321,abcd,Unclosed String:  """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 130))

    #131 -> 140
    def test_illegal_escape_131(self):
        input = """ thang "123a\\m123" """
        expect = """thang,Illegal Escape In String: 123a\\m"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 131))
    def test_illegal_escape_132(self):
        input = """ chan "thiet\\chu" """
        expect = """chan,Illegal Escape In String: thiet\\c"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 132))
    def test_illegal_escape_133(self):
        input = """ "thiet\\a do minh thang" """
        expect = """Illegal Escape In String: thiet\\a"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 133))
    def test_illegal_escape_134(self):
        input = """ "Illegal escape  ... \\d do minh thang" """
        expect = """Illegal Escape In String: Illegal escape  ... \\d"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 134))
    def test_illegal_escape_135(self):
        input = """ "Illegal Escape In String: \\B" """
        expect = """Illegal Escape In String: Illegal Escape In String: \\B"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 135))
    def test_illegal_escape_136(self):
        input = """ "Illegal escape in string: \\F" """
        expect = """Illegal Escape In String: Illegal escape in string: \\F"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 136))
    def test_illegal_escape_137(self):
        input = """ "Illegal escape in string: \\N" """
        expect = """Illegal Escape In String: Illegal escape in string: \\N"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 137))
    def test_illegal_escape_138(self):
        input = """ J4fun "Illegal escape in string: \\." """
        expect = """J4fun,Illegal Escape In String: Illegal escape in string: \\."""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 138))
    def test_illegal_escape_139(self):
        input = """ "Illegal Escape In String: \\"" """
        expect = """Illegal Escape In String: \\",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 139))
    def test_illegal_escape_140(self):
        input = """ "Illegal escape in string: \\N" """
        expect = """Illegal Escape In String: Illegal escape in string: \\N"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 140))

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
        expect = "minhthang,Error Token `"
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
    def test_wrong_token_151(self):
        input = """ |asdf """
        expect = "Error Token |"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 151))
    def test_wrong_token_152(self):
        input = """ loi token ne \\  a"""
        expect = "loi,token,ne,Error Token \\"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 152))
    def test_wrong_token_153(self):
        input = """  lai loi ne :(( \\  a"""
        expect = "lai,loi,ne,Error Token :"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 153))
    def test_wrong_token_154(self):
        input = """ fail roi ((/  @ a"""
        expect = "fail,roi,(,(,/,Error Token @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 154))
    def test_wrong_token_155(self):
        input = """ asdf ^ """
        expect = "asdf,Error Token ^"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 155))
    def test_wrong_token_156(self):
        input = """ icon ^^! """
        expect = "icon,Error Token ^"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 156))
    def test_wrong_token_157(self):
        input = """ dau_va & """
        expect = "dau_va,Error Token &"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 157))
    def test_wrong_token_158(self):
        input = """ dau_sao ne__ ^& """
        expect = "dau_sao,ne__,Error Token ^"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 158))
    def test_wrong_token_159(self):
        input = """ "string ne" loi_ne 123?321 """
        expect = "string ne,loi_ne,123,Error Token ?"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 159))
    def test_wrong_token_160(self):
        input = """ QWER@!@# """
        expect = "QWER,Error Token @"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))

    # ---- test bracket --------
    def test_bracket_161(self):
        input = """ (([({})])) """
        expect = "(,(,[,(,{,},),],),),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))
    def test_bracket_162(self):
        input = """ [mo""dong] """
        expect = "[,mo,,dong,],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 162))
    def test_bracket_163(self):
        input = """ (mo"{abc}"dong] """
        expect = "(,mo,{abc},dong,],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 163))
    def test_bracket_164(self):
        input = """ >_< """
        expect = ">,_,<,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 164))
    def test_bracket_165(self):
        input = """ >>>.< """
        expect = ">,>,>,Error Token ."
        self.assertTrue(TestLexer.checkLexeme(input, expect, 165))
    def test_bracket_166(self):
        input = """ <EOF> """
        expect = "<,EOF,>,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 166))
    def test_bracket_167(self):
        input = """ <Pl[}:<M """
        expect = "<,EOF,>,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 167))
    def test_bracket_168(self):
        input = """ <EOF> """
        expect = "<,EOF,>,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 168))
    def test_bracket_169(self):
        input = """ <EOF> """
        expect = "<,EOF,>,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 169))
    def test_bracket_170(self):
        input = """ <EOF> """
        expect = "<,EOF,>,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 170))


    def test_comment_line_152(self):
        input = "Alo lan\t 1 //abc \ndong2\n dong3 \n"
        expect = "Alo,lan,1,dong2,dong3,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))