import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # Identifier
    def test_identifier1(self):
        self.assertTrue(TestLexer.test("aBc", "aBc,<EOF>", 101))

    def test_identifier2(self):
        self.assertTrue(TestLexer.test("8cjj", "8,cjj,<EOF>", 102))

    def test_identifier3(self):
        self.assertTrue(TestLexer.test("ajc_sjs", "ajc_sjs,<EOF>", 1033))

    def test_identifier4(self):
        self.assertTrue(TestLexer.test("_@#", "_,Error Token @", 104))

    def test_identifier5(self):
        self.assertTrue(TestLexer.test(";asd @", ";,asd,Error Token @", 105))

    def test_identifier6(self):
        self.assertTrue(TestLexer.test("asd Asd asd9 a9 _9 _ha","asd,Asd,asd9,a9,_9,_ha,<EOF>", 106))

    # Integer
    def test_integer1(self):
        self.assertTrue(TestLexer.test(
            "01 012 025 1365", "01,012,025,1365,<EOF>", 107))

    def test_integer2(self):
        self.assertTrue(TestLexer.test("1ab", "1,ab,<EOF>", 108))

    def test_integer3(self):
        self.assertTrue(TestLexer.test("12cb289.90", "12,cb289,.90,<EOF>", 109))

    # Real
    def test_real1(self):
        self.assertTrue(TestLexer.test("1.1", "1.1,<EOF>", 110))

    def test_real2(self):
        self.assertTrue(TestLexer.test(".2", ".2,<EOF>", 111))

    def test_real3(self):
        self.assertTrue(TestLexer.test("3.", "3.,<EOF>", 112))

    def test_real4(self):
        self.assertTrue(TestLexer.test("3e2", "3e2,<EOF>", 113))

    def test_real5(self):
        self.assertTrue(TestLexer.test("1.2e-5", "1.2e-5,<EOF>", 114))

    def test_err_real1(self):
        self.assertTrue(TestLexer.test("e12", "e12,<EOF>", 115))

    def test_err_real2(self):
        self.assertTrue(TestLexer.test("e-12", "e,-,12,<EOF>", 116))

    def test_err_real3(self):
        self.assertTrue(TestLexer.test(".e12", "Error Token .", 117))
    
    
    # Comment

    def test_comment1(self):
        self.assertTrue(TestLexer.test("abc//a", "abc,<EOF>", 118))

    def test_comment2(self):
        self.assertTrue(TestLexer.test(
            "abc//comment \r\nxyz", "abc,xyz,<EOF>", 119))

    def test_comment3(self):
        self.assertTrue(TestLexer.test("{this is comment}", "<EOF>", 120))

    def test_comment4(self):
        self.assertTrue(TestLexer.test("//abc a \b \r \n //a", "<EOF>", 121))

    def test_comment5(self):
        self.assertTrue(TestLexer.test(
            "//xixindep\n1611dgdfg", "1611,dgdfg,<EOF>", 122))

    def test_comment6(self):
        self.assertTrue(TestLexer.test(
            "(*abcd(*abcd*)abcd*)", "abcd,*,),<EOF>", 123))

    def test_comment7(self):
        self.assertTrue(TestLexer.test(
            "//abcd(*ab//cd\nabcd*)", "abcd,*,),<EOF>", 124))

    def test_comment8(self):
        self.assertTrue(TestLexer.test(
            "(*{abcd(*abcd*)}abcd*)", "Error Token }", 125))

    def test_comment9(self):
        self.assertTrue(TestLexer.test(
            "(*/gdfg/fdfd)*)//fdzdsfdsfdf", "<EOF>", 126))

    def test_comment10(self):
        self.assertTrue(TestLexer.test(
            "(*//xi xinhdep}*)\n/ff", "/,ff,<EOF>", 127))

    def test_comment11(self):
        self.assertTrue(TestLexer.test("abcd(*abcd*)abcd*)",
                                       "abcd,abcd,*,),<EOF>", 128))

    def test_comment12(self):
        self.assertTrue(TestLexer.test(
            "(//abcd(*ab}xx*)cd/nabcd*)", "(,<EOF>", 129))

    def test_comment13(self):
        self.assertTrue(TestLexer.test(
            "((*abcd(*ab}xx*)cd\nabcd*)", "(,cd,abcd,*,),<EOF>", 130))

    def test_comment14(self):
        self.assertTrue(TestLexer.test(
            "(*//aaaa {*)xinhdep*)\n//ff", "xinhdep,*,),<EOF>", 131))

    def test_comment15(self):
        self.assertTrue(TestLexer.test("\\asdsad}*)\n/ff","Illegal Escape In String: ", 132))
    # String

    def test_string1(self):
        self.assertTrue(TestLexer.test("\"string\"", "string,<EOF>", 133))

    def test_string2(self):
        self.assertTrue(TestLexer.test("\"svaf \\b \"", "svaf \\b ,<EOF>", 134))

    def test_string3(self):
        self.assertTrue(TestLexer.test("\"\"", ",<EOF>", 135))

    def test_string4(self):
        self.assertTrue(TestLexer.test("\"_!@#$%^\"", "_!@#$%^,<EOF>", 136))

    def test_string5(self):
        self.assertTrue(TestLexer.test(
            "\"182mcelv03j.20\"", "182mcelv03j.20,<EOF>", 137))

    def test_string6(self):
        self.assertTrue(TestLexer.test(' "XI xinh dep"',"XI xinh dep,<EOF>",138))

    def test_string7(self):
        self.assertTrue(TestLexer.test('(*fsfsdfd*)hii[1]','hii,[,1,],<EOF>',139))
    
    def test_string9(self):
        self.assertTrue(TestLexer.test("\"day la ass\" mot \"","day la ass,mot,Unclosed String: ", 140))

    # Keyword

    def test_keyword1(self):
        self.assertTrue(TestLexer.test("FUNCTION", "FUNCTION,<EOF>", 141))

    def test_keyword2(self):
        self.assertTrue(TestLexer.test("fUncTion", "fUncTion,<EOF>", 142))

    def test_keyword3(self):
        self.assertTrue(TestLexer.test("boolean break continue else for", "boolean,break,continue,else,for,<EOF>", 143))

    def test_keywords4(self):
        self.assertTrue(TestLexer.test("break continue for to downto do", "break,continue,for,to,downto,do,<EOF>", 144))

    def test_keywords5(self):
        self.assertTrue(TestLexer.test("if then else return while begin end function","if,then,else,return,while,begin,end,function,<EOF>", 145))

    # Operator
    def test_operator1(self):
        self.assertTrue(TestLexer.test("+slc-slc*sj", "+,slc,-,slc,*,sj,<EOF>", 146))

    def test_operator2(self):
        self.assertTrue(TestLexer.test("+ - * $ % ^", "+,-,*,Error Token $", 147))

    def test_operator3(self):
        self.assertTrue(TestLexer.test("+-*/not mod or and","+,-,*,/,not,mod,or,and,<EOF>", 148))

    def test_operator4(self):
        self.assertTrue(TestLexer.test("<> = < > <= >= div","<>,=,<,>,<=,>=,div,<EOF>", 149))

    def test_operator5(self):
        self.assertTrue(TestLexer.test("<= >= aNd oR == :=","<=,>=,aNd,oR,=,=,:=,<EOF>", 150))

    def test_operator6(self):
        self.assertTrue(TestLexer.test("5+7*(9-3)/(6+7)","5,+,7,*,(,9,-,3,),/,(,6,+,7,),<EOF>", 151))

    def test_operator7(self):
        self.assertTrue(TestLexer.test("+ * =", "+,*,=,<EOF>", 152))

    def test_operator8(self):
        self.assertTrue(TestLexer.test("+123+24", "+,123,+,24,<EOF>", 153))

    # Seperator
    def test_seperator1(self):
        self.assertTrue(TestLexer.test("sdjksd,jksd:sdjska","sdjksd,,,jksd,:,sdjska,<EOF>", 154))

    def test_seperator2(self):
        self.assertTrue(TestLexer.test(",.&,:", ",,Error Token .", 155))

    def test_seperator3(self):
        self.assertTrue(TestLexer.test("..(]{())", "..,(,],Error Token {", 156))

    # Error
    def test_error1(self):
        self.assertTrue(TestLexer.test(
            "\"sjcl{\n\s\m\d\s\tsjdk\"", "Unclosed String: sjcl{", 157))

    def test_error2(self):
        self.assertTrue(TestLexer.test(
            "35=sllx=10;{aAs\a\b\c\d\}e\f\g\h\i\j\k\l\m\\q'N}i=5;", "35,=,sllx,=,10,;,e,Error Token ", 158))

    def test_error3(self):
        self.assertTrue(TestLexer.test(
            "\"sjcjsl", "Unclosed String: sjcjsl", 159))

    def test_error4(self):
        self.assertTrue(TestLexer.test("\"aavbbb\nihaa\"","Unclosed String: aavbbb", 160))

    def test_error5(self):
        self.assertTrue(TestLexer.test("ONE 2 THREE ^ FOUR","ONE,2,THREE,Error Token ^", 161))

    
    def test_index(self):
        self.assertTrue(TestLexer.test("ONE[1]", "ONE,[,1,],<EOF>", 162))

    def test_exp(self):
        self.assertTrue(TestLexer.test(
            "1 := 2 + 3 * 4", "1,:=,2,+,3,*,4,<EOF>", 163))

    def test_unclose(self):
        self.assertTrue(TestLexer.test("\"Unclose_string","Unclosed String: Unclose_string",164))

    def test_block_cmt2(self):
        self.assertTrue(TestLexer.test(
            "3=5=r=10;{aAs\a\b\c\d\e\f\g\h\i\j\k\l\m\\q'N}i=5;", "3,=,5,=,r,=,10,;,i,=,5,;,<EOF>", 165))

    def test_brack(self):
        self.assertTrue(TestLexer.test(
            "[]();:..,", "[,],(,),;,:,..,,,<EOF>", 166))

    def test_function1(self):
        self.assertTrue(TestLexer.test("function a():integer;","function,a,(,),:,integer,;,<EOF>", 167))

    def test_function2(self):
        self.assertTrue(TestLexer.test("function f ( ) : integer ;begin return 200; end","function,f,(,),:,integer,;,begin,return,200,;,end,<EOF>", 168))

    def test_function_index(self):
        self.assertTrue(TestLexer.test("foo(2)[3+x]", "foo,(,2,),[,3,+,x,],<EOF>", 169))
    
    def test_procedure_main(self):
        self.assertTrue(TestLexer.test("procedure main ();","procedure,main,(,),;,<EOF>", 170))

    def test_var(self):
        self.assertTrue(TestLexer.test(
            "var i : array [1 ..5] of integer ;", "var,i,:,array,[,1,..,5,],of,integer,;,<EOF>", 171))

    def test_escape(self):
        self.assertTrue(TestLexer.test("\"dkjoiue\\s\"","Unclosed String: dkjoiue", 172))

    def test_escape2(self):
        self.assertTrue(TestLexer.test(
            "\"aA\tqq\\a\rd\n\fsVNgge\"", "Unclosed String: aA", 173))

    def test_escape3(self):
        self.assertTrue(TestLexer.test("\"aAsVN\r\rgge","Unclosed String: aAsVN", 174))

    def test_procedure(self):
        self.assertTrue(TestLexer.test(
            "procedure goo( x : array [ 1 .. 2] of real);", "procedure,goo,(,x,:,array,[,1,..,2,],of,real,),;,<EOF>", 175))

    def test_if1(self):
        self.assertTrue(TestLexer.test(
            "if (1) then return 2.3; //CORRECT else return 2 ;", "if,(,1,),then,return,2.3,;,<EOF>", 176))

    def test_if2(self):
        self.assertTrue(TestLexer.test("if x > y then m := y; else m := x ;","if,x,>,y,then,m,:=,y,;,else,m,:=,x,;,<EOF>", 177))

    def test_assign(self):
        self.assertTrue(TestLexer.test("a := b [10] := foo()[3] := x := 1 ;", "a,:=,b,[,10,],:=,foo,(,),[,3,],:=,x,:=,1,;,<EOF>", 178))

    def test_doubledot(self):
        self.assertTrue(TestLexer.test("1..2", "1.,.2,<EOF>", 179))

    def test_forstm(self):
        self.assertTrue(TestLexer.test("for i := 1 to n do begin end", "for,i,:=,1,to,n,do,begin,end,<EOF>", 180))

    def test_kw_or(self):
        self.assertTrue(TestLexer.test("or OR oR","or,OR,oR,<EOF>",181))

    def test_kw_div(self):
        self.assertTrue(TestLexer.test("div 20 div 3dIV 3","div,20,div,3,dIV,3,<EOF>",182))

    def test_kw_mod(self):
        self.assertTrue(TestLexer.test("mod 100 mOD 7 div -4e3moD 9","mod,100,mOD,7,div,-,4e3,moD,9,<EOF>",183))

    def test_space_0(self):
        self.assertTrue(TestLexer.test("\t","<EOF>",184))

    def test_space_1(self):
        self.assertTrue(TestLexer.test("\r\t.3e10\t",".3e10,<EOF>",185))

    def test_space_2(self):
        self.assertTrue(TestLexer.test("\n\n\n","<EOF>",186))

    def test_space_3(self):
        self.assertTrue(TestLexer.test("abc\t\tbcXd","abc,bcXd,<EOF>",187))

    def test_space_4(self):
        self.assertTrue(TestLexer.test("\tbienbien\t","bienbien,<EOF>",188))
        
    def test_op_1(self):
        self.assertTrue(TestLexer.test("a:=b/2 >= 2 \n<=3","a,:=,b,/,2,>=,2,<=,3,<EOF>",189))

    def test_op_2(self):
        self.assertTrue(TestLexer.test("a>b<c=d+e+f","a,>,b,<,c,=,d,+,e,+,f,<EOF>",190))
    
    def test_op_3(self):
        self.assertTrue(TestLexer.test("a<>b :=c {asc <5}","a,<>,b,:=,c,<EOF>",191))

    def test_op_4(self):
        self.assertTrue(TestLexer.test("5*3:=a+5>=4","5,*,3,:=,a,+,5,>=,4,<EOF>",192))

    def test_str_unclosed_1(self):
        self.assertTrue(TestLexer.test(""" "Not string""","Unclosed String: Not string",193))

    def test_str_unclosed_2(self):
        self.assertTrue(TestLexer.test(""" Not string"  ""","Not,string,Unclosed String:   ",194))
    
    def test_keywords_with(self):
        self.assertTrue(TestLexer.test("with WiTH 4wiTH with3 asWITH 3.4e10WITH","with,WiTH,4,wiTH,with3,asWITH,3.4e10,WITH,<EOF>",195))

    def test_separators(self):
        self.assertTrue(TestLexer.test("((()))[[]]","(,(,(,),),),[,[,],],<EOF>",196))

    def test_sep_cmt_0(self):
        self.assertTrue(TestLexer.test("(*(()))[[*)]]","],],<EOF>",197))

    def test_sep_CM_SEMI_CL(self):
        self.assertTrue(TestLexer.test(",,,,;;;;;::::",",,,,,,,,;,;,;,;,;,:,:,:,:,<EOF>",198))
    
    def test_cmt_error_0(self):
        self.assertTrue(TestLexer.test("ascas { scasasc","ascas,Error Token {",199))

    def test_cmt_error_1(self):
        self.assertTrue(TestLexer.test("(*{","(,*,Error Token {",200))