/**
 * Student name: Duong Tan Sang
 * Student ID: 1512777
 */
grammar MC;

@lexer::header{
	package mc.parser;
}

@lexer::members{
@Override
public Token emit() {
    switch (getType()) {
    case UNCLOSE_STRING:
        Token result = super.emit();
        // you'll need to define this method
        throw new UncloseString(result.getText());

    case ILLEGAL_ESCAPE:
    	result = super.emit();
    	throw new IllegalEscape(result.getText());

    case ERROR_CHAR:
    	result = super.emit();
    	throw new ErrorToken(result.getText());

    default:
        return super.emit();
    }
}
}

@parser::header{
	package mc.parser;
}

options{
	language=Java;
}

//Paser
program: declaration+;
declaration:vardecla|funcdecla;
//variable declaration
//vardecla: PRITYPE idlist SEMI;
vardecla: (BOOLTYPE|FLOATTYPE|INTTYPE|STRINGTYPE) idlist SEMI;
idlist: id COMMA idlist|id;
id: idalone|idarray;
idalone: ID;
idarray: ID '[' INTLIT ']';
//function declaration
funcdecla: (BOOLTYPE|FLOATTYPE|INTTYPE|STRINGTYPE|VOIDTYPE|arraypointertype) ID LB paralist_decla? RB block;
arraypointertype: (BOOLTYPE|FLOATTYPE|INTTYPE|STRINGTYPE) '[' ']';
//parameter in declaration
paralist_decla: paradecla COMMA paralist_decla|paradecla;
paradecla: (BOOLTYPE|FLOATTYPE|INTTYPE|STRINGTYPE) (ID|ID LSB RSB);
//arraypointertypein: (BOOLTYPE|FLOATTYPE|INTTYPE|STRINGTYPE) ID '[' ']';
//function body declaration
block: LP vardecla* statementpart? RP ;
statementpart: statement+;
statement: ifstmt
          |forstmt
          |dowhilestmt
          |breakstmt
          |continuestmt
          |returnstmt
          |expressionstmt
          |block;

ifstmt: IF LB expression RB statement (ELSE statement)?;
dowhilestmt: DO statementpart WHILE expression SEMI;
forstmt: FOR LB expression SEMI expression SEMI expression RB statement;
breakstmt: BREAK SEMI; //chi xuat hien trong for, do while
continuestmt: CONTINUE SEMI; //chi xuat hien trong for, do while
returnstmt: RETURN expression? SEMI;


funccall: ID LB paralist_call? RB;
paralist_call: para_call COMMA paralist_call| para_call;
para_call: ID|BOOLLIT|INTLIT|STRINGLIT|FLOATLIT|expression;

expressionstmt: expression SEMI;

//expression: LB expression RB
//            |expression LSB expression RSB //non associative
//            |<assoc=right>(SUBOP|NOTOP) expression
//            |<assoc=left>  (DIVOP|MULOP|MODOP) expression
//            |<assoc=left> expression (ADDOP|SUBOP) expression
//            |expression ('<'|'<='|'>='|'>') expression //non associative
//            |expression (EQUALOP|NOTEQUALOP) expression //non associative
//            |<assoc=left> expression ANDOP expression
//            |<assoc=left> expression OROP expression
//            |<assoc=right> expression ASSIGNOP expression
//            |operand|funccall;

expression:exp1 ASSIGNOP expression|exp1;
exp1: exp1 OROP exp2|exp2;
exp2: exp2 ANDOP exp3|exp3;
exp3: exp4 (EQUALOP|NOTEQUALOP) exp4|exp4;
exp4: exp5 (LESSOP|LEOREQUOP|GREATEROP|GROREQUOP) exp5|exp5;
exp5: exp5 (ADDOP|SUBOP) exp6|exp6;
exp6: exp6 (DIVOP|MULOP|MODOP) exp7|exp7;
exp7: (SUBOP|NOTOP) exp7|exp8;
exp8: exp9 LSB expression RSB|exp9;
exp9: LB expression RB|exp10;
exp10: operand|funccall;

operand: INTLIT|FLOATLIT|STRINGLIT|BOOLLIT|ID;

BOOLLIT: TRUE|FALSE;
//Keywords
BOOLTYPE: 'boolean';
BREAK: 'break';
CONTINUE: 'continue';
ELSE: 'else';
FOR: 'for';
IF: 'if';
RETURN: 'return';
DO: 'do';
WHILE: 'while';
TRUE: 'true';
FALSE: 'false';
STRINGTYPE: 'string';
FLOATTYPE: 'float';
INTTYPE: 'int' ;
VOIDTYPE: 'void' ;

//fragment PRITYPE:BOOLTYPE|FLOATTYPE|INTTYPE|STRINGTYPE;

ID: [a-zA-Z_][a-zA-Z_0-9]* ;

//Literals
INTLIT: [0-9]+;
FLOATLIT: FRAC|EXP;
FRAC: INTLIT?'.'INTLIT|INTLIT'.'INTLIT?;
    EXP: (FRAC | INTLIT)[Ee][+-]?INTLIT;
//BOOLLIT: TRUE|FALSE;

ILLEGAL_ESCAPE: '"' .*? '\\' ~[bfrnt'"\\] .*? {
                              String s = getText();
                              int i = 0;
                              for(i=0; i<s.length(); i++) {
                                  char a = s.charAt(i+1);
                              Boolean b = ((a != 'b') && (a != 'f') && (a != 'r') && (a != 'n')&& (a != 't')&& (a != '\'')&& (a != '"')&& (a != '\\'));
                                  if (( s.charAt(i) == '\\') && (b == true)) {break;}
                              }
                              s = s.substring(1,i+2);
                              setText(s);
                          };
STRINGLIT: '"''\'[n]| ~[\n"]* '"'
    String s = getText();
    s = s.substring(1,s.length()-1);
    setText(s);
};
//Separators
LB: '(';
RB: ')';
LP: '{';
RP: '}';
LSB: '[';
RSB: ']';
SEMI: ';' ;
COMMA: ',';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

//Operator
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';
NOTOP: '!';
OROP: '||';
ANDOP: '&&';
NOTEQUALOP: '!=';
EQUALOP: '==';
LESSOP: '<';
GREATEROP: '>';
LEOREQUOP: '<=';
GROREQUOP: '>=';
ASSIGNOP: '=';

BLOCKCOM:  '/*' .*? '*/' -> skip;
LINECOM:  '//' ~[\r\n]* -> skip;

UNCLOSE_STRING: '"'~[\n"]*{
    String s = getText();
    s = s.substring(1,s.length());
    setText(s);
};
ERROR_CHAR: .;
