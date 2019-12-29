grammar Scratch;

json
    : object
    | array
    ;
object
    : '{' pair (',' pair)* '}'  # AnObject
    | '{' '}'   # EmptyObject
    ;
pair
    : STRING ':' value  # APair
    ;
array
    : '[' value (',' value)* ']'  # ArrayOfValues
    | '[' ']'   # EmptyArray
    ;
value
    : STRING  # Stringjson
    | NUMBER  # Atom
    | object  # ObjectValue  // recursion
    | array  # ArrayValue // recursion
    | 'true'  # Atom  // keywords
    | 'false'  # Atom
    | 'null'  # Atom
    ;
STRING : '"' (ESC | ~["\\])* '"' ;

fragment ESC : '\\' (["\\/bfnrt] | UNICODE) ;
fragment UNICODE : 'u' HEX HEX HEX HEX ;
fragment HEX : [0-9a-fA-F] ;

NUMBER
    : '-'? INT '.' INT EXP? // 1.35, 1.35E-9, 0.3, -4.5
    | '-'? INT EXP // 1e10 -3e4
    | '-'? INT // -3, 45
    ;

fragment INT : '0' | [0-9] [0-9]* ; // no leading zeros
fragment EXP : [Ee] [+\-]? INT ; // \- since - means "range" inside [...]

WS : [ \t\n\r]+ -> skip ;
