%{
#include <stdio.h>
#include "ice9.tab.h"

extern void yyerror();
int yynewlines=1;

%}

%%

if	return TK_IF;
"[]"	return TK_BOX;

\n			{ yynewlines++; }

.		{ yyerror("Illegal charactor"); }
%%


