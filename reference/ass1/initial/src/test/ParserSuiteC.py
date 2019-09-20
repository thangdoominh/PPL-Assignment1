import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_var_1(self):
        input = """
var a, b, c: integer;
var y,z: real;
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_var_2(self):
        input = """
var a, b, c: integer;
    x,y,z:real;
    c:string;    
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_var_3(self):
        input = """
var a, b, c: integer;
procedure main();
begin
a := 1 = 2 = 3 = 4;
end
        """
        expect = "Error on line 5 col 11: ="
        self.assertTrue(TestParser.test(input,expect,203))
        

    def test_var_4(self):
        input = """
Var       
    Num1, Num2, Sum : Integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
        

    def test_var_5(self):
        input = """
Var name, surname: String
    x,y:integer;
        """
        expect = "Error on line 3 col 4: x"
        self.assertTrue(TestParser.test(input,expect,205))


    def test_var_6(self):
        input = """
Var 
	surname: String;
procedure main();
Begin
	Write("Enter your surname:");
	readln(surname);
	writeln();
	writeln();
	Writeln("Your full name is: ",name," ",surname);
	readln();
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
        
    def test_var_7(self):
        input = """
        Var curterm11 : integer = 1 ;
        """
        expect = "Error on line 2 col 32: ="
        self.assertTrue(TestParser.test(input,expect,207))
    
    def test_var_12(self):
        input = """var a: array[1 .. 3] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_var_8(self):
        input = """var a: array[1 .. -2] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_var_9(self):
        input = """var a: array[2 .. 10] of real;
            b,c: integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))

    def test_var_10(self):
        input = """var a: array[2 .. 10] of real;
            b,c: integer
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,211))    

    def test_var_11(self):
        input = """
Var Sel: String;
    N1,N2, Total : Real;
    YN : String;  { this is a character variable type, which holds single characters ONLY }
procedure main();
Begin
	Total := 0;  { always initialise integer/real variables }
	GotoXy(4,3);
	Writeln("1.Addition");
	GotoXy(4,4);
	Writeln("2.Subtraction");
	GotoXy(4,5);
	Writeln("3.Exit");
	GotoXy(6,8);
	Write("Select: ");
	Sel := Readkey();

	If Sel = "1" {condition} Then 
	Begin  {more than one statement}
		ClrScr();
		Write("Input No.1:");
		Readln(N1);
		Write("Input No.2:");
		Readln(N2);
		Total := N1 + N2;
		Writeln("Addition: ",N1," + ",N2," = ",Total);
		Write("Press any key to continue...");
		Readkey();
	end { Closing the if statement }

	If Sel = "2" Then { note that here we do not use an assignment statement } 
	Begin 
		ClrScr();
		Write("Input No.1:");
		Readln(N1);
		Write("Input No.2:");
		Readln(N2);
		Total := N1 - N2;
		Write("Subtraction: ");
		Write(N1," - ",N2," = ",Total);
		Write("Press any key to continue...");
		Readkey();
	end  { Closing the if statement }

	If Sel = "3" Then 
	Begin
		ClrScr();
		Write("Are you sure?(Y/N)");
		YN := Readkey();
		If YN = "y" Then Halt(); { 1 instruction, so no need of Begin..End }
		If YN = "n" Then Goto1(); { the goto statement is not recommended for frequent use }
	End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
        
    def test_if_1(self):
        input = """procedure ifelse();
var
   { local variable definition }
   a, b : integer;

begin
   a := 100;
   b:= 200;
   
   (* check the boolean condition *)
   if (a = 100) then
      (* if condition is true then check the following *)
      if ( b = 200 ) then
         (* if nested if condition is true  then print the following *)
         writeln("Value of a is 100 and value of b is 200" );
   
   writeln("Exact value of a is: ", a );
   writeln("Exact value of b is: ", b );
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_if_2(self):
        input = """
        procedure foo();
        begin
        if (-4*a*c<b*b) then
            a:=b;
        (*here it breaks*) else
        readln();
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_if_3(self):
        input = """
Var
	SEL : Integer;
	YN : String;
procedure main();
Begin
	Writeln("[1]. PLAY GAME");
	WRITELN("[2]. LOAD GAME");
	WRITELN("[3]. MULTIPLAYER");
	WRITELN("[4]. EXIT GAME");
	Writeln("note: Do not press anything except");
	Writeln("numbers; otherwise an error occurs!");
	Readln(SEL);
	
	If SEL = 1 Then
	Begin
		Writeln("You will soon be able to create");
		Writeln("games using Pascal Programming :-)");
		Delay(2000);
		Goto(Ret);
	end

	If SEL = 2 Then
	Begin
		Writeln("Ahhh... no saved games");
		Delay(2000);
		Goto(Ret);
	end

	If SEL = 3 Then
	Begin
		Writeln("networking or 2 players?");
		Delay(2000);
		Goto(Ret);
	end

	If SEL = 4 Then
	Begin
		Writeln("Are you sure you want to Exit?");
		YN := Readkey;
		If YN = "y" Then
		Begin
			Writeln("Good Bye...");
			Delay(1000);
			Halt(); {EXIT PROGRAM}
		end

		If YN = "n" Then
			Goto(Ret);
	end
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_if_4(self):
        input = """
            function foo():real;
            begin
            if (color = red) then
                writeln("You have chosen a red car");

            else
                writeln("Please choose a color for your car");
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def test_if_5(self):
        input = """
            function foo():real;
            begin
            if( a < 20 ) then
                (* if condition is true then print the following *)
                writeln("a is less than 20" );
            
            else
                (* if condition is false then print the following *) 
                writeln("a is not less than 20" );
                writeln("value of a is : ", a);
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))

    def test_if_6(self):
        input = """
            procedure main();
            var
                { local variable definition }
                a : integer;

            begin
            a := 100;
            (* check the boolean condition *)
            if( a < 20 ) then
                (* if condition is true then print the following *)
                writeln("a is less than 20" );
            
            else
                (* if condition is false then print the following *) 
                writeln("a is not less than 20" );
                writeln("value of a is : ", a);
            end
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_if_7(self):
        input = """
            procedure main();
            begin
                if (a <= 20) then
                c:= c+1;
                else 
                begin end
            end
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_if_8(self):
        input = """
           procedure main();
            begin
                if (a <= 20) then
                c:= c+1;
                else 
                else
                begin end
            end
        
        """
        expect = "Error on line 7 col 16: else"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_while_1(self):
        input = """
           procedure main();
                begin
                a := 10;
                while  a < 20  do
                
                begin
                    writeln("value of a: ", a);
                    a := a + 1;
                end
                end
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_while_2(self):
        input = """
           procedure main();
           begin
           while number>0 do
                begin
                sum := sum + number;
                number := number - 2;
                end
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_while_3(self):
        input = """
           procedure main();
          
           while number>0 do
                begin
                sum := sum + number;
                number := number - 2;
                end
           
        
        """
        expect = "Error on line 4 col 11: while"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_while_4(self):
        input = """
           procedure main();
           begin
                a := 5;
                    while a < 6 do 
                    {
                    writeln (a);
                    a := a + 1
                    }
           end
        
        """
        expect = "Error on line 10 col 11: end"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_while_5(self):
        input = """
            procedure main();
           begin
                a := 5;
                    while a < 6 do 
                    {
                    writeln (a);
                    a := a + 1
                    }
                    a:=10*a;
           end
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))    

    def test_while_6(self):
        input = """
Var n1, n2 : string;
procedure main();
Begin
	Writeln("Enter two numbers: (\\\"\\\"0\\\"\\\" & \\\"\\\"0\\\"\\\" to exit)");
	While not ((n1 = "0") AND (n2 = "0")) do
    Begin
		Write("No.1: ");
		Readln(n1);
		Write("No.2: ");
		Readln(n2);
		If (n1 = "0") AND (n2 = "0") Then Halt(0);
    End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
        

    def test_or_1(self):
        input = """
Var n1, n2 : string;
procedure main();
Begin
	Writeln("Enter two numbers: (\\\"\\\"0\\\"\\\" & \\\"\\\"0\\\"\\\" to exit)");
	While not ((n1 = "0") OR (n2 = "0")) do
    Begin
		Write("No.1: ");
		Readln(n1);
		Write("No.2: ");
		Readln(n2);
		If (n1 = "0") OR (n2 = "0") Then Halt(0);
    End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
        

    def test_not_1(self):
        input = """
Var n1, n2 : string;
procedure main();
Begin
	Writeln("Enter two numbers: (\\\"\\\"0\\\"\\\" & \\\"\\\"0\\\"\\\" to exit)");
	While not (NOT (n1 = "0")) do
    Begin
		Write("No.1: ");
		Readln(n1);
		Write("No.2: ");
		Readln(n2);
		If NOT (n1 = "0") Then Halt(0);
    End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
        

    def test_and_1(self):
        input = """
Var age : Integer;
procedure main();
Begin
	While (age > 0) AND (age <= 100) Do
    Begin
		Write("Enter age (1 - 100): ");
		Readln(age);
		If (age < 1) Then
			Writeln("Age cannot be less than 1...");
		Else If (age > 100) Then
			Writeln("Age cannot be greater than 100...");
    End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
        

    def test_bool_1(self):
        input = """
Var 
	bool : Boolean;
	A, B : Integer;
Procedure main();
Begin
	A := 10;
	B := 20;
	bool := False;
	bool := (A = 10) OR (B = 10);
	Writeln(bool); { outputs TRUE }
	bool := (A = 10) AND (B = 10);
	Writeln(bool); { outputs FALSE }
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
        

    def test_bool_2(self):
        input = """
Var quit : Boolean;
    a    : String;
Procedure main();
Begin
	While NOT (quit = True) Do
    Begin
		Writeln("Type \\\"\\\"exit\\\"\\\" to quit:");
		Readln(a);
		If a = "exit" Then 
			quit := True;
    End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
        

    def test_for_1(self):
        input = """
Procedure DrawLine(); 
{This procedure helps me to avoid the rewriting the for loops}
Var Counter : Integer;
Begin
	textcolor(green);
	For Counter := 1 to 10 do
	Begin 
		Write(chr(196)); 
	End
End

Procedure Main();
Begin
	GotoXy(10,5);
	DrawLine();
	GotoXy(10,6);
	DrawLine();
	GotoXy(10,7);
	DrawLine();
	GotoXy(10,10);
	DrawLine();
	Readkey();
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
        

    def test_for_2(self):
        input = """
Procedure DrawLine(X : Integer; Y : Integer);
{ the declaration of the variables in brackets are called parameters }
Var Counter : Integer; { this is called a local variable }
Begin
	GotoXy(X,Y); {here I use the arguments of X and Y}
	textcolor(green);
	For Counter := 1 to 10 do
	Begin 
		Write(chr(196));
	End
End

Procedure main();
Begin
	DrawLine(10,5);
	DrawLine(10,6);
	DrawLine(10,7);
	DrawLine(10,10);
	Readkey();
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
        

    def test_string_1(self):
        input = """
Var
	UserFile : String;
	FileName, TFile : String;

Procedure Main();
Begin
	Writeln("Enter the file name (including its full path) of the text file (without the extension):");
	Readln(FileName); { A .txt file will be assigned to a text variable }
	Assign(UserFile, FileName + ".txt");
	Reset(UserFile); { "Reset(x)" - means open the file x and reset cursor to the beginning of file }
	While NOT Eof(UserFile) Do
    Begin
		Readln(UserFile,TFile);
		Writeln(TFile);
	End
	Close(UserFile);
	Readln();
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
        

    def test_string_2(self):
        input = """
Var
	FName, Txt : String;
	UserFile   : String; 

Procedure Main();
Begin
	FName := "Textfile";
	Assign(UserFile, "C:\\\\" + FName + ".txt"); {assign a text file}
	Rewrite(UserFile); {open the file "fname" for writing}
	Writeln(UserFile, "PASCAL PROGRAMMING");
	Writeln(UserFile, "if you did not understand something,");
	Writeln(UserFile, "please send me an email to:");
	Writeln(UserFile, "victorsaliba@hotmail.com");
	Writeln("Write some text to the file:");
	Readln(Txt);
	Writeln(UserFile, "");
	Writeln(UserFile, "The user entered this text:");
	Writeln(UserFile, Txt);
	Close(UserFile);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
        

    def test_string_3(self):
        input = """
Var
	UFile : String;

Procedure main();
Begin
	Assign(UFile, "C:\\\\ADDTEXT.TXT");
	ReWrite(UFile); 
	Writeln(UFile, "How many sentences " + "are present in this file?");
	Close(UFile);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
        

    def test_string_4(self):
        input = """
Var
	UFile : String;

Procedure Main();
Begin
	Assign(UFile, "C:\\\\ADDTEXT.TXT");
	Append(UFile); 
	Writeln(UFile, "How many sentences, "+"are present in this file?");
	Close(UFile);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
        

    def test_string_5(self):
        input = """
Var
	UFile : String; { or it could be of "file" type}

Procedure Main();
Begin
	Assign(UFile, "C:\\\\ADDTEXT.TXT");
	Erase(UFile); 
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
        

    def test_string_6(self):
        input = """
Var
	t : String;
	s : String;

Procedure main();
Begin
	Assign(t, "C:\\\\ABC.DEF");
	{$I-}   { disable i/o error checking }
	Reset(t);
	{$I+}   { enable again i/o error checking - important }
	If (IOResult <> 0) Then
	Begin
		Writeln("The file required to be opened is not found!");
		Readln();
	End Else 
	Begin
		Readln(t,s);
		Writeln("The first line of the file reads: ",s);
		Close(t);
	End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
        

    def test_string_7(self):
        input = """
Var
	NewDir : String; { for searching the dir and create a new one, if it does not exist }
	F : String;

Procedure Main();
Begin
	{ search for the dir }
	NewDir := FSearch("C:\\\\Pascal Programming", GetEnv("")); 
	{ create a new one, if it does not exist }
	If NewDir = "" Then
		CreateDir("C:\\\\Pascal Programming"); 
	Assign(F,"C:\\\\Pascal Programming\\\\pascal-programming.txt");
	{$I-} ReWrite(F); {$I+} { disable and enable back again I/O error checking } 
	{ write to text file } 
	Writeln(F,"http://pascal-programming.info/"); 
	{$I-} Close(F); {$I+}
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
        

    def test_string_8(self):
        input = """
Var
	f : String; { file var of type byte }
	sz : Integer;  { var for the size }

Procedure Main();
Begin
	Assign(f,"C:\\\\anyfile.txt");
	{$I-} Reset(f); {$I+}
	If (IOResult <> 0) Then
    Begin     { file found? }
        Writeln("File not found.. exiting");
        Readln();
    End Else
    Begin
			{ Return the file size in Kilobytes }
        sz := Round(FileSize(f)/1024);
        Writeln("Size of the file in Kilobytes: ",sz," Kb");
        Readln();
    Close(f); 
    End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
        

    def test_array_1(self):
        input = """
Var
	myVar : Integer;
	myArray : Array[1 .. 5] of Integer;

Procedure Main();
Begin
	myArray[2] := 25;
	myVar := myArray[2];
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
        

    def test_array_2(self):
        input = """
Var
	i : Integer;
	myIntArray : Array[1 .. 20] of Integer;
	myBoolArray : Array[1 .. 20] of Boolean;

Procedure Main();
Begin
	For i := 1 to Length(myIntArray) do
	Begin
		myIntArray[i] := 1;
		myBoolArray[i] := True;
	End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
        

    def test_string_9(self):
        input = """
Var
    myString : String;

Procedure Main();
Begin
	myString := "Hey! How are you?";
	Writeln("The length of the string is ", byte(myString[0]));
	Write(myString[byte(myString[0])]);
	Write(" is the last character.");
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
        

    def test_string_10(self):
        input = """
Var
	S : String;

Procedure main();
Begin
	S := "Hey there! How are you?";
	Write("The word \\"How\\" is found at char index ");
	Writeln(Pos("How", S));
	If Pos("Why", S) <= 0 Then
		Writeln("\\"Why\\" is not found.");
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
        

    def test_string_11(self):
        input = """
Var 
	S : String;

Procedure main();
Begin
	S := "Hey there! How are you?";
	S := Copy(S, 5, 6); { "there!" }
	Write(S);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
        

    def test_string_12(self):
        input = """
Var 
	S : String;

Procedure main();
Begin
	S := "Hey Max! How are you?";
	Delete(S, 4, 4); { "Hey! How are you?" }
	Write(S);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
        

    def test_string_13(self):
        input = """
Var 
	S : String;

Procedure main();
Begin
	S := "Hey! How are you?";
	Insert(" Max", S, 4);
	Write(S);
    { "Hey Max! How are you?" }
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
        

    def test_string_14(self):
        input = """
Var 
	S1, S2 : String;

Procedure main();
Begin
	S1 := "Hey!";
	S2 := " How are you?";
	Write(Concat(S1, S2)); { "Hey! How are you?" }
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
        

    def test_string_15(self):
        input = """
Var 
	S1, S2 : String;

Procedure main();
Begin
	S1 := "Hey!";
	S2 := " How are you?";
	Write(S1 + S2); { "Hey! How are you?" }
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
        

    def test_string_16(self):
        input = """
Var 
    S : String;
    i : Integer;

Procedure main();
Begin
	S := "Hey! How are you?";
	For i := 1 to length(S) do
		S[i] := UpCase(S[i]);
	Write(S); { "HEY! HOW ARE YOU?" }
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
    
    def test_procedure_1(self):
        input="""
        procedure foo (a,b: integer;c: real);
        var x,y: real;
        begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_procedure_2(self):
        input="""
        procedure foo (a,b: integer);
        var x,y: real;
        begin
        end
        procedure main();
        //this is a comment
        var a,b: integer;
        begin
        foo();
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_procedure_3(self):
        input = """
        procedure foo (a,b: integer);
        var x,y: real;
        begin
        end
        procedure main();
        //this is a comment
        var a,b: integer;
        begin
            a:= 1;
            for i:=1 to 5 do
            begin
                pritnt(a);
                foo(a,b);
            end                  
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_procedure_4(self):
        input = """
        procedure main();
        //this is a comment
        var a,b: integer;
            c:array [1 .. 2] of real;
        begin
            a:= 1;
            if a>1 then
                foo(a,b);
            else
                a := foo(a,b)+3;
            while a=1 do a:=c-b;
            for i:=1 to a*2 do foo(a,b);
            break;
            continue;
            return foo(a,b);
            with a:integer; b:real; do
            begin
                a:=foo(a,b);
                print(a);
            end

        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))


    def test_error_semi(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            for a:=1 to n do
            begin
                if x >= 4 or  x < 4 then
                begin
                    foo(3);
                    a:=1;
                end
                else
                begin
                    foo(1.);
                    ;
                end
            end
        end
        """
        expect = "Error on line 7 col 32: <"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_operator_error_1(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            foo(-+3);
        end
        """
        expect = "Error on line 5 col 17: +"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_for_error(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            for a:=1,b:=2 to n do foo(a,b);  
        end
        """
        expect = "Error on line 5 col 20: ,"
        self.assertTrue(TestParser.test(input,expect,258))

    def test_operator_error_2(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            a:=1;
            x:= + 1;
        end
        """
        expect = "Error on line 6 col 16: +"
        self.assertTrue(TestParser.test(input,expect,259))

    def test_index_exp_1(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            a[.2e+12 + 3] := 3;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_non_assoc(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            a[.2e3 >= 5 < 12 + 3] := 3;
        end
        """
        expect = "Error on line 5 col 24: <"
        self.assertTrue(TestParser.test(input,expect,261))


    def test_exp_error(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            a[1] := 02_;
        end
        """
        expect = "Error on line 5 col 22: _"
        self.assertTrue(TestParser.test(input,expect,262))

    def test_index_exp_2(self):
        input = """
        procedure foo(a,b:integer);
        var x:real;
        begin
            a[-1] := 02;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))

    def test_complex_function_1(self):
        input = """
Procedure BubbleSort(numbers : Array[1 .. n] of Integer; size : Integer);
Var
	i, j, temp : Integer;

Begin
	For i := size-1 DownTo 1 do
		For j := 2 to i do
			If (numbers[j-1] > numbers[j]) Then
			Begin
				temp := numbers[j-1];
				numbers[j-1] := numbers[j];
				numbers[j] := temp;
			End

End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
        

    def test_complex_function_2(self):
        input = """
Procedure InsertionSort(numbers : Array[1 .. n] of Integer; size : Integer);
Var
	i, j, index : Integer;


Begin
	For i := 2 to size-1 do
	Begin
		index := numbers[i];
		j := i;
		While ((j > 1) AND (numbers[j-1] > index)) do
		Begin
			numbers[j] := numbers[j-1];
			j := j - 1;
		End
		numbers[j] := index;
	End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
        

    def test_complex_function_3(self):
        input = """
Procedure QSort(numbers : Array [1 .. n] of Integer; left : Integer; right : Integer);
Var 
	pivot, l_ptr, r_ptr : Integer;

Begin
	l_ptr := left;
	r_ptr := right;
	pivot := numbers[left];

	While (left < right) do
	Begin
		While ((numbers[right] >= pivot) AND (left < right)) do
			right := right - 1;

		If (left <> right) Then
		Begin
			numbers[left] := numbers[right];
			left := left + 1;
		End

		While ((numbers[left] <= pivot) AND (left < right)) do
			left := left + 1;

		If (left <> right) Then
		Begin
			numbers[right] := numbers[left];
			right := right - 1;
		End
	End

	numbers[left] := pivot;
	pivot := left;
	left := l_ptr;
	right := r_ptr;

	If (left < pivot) Then
		QSort(numbers, left, pivot-1);

	If (right > pivot) Then
		QSort(numbers, pivot+1, right);
End

Procedure QuickSort(numbers : Array [1 .. n] of Integer; size : Integer);
Begin
	QSort(numbers, 0, size-1);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
        
    def test_break(self):
        input = """
var
    a: integer;
procedure main();
begin
    a := 10;
   (* while loop execution *)
    while  a < 20 do
    begin
        writeln("value of a: ", a);
        a:=a +1;
    
        if( a > 15) then
            (* terminate the loop using break statement *)
        break;
    end
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
        

    def test_continue(self):
        input = """
var
    a: integer;

procedure main();
begin
    a := 10;

    while not ( a = 20 ) do
    begin
        if( a = 15) then

    begin
            (* skip the iteration *)
            a := a + 1;
            continue;
        end
        writeln("value of a: ", a);
        a := a+1;
    end
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))

    def test_wrong_miss_close_1(self):
        input = """proceDure main( beGin end"""
        expect = "Error on line 1 col 16: beGin"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_wrong_miss_close_2(self):
        input = """function main( beGin end"""
        expect = "Error on line 1 col 15: beGin"
        self.assertTrue(TestParser.test(input,expect,270))

    def test_function_decl_1(self):
        input = """FUNcTION fooc( b: boolean; c: real):array [1 .. 2] of integer ;
                var x: real ;
                BEGIN
                END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))

    def test_function_decl_2(self):
        input = """
                FUNcTION foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                    var t,y: real ;
                    BEGIN
                    return a[1];
                    END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def test_procedure_decl_1(self):
        input = """proCeduRe foo(a, b: integer ; c: real) ;
                    var x,y: real ;
                    BEGIN
                    END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_procedure_decl_2(self):
        input = """proCeduRe foo(c: real) ;
                    var x,y: real ;
                    BEGIN
                    END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

    def test_assign_stmt_1(self):
        input = """proCeduRe foo(a, b: integer ; c: real) ;
                var x,y: real ;
                BEGIN
                    a := 1;
                    b := a[12] ;
                END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))

    def test_assign_stmt_2(self):
        input = """proCeduRe foo() ;
                var x,y: real ;
                BEGIN
                    a := "conga";
                    b := func(1,a+1) ;
                END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_assign_stmt_3(self):
        input = """proCeduRe foo(c: real) ;
                    var x,y: real ;
                    BEGIN
                    z := asdfas[afas]+2;
                    c := a[12] ;
                    END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))

    def test_error_1(self):
        input = """
        PROCEDURE test_err();
        begin
            foo(a >= b = 1);
        end
        """
        expect = "Error on line 4 col 23: ="
        self.assertTrue(TestParser.test(input,expect,278))

    def test_error_2(self):
        input = """
        PROCEDURE test_err();
        begin
            foo(a[1][1] >= b[1] = 1);
        end
        """
        expect = "Error on line 4 col 32: ="
        self.assertTrue(TestParser.test(input,expect,279))

    def test_error_3(self):
        input = """
        PROCEDURE test_err();
        begin
            (-(1[1]))[1] := """"asd"""" := ("aasd"+1;
        end
        """
        expect = "Error on line 4 col 12: ("
        self.assertTrue(TestParser.test(input,expect,280))

    def test_error_4(self):
        input = """
        PROCEDURE test_err();
        begin
            foo();
        end+
        """
        expect = "Error on line 5 col 11: +"
        self.assertTrue(TestParser.test(input,expect,281))

    def test_error_5(self):
        input = """
        function test_err():boolean;
        begin
            foo();
        end ;;;;;
        """
        expect = "Error on line 5 col 12: ;"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_error_6(self):
        #wrong type
        input = """
        PROCEDURE test_err();
        var asd:longint;
        begin
            foo();
        end
        """
        expect = "Error on line 3 col 16: longint"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_error_7(self):
        #unknown token
        input = """
        PROCEDURE test_err();
        begin
            1e := 1;
        end
        """
        expect = "Error on line 4 col 12: 1"
        self.assertTrue(TestParser.test(input,expect,284))
    
    def test_error_10(self):
        #wrong var usage
        input = """
        begin;
        end
        """
        expect = "Error on line 2 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_error_8(self):
        #wrong var usage
        input = """
        var a:integer;
        begin
        end
        """
        expect = "Error on line 3 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_error_9(self):
        input = """
        PROCEDURE test_err();
        var a, b, c: integer;
        begin
            while true do
            begin
                for i:=1 TO iNfInItY_aNd_bEyOnD do
                    begin
                        with d:integer; do arr[3][3][3] := arr[2][2] := "str" := a[3];
                    end
            end
        end
        """
        expect = "Error on line 9 col 49: ["
        self.assertTrue(TestParser.test(input,expect,287))

    def test_nested_1(self):
        input = """
                function foo(): boolean;
                    procedure foo_child(); 
                        begin
                        end
                    begin
                    end
                """
        expect = "Error on line 3 col 20: procedure"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_nested_2(self):
        input = """
                procedure foo();
                    function foo_child():boolean; 
                        begin
                        end
                    begin
                    end
                """
        expect = "Error on line 3 col 20: function"
        self.assertTrue(TestParser.test(input,expect,289))

    def test_built_in(self):
        input = """procedure foo(a : integer);
            begin
            putIntLn(4);
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))
    
    def test_array_4(self):
        input = """procedure foo();
    begin
        a := b[4+1+2];
    return;
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_array_3(self):
        input = """procedure foo(a : integer;b : real);
    begin
        e := (3+4)/3;
        putint(a);
        a := b[4];
    return;
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

    def test_with_1(self):
        input = """procedure foo(a : integer;b : real);
    begin
        with a,b : integer; d: integer; do d := c[b] + a;
    return;
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))

    def test_assign_stmt_4(self):
        input = """procedure foo(a : integer;b : real);
    begin
        d := a[b] := b + 5;
    return;
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))

    def test_index_exp_3(self):
        input = """function foo(a : integer;b : real): array [1 .. 5] of real;
            begin
                foo(2)[3+x] := a[b[2]] + 3;
                return a;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

    def test_if_9(self):
        input = """procedure main();
            begin
                if a>b then a := b; else b:=a ;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_exp_1(self):
        input = """procedure main();
            begin
                 a := (3+4*(5/4)-20+100 mod 4) ;
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))

    def test_exp_2(self):
        input = """procedure foo(a:integer);
                begin
                    while true do putstring(a);
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))

    def test_with_2(self):
        input = """var i : integer;
        function f(): integer;
        begin
        return 200;
        end
        procedure main();
        var
            main: integer;
        begin
            main := f;
            foo();
            putintln(main);
            with 
                i: integer;
                main: integer;
                f: integer;
            do  begin 
                main := f := i := 100;
                putIntLn(main);
                putIntLn(f);
                putIntLn(i);
                end
                putintlN(main);
        end
            var g: real;

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))

    def test_call_stmt(self):
        input = """function xix(c: real): integer;
                BEgin
                    test(brown);
                	ClrScr(); 
                    return func(a(1,2));
                EnD
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))    

    