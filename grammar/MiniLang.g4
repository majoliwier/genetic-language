grammar MiniLang;

program
    : block EOF
    ;

block
    : '{' statement* '}'
    ;

statement
    : assignStatement
    | whileStatement
    | ifStatement
    | ioStatement
    | breakStatement
    | continueStatement
    ;

assignStatement
    : ID '=' expression ';'
    ;

whileStatement
    : WHILE '(' expression ')' block
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
    : expression ('*' | '/' | '%') expression
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
    : [0-9]+ '.' [0-9]* ([eE][+-]? [0-9]+)?
    | '.' [0-9]+ ([eE][+-]? [0-9]+)?
    | [0-9]+ ([eE][+-]? [0-9]+)
    ;

INT      : [0-9]+;

ID       : [a-zA-Z_][a-zA-Z_0-9]*;

WS       : [ \t\r\n]+ -> skip;
