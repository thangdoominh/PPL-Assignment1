grammar MC;

//Parser part

prog: declar+;
declar: vardeclar | funcdeclar;
vardeclar: PRITYPE variable (COMMA variable)* SEMI;
variable: ID (LS INTLIT RS)?;
funcdeclar: types ID LB (para (COMMA para)*)? RB block;
para: PRITYPE ID (LS INTLIT RS)?;
types: PRITYPE|VOIDTYPE|array_type|array_pointer_type;
array_type: PRITYPE ID LS INTLIT RS;
array_pointer_type: input_apt|output_apt;
input_apt: PRITYPE ID LS RS;
output_apt: PRITYPE LS RS;
expr: LB expr RB
    | LS operands RS
    | <assoc = right>(SUB|LOGICNOT) expr
    | expr (MUL|DIV|MOD) expr
    | expr (ADD|SUB) expr
    | operands (LESS|LESSEQ|GREATER|GREATEREQ) operands
    | expr LOGICAND expr
    | expr LOGICOR expr
    | <assoc = right> expr AS expr
    | operands;

operands: ID|INTLIT| ele_array| function_call;
ele_array:  ID LS INTLIT RS;
function_call: ID LB (expr (COMMA expr)*)? RB;
staments: if_st|for_st|do_while|break_st|continue_st|return_st|expression|block;
if_st: If LB expr RB staments (Else staments)?;
for_st: For LB expr SEMI expr SEMI expr RB staments;
do_while: Do staments While expr SEMI;
break_st: Break SEMI;
continue_st: Continue SEMI;
return_st: Return expr? SEMI;
expression: expr SEMI;
block: LP (staments|vardeclar)* RP;
special_fuction: 'put' (Put LB expr RB)|(Ln LB RB)|'get' Get LB RB; 

// Lexer Part

// KeyWord
PRITYPE : INT|BOOLEAN|FLOAT|STRING;
VOIDTYPE: VOID;
If: IF;
Else: ELSE;
For: FOR;
Do: DO;
While: WHILE;
Break: BREAK;
Continue: CONTINUTE;
Return: RETURN;
Put: Int|Float|Bool|String;
Ln: 'Ln';
Get: 'Int'|'Float'|'Bool'|'String';


// Operator
ADD: '+';
MUL: '*';
LOGICNOT: '!';
LOGICOR: '||';
NOTEQ: '!=';
LESS: '<';
LESSEQ: '<=' ;
AS : '=';
SUB: '-';
DIV: '/';
MOD: '%';
LOGICAND: '&&';
EQ: '==';
GREATER: '>';
GREATEREQ: '>=';

// Separator
LS: '[';
RS: ']';
LP: '{';
RP: '}';
LB: '(' ;
RB: ')' ;
SEMI: ';' ;
COMMA: ',';

// Token
ID: [a-zA-Z_][a-zA-Z0-9_]*;

INTLIT: [0-9]+;

FLOATLIT: [0-9]+'.'(([0-9]+[Ee]'-'?)?[0-9]+)? | [0-9]*'.'([0-9]+[Ee]'-'?)?[0-9]+ 
            | [0-9]+[eE][-]?[0-9]+;

BOOLEANLIT : TRUE|FALSE ;

STRINGLIT: DOUQUOTES (STRINGKEY|.)* DOUQUOTES;

// Fragment
fragment BOOLEAN: 'boolean';
fragment BREAK: 'break';
fragment CONTINUTE: 'continute';
fragment ELSE: 'else';
fragment FOR: 'for';
fragment FLOAT: 'float';
fragment IF: 'if';
fragment INT: 'int';
fragment RETURN: 'return';
fragment VOID: 'void';
fragment DO: 'do';
fragment WHILE : 'while';
fragment STRING: 'string';
fragment TRUE: 'true';
fragment FALSE: 'false';
fragment STRINGKEY: '\\'[bfrnt"\\]|[ ];
fragment DOUQUOTES: '"';
fragment Float: 'Float'|'FloatLn';
fragment Int: 'Int'|'IntLn';
fragment Bool: 'Bool'|'BoolLn';
fragment String: 'String'|'StringLn';


// Skip part

LINECOMMENT : '//' .* -> skip;

BLOCKCOMMENT : '/*' .* '*/' -> skip;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
