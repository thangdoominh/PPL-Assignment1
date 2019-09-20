import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_001(self):
        self.assertTrue(TestLexer.test("_ABC_abc","_ABC_abc,<EOF>",101))
    
    def test_002(self):
        self.assertTrue(TestLexer.test("_123 123","_123,123,<EOF>",102))

    def test_003(self):
        self.assertTrue(TestLexer.test("123123","123123,<EOF>",103))
    
    def test_004(self):
        self.assertTrue(TestLexer.test("CSVNmmZZZ","CSVNmmZZZ,<EOF>",104))

    def test_005(self):
        self.assertTrue(TestLexer.test("VN123","VN123,<EOF>",105))

    def test_006(self):
        self.assertTrue(TestLexer.test("123_VN123","123,_VN123,<EOF>",106))

    def test_007(self):
        self.assertTrue(TestLexer.test("\"","Unclosed String: ",107))

    def test_008(self):
        self.assertTrue(TestLexer.test("ONE_TWO_THREE","ONE_TWO_THREE,<EOF>",108))

    def test_009(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE","ONE_2_THREE,<EOF>",109))

    def test_010(self):
        self.assertTrue(TestLexer.test("0ONE_2_THREE4_FIVE","0,ONE_2_THREE4_FIVE,<EOF>",110))

    def test_011(self):
        self.assertTrue(TestLexer.test("function f()","function,f,(,),<EOF>",111))

    def test_012(self):
        self.assertTrue(TestLexer.test("\"This is normal string\"","This is normal string,<EOF>",112))

    def test_013(self):
        self.assertTrue(TestLexer.test(";asd @",";,asd,Error Token @",113))

    def test_014(self):
        self.assertTrue(TestLexer.test("//Viet Dep Trai Nhat Khoa May Tinh","<EOF>",114))

    def test_015(self):
        self.assertTrue(TestLexer.test("(*Viet Dep Trai Nhat Khoa May Tinh*)","<EOF>",115))

    def test_016(self):
        self.assertTrue(TestLexer.test("{Viet Dep Trai Nhat Khoa May Tinh} return","return,<EOF>",116))

    def test_017(self):
        self.assertTrue(TestLexer.test("1. .00 00.e00 .00E-010 120.10e100 01.10 100E3","1.,.00,00.e00,.00E-010,120.10e100,01.10,100E3,<EOF>",117))
    
    def test_018(self):
        self.assertTrue(TestLexer.test("ONE[1]","ONE,[,1,],<EOF>",118))
    
    def test_019(self):
        self.assertTrue(TestLexer.test("1 := 2 + 3 * 4","1,:=,2,+,3,*,4,<EOF>",119))
    
    def test_020(self):
        self.assertTrue(TestLexer.test("\"Unclosed string","Unclosed String: Unclosed string",120))
    
    def test_021(self):
        self.assertTrue(TestLexer.test("3=5=r=10;{aAs\a\b\c\d\e\f\g\h\i\j\k\l\m\\q'N}i=5;","3,=,5,=,r,=,10,;,i,=,5,;,<EOF>",121))
    
    def test_022(self):
        self.assertTrue(TestLexer.test("break continue for to downto do if then else return while begin end function","break,continue,for,to,downto,do,if,then,else,return,while,begin,end,function,<EOF>",122))
    
    def test_023(self):
        self.assertTrue(TestLexer.test("procedure var true false array of real boolean integer string not and or div mod","procedure,var,true,false,array,of,real,boolean,integer,string,not,and,or,div,mod,<EOF>",123))
    
    def test_024(self):
        self.assertTrue(TestLexer.test("+-*/not mod or and <> = < > <= >= div","+,-,*,/,not,mod,or,and,<>,=,<,>,<=,>=,div,<EOF>",124))
    
    def test_025(self):
        self.assertTrue(TestLexer.test("[]();:..,","[,],(,),;,:,..,,,<EOF>",125))
    
    def test_026(self):
        self.assertTrue(TestLexer.test("askjdh_3497jasd+kjd","askjdh_3497jasd,+,kjd,<EOF>",126))
    
    def test_027(self):
        self.assertTrue(TestLexer.test("foo(2)[3+x]","foo,(,2,),[,3,+,x,],<EOF>",127))

    def test_028(self):
        self.assertTrue(TestLexer.test("ONE 2 THREE ^ FOUR","ONE,2,THREE,Error Token ^",128))

    def test_029(self):
        self.assertTrue(TestLexer.test("function f ( ) : integer ;begin return 200; end","function,f,(,),:,integer,;,begin,return,200,;,end,<EOF>",129))

    def test_030(self):
        self.assertTrue(TestLexer.test("with i : integer ; main : integer ; f : integer ; do","with,i,:,integer,;,main,:,integer,;,f,:,integer,;,do,<EOF>",130))

    def test_031(self):
        self.assertTrue(TestLexer.test("procedure main ();","procedure,main,(,),;,<EOF>",131))

    def test_032(self):
        self.assertTrue(TestLexer.test("var i : array [1 ..5] of integer ;","var,i,:,array,[,1,..,5,],of,integer,;,<EOF>",132))

    def test_033(self):
        self.assertTrue(TestLexer.test("\"dkjoiue\\s\"","Illegal Escape In String: dkjoiue\\",133))

    def test_034(self):
        self.assertTrue(TestLexer.test("\"aA\tqq\\a\rd\n\fsVNgge\"","Illegal Escape In String: aA\t",134))

    def test_035(self):
        self.assertTrue(TestLexer.test("uses crt;\nvar i:integer;\n\tst:string;\nbegin\n\tclrscr;\n\tst=\"abcx\\tyz\";\n\twriteln(st);\nend","uses,crt,;,var,i,:,integer,;,st,:,string,;,begin,clrscr,;,st,=,abcx\\tyz,;,writeln,(,st,),;,end,<EOF>",135))

    def test_036(self):
        self.assertTrue(TestLexer.test("\"aAsVN\r\r\n\tgge","Illegal Escape In String: aAsVN\n",136))

    def test_037(self):
        self.assertTrue(TestLexer.test("procedure goo( x : array [ 1 ..2] of real);","procedure,goo,(,x,:,array,[,1,..,2,],of,real,),;,<EOF>",137))

    def test_038(self):
        self.assertTrue(TestLexer.test("if (1) then return 2.3; //CORRECT else return 2 ;","if,(,1,),then,return,2.3,;,<EOF>",138))

    def test_039(self):
        self.assertTrue(TestLexer.test("a := b [10] := foo()[3] := x := 1 ;","a,:=,b,[,10,],:=,foo,(,),[,3,],:=,x,:=,1,;,<EOF>",139))

    def test_040(self):
        self.assertTrue(TestLexer.test("i : integer ; main : integer ; f : integer ;","i,:,integer,;,main,:,integer,;,f,:,integer,;,<EOF>",140))

    def test_041(self):
        self.assertTrue(TestLexer.test("procedure putIntLn(i:integer)","procedure,putIntLn,(,i,:,integer,),<EOF>",141))

    def test_042(self):
        self.assertTrue(TestLexer.test("function foo (b : array [1 ..2] of integer):array [2 ..3] of real;","function,foo,(,b,:,array,[,1,..,2,],of,integer,),:,array,[,2,..,3,],of,real,;,<EOF>",142))

    def test_043(self):
        self.assertTrue(TestLexer.test("\"ONE_2_THREE\ta\"","Illegal Escape In String: ONE_2_THREE\t",143))

    def test_044(self):
        self.assertTrue(TestLexer.test("Var\nNum1, Num2, Sum : Integer;","Var,Num1,,,Num2,,,Sum,:,Integer,;,<EOF>",144))

    def test_045(self):
        self.assertTrue(TestLexer.test("write(\"Nhap ten cua ban:\");readln(name);write(\"Nhap ho cua ban:\");readln(surname);","write,(,Nhap ten cua ban:,),;,readln,(,name,),;,write,(,Nhap ho cua ban:,),;,readln,(,surname,),;,<EOF>",145))

    def test_046(self):
        self.assertTrue(TestLexer.test("Procedure DrawLine(X : Integer; Y : Integer);\n{ the declaration of the variables in brackets are called parameters }\nVar Counter : Integer; { this is called a local variable }","Procedure,DrawLine,(,X,:,Integer,;,Y,:,Integer,),;,Var,Counter,:,Integer,;,<EOF>",146))

    def test_047(self):
        self.assertTrue(TestLexer.test("ClrScr(); {Clear screen with a brown colour. Try run the program without this..}","ClrScr,(,),;,<EOF>",147))

    def test_048(self):
        self.assertTrue(TestLexer.test("beGin \nfor i := 0 to n - 2 do \n for j:= i+1 to n-1 do \n if(a[i]>a[j]) then beGin \n temp := a[i];\n a[i] := a[j];\n a[j] := temp;\n eND\n print(a);\neND","beGin,for,i,:=,0,to,n,-,2,do,for,j,:=,i,+,1,to,n,-,1,do,if,(,a,[,i,],>,a,[,j,],),then,beGin,temp,:=,a,[,i,],;,a,[,i,],:=,a,[,j,],;,a,[,j,],:=,temp,;,eND,print,(,a,),;,eND,<EOF>",148))

    def test_049(self):
        self.assertTrue(TestLexer.test("pROCEDURE foo(c: real);\nBEGIN\n while (1) do reTuRn ;\n END","pROCEDURE,foo,(,c,:,real,),;,BEGIN,while,(,1,),do,reTuRn,;,END,<EOF>",149))

    def test_050(self):
        self.assertTrue(TestLexer.test("function foo(c: real): integer;\nBEGIN\nwhile (1) do reTuRn foo(a+1);\nEND\n","function,foo,(,c,:,real,),:,integer,;,BEGIN,while,(,1,),do,reTuRn,foo,(,a,+,1,),;,END,<EOF>",150))

    def test_051(self):
        self.assertTrue(TestLexer.test("function foo(c: real): sTRIng;\n BEGIN\nFOR i:=1 to m+10 do beGin\ns := s + 1;\nif(a=1) then s:=s-1;\nend\nEND","function,foo,(,c,:,real,),:,sTRIng,;,BEGIN,FOR,i,:=,1,to,m,+,10,do,beGin,s,:=,s,+,1,;,if,(,a,=,1,),then,s,:=,s,-,1,;,end,END,<EOF>",151))

    def test_052(self):
        self.assertTrue(TestLexer.test("function foo(c: real): real ;\nvar x: integer ;\nBEGIN\n a[m+n] := a[m+1] := foo()[m*1] := a[a div 3] := (a>m) and then (b<n);\nEND","function,foo,(,c,:,real,),:,real,;,var,x,:,integer,;,BEGIN,a,[,m,+,n,],:=,a,[,m,+,1,],:=,foo,(,),[,m,*,1,],:=,a,[,a,div,3,],:=,(,a,>,m,),and,then,(,b,<,n,),;,END,<EOF>",152))

    def test_053(self):
        self.assertTrue(TestLexer.test("procedurE foo (b : real) ;\nbegin\n1[1] := 1;\n(1>=0)[2] := 2+a[1][1]+c+(\"abc\"< 0);\nahihi(1)[m+1] := 3;\n(1+a[1]+(1<0))[10] := 4;\nEnd","procedurE,foo,(,b,:,real,),;,begin,1,[,1,],:=,1,;,(,1,>=,0,),[,2,],:=,2,+,a,[,1,],[,1,],+,c,+,(,abc,<,0,),;,ahihi,(,1,),[,m,+,1,],:=,3,;,(,1,+,a,[,1,],+,(,1,<,0,),),[,10,],:=,4,;,End,<EOF>",153))

    def test_054(self):
        self.assertTrue(TestLexer.test("function foo(c: real): integer;\nBEGIN\nfoo (3,a+1);\nfoo1();\nEND","function,foo,(,c,:,real,),:,integer,;,BEGIN,foo,(,3,,,a,+,1,),;,foo1,(,),;,END,<EOF>",154))

    def test_055(self):
        self.assertTrue(TestLexer.test("function foo(c: real): integer;\nBEGIN\nwhile (1=1) do begin eND\nEND","function,foo,(,c,:,real,),:,integer,;,BEGIN,while,(,1,=,1,),do,begin,eND,END,<EOF>",155))

    def test_056(self):
        self.assertTrue(TestLexer.test("function foo(c: real): integer;\nBEGIN\nfoo(3,a+1,a<>1,a[1]);\nreturn 1;\nEND","function,foo,(,c,:,real,),:,integer,;,BEGIN,foo,(,3,,,a,+,1,,,a,<>,1,,,a,[,1,],),;,return,1,;,END,<EOF>",156))

    def test_057(self):
        self.assertTrue(TestLexer.test("Function UCLN(m,n:integer):integer;\nBegin\nIf(m=n) then RETURN m ;\nelse\nIf (m>n) then return UCLN(m-n,n);\nelse return UCLN(m,n-m);\nEnd","Function,UCLN,(,m,,,n,:,integer,),:,integer,;,Begin,If,(,m,=,n,),then,RETURN,m,;,else,If,(,m,>,n,),then,return,UCLN,(,m,-,n,,,n,),;,else,return,UCLN,(,m,,,n,-,m,),;,End,<EOF>",157))

    def test_058(self):
        self.assertTrue(TestLexer.test("If(m=n) then RETURN m ;\nelse\nIf (m>n) then return UCLN(m-n,n);\nelse return UCLN(m,n-m);","If,(,m,=,n,),then,RETURN,m,;,else,If,(,m,>,n,),then,return,UCLN,(,m,-,n,,,n,),;,else,return,UCLN,(,m,,,n,-,m,),;,<EOF>",158))

    def test_059(self):
        self.assertTrue(TestLexer.test("Begin\nFor i:=N downto k+ 1 do\nA[i] := A[i-1];\nA[k] := X;\nEnd","Begin,For,i,:=,N,downto,k,+,1,do,A,[,i,],:=,A,[,i,-,1,],;,A,[,k,],:=,X,;,End,<EOF>",159))

    def test_060(self):
        self.assertTrue(TestLexer.test("Function KtraMangTang ( A:array[0 .. 10] of REAL; N :Integer) : Boolean;","Function,KtraMangTang,(,A,:,array,[,0,..,10,],of,REAL,;,N,:,Integer,),:,Boolean,;,<EOF>",160))

    def test_061(self):
        self.assertTrue(TestLexer.test("For i:=2 to N-1 do\nIf(N mod i = 0) then\nreturn 0;\nElse\nreturn 1;","For,i,:=,2,to,N,-,1,do,If,(,N,mod,i,=,0,),then,return,0,;,Else,return,1,;,<EOF>",161))

    def test_062(self):
        self.assertTrue(TestLexer.test("temp := a[i];\na[i] := a[j];\na[j] := temp;","temp,:=,a,[,i,],;,a,[,i,],:=,a,[,j,],;,a,[,j,],:=,temp,;,<EOF>",162))

    def test_063(self):
        self.assertTrue(TestLexer.test("reTuRn s;","reTuRn,s,;,<EOF>",163))

    def test_064(self):
        self.assertTrue(TestLexer.test("If(A[i] mod 5=0) then\nS := S+A[i];","If,(,A,[,i,],mod,5,=,0,),then,S,:=,S,+,A,[,i,],;,<EOF>",164))

    def test_065(self):
        self.assertTrue(TestLexer.test("Function DemPtuX(A:array[0 .. 10] of integer; N,X : Integer) : Integer;","Function,DemPtuX,(,A,:,array,[,0,..,10,],of,integer,;,N,,,X,:,Integer,),:,Integer,;,<EOF>",165))

    def test_066(self):
        self.assertTrue(TestLexer.test("while(i<n) do begin\nIf(A[i] < A[i-1]) Then\nFlag :=False; { Cham dut kiem tra, ket qua qua trinh : khong tang }\ni:=i+1;\nend","while,(,i,<,n,),do,begin,If,(,A,[,i,],<,A,[,i,-,1,],),Then,Flag,:=,False,;,i,:=,i,+,1,;,end,<EOF>",166))

    def test_067(self):
        self.assertTrue(TestLexer.test("return func(a(1,2));","return,func,(,a,(,1,,,2,),),;,<EOF>",167))

    def test_068(self):
        self.assertTrue(TestLexer.test("whILe(a<>1) do beGin end","whILe,(,a,<>,1,),do,beGin,end,<EOF>",168))

    def test_069(self):
        self.assertTrue(TestLexer.test("var a: array[0 .. m-1] of real; n:integer;","var,a,:,array,[,0,..,m,-,1,],of,real,;,n,:,integer,;,<EOF>",169))

    def test_070(self):
        self.assertTrue(TestLexer.test("If(b=0) then Writeln(\" Phuong trinh co vo so nghiem\");\nElse writeln(\"Phuong tring vo nghiem\");","If,(,b,=,0,),then,Writeln,(, Phuong trinh co vo so nghiem,),;,Else,writeln,(,Phuong tring vo nghiem,),;,<EOF>",170))

    def test_071(self):
        self.assertTrue(TestLexer.test(",",",,<EOF>",171))

    def test_072(self):
        self.assertTrue(TestLexer.test("pROCEDURE main() ;","pROCEDURE,main,(,),;,<EOF>",172))

    def test_073(self):
        self.assertTrue(TestLexer.test("function fibo(x: integer): integer;","function,fibo,(,x,:,integer,),:,integer,;,<EOF>",173))

    def test_074(self):
        self.assertTrue(TestLexer.test("Var flag :boolean;\ni :Integer;","Var,flag,:,boolean,;,i,:,Integer,;,<EOF>",174))

    def test_075(self):
        self.assertTrue(TestLexer.test("with c , d : integer ; c : array [1 .. 2] of real ; do\nwith a , b : integer ; do\nfoo2(a,b,\"anc\");","with,c,,,d,:,integer,;,c,:,array,[,1,..,2,],of,real,;,do,with,a,,,b,:,integer,;,do,foo2,(,a,,,b,,,anc,),;,<EOF>",175))

    def test_076(self):
        self.assertTrue(TestLexer.test("d := c [a] + b ;","d,:=,c,[,a,],+,b,;,<EOF>",176))

    def test_077(self):
        self.assertTrue(TestLexer.test("FUNcTION foo(a, b: integer ; c: real):array [1 .. 2] of integer ;","FUNcTION,foo,(,a,,,b,:,integer,;,c,:,real,),:,array,[,1,..,2,],of,integer,;,<EOF>",177))

    def test_078(self):
        self.assertTrue(TestLexer.test("Writeln(UserFile, \"PASCAL PROGRAMMING\");","Writeln,(,UserFile,,,PASCAL PROGRAMMING,),;,<EOF>",178))

    def test_079(self):
        self.assertTrue(TestLexer.test("Var\ni : Integer;\nmyIntArray : Array[1 .. 20] of Integer;\nmyBoolArray : Array[1 .. 20] of Boolean;","Var,i,:,Integer,;,myIntArray,:,Array,[,1,..,20,],of,Integer,;,myBoolArray,:,Array,[,1,..,20,],of,Boolean,;,<EOF>",179))

    def test_080(self):
        self.assertTrue(TestLexer.test("S := \"Hey there! How are you?\";","S,:=,Hey there! How are you?,;,<EOF>",180))

    def test_081(self):
        self.assertTrue(TestLexer.test("Var \nS     : String;\nerror : Integer;\nR     : Real;","Var,S,:,String,;,error,:,Integer,;,R,:,Real,;,<EOF>",181))

    def test_082(self):
        self.assertTrue(TestLexer.test("foo(3,foo(foo1(foo(2,a+1))));","foo,(,3,,,foo,(,foo1,(,foo,(,2,,,a,+,1,),),),),;,<EOF>",182))

    def test_083(self):
        self.assertTrue(TestLexer.test("if( a < 20 ) then\n(* if condition is true then print the following *) \nwriteln(\"a is less than 20 \");","if,(,a,<,20,),then,writeln,(,a is less than 20 ,),;,<EOF>",183))

    def test_084(self):
        self.assertTrue(TestLexer.test("if a=b then if c=d then while (d=e) do\nbeGin\neND","if,a,=,b,then,if,c,=,d,then,while,(,d,=,e,),do,beGin,eND,<EOF>",184))

    def test_085(self):
        self.assertTrue(TestLexer.test("var\n{ local variable definition }\na : integer;","var,a,:,integer,;,<EOF>",185))

    def test_086(self):
        self.assertTrue(TestLexer.test("var\n{ local variable definition }\na : integer;","var,a,:,integer,;,<EOF>",186))

    def test_087(self):
        self.assertTrue(TestLexer.test("var\nage, weekdays : integer;\ntaxrate, net_income: real;\nchoice, isready: boolean;\nname, surname : string;","var,age,,,weekdays,:,integer,;,taxrate,,,net_income,:,real,;,choice,,,isready,:,boolean,;,name,,,surname,:,string,;,<EOF>",187))

    def test_088(self):
        self.assertTrue(TestLexer.test("for i:=n-1 doWnTO 0 do s:=s+a[i];","for,i,:=,n,-,1,doWnTO,0,do,s,:=,s,+,a,[,i,],;,<EOF>",188))

    def test_089(self):
        self.assertTrue(TestLexer.test("procedure findMin(x, y, z: integer; m: integer); ","procedure,findMin,(,x,,,y,,,z,:,integer,;,m,:,integer,),;,<EOF>",189))

    def test_090(self):
        self.assertTrue(TestLexer.test("procedure findMin(x, y, z: integer; m: integer); ","procedure,findMin,(,x,,,y,,,z,:,integer,;,m,:,integer,),;,<EOF>",190))

    def test_091(self):
        self.assertTrue(TestLexer.test("function fact(x: integer): integer; (* calculates factorial of x - x! *)","function,fact,(,x,:,integer,),:,integer,;,<EOF>",191))

    def test_092(self):
        self.assertTrue(TestLexer.test("return fibo(x-2)+ fibo(x-1);","return,fibo,(,x,-,2,),+,fibo,(,x,-,1,),;,<EOF>",192))

    def test_093(self):
        self.assertTrue(TestLexer.test("if copy(s,i-2*k+1,k) = copy(s,i-k+1,k) then\nbegin\nok := false;\nexit();\nend","if,copy,(,s,,,i,-,2,*,k,+,1,,,k,),=,copy,(,s,,,i,-,k,+,1,,,k,),then,begin,ok,:=,false,;,exit,(,),;,end,<EOF>",193))

    def test_094(self):
        self.assertTrue(TestLexer.test("fact := x * fact(x-1); (* recursive call *)","fact,:=,x,*,fact,(,x,-,1,),;,<EOF>",194))

    def test_095(self):
        self.assertTrue(TestLexer.test("s:=sqrt(p*(p-a)*(p-b)*(p-c));","s,:=,sqrt,(,p,*,(,p,-,a,),*,(,p,-,b,),*,(,p,-,c,),),;,<EOF>",195))

    def test_096(self):
        self.assertTrue(TestLexer.test("copy(s,i-2*k+1,k) = copy(s,i-k+1,k)","copy,(,s,,,i,-,2,*,k,+,1,,,k,),=,copy,(,s,,,i,-,k,+,1,,,k,),<EOF>",196))

    def test_097(self):
        self.assertTrue(TestLexer.test("A[i-1]+A[i]) mod 10 = 0","A,[,i,-,1,],+,A,[,i,],),mod,10,=,0,<EOF>",197))

    def test_098(self):
        self.assertTrue(TestLexer.test("A[i] <> A[N-i  +1]","A,[,i,],<>,A,[,N,-,i,+,1,],<EOF>",198))

    def test_099(self):
        self.assertTrue(TestLexer.test("Procedure _Replace(A:array[0 .. 10] of integer; N:Integer; X, Y:Integer);","Procedure,_Replace,(,A,:,array,[,0,..,10,],of,integer,;,N,:,Integer,;,X,,,Y,:,Integer,),;,<EOF>",199))

    def test_100(self):
        self.assertTrue(TestLexer.test("for i:=n-1 doWnTO 0 do s:=s+a[i];","for,i,:=,n,-,1,doWnTO,0,do,s,:=,s,+,a,[,i,],;,<EOF>",200))