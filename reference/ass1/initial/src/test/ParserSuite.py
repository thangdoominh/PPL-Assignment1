import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_procedure_findMin(self):
        input = """
                var
            a, b, c,  min: integer;
        procedure findMin(x, y, z: integer; m: integer); 
        (* Finds the minimum of the 3 values *)

        begin
            if x < y then
                m:= x;
            else
                m:= y;

            if z < m then
                m:= z;
        end { end of procedure findMin }  

        procedure main();
        begin
            writeln(" Enter three numbers: ");
            readln( a, b, c);
           findMin(a, b, c, min); (* Procedure call *)

            writeln(" Minimum: ", min);
        end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_function_checkSymmetric(self):
        """More complex program"""
        input = """
        Function checkSymmetric (A:array[0 .. 10] of REAL; N:Integer ) : Boolean;
                Var Flag:Boolean;
                    i :Integer;
                Begin
                Flag:=True;
                For  i :=1 to N do
                If(A[i] <> A[N-i  +1]) Then
                Flag :=False;       { Cham dut kiem tra, ket qua qua trinh : khong doi xung }
                return flag;
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_function_findFibonacci(self):
        input = """
        function fibo(x: integer): integer;
                var f1,f2: integer;
                Begin
                if x<=2 then
                return 1;
                else
                return fibo(x-2)+ fibo(x-1);
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_function_UCLN(self):
        input = """
        Function UCLN(m,n:integer):integer;
        Begin
        If(m=n) then RETURN m ;
        else
            If (m>n) then return UCLN(m-n,n);
            else return UCLN(m,n-m);
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_function_findMax(self):
        input = """
        function max(num1, num2: integer): integer;

        var
        (* local variable declaration *)
        result: integer;
        
        begin
        if (num1 > num2) then
            result := num1;
        
        else
            result := num2;
            max := result;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_function_sumRealArray(self):
        input = """
        function sum_real_array(a: array[0 .. m-1] of real;n:integer):real;
                var i:integer;s:real;
                beGin
                    s:=0.;
                    for i:=n-1 doWnTO 0 do s:=s+a[i];
                    reTuRn s;
                eND
                procedure main() ;
                var a: array[0 .. m-1] of real; n:integer;
                beGin
                    Writeln("Sum of real array: "+sum_real_array(a,n));
                eND
        """
        expect = "Error on line 2 col 46: m"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_varDeclare(self):
        input = """var a: array[2 .. 10] of real;
            b,c: integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_procedure_BubbleSort(self):
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
        expect = "Error on line 2 col 58: n"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_procedure_InsertionSort(self):
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
        expect = "Error on line 2 col 53: n"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_procedure_QuickSort(self):
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
        expect = "Error on line 2 col 46: n"
        self.assertTrue(TestParser.test(input,expect,210))
    
    def test_function_findMax_Err(self):
        input = """
                var
            a, b, ret : integer;
        (*function definition *)
        function max(num1, num2: integer): integer;
        var
           (* local variable declaration *)
            result: integer;
        begin
            if (num1 > num2) then
            result := num1;
            else
            result := num2;
            max := result;
        end
        begin
        end
        """
        expect = "Error on line 16 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_procedure_findMin_Err(self):
        input = """
                var
        a, b, c,  min: integer;
        procedure findMin(x, y, z: integer; m: integer); 
        (* Finds the minimum of the 3 values *)
        
        begin
            check: boolean;
            if x < y then
            m:= x;
            else
            m:= y;
        
            if z < m then
            m:= z;
        end { end of procedure findMin }  
        
        procedure main();
        begin
            writeln(" Enter three numbers: ");
            readln( a, b, c);
            findMin(a, b, c, min); (* Procedure call *)
        
            writeln(" Minimum: ", min);
        end
        """
        expect = "Error on line 8 col 17: :"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_function_Assign(self):
        input = """
        function foo(c: real): real ;
        var x: integer ;
        BEGIN
         a[m+n] := a[m+1] := foo()[m*1] := a[a div 3] := (a>m) and then (b<n);
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_function_Call(self):
        input = """
        function foo(c: real): integer;
        BEGIN
            foo(3,a+1,x and then y,a[1],foo(1,2)[m+1]);
            return 1;
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_procedure_If(self):
        input = """
        procedure test1() ;
        bEgin
	        if a=b then
	        begin
		        b := c ;
	            if(e <> f) then foo(a,c) ;
	        end
        eNd
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_procedure_Swap(self):
        input = """
                var
            a, b : integer;
        (*procedure definition *)
        procedure swap(x, y: integer); 

        var
            temp: integer;

        begin
            temp := x;
            x:= y;
            y := temp;
        end

        procedure main();
        begin
            a := 100;
            b := 200;
            writeln("Before swap, value of a : ", a );
            writeln("Before swap, value of b : ", b );

            (* calling the procedure swap  by value   *)
            swap(a, b);
            writeln("After swap, value of a : ", a );
            writeln("After swap, value of b : ", b );
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def test_procedure_Triangle(self):
        input = """
        Var a,b,c,s,p: real;
        pROCEDURE main() ;
        Begin
        Clrscr();
        Writeln("Triangle:");
        Writeln("---------------------------------");
        Write("a =");readln(a);
        Write("b =");readln(b);
        Write("c =");readln(c);
        If ((a+b)>c)and((b+c)>a)and((a+c)>b) then
            Begin
            p:=(a+b+c)/2;
            s:=sqrt(p*(p-a)*(p-b)*(p-c));
            Writeln("P= ",2*p);
            Writeln("S=",s);
            End
        Else Writeln(a,", ", b,", ", c, ": Not a triangle!");
        Readln();
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))

    def test_procedure_Circle(self):
        input = """
        Var r,dt,cv:real;
        pROCEDURE main() ;
        Begin
            Clrscr();
            Writeln("Circle:");
            Writeln("--------------------------------------------------");
            Write ("R="); readln(r);
            dt:=pi*r*r;
            cv:=2*pi*r;
            Writeln("S= ",dt);
            Writeln("P= ",cv);
            Readln();
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_procedure_For(self):
        input = """
        Procedure ForCheck(A:array[0 .. 10] of REAL;N: Integer; k, X:Integer);
                Var i :Integer;
                Begin
                For i:=N downto k+ 1 do
                A[i] := A[i-1];
                A[k] := X;
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_varDeclaration_Array(self):
        input = """
        A:array[0 .. 10] of REAL
        """
        expect = "Error on line 2 col 8: A"
        self.assertTrue(TestParser.test(input,expect,220))
    
    def test_varDeclaration_Array_Err(self):
        input = """
        fun()[69]:array[0 .. 10] of REAL
        """
        expect = "Error on line 2 col 8: fun"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_procedure_Null(self):
        input = """
        VAR Hours, Pay: INTEGER;
        PROCEDURE main();
        """
        expect = "Error on line 4 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_procedure_With_Err(self):
        input = """
        var
            greetings: string;
            name: array [1 .. 10] of integer;
            organisation: string;

        procedure main();
        begin
            greetings := "Hello ";
            message := "Good Day!";

            writeln("Please Enter your Name");
            readln(name);
        with
            writeln("Please Enter the name of your Organisation");
            readln(organisation);

            writeln(greetings, name, " from ", organisation);
            writeln(message); 
        end
        """
        expect = "Error on line 15 col 19: ("
        self.assertTrue(TestParser.test(input,expect,223))

    def test_procedure_checkDeclaration_Err_01(self):
        input = """
        var
        a, b, c: integer;
        procedure display();
        var
        """
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_procedure_checkDeclaration_Err_02(self):
        input = """
                var
        a, b, c: integer;
        procedure display();
        var
        x, y, z: integer;
        """
        expect = "Error on line 7 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_procedure_Swap_Err(self):
        input = """
        procedure swap(x, y: integer); 
        var
            temp: integer;
        beGin
        var A:array[0-100 .. a-10] of REAL;
        begin
            temp := x;
            x:= y;
            y := temp;
        end
        end
        """
        expect = "Error on line 6 col 8: var"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_function_CountFromX(self):
        input = """
        Function CountFromX(A:array[0 .. 10] of integer; N,X : Integer) : Integer;
                Var i , Count : Integer;
                Begin
                    Count := 0;
                    For i:=0 to N do
                    If ( A[i] = X ) then
                    Count := Count + 1;
                    return Count;
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_procedure_Array1D(self):
        input = """
        Procedure Array1D(A : array[0 .. 10] of integer;N:Integer);
                Var i: Integer;
                Begin
                Write("N=");
                Readln( N);
                For i:=0 to N do
                    Begin
                        Write("N[", i,"]= ");
                        Readln( A[i] );
                    End
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_function_statement_Err(self):
        input = """
        function statement(c: real): integer;
        BEGIN
            if()
            then
            statement(3,a+1,a<>1,a[1]);
            return 1;
            else
            return;
        END
        """
        expect = "Error on line 4 col 15: )"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_procedure_sumRealArray(self):
        input = """
        function sum_real_array(a: array[0 .. m-1] of real;n:integer):real;
                var i:integer;s:real;
                beGin
                    s:=0.;
                    for i:=n-1 doWnTO 0 do s:=s+a[i];
                    reTuRn s;
                eND
                procedure main() ;
                var a: array[0 .. m-1] of real; n:integer;
                beGin
                    Writeln("Sum of real array: "+sum_real_array(a,n));
                eND
        """
        expect = "Error on line 2 col 46: m"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_procedure_Sum(self):
        input = """
        Var
                Num1, Num2, Sum : Integer;
            Procedure Sum(a, c:Real);
            Begin {no semicolon}
                Write("Input num 1:");
                Readln(Num1);
                Writeln("Input num 2:");
                Readln(Num2);
                Sum := Num1 + Num2;
                Write(Sum);
                Readln();
            End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    
    def test_procedure_Coercions(self):
        input = """
        Procedure Array1D(A : array[0 .. 10] of integer;N:Integer);
        begin
        Procedure Sum(a, c:Real);
        begin
        end
        end
        """
        expect = "Error on line 4 col 8: Procedure"
        self.assertTrue(TestParser.test(input,expect,232))
    
    def test_function_PrimeNum(self):
        input = """
        Function getPrime(N:Integer) :Integer;
                Var i:Integer;
                Begin
                    For i:=2 to N-1 do
                    If(N mod i = 0) then
                        return 0;
                    Else
                        return 1;
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
    
    def test_function_IncreaseArray(self):
        input = """
        Function checkIncreaseArray( A:array[0 .. 10] of REAL; N :Integer) : Boolean;
            Var Flag : Boolean;
                i :Integer;
            Begin
                Flag := True;
                i:= 0;
                while(i<n) do begin
                    If(A[i] < A[i-1]) Then
                    Flag :=False; { Cham dut kiem tra, ket qua qua trinh : khong tang }
                i:=i+1;
            end
                return Flag;
            End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    
    def test_procedure_EasyTest_01(self):
        input = """
        Var
            S : String;
            i : Real;

        Procedure main();
        Begin
            i := -0.563;
            Str(i, S);
            Write(S);
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    
    def test_procedure_EasyTest_02(self):
        input = """
        Var
            S     : String;
            error : Integer;
            R     : Real;

        Procedure main();
        Begin
            S := "-0.563";
            Val(S, R, error);
            If error > 0 Then
                Write("Error in conversion.");
            Else
                Write(R);
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    
    def test_procedure_Push(self):
        input = """
        Procedure Push(item : Integer);
        Begin
            If not IsFull Then
        Begin
            myStack[topPointer+1] := item;
            topPointer := topPointer + 1;
        End
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    
    def test_function_getSite(self):
        input = """
        Function GetSize() : Integer;
        Begin
        GetSize := topPointer;
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    
    def test_procedure_EasyTest_03(self):
        input = """
        
        Var Ch : String;

        Procedure main();
        Begin
        Writeln("Press \\"\\"q\\"\\" to exit...");
        Ch := Readkey();
        While Ch <> "q" do
        Begin
            Writeln("Please press \\"\\"q\\"\\" to exit.");
            Ch := Readkey();
        End
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    
    def test_procedure_Factorial_01(self):
        input = """
        Function Factorial(n : Integer) : Integer;
        Var
            Result : Integer;
            i : Integer;

        Begin
            Result := n;
            If (n <= 1) Then
                Result := 1;
            Else
            For i := n-1 DownTo 1 do
                Result := Result * i;
            Factorial := Result;
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    
    def test_procedure_Factorial_02(self):
        input = """
        Function Factorial(n : Integer) : Integer;
        Var
            Result : Integer;

        Begin
            If n = 1 Then
                Factorial := 1;
            Else
                Factorial := n*Factorial(n-1);
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    
    def test_procedure_EasyTest_Err_01(self):
        input = """
        procEdure main();
        var a:integer;
        begin
            a := a = a and then b or else ;
        end
        """
        expect = "Error on line 5 col 37: else"
        self.assertTrue(TestParser.test(input,expect,242))
    
    def test_procedure_EasyTest_Err_02(self):
        input = """
        procedure main();
        begin
            writeln("Please enter your first name: ");
            readln(firstname);

            writeln("Please enter your surname: ");
            readln(surname);
            /""''""
            writeln();
            writeln(message, " ", firstname, " ", surname);
        end
        """
        expect = "Error on line 9 col 12: /"
        self.assertTrue(TestParser.test(input,expect,243))
    
    def test_procedure_Writeln(self):
        input = """
        procedure main();
        begin
            a := 100;
            (* check the boolean condition *)
            if( a < 20 ) then
                (* if condition is true then print the following *)
            writeln("a is less than 20" );
            writeln(((())));
            else
              (* if condition is false then print the following *)
                writeln("a is not less than 20" );
                writeln("value of a is : ", a);
        end
        """
        expect = "Error on line 9 col 23: )"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_procedure_Loop_Err(self):
        input = """
        Procedure main();
        Begin
            For Counter := 1 to 7 do { it"s easy and fast! }
                Writeln("for loop");
            Readln();
            return ret[1][1]++;
        End
        """
        expect = "Error on line 7 col 29: +"
        self.assertTrue(TestParser.test(input,expect,245))
    
    def test_function_TRUEFALSE(self):
        input = """
        Function IsFull() : Boolean;
        Begin
            IsFull := False;
            If ((topPointer + 1) = STACK_SIZE) Then
                IsFull := True;
            return TRUE-FALSE;
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    
    def test_function_Empty(self):
        input = """
        Function IsEmpty() : Boolean;
        Begin
            IsEmpty := False;
            If (topPointer = 0) Then
            IsEmpty := true;
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    
    def test_procedure_Pop(self):
        input = """
        Procedure Pop(item : Integer);
        Begin
            If not IsFull Then
        Begin
            item:= myStack[topPointer];
            topPointer := topPointer - 1;
        End
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_EOF(self):
        input = """
        EOF
        """
        expect = "Error on line 2 col 8: EOF"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_procedure_EasyTest_04(self):
        input = """
        procedure main();
        begin
            a:= 10;
            (* check the boolean condition using if statement *)

            if( a < 20 ) then
            (* if condition is true then print the following *)
            writeln("a is less than 20 " );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_fucntion_Miss_EOF(self):
        input = """
        var
        a, b, ret : integer;

        (*function definition *)
        function max(num1, num2: integer): integer;
        var
        (* local variable declaration *)
        result: integer;

        begin
        if (num1 > num2) then
        result := num1;

        else
        result := num2;
        max := result;

        begin
        a := 100;
        b := 200;
        (* calling a function to get max value *)
        ret := max(a, b);

        writeln( "Max value is : ", ret );
        end
        """
        expect = "Error on line 27 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_procedure_Name(self):
        input = """
        VAR FirstName,  LastName, FullName: STRING;
        Count,  NameCount, Gap: INTEGER;
        PROCEDURE main();
        BEGIN
        Space := "  ";
        Hyphen := "-";
        Greeting :=  "Hello there ";
        Write("Enter the  number of names: ");
        ReadLn(NameCount);
        WriteLn();
        WHILE NameCount  >0 DO BEGIN
        Write("Enter a  name, last name first: ");
        Read(FullName);
        Gap :=  POS(Space, FullName); { NOTE }
        IF Gap > 0  THEN BEGIN
        LastName :=  Copy(FullName, 1, Gap);
        Delete(FullName,  1, Gap); { NOTE }
        FirstName :=  FullName;
        IF Length(LastName) <= 4 THEN
        WriteLn("That is  a short last name");
        IF Pos(Hyphen,  LastName) <> 0 THEN
        WriteLn("That is  a hyphenated name");
        IF FirstName =  "Bill" THEN { etc., etc. }
        WriteLn("Bill is  a good name ");
        FullName :=  FirstName + Space + LastName;
        WriteLn(Greeting,  FullName);
        WriteLn();
        END { IF }
        NameCount :=  NameCount - 1;
        END { WHILE }
        END { NameParse  }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    
    def test_procedure_Cost(self):
        input = """
        VAR Pennies:  INTEGER;
        Tendered, Cost,  Remainder: REAL;
        PROCEDURE Main();
        BEGIN
        (* Input  necessary information *)
        Write("Enter cost  of item: ");
        Read(Cost);
        Write("Enter  amount tendered: ");
        Read(Tendered);
        (* Compute the  change in pennies *)
        Remainder :=  Tendered - Cost;
        Pennies := 0;
        WHILE Remainder  > 0 DO BEGIN
        Remainder :=  Remainder - 0.01;
        Pennies :=  Pennies + 1;
        END (* WHILE *)
        (* Output all  required Results *)
        Write("Cost is:  ");
        Write(Cost);
        Write(" Amount  tendered is: ");
        Write(Tendered);
        Write(" Change  is: ");
        WriteLn(Pennies);
        END (*  BadChanger *)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_procedure_Time(self):
        input = """
        { An Extended  Payroll program
        }
        { Selection  nested in Else branch of outer
        Selection }

        VAR Hours, Pay: INTEGER;
        PROCEDURE main();
        BEGIN
        RegularRate := 10;
        ExtraRate := 15;
        DoubleRate := 20;
        BaseHours := 40;
        ExtraHours := 20;
        DoubleTimeStart  := BaseHours + ExtraHours;
        BasePay :=  RegularRate * BaseHours;
        ExtraPay :=  ExtraRate * ExtraHours;
        Write("Enter  hours");
        Read(Hours);
        WriteLn();
        IF Hours >  DoubleTimeStart THEN
        Pay := BasePay +  ExtraPay +
        DoubleRate *  (Hours -
        DoubleTimeStart);
        ELSE
        IF Hours <=  BaseHours THEN
        Pay :=  RegularRate * Hours;
        ELSE
        Pay := BasePay +
        ExtraRate *  (Hours -
        BaseHours);
        Write("The gross  pay is ");
        Write(Pay);
        WriteLn();
        END {  ExtendedPay }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_procedure_Payroll(self):
        input = """
        var i: integer ;
                function f(): integer ;
                begin
	                return 200;
                end
                procedure main() ;
                var
	                main: integer ;
                begin
	                main := f() ;
	                putIntLn(main);
	                with
                        i: integer;
            		    main: integer;
            		    f: integer;
	                do begin
		                main := f := i:= 100;
		                putIntLn (i);
		                putIntLn (main );
		                putIntLn (f);
	                end
	                putIntLn (main);
                end
                var g: real ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))

    def test_procedure_Writeln_Hash(self):
        input = """
        procedure main();
        begin
            writeln("27e1615212f3c6ea846ed6c412df1361ce97f006ee20bb5aa2483a3b61d5cadd");
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_procedure_EasyTest_Err_03(self):
        input = """
        var
        a: integer;

        procedure main();
        begin
            for a := 10  to 20 do
                b: integer;
            begin
                writeln("value of a: ", a);
            end
        end
        """
        expect = "Error on line 8 col 17: :"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_procedure_EasyTest_Err_04(self):
        input = """
        var
            a: integer;

        procedure main();
        begin
            a := := 10;
            while  a < 20  do

            begin
                writeln("value of a: ", a);
                a := a + 1;
            end
        end
        """
        expect = "Error on line 7 col 17: :="
        self.assertTrue(TestParser.test(input,expect,258))

    def test_procedure_EasyTest_Err_05(self):
        input = """
        pROCEDURE foo(c: real) ;
            BEGIN
                with a , b : integer ; c : array [1 .. 2] of real;
            END
        """
        expect = "Error on line 5 col 12: END"
        self.assertTrue(TestParser.test(input,expect,259))

    def test_procedure_EasyTest_Err_06(self):
        input = """
        pROCEDURE foo(c: real) ;
            BEGIN
            with a , b : integer ; c : array [1 .. 2] of real ;
            d := c [a] + b ;
            END
        """
        expect = "Error on line 5 col 14: :="
        self.assertTrue(TestParser.test(input,expect,260))

    def test_procedure_EasyTest_Err_07(self):
        input = """
        pROCEDURE foo(c: real) ;
            BEGIN
                whILe(a<>1) do beGin
                    while(1) do x:=1;
                    if(a=1) then begin
                end
            END
        """
        expect = "Error on line 9 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,261))

    def test_procedure_EasyTest_Err_08(self):
        input = """
        var x:real ;
            BEGIN
                whILe(a<>1) do beGin
                    if(a=1) then;
                    foo();
                end
            END
        """
        expect = "Error on line 3 col 12: BEGIN"
        self.assertTrue(TestParser.test(input,expect,262))

    def test_procedure_EasyTest_Err_09(self):
        input = """
        procedurE foo (b : real) ;
            begin
            1[1] := 1[1..1];
            (1>=0)[2] := 2+a[1][1]+c+("abc"< 0);
            ahihi(1)[m+1] := 3;
            (1+a[1]+(1<0))[10] := 4;
            End
        """
        expect = "Error on line 4 col 24: .1"
        self.assertTrue(TestParser.test(input,expect,263))

    def test_procedure_ArrayIndex1(self):
        input = """
        procedurE foo (b : real) ;
            begin
            1[1] := 1;
            (1>=0)[2] := 2+a[1][1]+c+("abc"< 0);
            ahihi(1)[m+1] := 3;
            (1+a[1]+(1<0))[10] := 4;
            End
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))

    def test_procedure_EasyTest_Err_10(self):
        input = """
        FUNcTION foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
                var x,y: real ;
                END
                BEGIN
        """
        expect = "Error on line 4 col 16: END"
        self.assertTrue(TestParser.test(input,expect,265))

    def test_procedure_EasyTest_Err_11(self):
        input = """
        function foo(c: real): integer;
            BEGIN
            textbackground(brown); {background colour}
            ClrScr(); {Clear screen with a brown colour. Try run the program without this..}
            return func(a(1,2))[2]:=1;*
            END
        """
        expect = "Error on line 6 col 31: ["
        self.assertTrue(TestParser.test(input,expect,266))

    def test_procedure_EasyTest_Err_12(self):
        input = """
        function foo(c: real): integer;
            BEGIN
            while (1] do reTuRn foo(a+1) with;
            END
        """
        expect = "Error on line 4 col 20: ]"
        self.assertTrue(TestParser.test(input,expect,267))

    def test_procedure_EasyTest_Err_13(self):
        input = """
        function foo(c: real): integer;
            BEGIN
                foo(3,a+1,a<>1,a[1]);
                return 1;
                -1--[];
            END
        """
        expect = "Error on line 6 col 20: ["
        self.assertTrue(TestParser.test(input,expect,268))

    def test_procedure_EasyTest_05(self):
        input = """
        procedure test() ;
                begin
	                if a<>b then
	                begin
		                b := c ;
		                if(e <> f) then foo(a,c) ;
	                end
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_procedure_EasyTest_06(self):
        input = """
        procedure test2() ;
                begin
	                if a=b then if c=d then while (d=e) do
                    beGin
                    eND
                else c := 1;
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

    def test_procedure_EasyTest_07(self):
        input = """
        proceDure Hello(a, b:integer);
                begin
                    a := b + c;
                    writeln("Hello, world!");
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))

    def test_procedure_EasyTest_08(self):
        input = """
        procedure main() ;
                beGin
                    if a=b then if c = d then e := f;
                    else i := 1;
                    else x := 2 ;
                eND
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def test_procedure_EasyTest_09(self):
        input = """
        Function Sum5DivisibleIn(A:array[0 .. 10] of integer ; N:Integer):Integer;
                Var S,i :Integer;
                Begin
                	S:=0;
                	For i:=0 to N do
                	If(A[i] mod 5=0) then
                	S := S+A[i];
                	return S;
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_procedure_EasyTest_10(self):
        input = """
        function factorial(x:integer):integer;
                begin
                if x = 0 then
                    return 1;
                else
                    return x*gt(x-1);
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

    def test_procedure_EasyTest_11(self):
        input = """
        procEdure main();
        var a:integer;
        begin
            a <> c and then b or else b <> c ;
        end
        """
        expect = "Error on line 5 col 33: else"
        self.assertTrue(TestParser.test(input,expect,275))

    def test_procedure_EasyTest_12(self):
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
        """
        expect = "Error on line 19 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_procedure_EasyTest_13(self):
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
        self.assertTrue(TestParser.test(input,expect,277))

    def test_procedure_String_Plus(self):
        input = """
        Var 
	    S1, S2, S3 : String;

        Procedure main();
        Begin
    	S1 := "Woaw!";
	    S2 := " Viet ";
        S3 := " is such a handsome man!";
    	Write(S1 + S2 + S3); { "Woaw! Viet is such a handsome man!" }
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))

    def test_procedure_arrayTest(self):
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
        self.assertTrue(TestParser.test(input,expect,279))

    def test_declaration_Array(self):
        input = """
        Var
	    i : Integer;
	        myIntArray : Array[1 .. 20] of Integer;
	        myBoolArray : Array[1 .. 20] of Boolean;
            myStringArray : Array[1 .. 20] of String;
	        myRealArray : Array[1 .. 20] of Real;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))

    def test_procedure_appendString(self):
        input = """
        var
        str1, str2, str3 : string;
        str4: string;
        len: integer;

        procedure main();
        begin
            str1 := "Hello ";
            str2 := "There!";

            (* copy str1 into str3 *)
            str3 := str1;
            writeln("appendstr( str3, str1) :  ", str3 );

            (* concatenates str1 and str2 *)
            appendstr( str1, str2);
            writeln( "appendstr( str1, str2) " , str1 );
            str4 := str1 + str2;
            writeln("Now str4 is: ", str4);

            (* total lenghth of str4 after concatenation  *)
            len := byte(str4[0]);
            writeln("Length of the final string str4: ", len); 
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))

    def test_procedure_InfinityLoop_01(self):
        input = """
        Procedure Main();
        Begin
            While 1 do
            Begin
                myIntArray[i] := 1;
                myBoolArray[i] := True;
            End
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_procedure_InfinityLoop_02(self):
        input = """
        Procedure Main();
        Begin
            While 1 do 2;
        """
        expect = "Error on line 4 col 24: ;"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_multiDeclaration(self):
        input = """
        var
            a, b, c: integer;
        procedure display();

        var
            a, b, c: integer;
        """
        expect = "Error on line 8 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_statementWithoutDeclaration(self):
        input = """
        writeln("Winthin the procedure display");
        writeln("Winthin the procedure display");
        writeln("Winthin the procedure display");
        """
        expect = "Error on line 2 col 8: writeln"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_procedure_main_01(self):
        input = """
        procedure main();
        begin
            a:= 10;
            (* check the boolean condition using if statement *)

            if( a < 20 ) then
              (* if condition is true then print the following *) 
                writeln("a is less than 20 " );
            writeln("value of a is : ", a);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_procedure_main_02(self):
        input = """
        procedure main();
        begin
            writeln("Please enter your first name: ");
            readln(firstname);

            writeln();
            writeln(message, " ", firstname);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def test_procedure_main_03(self):
        input = """
        Procedure main();
        Begin
        	For Counter := 1 to 7 do { it"s easy and fast! }
        		Writeln("for loop");
        	Readln();
        End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_procedure_main_04(self):
        input = """
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
        self.assertTrue(TestParser.test(input,expect,289))

    def test_procedure_main_05(self):
        input = """
        procedure main();
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
        self.assertTrue(TestParser.test(input,expect,290))

    def test_multiCompoundWithoutDeclare(self):
        input = """
        begin
        if (num1 > num2) then
            result := num1;

        else
            result := num2;
        max := result;
        end

        begin
            a := 100;
            b := 200;
           (* calling a function to get max value *)
            ret := max(a, b);

            writeln( "Max value is : ", ret );
        end
        """
        expect = "Error on line 2 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_HelloWorld(self):
        input = """
        proceDure Hello(a, b:integer);
                begin
                    writeln("Hello, world!");
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

    def test_statementOutOfCompound(self):
        input = """
        procedure main() ;
                beGin
                if a=b then if c = d then e := f;
                else i := 1;
                eND
                else x := 2;
        """
        expect = "Error on line 7 col 16: else"
        self.assertTrue(TestParser.test(input,expect,293))

    def test_LBRB(self):
        input = """
        procedure main((()) ;
                beGin
                if a=b then if c = d then e := f;
                else i := 1;
                else x := 2;
                end
        """
        expect = "Error on line 2 col 23: ("
        self.assertTrue(TestParser.test(input,expect,294))

    def test_checkArithmeticProgression(self):
        input = """
        Function checkArithmeticProgression(A:Mang20;  N:Integer; k:Integer):Boolean;
                Var flag :boolean;
                i :Integer;
                Begin
                    for i:=1 to N do
                    if(A[i] <> A[i-1] + k) then
                    flag:=false;     // Cham dut, ket qua: khong phai
                    return flag; {Ket qua kiem tra la mang cap so cong}
                End
        """
        expect = "Error on line 2 col 46: Mang20"
        self.assertTrue(TestParser.test(input,expect,295))

    def test_procedure_InsertToArray(self):
        input = """
        Procedure Insert(A:array[0 .. 10] of REAL;N: Integer; k, X:Integer);
                Var i :Integer;
                Begin
                    For i:=N downto k+ 1 do
                    A[i] := A[i-1];
                    A[k] := X;
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_procedure_Reverse(self):
        input = """
        Procedure Reverse(n: integer);
                Begin
                    Assign(f,fo);
                    Rewrite(f);
                    If n > 0 then
                    Begin
                    Write(f,n mod 10);
                    Daoso(n div 10);
                    End
                    Close(f);
                End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))

    def test_procedure_Withstatement(self):
        input = """
        function fun(c: real): sTRIng;
            BEGIN
                with c , d : integer ; 
                c : array [1 .. 2] of real ;
                do
                with a , b : integer ;
            END
        """
        expect = "Error on line 8 col 12: END"
        self.assertTrue(TestParser.test(input,expect,298))

    def test_procedure_main_06(self):
            input = """
            procedure main();
            begin
                a:= 5;

                if( a < 20 ) then
                    writeln("a is less than 20 " );
                writeln("value of a is : ", a);
            end
            """
            expect = "successful"
            self.assertTrue(TestParser.test(input,expect,299))

    def test_procedure_main_07(self):
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
            self.assertTrue(TestParser.test(input,expect,300))
