/**
*   Student's Name    : Nguyen Le Quoc Viet
*
*   Student's ID      : 1614096
**/
grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

//***PARSER***
program
    : (funcdeclaration | vardeclaration | procdeclaration)+ EOF;

//Variable Declaration
vardeclaration
    : VAR vardeclarationlist+;

vardeclarationlist
    : parameter SEMI;
parameter
    : ID (COMMA ID)* COLON (arraytype | singletype);
singletype 
    : BOOLTYPE|REALTYPE|INTTYPE|STRINGTYPE;
arraytype
    : ARRAY LSB SUBOP? INTLIT DDOT SUBOP? INTLIT RSB OF singletype;

//Function Declaration
funcdeclaration
    :   FUNCTION ID LB (parameter (SEMI parameter)*)? RB COLON (singletype|arraytype) SEMI vardeclaration? compoundstatement;

//Procedure Declaration
procdeclaration
    :   PROCEDURE ID LB (parameter  (SEMI parameter)*)? RB SEMI vardeclaration? compoundstatement;

//***Statement***
statementpart
    :    assignstatement
        |ifstatement
        |whilestatement
        |forstatement
        |breakstatement
        |continuestatement
        |returnstatement
        |compoundstatement
        |withstatement
        |callstatement;
assignstatement
    :  ((ID|arrayindex) ASSIGN)+ expressions SEMI;
ifstatement
    :  IF expressions THEN statementpart (ELSE statementpart)?;
whilestatement
    :  WHILE expressions DO statementpart;
forstatement
    :  FOR ID ASSIGN expressions (TO|DOWNTO) expressions DO statementpart;
breakstatement
    :  BREAK SEMI;
continuestatement
    :  CONTINUE SEMI;
returnstatement
    :  RETURN expressions? SEMI;
compoundstatement
    :  BEGIN statementpart* END;
withstatement
    :  WITH vardeclarationlist+ DO statementpart;
callstatement
    :  funccall SEMI;
//Expression
expressions
    : expressions ANDOP THEN exp0
    | expressions OROP THEN exp0 
    | exp0;
exp0
    : exp1 EQUALOP exp1
    | exp1 NOTEQUALOP exp1
    | exp1 LESSOP exp1
    | exp1 LEOREQUOP exp1
    | exp1 GREATEROP exp1
    | exp1 GROREQUOP exp1
    | exp1;
exp1
    : exp1 ADDOP exp2
    | exp1 SUBOP exp2
    | exp1 OROP exp2
    | exp2;
exp2
    : exp2 SDIVOP exp3
    | exp2 MULOP exp3
    | exp2 DIVOP exp3
    | exp2 MODOP exp3
    | exp2 ANDOP exp3
    | exp3;
exp3
    : (SUBOP|NOTOP) exp3
    | exp4;
//index expression
exp4
    : exp5 (LSB expressions RSB)*;
exp5
    : LB expressions RB | exp6;
exp6
    : (operand|funccall);
operand
    : INTLIT | REALLIT | STRINGLIT | BOOLLIT|ID;
funccall
    : ID LB (expressions (COMMA expressions)*)? RB;
arrayindex
    : expressions LSB expressions RSB;

//***Token Set***
//Keywords
VAR 
    : V A R;
BREAK
    : B R E A K;
CONTINUE
    : C O N T I N U E;
FOR
    : F O R;
WITH
    : W I T H;
TO			
    : T O;
DOWNTO		
    : D O W N T O;
DO			
    : D O;
IF			
    : I F;
THEN		
    : T H E N;
ELSE
    : E L S E;
RETURN		
    : R E T U R N;
WHILE		
    : W H I L E;
BEGIN		
    : B E G I N;
END			
    : E N D;
FUNCTION	
    : F U N C T I O N;
PROCEDURE	
    : P R O C E D U R E;
fragment TRUE
    : T R U E;
fragment FALSE
    : F A L S E;
ARRAY		
    : A R R A Y;    
OF			
    : O F;
REALTYPE	
    : R E A L;
BOOLTYPE	
    : B O O L E A N;
INTTYPE		
    : I N T E G E R;
STRINGTYPE	
    : S T R I N G;

//Operator
ASSIGN
    : ':=';
ADDOP		
    : '+';
SUBOP		
    : '-';
MULOP		
    : '*';
SDIVOP      
    : '/';
DIVOP		
    : D I V;
MODOP		
    : M O D;
NOTOP		
    : N O T;
OROP 		
    : O R;
ANDOP		
    : A N D;
NOTEQUALOP  
    : '<>';
EQUALOP		
    : '=';
LESSOP		
    : '<';
GREATEROP	
    : '>';
LEOREQUOP	
    : '<=';
GROREQUOP	
    : '>=';

//***Separators***
LB		
    : '(';
RB		
    : ')';
LP		
    : '{';
RP		
    : '}';
LSB		
    : '[';
RSB		
    : ']';
COLON	
    : ':';
SEMI	
    : ';';
DDOT	
    : '..';
COMMA	
    : ',';

WS 
    : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

//Identifiers
ID   
    : [a-zA-Z_][a-zA-Z0-9_]* ;

//***Literals***
INTLIT
    : [0-9]+;

REALLIT
    : ([0-9]+ (('.'[0-9]*(EXP)?)?|EXP) | [0-9]+'.' | '.'[0-9]*(EXP)?);
    fragment EXP : E ('-')?[0-9]+;

STRINGLIT
    : '"' ('\\' [bfrnt"'\\] | ~[\b\n\t\f\r'\\"])* '"' {self.text = self.text[1:-1]};

BOOLLIT
    : TRUE|FALSE;

//Comment
TRADITIONALblockCOMMENT
    : '(*' .*? '*)' -> skip;
BLOCKCOMMENT
    : '{' .*? '}' -> skip;
LINECOMMENT	
    :  '//' ~[\r\n]* -> skip;
//Fragments are used to explicit upper-case and lower-case 
fragment A 
    : ('a'|'A');
fragment B 
    : ('b'|'B');
fragment C 
    : ('c'|'C');
fragment D 
    : ('d'|'D');
fragment E 
    : ('e'|'E');
fragment F 
    : ('f'|'F');
fragment G 
    : ('g'|'G');
fragment H 
    : ('h'|'H');
fragment I 
    : ('i'|'I');
fragment J 
    : ('j'|'J');
fragment K 
    : ('k'|'K');
fragment L 
    : ('l'|'L');
fragment M 
    : ('m'|'M');
fragment N 
    : ('n'|'N');
fragment O 
    : ('o'|'O');
fragment P 
    : ('p'|'P');
fragment Q 
    : ('q'|'Q');
fragment R 
    : ('r'|'R');
fragment S 
    : ('s'|'S');
fragment T 
    : ('t'|'T');
fragment U 
    : ('u'|'U');
fragment V 
    : ('v'|'V');
fragment W 
    : ('w'|'W');
fragment X 
    : ('x'|'X');
fragment Y 
    : ('y'|'Y');
fragment Z 
    : ('z'|'Z');
UNCLOSE_STRING
    : '"' ( '\\' [btnfr"'\\] | ~[\b\t\f\r\n\\'"] )*{
        self.text = self.text[1:]
        raise UncloseString(self.text)
    };
ILLEGAL_ESCAPE
    : '"' .*? ESCAPE .*? {
        self.text = self.text[1:]
        raise IllegalEscape(self.text)
    };
fragment ESCAPE: [\r\n\b\f\t'"\\];
ERROR_CHAR
    : .{
        raise ErrorToken(self.text)
    };
