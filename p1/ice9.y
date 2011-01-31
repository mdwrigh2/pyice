%{

#include <stdio.h>

extern int yynewlines;
extern char *yytext;

int yylex(void); /* function prototype */

void yyerror(char *s)
{
  if ( *yytext == '\0' )
    fprintf(stderr, "line %d: %s near end of file\n", 
	    yynewlines,s);
  else
    fprintf(stderr, "line %d: %s near %s\n",
	    yynewlines, s, yytext);
}

%}

%union {
  int intt;
  char *str;
}

%token TK_IF
%token TK_FI
%token TK_ELSE
%token TK_DO
%token TK_OD
%token TK_FA
%token TK_AF
%token TK_TO
%token TK_PROC
%token TK_END
%token TK_RETURN
%token TK_FORWARD
%token TK_VAR
%token TK_TYPE
%token TK_BREAK
%token TK_EXIT
%token TK_TRUE
%token TK_FALSE
%token TK_WRITE
%token TK_WRITES
%token TK_READ
%token TK_BOX
%token TK_ARROW
%token TK_LPAREN
%token TK_RPAREN
%token TK_LBRACK
%token TK_RBRACK
%token TK_COLON
%token TK_SEMI
%token TK_ASSIGN
%token TK_QUEST
%token TK_COMMA
%token TK_PLUS
%token TK_MINUS
%token TK_STAR
%token TK_SLASH
%token TK_MOD
%token TK_EQ
%token TK_NEQ
%token TK_GT
%token TK_LT
%token TK_GE
%token TK_LE

%token <str> TK_SLIT
%token <intt> TK_INT
%token <str> TK_ID

%start program

%%

program: /* empty rule */
	;

%%

int main() {
  int tok;
  while (1) {
    tok = yylex();
    if (tok == 0) break;
    switch (tok) {
    case TK_ID:
      printf("ID  : \t\"%s\"\n", yylval.str);
      break;
    case TK_INT:
      printf("ILIT:\t%d\n", yylval.intt);
      break;
    default:
      printf("TOK : \t%d\n", tok);
    }
  }
}
