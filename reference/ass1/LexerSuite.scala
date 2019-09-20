import org.scalatest.FunSuite

/**
  * Created by nhphung on 4/28/17.
  * Modified by Tan Sang
  */
class LexerSuite extends FunSuite with TestLexer {

  test("a simple identifier") {
    val input = "abc"
    val expect = "abc,<EOF>"
    assert(checkLex(input,expect,1))
  }
  test("half function declare") {
    val input = "main int {"
    val expect = """main,int,{,<EOF>"""
    assert(checkLex(input,expect,2))
  }
  test("open and close parentheses"){
    val input = "} int main {"
    val expect = """},int,main,{,<EOF>"""
    assert(checkLex(input,expect,3))
  }

  test("traditional block comment"){
    val input = "abc /* skip" +
      "this */ int"
    val expect = """abc,int,<EOF>"""
    assert(checkLex(input,expect,4))
  }

  test("line comment"){
    val input =
      """int//dsaasd
        |float
      """.stripMargin
    val expect = """int,float,<EOF>"""
    assert(checkLex(input,expect,5))
  }
  test("line comment in block comment"){
    val input = """int /*//Line comment in block comment*/ int"""
    val expect = """int,int,<EOF>"""
    assert(checkLex(input,expect,6))
  }
  test("block comment in line comment"){
    val input =
      """int///*skip this line
        |ahihi */
      """.stripMargin
    val expect = """int,ahihi,*,/,<EOF>"""
    assert(checkLex(input,expect,7))
  }
  test("Identifier"){
    val input = """asd Asd asd9 a9 _9 _ha"""
    val expect = """asd,Asd,asd9,a9,_9,_ha,<EOF>"""
    assert(checkLex(input,expect,8))
  }
  test("Error Identifier start with number"){
    val input = """8asf"""
    val expect = """8,asf,<EOF>"""
    assert(checkLex(input,expect,9))
  }
  test("Error Identifier start with other character"){
    val input = """;asd @"""
    val expect = """;,asd,ErrorToken @"""
    assert(checkLex(input,expect,10))
  }
  test("Keywords"){
    val input = """boolean break continue else for"""
    val expect = """boolean,break,continue,else,for,<EOF>"""
    assert(checkLex(input,expect,11))
  }
  test("Some operators"){
    val input = """+ * ! || !="""
    val expect = """+,*,!,||,!=,<EOF>"""
    assert(checkLex(input,expect,12))
  }
  test("All separators"){
    val input = """{ } ( ) [ ] ; ,"""
    val expect = """{,},(,),[,],;,,,<EOF>"""
    assert(checkLex(input,expect,13))
  }
  test("Integer literal"){
    val input = """01 012 025 1365"""
    val expect = """01,012,025,1365,<EOF>"""
    assert(checkLex(input,expect,14))
  }
  test("Floating-point literal"){
    val input = """1. .00 00.e+00 .00E-010 120.10e100 01.10 100E3"""
    val expect = """1.,.00,00.e+00,.00E-010,120.10e100,01.10,100E3,<EOF>"""
    assert(checkLex(input,expect,15))
  }
  test("Error floating-point literal 1"){
    val input = """."""
    val expect = """ErrorToken ."""
    assert(checkLex(input,expect,16))
  }
  test("Error floating-point literal 2"){
    val input = """e10"""
    val expect = """e10,<EOF>"""
    assert(checkLex(input,expect,17))
  }
  test("Error floating-point literal 3"){
    val input = """e-1"""
    val expect = """e,-,1,<EOF>"""
    assert(checkLex(input,expect,18))
  }
  test("Normal string"){
    val input = """"This is normal string """"
    val expect = """This is normal string ,<EOF>"""
    assert(checkLex(input,expect,19))
  }
  test("Normal string with legal escape"){
    val input = """"This is normal  string """"
    val expect = """This is normal  string ,<EOF>"""
    assert(checkLex(input,expect,20))
  }
  test("Normal string with legal escape 1"){
    val input = "\"svaf \b \' \""
    val expect = "svaf \b ' ,<EOF>"
    assert(checkLex(input,expect,21))
  }
  test("Array pointer type"){
    val input = """int[3]"""
    val expect = """int,[,3,],<EOF>"""
    assert(checkLex(input,expect,22))
  }
  test("Boolean expression"){
    val input = """a + 5"""
    val expect = """a,+,5,<EOF>"""
    assert(checkLex(input,expect,23))
  }
  test("Unclosed string"){
    val input = """"Unclose string"""
    val expect = """Unclosed string: Unclose string"""
    assert(checkLex(input,expect,24))
  }
  test("Variable declaration"){
    val input = """int a;"""
    val expect = """int,a,;,<EOF>"""
    assert(checkLex(input,expect,25))
  }
  test("Function declaration"){
    val input = """int foo(){}"""
    val expect = """int,foo,(,),{,},<EOF>"""
    assert(checkLex(input,expect,26))
  }
  test("Expression"){
    val input = """a+b"""
    val expect = """a,+,b,<EOF>"""
    assert(checkLex(input,expect,27))
  }
  test("Index Expression"){
    val input = """foo(2)[3+x]"""
    val expect = """foo,(,2,),[,3,+,x,],<EOF>"""
    assert(checkLex(input,expect,28))
  }
  test("Invocation expression"){
    val input = """goku(a,4,2+3)"""
    val expect = """goku,(,a,,,4,,,2,+,3,),<EOF>"""
    assert(checkLex(input,expect,29))
  }
  test("Float variable declaration"){
    val input = """float y[5]"""
    val expect = """float,y,[,5,],<EOF>"""
    assert(checkLex(input,expect,30))
  }
  test("why so serious!"){
    val input = """neu nah ft. dsk"""
    val expect = """neu,nah,ft,ErrorToken ."""
    assert(checkLex(input,expect,31))
  }
  test("Another Unclose string"){
    val input = """"mon men = than """
    val expect = """Unclosed string: mon men = than """
    assert(checkLex(input,expect,32))
  }
  test("Messenger in comment"){
    val input =
      """aaaaaa//Buon ngu qua"""
    val expect = """aaaaaa,<EOF>"""
    assert(checkLex(input,expect,33))
  }
  test("I am hungry"){
    val input = """I am hungry : olala"""
    val expect = """I,am,hungry,ErrorToken :"""
    assert(checkLex(input,expect,34))
  }
  test("Am i cool"){
    val input = """yes = true"""
    val expect = """yes,=,true,<EOF>"""
    assert(checkLex(input,expect,35))
  }
  test("Daxua 20 minute"){
    val input = """F10 E Q"""
    val expect = """F10,E,Q,<EOF>"""
    assert(checkLex(input,expect,36))
  }
  test("NCL"){
    val input = """mra(do(you(know)))"""
    val expect = """mra,(,do,(,you,(,know,),),),<EOF>"""
    assert(checkLex(input,expect,37))
  }
  test("do while statement"){
    val input = """do a+b while 5;"""
    val expect = """do,a,+,b,while,5,;,<EOF>"""
    assert(checkLex(input,expect,38))
  }
  test("Lady and error"){
    val input = """lay ^"""
    val expect = """lay,ErrorToken ^"""
    assert(checkLex(input,expect,39))
  }
  test("The testcase 40th - illegal escape"){
    val input = """~"""
    val expect = """ErrorToken ~"""
    assert(checkLex(input,expect,40))
  }
  test("return statement"){
    val input = """return s;"""
    val expect = """return,s,;,<EOF>"""
    assert(checkLex(input,expect,41))
  }
  test("break statement"){
    val input = """break;"""
    val expect = """break,;,<EOF>"""
    assert(checkLex(input,expect,42))
  }
  test("continue statement"){
    val input = """"""
    val expect = """<EOF>"""
    assert(checkLex(input,expect,43))
  }
  test("for statement"){
    val input = """for (a=2;a<5;a+1)"""
    val expect = """for,(,a,=,2,;,a,<,5,;,a,+,1,),<EOF>"""
    assert(checkLex(input,expect,44))
  }
  test("Super expression"){
    val input = """a=!!!!!!5--2"""
    val expect = """a,=,!,!,!,!,!,!,5,-,-,2,<EOF>"""
    assert(checkLex(input,expect,45))
  }
  test("Identifier n"){
    val input = """Identifier"""
    val expect = """Identifier,<EOF>"""
    assert(checkLex(input,expect,46))
  }
  test("Identifier n+2"){
    val input = """Paolo"""
    val expect = """Paolo,<EOF>"""
    assert(checkLex(input,expect,47))
  }
  test("Identifier n+10\""){
    val input = """Identifier n+4"""
    val expect = """Identifier,n,+,4,<EOF>"""
    assert(checkLex(input,expect,48))
  }
  test("Identifier n+7\""){
    val input = """New 54a"""
    val expect = """New,54,a,<EOF>"""
    assert(checkLex(input,expect,49))
  }
  test("no thing"){
    val input = """afasw2543"""
    val expect = """afasw2543,<EOF>"""
    assert(checkLex(input,expect,50))
  }

  test("int literal"){
    val input = "123 465 _jdk"
    val expect = """123,465,_jdk,<EOF>"""
    assert(checkLex(input,expect,51))
  }
  test("float literal "){
    val input = "000-567 678int567"
    val expect = """000,-,567,678,int567,<EOF>"""
    assert(checkLex(input,expect,52))
  }
  test("float literal 2"){
    val input = "000/567 678int567"
    val expect = """000,/,567,678,int567,<EOF>"""
    assert(checkLex(input,expect,53))
  }
  test("float literal 3"){
    val input = "000+567 678int567"
    val expect = """000,+,567,678,int567,<EOF>"""
    assert(checkLex(input,expect,54))
  }
  test("float literal 4"){
    val input = "000+567 678int567"
    val expect = """000,+,567,678,int567,<EOF>"""
    assert(checkLex(input,expect,55))
  }
  test("int literal 2"){
    val input = "i = a * 24;"
    val expect = """i,=,a,*,24,;,<EOF>"""
    assert(checkLex(input,expect,56))
  }
  test("int literal 3"){
    val input = "a[12] = inc * (dec - 1);"
    val expect = """a,[,12,],=,inc,*,(,dec,-,1,),;,<EOF>"""
    assert(checkLex(input,expect,57))
  }
  test("int literal 4"){
    val input = "for (int i=0;i<5){}"
    val expect = "for,(,int,i,=,0,;,i,<,5,),{,},<EOF>"
    assert(checkLex(input,expect,58))
  }
  test("int literal 5"){
    val input = "while(1){}"
    val expect = "while,(,1,),{,},<EOF>"
    assert(checkLex(input,expect,59))
  }
  test("int literal 6"){
    val input = " do {} while(i<5)"
    val expect = "do,{,},while,(,i,<,5,),<EOF>"
    assert(checkLex(input,expect,60))
  }
  test("int literal 7"){
    val input = " if (i<1){} else {}"
    val expect = "if,(,i,<,1,),{,},else,{,},<EOF>"
    assert(checkLex(input,expect,61))
  }
  test("int literal 8"){
    val input = " int i;"
    val expect = "int,i,;,<EOF>"
    assert(checkLex(input,expect,62))
  }
  test("int literal 9"){
    val input = " char ma[4];"
    val expect = "char,ma,[,4,],;,<EOF>"
    assert(checkLex(input,expect,63))
  }
  test("lon hon"){
    val input = """ a>b"""
    val expect = """a,>,b,<EOF>"""
    assert(checkLex(input,expect,64))
  }
  test("nho hon"){
    val input = """a<b """
    val expect = """a,<,b,<EOF>"""
    assert(checkLex(input,expect,65))
  }

  test("phep gan"){
    val input = """ a[5]=b; """
    val expect = """a,[,5,],=,b,;,<EOF>"""
    assert(checkLex(input,expect,66))
  }

  test("bang"){
    val input = """ a == b"""
    val expect = """a,==,b,<EOF>"""
    assert(checkLex(input,expect,67))
  }
  test("if literal 1"){
    val input = "if (sysyear>year) { return true;} else { if (sysmonth>month) return true; else { if (sysday>day)return true; else return false;}}"
    val expect = """if,(,sysyear,>,year,),{,return,true,;,},else,{,if,(,sysmonth,>,month,),return,true,;,else,{,if,(,sysday,>,day,),return,true,;,else,return,false,;,},},<EOF>"""
    assert(checkLex(input,expect,68))
  }
  test(" string input"){
    val input = """ "a bc\m" """
    val expect = """Illegal escape in string: a bc\m"""
    assert(checkLex(input,expect,69))
  }
  test("return"){
    val input ="""return; """
    val expect = """return,;,<EOF>"""
    assert(checkLex(input,expect,70))
  }

  test("break"){
    val input ="""break; """
    val expect = """break,;,<EOF>"""
    assert(checkLex(input,expect,71))
  }
  test("continue"){
    val input ="""continue; """
    val expect = """continue,;,<EOF>"""
    assert(checkLex(input,expect,72))
  }
  test("for"){
    val input ="""for(){} """
    val expect = """for,(,),{,},<EOF>"""
    assert(checkLex(input,expect,73))
  }
  test("if"){
    val input ="""if """
    val expect = """if,<EOF>"""
    assert(checkLex(input,expect,74))
  }
  test("else"){
    val input ="""else """
    val expect = """else,<EOF>"""
    assert(checkLex(input,expect,75))
  }
  test("if else"){
    val input ="""if (){} else {} """
    val expect = """if,(,),{,},else,{,},<EOF>"""
    assert(checkLex(input,expect,76))
  }
  test("do"){
    val input ="""do """
    val expect = """do,<EOF>"""
    assert(checkLex(input,expect,77))
  }
  test("while"){
    val input = """while"""
    val expect = """while,<EOF>"""
    assert(checkLex(input,expect,78))
  }
  test("do while"){
    val input ="""do {} while () """
    val expect = """do,{,},while,(,),<EOF>"""
    assert(checkLex(input,expect,79))
  }
  test("float"){
    val input = """1e-2 """
    val expect ="""1e-2,<EOF>"""
    assert(checkLex(input,expect,80))
  }
  test("string 1"){
    val input = """string """
    val expect = """string,<EOF>"""
    assert(checkLex(input,expect,81))
  }
  test("false"){
    val input = """false """
    val expect = """false,<EOF>"""
    assert(checkLex(input,expect,82))
  }
  test("true"){
    val input = """true """
    val expect = """true,<EOF>"""
    assert(checkLex(input,expect,83))
  }
  test("nhan"){
    val input = """a*b """
    val expect = """a,*,b,<EOF>"""
    assert(checkLex(input,expect,84))
  }
  test("chia"){
    val input = """a/b """
    val expect = """a,/,b,<EOF>"""
    assert(checkLex(input,expect,85))
  }
  test("chia du"){
    val input = """ab """
    val expect = """ab,<EOF>"""
    assert(checkLex(input,expect,86))
  }
  test("OR"){
    val input = """ a || b; """
    val expect = """a,||,b,;,<EOF>"""
    assert(checkLex(input,expect,87))
  }
  test("and"){
    val input = """ a&&b; """
    val expect = """a,&&,b,;,<EOF>"""
    assert(checkLex(input,expect,88))
  }
  test("khac"){
    val input = """a!=b """
    val expect = """a,!=,b,<EOF>"""
    assert(checkLex(input,expect,89))
  }
  test("nho hon bang"){
    val input = """a <=b """
    val expect = """a,<=,b,<EOF>"""
    assert(checkLex(input,expect,90))
  }
  test("lon hon bang"){
    val input = """a >= b"""
    val expect = """a,>=,b,<EOF>"""
    assert(checkLex(input,expect,91))
  }
  test("float 3"){
    val input = """ float a"""
    val expect = """float,a,<EOF>"""
    assert(checkLex(input,expect,92))
  }
  test("not"){
    val input = """ ! """
    val expect = """!,<EOF>"""
    assert(checkLex(input,expect,93))
  }
  test("phay"){
    val input = """ ,"""
    val expect = """,,<EOF>"""
    assert(checkLex(input,expect,94))
  }
  test("boolean"){
    val input = """boolean """
    val expect = """boolean,<EOF>"""
    assert(checkLex(input,expect,95))
  }

  test("\b"){
    val input = """ "abc\ndef" """
    val expect = """abc\ndef,<EOF>"""
    assert(checkLex(input,expect,96))
  }
  test("block comment"){
    val input = " /* abc a \b \r ?a */ abc "
    val expect = """abc,<EOF>"""
    assert(checkLex(input,expect,97))
  }

  test("comment"){
    val input = """ //abc \n \a \b
                    abc"""
    val expect = """abc,<EOF>"""
    assert(checkLex(input,expect,98))
  }
  test("if one more time"){
    val input = """ if (a>0) a = 0 ;
                    else a < 0;"""
    val expect = """if,(,a,>,0,),a,=,0,;,else,a,<,0,;,<EOF>"""
    assert(checkLex(input,expect,99))
  }
  test("for one more time"){
    val input = """for(i=0;i<5)a = b;  """
    val expect = """for,(,i,=,0,;,i,<,5,),a,=,b,;,<EOF>"""
    assert(checkLex(input,expect,100))
  }

  }