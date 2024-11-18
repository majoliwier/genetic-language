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
    ;

whileStatement
    : WHILE '(' expression ')' block
    ;

ifStatement
    : IF '(' expression ')' block (ELSE block)?
    ;

assignStatement
    : ID '=' expression ';'
    ;

ioStatement
    : INPUT '(' ID ')' ';'
    | OUTPUT '(' expression ')' ';'
    ;

expression
    : expression ('*' | '/' | '%') expression
    | expression ('+' | '-') expression
    | expression ('==' | '!=' | '<' | '>' | '<=' | '>=') expression
    | expression ('&&' | '||') expression
    | '(' expression ')'
    | ID
    | NUMBER
    ;

// Tokens
WHILE : 'while';
IF : 'if';
ELSE : 'else';
INPUT : 'input';
OUTPUT : 'output';
ID : [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER : [0-9]+;
WS : [ \t\r\n]+ -> skip;