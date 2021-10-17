grammar MyGrammer;
s   : left=s right=s                     # InfixExpr
    | atom=LETTER                        # LetterExpr
    ;

line: s EOF                                 # LineExpr
;                                

LETTER: [a-zA-Z];
WS: [ \n\r\t]+ -> skip ;