grammar MiniLang;

program
    : statement* EOF
    ;

block
    : '{' loopIfStatement* '}'
    ;

statement
    : assignStatement
    | whileStatement
    | ifStatement
    | ioStatement
    ;

assignStatement
    : ID '=' expression ';'
    ;

whileStatement
    : WHILE '(' expression ')' block
    ;

loopIfStatement
    : assignStatement
    | whileStatement
    | ifStatement
    | ioStatement
    | breakStatement
    | continueStatement
    ;

ifStatement
    : IF '(' expression ')' block (ELSE block)?
    ;

ioStatement
    : INPUT '(' ID ')' ';'
    | OUTPUT '(' expression ')' ';'
    ;

breakStatement
    : BREAK ';'
    ;

continueStatement
    : CONTINUE ';'
    ;
expression
    : expression ('*' | '/') expression
    | expression ('+' | '-') expression
    | expression ('==' | '!=' | '<' | '>' | '<=' | '>=') expression
    | expression ('&&' | '||') expression
    | '(' expression ')'
    | ID
    | INT
    | FLOAT
    ;

WHILE    : 'while';
IF       : 'if';
ELSE     : 'else';
BREAK    : 'break';
CONTINUE : 'continue';
INPUT    : 'input';
OUTPUT   : 'output';

FLOAT
    : '-'? [0-9]+ '.' [0-9]*
    ;

INT      : '-'? [0-9]+;

ID       : [a-zA-Z_][a-zA-Z_0-9]*;

WS       : [ \t\r\n]+ -> skip;
