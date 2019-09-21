import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    #ID
    def test_lower_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("123abc12tru_flase","123,abc12tru_flase,<EOF>",100))
    def test_lower_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("123abc","123,abc,<EOF>",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("aA?sVN","aA,Error Token ?",103))
    def test_integer(self):
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",104))
    def test_lower_case_id(self):
        self.assertTrue(TestLexer.checkLexeme("abc_def","abc_def,<EOF>",105))
    def test_upper_case_id(self):
        self.assertTrue(TestLexer.checkLexeme("AAA1bc","AAA1bc,<EOF>",106))
    def test_under_score_id(self):
        self.assertTrue(TestLexer.checkLexeme("___AAA1bc","___AAA1bc,<EOF>",107))
    #BRACKET    
    def test_bracket_1(self):
        self.assertTrue(TestLexer.checkLexeme("schedule(an_expression, sc_time [, sc_cycle]) (sc)","schedule,(,an_expression,,,sc_time,[,,,sc_cycle,],),(,sc,),<EOF>",108))
    def test_bracket_2(self):
        self.assertTrue(TestLexer.checkLexeme("ABC (ABC1){ABCzyz();}","ABC,(,ABC1,),{,ABCzyz,(,),;,},<EOF>",109))
    def test_bracket_3(self):
        self.assertTrue(TestLexer.checkLexeme("if ((a == 1)) {if ((b == 3)) {c = 4;}d = 5;}","if,(,(,a,==,1,),),{,if,(,(,b,==,3,),),{,c,=,4,;,},d,=,5,;,},<EOF>",110))
    def test_bracket_4(self):
        self.assertTrue(TestLexer.checkLexeme("do a+b; while(a>1)","do,a,+,b,;,while,(,a,>,1,),<EOF>",111))
    def test_bracket_5(self):
        self.assertTrue(TestLexer.checkLexeme("foo(foo(foo(foo(foo(foo())))))","foo,(,foo,(,foo,(,foo,(,foo,(,foo,(,),),),),),),<EOF>",112))
    #OP
    def test_op_1(self):
        self.assertTrue(TestLexer.checkLexeme("a||b+b!=c","a,||,b,+,b,!=,c,<EOF>",113))
    def test_op_2(self):
        self.assertTrue(TestLexer.checkLexeme("a>c>=&&*!c","a,>,c,>=,&&,*,!,c,<EOF>",114))
    def test_op_3(self):
        self.assertTrue(TestLexer.checkLexeme("!a!d=abc>c=d==e","!,a,!,d,=,abc,>,c,=,d,==,e,<EOF>",115))
    def test_op_4(self):
        self.assertTrue(TestLexer.checkLexeme("a+b-c/*d","a,+,b,-,c,/,*,d,<EOF>",116))
    def test_op_5(self):
        self.assertTrue(TestLexer.checkLexeme("!a&&b+(a||c)+d","!,a,&&,b,+,(,a,||,c,),+,d,<EOF>",117))
    def test_op_6(self):
        self.assertTrue(TestLexer.checkLexeme("a<=c+d % d","a,<=,c,+,d,%,d,<EOF>",118))
    def test_op_7(self):
        self.assertTrue(TestLexer.checkLexeme("a-b-c+e%f","a,-,b,-,c,+,e,%,f,<EOF>",119))
    def test_op_8(self):
        self.assertTrue(TestLexer.checkLexeme("a||c>d+e--f","a,||,c,>,d,+,e,-,-,f,<EOF>",120))
    def test_op_9(self):
        self.assertTrue(TestLexer.checkLexeme("a++++++++++","a,+,+,+,+,+,+,+,+,+,+,<EOF>",121))
    def test_op_10(self):
        self.assertTrue(TestLexer.checkLexeme(">>===abc",">,>=,==,abc,<EOF>",122))
    #FLOATLIT
    def test_float_lit_1(self):
        self.assertTrue(TestLexer.checkLexeme("a=1.2 a=1. a=.1 a=1e2 ","a,=,1.2,a,=,1.,a,=,.1,a,=,1e2,<EOF>",123))
    def test_float_lit_2(self):
        self.assertTrue(TestLexer.checkLexeme("a=1.2 a=12 e=1.2e-2 e=.1E2 e=9.0 e=12e8 e= 0.33E-3 e=128e-42","a,=,1.2,a,=,12,e,=,1.2e-2,e,=,.1E2,e,=,9.0,e,=,12e8,e,=,0.33E-3,e,=,128e-42,<EOF>",124))
    def test_float_lit_3(self):
        self.assertTrue(TestLexer.checkLexeme(".0e12,0.e13,,.0E-0",".0e12,,,0.e13,,,,,.0E-0,<EOF>",125))
    def test_float_lit_4(self):
        self.assertTrue(TestLexer.checkLexeme(" a=1.2E-2 e=1.2e-2 e=.1E2 e=9.0 e=12e8 e= 0.33E-3 e=128e-42","a,=,1.2E-2,e,=,1.2e-2,e,=,.1E2,e,=,9.0,e,=,12e8,e,=,0.33E-3,e,=,128e-42,<EOF>",126))
    def test_float_lit_5(self):
        self.assertTrue(TestLexer.checkLexeme("a=1.2 a=1. a=.1 a=1e2 a=1.2E-2 e=1.2e-2 e=.1E2 e=9.0 e=12e8 e= 0.33E-3 e=128e-42","a,=,1.2,a,=,1.,a,=,.1,a,=,1e2,a,=,1.2E-2,e,=,1.2e-2,e,=,.1E2,e,=,9.0,e,=,12e8,e,=,0.33E-3,e,=,128e-42,<EOF>",127))
    def test_float_lit_6(self):
        self.assertTrue(TestLexer.checkLexeme(" e= 0.33E-3 e=128e-42","e,=,0.33E-3,e,=,128e-42,<EOF>",128))
    def test_float_lit_7(self):
        self.assertTrue(TestLexer.checkLexeme("a=1.2 a=1. a=.1 a=1ecde2 a=1.2E-2 e=1.2e-2 c=e-42","a,=,1.2,a,=,1.,a,=,.1,a,=,1,ecde2,a,=,1.2E-2,e,=,1.2e-2,c,=,e,-,42,<EOF>",129))
    def test_float_lit_8(self):
        self.assertTrue(TestLexer.checkLexeme(" a=1.2e1.3.4e-7","a,=,1.2e1,.3,.4e-7,<EOF>",130))
    #COMMENT
    def test_cmt_1(self):
        self.assertTrue(TestLexer.checkLexeme("//abcxyz","<EOF>",131))
    def test_cmt_2(self):
        self.assertTrue(TestLexer.checkLexeme("/*abc*/123a=1","123,a,=,1,<EOF>",132))
    def test_cmt_3(self):
        self.assertTrue(TestLexer.checkLexeme(" //TO DO/*dsddsdsdsds*/","<EOF>",133))
    def test_cmt_4(self):
        self.assertTrue(TestLexer.checkLexeme("/*acccx/*c/*xc*/*/*/*/","*,<EOF>",134))
    def test_cmt_5(self):
        self.assertTrue(TestLexer.checkLexeme(" /*a*/axxcxc/*a*/","axxcxc,<EOF>",135))
    def test_cmt_6(self):
        self.assertTrue(TestLexer.checkLexeme(" /*/*abc*/*/","*,/,<EOF>",136))
    def test_cmt_7(self):
        self.assertTrue(TestLexer.checkLexeme(" //axcc*/","<EOF>",137))
    def test_cmt_8(self):
        self.assertTrue(TestLexer.checkLexeme(" /*//*/*/*/*/*/*/*?*/","*,*,<EOF>",138))
    def test_cmt_9(self):
        self.assertTrue(TestLexer.checkLexeme(" /*//*/?/*/*/*/*/*?*/","Error Token ?",139))
    def test_cmt_10(self):
        self.assertTrue(TestLexer.checkLexeme(" /*//*/?/*/*/*/*/*?*//**//////*/*/","Error Token ?",140))
    def test_cmt_11(self):
        self.assertTrue(TestLexer.checkLexeme("*/*/*/*/*/*/*/*/*/","*,*,*,<EOF>",141))
    def test_cmt_12(self):
        self.assertTrue(TestLexer.checkLexeme(" .1/*/*/*/*/*/*/*/*/",".1,*,*,<EOF>",142))
    def test_cmt_13(self):
        self.assertTrue(TestLexer.checkLexeme(" */*/*/*/*/*/*/*/*/","*,*,*,<EOF>",143))
    def test_cmt_14(self):
        self.assertTrue(TestLexer.checkLexeme(" _122/*/*/./*/*/*/*/*/","_122,Error Token .",144))
    def test_cmt_15(self):
        self.assertTrue(TestLexer.checkLexeme(" abcx12/*/*/!/*/*/*/*/*/","abcx12,!,*,<EOF>",145))
    def test_cmt_16(self):
        self.assertTrue(TestLexer.checkLexeme(" 123/123/*/*/*/while/*/*/*/","123,/,123,*,/,while,*,/,<EOF>",146))
    def test_cmt_17(self):
        self.assertTrue(TestLexer.checkLexeme(" */*/*/*/*/*/*/*/*/7","*,*,*,7,<EOF>",147))
    def test_cmt_18(self):
        self.assertTrue(TestLexer.checkLexeme(" */*/*/*/*////*/*/*/*/","*,*,*,<EOF>",148))
    def test_cmt_19(self):
        self.assertTrue(TestLexer.checkLexeme(" */*/*/true||false/*/*/*/*/*/","*,true,||,false,*,<EOF>",149))
    def test_cmt_20(self):
        self.assertTrue(TestLexer.checkLexeme(" */*/*/*/*/*/for(a[])/*/*/","*,*,for,(,a,[,],),<EOF>",150))
    #INTEGER
    def test_int_1(self):
        self.assertTrue(TestLexer.checkLexeme("a=123+b-34*000023","a,=,123,+,b,-,34,*,000023,<EOF>",151))
    def test_int_2(self):
        self.assertTrue(TestLexer.checkLexeme(" a[[[[0012/.1e12]]]]","a,[,[,[,[,0012,/,.1e12,],],],],<EOF>",152))
    def test_int_3(self):
        self.assertTrue(TestLexer.checkLexeme("0000000a_0a","0000000,a_0a,<EOF>",153))
    def test_int_4(self):
        self.assertTrue(TestLexer.checkLexeme(" 0e12","0e12,<EOF>",154))
    def test_int_5(self):
        self.assertTrue(TestLexer.checkLexeme("if(remainder<10)hex[id]=48+remainder;","if,(,remainder,<,10,),hex,[,id,],=,48,+,remainder,;,<EOF>",155))
    #MIX
    def test_mix_1(self):
        self.assertTrue(TestLexer.checkLexeme(" arr[j] = arr[j] * 10 + (str[i] - 48);","arr,[,j,],=,arr,[,j,],*,10,+,(,str,[,i,],-,48,),;,<EOF>",156))
    def test_mix_2(self):
        self.assertTrue(TestLexer.checkLexeme(" FILE *file_o = fopen ( filename_o, w );","FILE,*,file_o,=,fopen,(,filename_o,,,w,),;,<EOF>",157))
    def test_mix_3(self):
        self.assertTrue(TestLexer.checkLexeme("int arr[MAX]={0};","int,arr,[,MAX,],=,{,0,},;,<EOF>",158))
    def test_mix_4(self):
        self.assertTrue(TestLexer.checkLexeme(" int str_length = strlen(str);","int,str_length,=,strlen,(,str,),;,<EOF>",159))
    def test_mix_5(self):
        self.assertTrue(TestLexer.checkLexeme("i = 0; str[i] != 0; i++","i,=,0,;,str,[,i,],!=,0,;,i,+,+,<EOF>",160))
    #STRINGLIT
    def test_string_1(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n12\\b3" ""","""123a\\n12\\b3,<EOF>""",161))
    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n1\\rt23" ""","""123a\\n1\\rt23,<EOF>""",162))
    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n1\\"23" ""","""123a\\n1\\"23,<EOF>""",163))
    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme("""  "123a" ""","""123a,<EOF>""",164))
    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a"abc"123\\b" ""","""123a,abc,123\\b,<EOF>""",165))
    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "12"3.1e-12*"n123" ""","""12,3.1e-12,*,n123,<EOF>""",166))
    def test_string_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\\\abczy123" ""","""123a\\\\abczy123,<EOF>""",167))
    def test_string_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" printf("%c",hex[i]); ""","""printf,(,%c,,,hex,[,i,],),;,<EOF>""",168))
    def test_string_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" fprintf(file_o,"*********NEW TEST*********\\n"); ""","""fprintf,(,file_o,,,*********NEW TEST*********\\n,),;,<EOF>""",169))
    def test_string_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\\\123" ""","""123,123a\\\\123,<EOF>""",170))
    def test_string_11(self):
        self.assertTrue(TestLexer.checkLexeme("""fprintf(file_o,"\\n"); ""","""fprintf,(,file_o,,,\\n,),;,<EOF>""",187))
    def test_string_12(self):
        self.assertTrue(TestLexer.checkLexeme(""" fprintf(file_o,"%d",k); ""","""fprintf,(,file_o,,,%d,,,k,),;,<EOF>""",188))
    def test_string_13(self):
        self.assertTrue(TestLexer.checkLexeme(""" system("cls"); printf("test!\\t"); ""","""system,(,cls,),;,printf,(,test!\\t,),;,<EOF>""",189))
    def test_string_14(self):
        self.assertTrue(TestLexer.checkLexeme(""" scanf("%d",&&luachon); ""","""scanf,(,%d,,,&&,luachon,),;,<EOF>""",190))
    def test_string_15(self):
        self.assertTrue(TestLexer.checkLexeme(""" //"???" ""","""<EOF>""",191))
    def test_string_16(self):
        self.assertTrue(TestLexer.checkLexeme(""" +-*//*"??""?"*/ ""","""+,-,*,<EOF>""",192))
    #UNCLOSED
    def test_unclose_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\n123 ""","Unclosed String: 123a\\n123 ",171))
    def test_unclose_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\n\n ""","Unclosed String: 123a",172))#?????
    def test_unclose_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "a" "aa" "" " ""","a,aa,,Unclosed String:  ",173))#?????
    def test_unclose_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\123a\\n123 ""","Illegal Escape In String: \\1",174))
    def test_unclose_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc"xyz"mnl ""","abc,xyz,Unclosed String: mnl ",175))
    def test_unclose_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" print("div none,a[13]); ""","print,(,Unclosed String: div none,a[13]); ",176))
    def test_unclose_string_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" scanf("abc,); ""","scanf,(,Unclosed String: abc,); ",177))
    def test_unclose_string_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" _abc="//abcd ""","_abc,=,Unclosed String: //abcd ",178))
    #ILLEGAL ESCAPE
    def test_illegal_escape_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\m123" ""","123,Illegal Escape In String: 123a\\m",179))
    def test_illegal_escape_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\\\\\m123" ""","123,Illegal Escape In String: 123a\\\\\\m",180))
    def test_illegal_escape_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\m123""\\a" ""","Illegal Escape In String: 123a\\m",181))
    def test_illegal_escape_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\am123" ""","Illegal Escape In String: 123a\\a",182))
    def test_illegal_escape_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\\\a"// "123a\\m123" ""","\\\\a,<EOF>",183))
    def test_illegal_escape_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\!" "123a\\m123" ""","Illegal Escape In String: \\!",184))
    def test_illegal_escape_7(self):
        self.assertTrue(TestLexer.checkLexeme("""  "123""a\\****m123" ""","123,Illegal Escape In String: a\\*",185))
    def test_illegal_escape_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123a\\_sncxyz123" ""","Illegal Escape In String: 123a\\_",186))
    #ERROR CHAR
    def test_error_char_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" ""??"" """,",Error Token ?",193))
    def test_error_char_2(self):
        self.assertTrue(TestLexer.checkLexeme(" print('error?');  ","print,(,Error Token '",194))
    def test_error_char_3(self):
        self.assertTrue(TestLexer.checkLexeme(" _@abc=xyz ","_,Error Token @",195))
    def test_error_char_4(self):
        self.assertTrue(TestLexer.checkLexeme(" 12..12*.e-6 ","12.,.12,*,Error Token .",196))
    def test_error_char_5(self):
        self.assertTrue(TestLexer.checkLexeme(" _abc/? ","_abc,/,Error Token ?",197))
    def test_error_char_6(self):
        self.assertTrue(TestLexer.checkLexeme(" a&b=true","a,Error Token &",198))
    def test_error_char_7(self):
        self.assertTrue(TestLexer.checkLexeme("_########Test ","_,Error Token #",199))
    