grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::member {
def emit(self):
    tk = self.type
    if tk == UNCLOSE_STRING:       
        result = super.emit();
        raise UncloseString(result.text);
    elif tk == ILLEGAL_ESCAPE:
        result = super.emit();
        raise IllegalEscape(result.text);
    elif tk == ERROR_CHAR:
        result = super.emit();
        raise ErrorToken(result.text); 
    else:
        return super.emit();
}

options{
	language=Python3;
}

program  : mctype FLOATLIT EOF ;
//program : mctype COMMENTS_LINE EOF;

mctype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

// Type value
INTTYPE     : 'int';
BOOLTYPE    : 'boolean';
STRINGTYPE  : 'string';
FLOATTYPE   : 'float';
VOIDTYPE    : 'void';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// 3.2 Comments
COMMENTS_LINE   : '//' ~[\n\r\t\f]* -> skip;
COMMENTS_BLOCK  : '/*' .*? '*/' -> skip;

// 3.3 Token Set
// a. Identifiers
ID          : [_a-zA-Z][_a-zA-Z0-9]*;

// b. Keywords
BREAK       : 'break';
CONTINUE    : 'continue';
ELSE        : 'else';
FOR         : 'for';
IF          : 'if';
DO          : 'do';
WHILE       : 'while';
TRUE        : 'true';
FALSE       : 'false';

// c. Operators
ADD_OP              : '+';
SUB_OP              : '-';
MUL_OP              : '*';
DIV_OP              : '/';
NOT_OP              : '!';
MOD_OP              : '%';
OR_OP               : '|';
AND_OP              : '&&';
NOT_EQUAL_OP        : '!=';
EQUAL_OP            : '==';
LESS_OP             : '<';
GREATER_OP          : '>';
LESS_EQUAL_OP       : '<=';
GREATER_EQUAL_OP    : '>=';
ASSIGN_OP           : '=';

// 3.4 Separators
LSB     : '[';
RSB     : ']';
LP      : '{';
RP      : '}';
LB      : '(' ;
RB      : ')' ;
SEMI    : ';' ;
COMMA   : ',';

// 3.5 Literals
INTLIT: [0-9]+;
FLOATLIT: FRAC|EXPONENT;
FRAC: INTLIT?'.'INTLIT|INTLIT'.'INTLIT?;
EXPONENT: ;
BOOLLIT: TRUE|FALSE;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;