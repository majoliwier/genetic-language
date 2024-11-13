grammar MiniLang;

// rules
program:
    (statement | block)+ EOF
    ;

statement:
    ifStatement
    | loopStatement
    | assignStatement
    | ioStatement
    | functionCall SEMICOLON
    | SEMICOLON
    ;

ifStatement:
    IF LPAREN expression RPAREN statementOrBlock (ELSE statementOrBlock)?
    ;

loopStatement:
    WHILE LPAREN expression RPAREN statementOrBlock
    | FOR LPAREN (expressionList)? SEMICOLON (expression)? SEMICOLON (expressionList)? RPAREN statementOrBlock
    | DO statementOrBlock WHILE LPAREN expression RPAREN SEMICOLON
    ;

statementOrBlock:
    block
    | statement
    ;

block:
    LBRACE statement* RBRACE
    ;

assignStatement:
    ID ASSIGN expression SEMICOLON
    ;

ioStatement:
    INPUT LPAREN ID RPAREN SEMICOLON
    | OUTPUT LPAREN expression RPAREN SEMICOLON
    | PRINTLN LPAREN expression? RPAREN SEMICOLON
    ;

functionCall:
    ID LPAREN expressionList? RPAREN
    ;

expressionList:
    expression (COMMA expression)*
    ;

expression:
    assignmentExpression
    ;

assignmentExpression:
    ID ASSIGN assignmentExpression
    | logicalOrExpression
    ;

logicalOrExpression:
    logicalOrExpression OR logicalAndExpression
    | logicalAndExpression
    ;

logicalAndExpression:
    logicalAndExpression AND equalityExpression
    | equalityExpression
    ;

equalityExpression:
    equalityExpression (EQUALS | NOT_EQUALS) relationalExpression
    | relationalExpression
    ;

relationalExpression:
    relationalExpression (LESS_THAN | GREATER_THAN | LESS_THAN_EQ | GREATER_THAN_EQ) additiveExpression
    | additiveExpression
    ;

additiveExpression:
    additiveExpression (PLUS | MINUS) multiplicativeExpression
    | multiplicativeExpression
    ;

multiplicativeExpression:
    multiplicativeExpression (MULTIPLY | DIVIDE | MODULO) unaryExpression
    | unaryExpression
    ;

unaryExpression:
    MINUS unaryExpression
    | NOT unaryExpression
    | primaryExpression
    ;

primaryExpression:
    LPAREN expression RPAREN
    | functionCall
    | ID
    | NUMBER
    | STRING
    ;

// tokens

IF              : 'if' ;
ELSE            : 'else' ;
WHILE           : 'while' ;
FOR             : 'for' ;
DO              : 'do' ;
INPUT           : 'input' ;
OUTPUT          : 'output' ;
PRINTLN         : 'println' ;

ASSIGN          : '=' ;
PLUS            : '+' ;
MINUS           : '-' ;
MULTIPLY        : '*' ;
DIVIDE          : '/' ;
MODULO          : '%' ;

EQUALS          : '==' ;
NOT_EQUALS      : '!=' ;
LESS_THAN       : '<' ;
GREATER_THAN    : '>' ;
LESS_THAN_EQ    : '<=' ;
GREATER_THAN_EQ : '>=' ;

AND             : '&&' ;
OR              : '||' ;
NOT             : '!' ;

LPAREN          : '(' ;
RPAREN          : ')' ;
LBRACE          : '{' ;
RBRACE          : '}' ;
SEMICOLON       : ';' ;
COMMA           : ',' ;

NUMBER          : [0-9]+ ('.' [0-9]+)? ;
STRING          : ('"' (~["\\] | '\\' .)* '"')
                | '\'' (~['\\] | '\\' .)* '\''
                ;

ID              : [a-zA-Z_][a-zA-Z_0-9]* ;

LINE_COMMENT    : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT   : '/*' .*? '*/' -> skip ;
WS              : [ \t\r\n]+ -> skip ;
