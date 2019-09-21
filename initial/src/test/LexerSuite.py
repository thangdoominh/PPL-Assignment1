import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
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
        expect = "<,Pl,[,},Error Token :"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 167))
    def test_bracket_168(self):
        input = """ [\n[\n[\t[/[//[[]]]]]] """
        expect = "[,[,[,[,/,[,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 168))
    def test_bracket_169(self):
        input = """ <<<{123{-zaz13{[] """
        expect = "<,<,<,{,123,{,-,zaz13,{,[,],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 169))
    def test_bracket_170(self):
        input = """ foo(\t)[thang] /* {[]}() */ """
        expect = "foo,(,),[,thang,],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 170))

#------------- TEST FLOATING POINTS ------------------------------
    def test_floating_points_171(self):
        input = """ 1.2 1. 1.e2 1.2E-2 """
        expect = "1.2,1.,1.e2,1.2E-2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 171))
    def test_floating_points_172(self):
        input = """ "\**\" """
        expect = "Illegal Escape In String: \*"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 172))
    def test_floating_points_173(self):
        input = """ 1.3e-2 9.0 12e8 0.33E-3 128e-42 """
        expect = "1.3e-2,9.0,12e8,0.33E-3,128e-42,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 173))
    def test_floating_points_174(self):
        input = """ .1 """
        expect = ".1,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 174))
    def test_floating_points_175(self):
        input = """ thang .1E2 """
        expect = "thang,.1E2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 175))
    def test_floating_points_176(self):
        input = """ 00.00e2 """
        expect = "00.00e2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))
    def test_floating_points_177(self):
        input = """ if error is fall .e2"""
        expect = "if,error,is,fall,Error Token ."
        self.assertTrue(TestLexer.checkLexeme(input, expect, 177))
    def test_floating_points_178(self):
        input = """ 1.e2 """
        expect = "1.e2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))
    def test_floating_points_179(self):
        input = """ e-12 """
        expect = "e,-,12,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 179))
    def test_floating_points_180(self):
        input = """ 143e """
        expect = "143,e,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 180))

#-------------------- overall -------------------
    def test_overall_181(self):
        input = """ line1 \\n line2 \n line3 """
        expect = "line1,Error Token \\"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 181))
    def test_overall_182(self):
        input = """ dong1 //dong2 \n dong3 """
        expect = "dong1,dong3,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 182))
    def test_overall_183(self):
        input = """ Thang \r Phong \n Thuan"""
        expect = "Thang,Phong,Thuan,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 183))
    def test_overall_184(self):
        input = """ So1 \r So2 // So3 \n So4 """
        expect = "So1,So2,So4,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 184))
    def test_overall_185(self):
        input = """ SV1 // \r SV2 SV3 \n SV4  """
        expect = "SV1,SV2,SV3,SV4,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 185))
    def test_overall_186(self):
        input = """ a \r b \r c \n d  """
        expect = "a,b,c,d,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 186))
    #?????? khoong chac
    def test_overall_187(self):
        input = """ Commentline // a \r b \t c \b d\f """
        expect = "Commentline,b,c,d,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 187))
    def test_overall_188(self):
        input = """ test cmt // 1 \r\r 2\n\n3\t """
        expect = "test,cmt,2,3,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 188))
    def test_overall_189(self):
        input = """ "honghieu \\" """
        expect = 'Unclosed String: honghieu \\" '
        self.assertTrue(TestLexer.checkLexeme(input, expect, 189))
    def test_overall_190(self):
        input = """ "vanchuahieu \\ " """
        expect = "Illegal Escape In String: vanchuahieu \\ "
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))
    def test_overall_191(self):
        input = """ 3dau\\ "test"  """
        expect = "3,dau,Error Token \\"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))
    def test_overall_192(self):
        input = """ 3dau "test \\\"  """
        expect = "3,dau,Unclosed String: test \\\"  "
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))
    def test_overall_193(self):
        input = """ 4dau "thu \\\\"  """
        expect = "4,dau,thu \\\\,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))
    def test_overall_194(self):
        input = """ 4daucocach "thu \\\\a "  """
        expect = "4,daucocach,thu \\\\a ,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))
    def test_overall_195(self):
        input = """ 5gach "a \\\\\" """
        expect = "5,gach,a \\\\,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))
    def test_overall_196(self):
        input = """ 5gachspace "5 \\\\\a "  """
        expect = "5,gachspace,5 \\\\ ,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))
    def test_overall_197(self):
        input = """ "string \\\\\c "  """
        expect = "Illegal Escape In String: string \\\\\c"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))
    def test_overall_198(self):
        input = """ 3dau "abc \\\est"  """
        expect = "3,dau,abc \\\est,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))

    def test_wrong_token_199(self):
        input = """ error dot . """
        expect = "error,dot,Error Token ."
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))
    def test_comment_line_200(self):
        input = "Alo lan\t 1 //abc \ndong2\n dong3 \n"
        expect = "Alo,lan,1,dong2,dong3,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))