grammar MyGrammer;
expr: left=expr right=expr                     # InfixExpr
    | atom=LETTER                              # LetterExpr
    ;

line: expr EOF                                 # LineExpr
;                                

LETTER: [a-z];
WS: [ \n\r\t]+ -> skip ;