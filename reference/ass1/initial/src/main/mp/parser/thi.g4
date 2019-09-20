//parser
program:(var_decl|func_decl|proc_decl)+ EOF;
var_decl: VAR var_decl_list+;
var_decl_list: idlist COLON vartype SEMI;
idlist: ID (COMMA ID)*;

func_decl: FUNCTION ID LB parameter_list RB COLON vartype SEMI var_decl? compound_stm;
proc_decl: PROCEDURE ID LB parameter_list RB SEMI var_decl? compound_stm;

parameter_list: (parameter_decl ( SEMI parameter_decl)*)?;
parameter_decl: idlist COLON vartype;
compound_stm : BEGIN statement* END;
statement: ((assign_stm | break_stm | continue_stm | return_stm | call_stm | while_stm) SEMI)|(if_stm | for_stm | with_stm | compound_stm);
//Statement
assign_stm: (assignID ASSIGN)+ exp;
assignID: ID | ID LS exp RS | ID LB exp? RB LS exp RS;
if_stm: IF exp THEN statement (ELSE statement)?;
while_stm: WHILE exp DO statement;
for_stm: FOR ID ASSIGN exp (TO|DOWNTO) exp DO statement;
break_stm: BREAK;
continue_stm: CONTINUE;
return_stm: RETURN exp?;
with_stm: WITH var_decl_list+ DO statement;
call_stm: ID LB (exp (COMMA exp)*)? RB;
//Expression
exp: exp (AND THEN | OR ELSE) exp1|exp1;
exp1: exp2 ((EQUAL | NOT_EQUAL | LESSTHAN | LESS_EQUAL | MORETHAN | MORE_EQUAL) exp2)?;
exp2: exp2 (ADD | SUB | OR) exp3|exp3;
exp3: exp3 (MUL | DIV | INT_DIV | MOD |AND) exp4|exp4;
exp4: (SUB | NOT) exp4|exp5;
exp5: exp6 LS exp RS|exp6;
exp6: LB exp RB | exp7;
exp7: operand|call_stm;
operand: INTLIT|STRINGLIT|BOOLEANLIT|FLOATLIT|ID;

vartype: BOOLEAN | INTEGER | REAL | STRING | arrayType;

arrayType: ARRAY LS INTLIT DOUBLE_DOT INTLIT RS OF (BOOLEAN | INTEGER | REAL | STRING);