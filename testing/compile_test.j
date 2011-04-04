.class public compile_test
.super java/lang/Object
.field public static y [[Ljava/lang/String;
.field public static x [I
.field public static z Ljava/lang/String;
.field public static w I
.field public static v I

.method public ()V 
    aload_0 
    invokespecial java/lang/Object/()V 
    return 
.end method 
  
; int read() 
.method public static read()I
    .limit locals 10 
    .limit stack 10 
    ldc 0 
    istore 1  ; this will hold our final integer 
Label1: 
    getstatic java/lang/System/in Ljava/io/InputStream; 
    invokevirtual java/io/InputStream/read()I 
    istore 2 
    iload 2 
    ldc 10   ; the newline delimiter 
    isub 
    ifeq Label2 
    iload 2 
    ldc 32   ; the space delimiter 
    isub 
    ifeq Label2 
    iload 2 
    ldc 48   ; we have our digit in ASCII, have to subtract it from 48 
    isub 
    ldc 10 
    iload 1 
    imul 
    iadd 
    istore 1 
    goto Label1 
Label2: 
    ;when we come here we have our integer computed in Local Variable 1 
    iload 1 
    ireturn 
.end method 

; void print(int) 
.method public static print(I)V 
    .limit locals 5 
    .limit stack 5 
    iload 0 
    getstatic java/lang/System/out Ljava/io/PrintStream; 
    swap 
    invokevirtual java/io/PrintStream/print(I)V 
    return 
.end method

; void print(string)
.method public static print(Ljava/lang/String;)V
    .limit locals 5 
    .limit stack 5 
    aload 0
    getstatic java/lang/System/out Ljava/io/PrintStream; 
    swap 
    invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V 
    return 
.end method
.method public static ret_true()I
.limit stack 100
ldc 0
istore 0
.limit locals 3
ldc 1
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 1
istore 0
iload 0
ireturn
.end method
 
 ; END BEGINS 
.method public static recurse(I)I
.limit stack 100
ldc 0
istore 1
.limit locals 5
iload 0
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
iload 0
ldc 5
isub
iflt label2
ldc 1
goto label3
label2:
ldc 0
label3:
ifeq label0
ldc 5
istore 1
iload 1
ireturn
goto label1
label0:
iload 0
ldc 1
iadd
invokestatic compile_test/recurse(I)I
istore 1
iload 1
ireturn
label1:
iload 1
ireturn
.end method
 
 ; END BEGINS 
.method public static multiarg(IILjava/lang/String;Ljava/lang/String;)I
.limit stack 100
ldc 0
istore 4
.limit locals 11
iload 0
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
iload 1
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
aload 2
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
aload 3
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
iload 0
istore 4
iload 4
ireturn
.end method
 
 ; END BEGINS 
 .method public static main([Ljava/lang/String;)V 
.limit stack 100
.limit locals 100
ldc 2
ldc 2
multianewarray [[Ljava/lang/String; 2
putstatic compile_test/y [[Ljava/lang/String;
ldc 2
multianewarray [I 1
putstatic compile_test/x [I
aconst_null
putstatic compile_test/z Ljava/lang/String;
ldc 0
putstatic compile_test/w I
ldc 0
putstatic compile_test/v I
getstatic compile_test/x [I
ldc 0
ldc 5
iastore
getstatic compile_test/x [I
ldc 1
ldc 6
iastore
ldc "TESTING Comparison Operators"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc ""
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING Equals:"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be false"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
ifne label4
ldc 1
goto label5
label4:
ldc 0
label5:
ifne label6
ldc 0
goto label7
label6:
ldc 1
label7:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 1
ldc 5
iastore
ldc " Should be true"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
ifne label8
ldc 1
goto label9
label8:
ldc 0
label9:
ifne label10
ldc 0
goto label11
label10:
ldc 1
label11:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING Not Equals"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be false"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
ifeq label12
ldc 1
goto label13
label12:
ldc 0
label13:
ifne label14
ldc 0
goto label15
label14:
ldc 1
label15:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be true"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 1
ldc 4
iastore
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
ifeq label16
ldc 1
goto label17
label16:
ldc 0
label17:
ifne label18
ldc 0
goto label19
label18:
ldc 1
label19:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING <"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be false"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
ifge label20
ldc 1
goto label21
label20:
ldc 0
label21:
ifne label22
ldc 0
goto label23
label22:
ldc 1
label23:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be false"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 1
ldc 5
iastore
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
ifge label24
ldc 1
goto label25
label24:
ldc 0
label25:
ifne label26
ldc 0
goto label27
label26:
ldc 1
label27:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be true"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 1
ldc 6
iastore
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
ifge label28
ldc 1
goto label29
label28:
ldc 0
label29:
ifne label30
ldc 0
goto label31
label30:
ldc 1
label31:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING <="
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be true"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
ifgt label32
ldc 1
goto label33
label32:
ldc 0
label33:
ifne label34
ldc 0
goto label35
label34:
ldc 1
label35:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be true"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 1
ldc 5
iastore
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
ifgt label36
ldc 1
goto label37
label36:
ldc 0
label37:
ifne label38
ldc 0
goto label39
label38:
ldc 1
label39:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be false"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 1
ldc 4
iastore
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
ifgt label40
ldc 1
goto label41
label40:
ldc 0
label41:
ifne label42
ldc 0
goto label43
label42:
ldc 1
label43:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING >="
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be true"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
iflt label44
ldc 1
goto label45
label44:
ldc 0
label45:
ifne label46
ldc 0
goto label47
label46:
ldc 1
label47:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be true"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 1
ldc 5
iastore
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
iflt label48
ldc 1
goto label49
label48:
ldc 0
label49:
ifne label50
ldc 0
goto label51
label50:
ldc 1
label51:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be false"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 1
ldc 6
iastore
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
iflt label52
ldc 1
goto label53
label52:
ldc 0
label53:
ifne label54
ldc 0
goto label55
label54:
ldc 1
label55:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING >"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be false"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
ifle label56
ldc 1
goto label57
label56:
ldc 0
label57:
ifne label58
ldc 0
goto label59
label58:
ldc 1
label59:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be false"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 1
ldc 5
iastore
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
ifle label60
ldc 1
goto label61
label60:
ldc 0
label61:
ifne label62
ldc 0
goto label63
label62:
ldc 1
label63:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be true"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 1
ldc 4
iastore
getstatic compile_test/x [I
ldc 0
iaload
getstatic compile_test/x [I
ldc 1
iaload
isub
ifle label64
ldc 1
goto label65
label64:
ldc 0
label65:
ifne label66
ldc 0
goto label67
label66:
ldc 1
label67:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING %"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be 1"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 5
ldc 2
ineg
irem
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be -1"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 5
ineg
ldc 2
ineg
irem
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING +"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be 3"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 1
ldc 2
iadd
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be -3"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 1
ineg
ldc 2
ineg
iadd
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING -"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be 3"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 6
ldc 3
isub
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be -6"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 3
ineg
ldc 3
isub
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING *"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be 6"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 3
ldc 2
imul
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be -6"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 3
ldc 2
ineg
imul
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING /"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be 1"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 5
ldc 4
idiv
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be 2"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 8
ldc 4
idiv
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be -1"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 5
ineg
ldc 4
idiv
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be -2"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 8
ineg
ldc 4
idiv
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING Boolean Or (+)"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be true"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 1
ifne label68
invokestatic compile_test/ret_true()I
goto label69
label68:
ldc 1
label69:
ifne label70
ldc 0
goto label71
label70:
ldc 1
label71:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be true and print 1"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 0
ifne label72
invokestatic compile_test/ret_true()I
goto label73
label72:
ldc 1
label73:
ifne label74
ldc 0
goto label75
label74:
ldc 1
label75:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be false"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 0
ifne label76
ldc 0
goto label77
label76:
ldc 1
label77:
ifne label78
ldc 0
goto label79
label78:
ldc 1
label79:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING Boolean And (+)"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be true"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 1
ifeq label80
ldc 1
goto label81
label80:
ldc 0
label81:
ifne label82
ldc 0
goto label83
label82:
ldc 1
label83:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be false"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 0
ifeq label84
ldc 1
goto label85
label84:
ldc 0
label85:
ifne label86
ldc 0
goto label87
label86:
ldc 1
label87:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be false"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 1
ifeq label88
ldc 0
goto label89
label88:
ldc 0
label89:
ifne label90
ldc 0
goto label91
label90:
ldc 1
label91:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should be false"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 0
ifeq label92
ldc 0
goto label93
label92:
ldc 0
label93:
ifne label94
ldc 0
goto label95
label94:
ldc 1
label95:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "Should print 1 and be true"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 1
ifeq label96
invokestatic compile_test/ret_true()I
goto label97
label96:
ldc 0
label97:
ifne label98
ldc 0
goto label99
label98:
ldc 1
label99:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "Should be false"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 0
ifeq label100
invokestatic compile_test/ret_true()I
goto label101
label100:
ldc 0
label101:
ifne label102
ldc 0
goto label103
label102:
ldc 1
label103:
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING If"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should print 1"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 0
iaload
ldc 5
isub
ifne label106
ldc 1
goto label107
label106:
ldc 0
label107:
ifeq label104
ldc 1
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
goto label105
label104:
label105:
; NULL
ldc " Should print 2"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 0
iaload
ldc 6
isub
ifne label110
ldc 1
goto label111
label110:
ldc 0
label111:
ifeq label108
ldc 0
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
goto label109
label108:
getstatic compile_test/x [I
ldc 0
iaload
ldc 7
isub
ifne label113
ldc 1
goto label114
label113:
ldc 0
label114:
ifeq label112
ldc 1
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
goto label109
label112:
ldc 2
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
label109:
ldc " Should print 3"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/x [I
ldc 0
iaload
ldc 6
isub
ifne label117
ldc 1
goto label118
label117:
ldc 0
label118:
ifeq label115
ldc 0
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
goto label116
label115:
getstatic compile_test/x [I
ldc 0
iaload
ldc 7
isub
ifne label120
ldc 1
goto label121
label120:
ldc 0
label121:
ifeq label119
ldc 1
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
goto label116
label119:
getstatic compile_test/x [I
ldc 0
iaload
ldc 5
isub
ifne label123
ldc 1
goto label124
label123:
ldc 0
label124:
ifeq label122
ldc 3
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
goto label116
label122:
ldc 2
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
label116:
ldc "TESTING do"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should print nothing:"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
label125:
ldc 0
ifeq label126
ldc 1
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
goto label125
label126:
ldc 1
putstatic compile_test/w I
ldc " Should print 1-5"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
label127:
getstatic compile_test/w I
ldc 6
isub
ifge label129
ldc 1
goto label130
label129:
ldc 0
label130:
ifeq label128
getstatic compile_test/w I
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/w I
ldc 1
iadd
putstatic compile_test/w I
goto label127
label128:
ldc 1
putstatic compile_test/w I
ldc " Should print 1-3 (testing break statement)"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
label131:
getstatic compile_test/w I
ldc 6
isub
ifge label133
ldc 1
goto label134
label133:
ldc 0
label134:
ifeq label132
getstatic compile_test/w I
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
getstatic compile_test/w I
ldc 3
isub
ifne label137
ldc 1
goto label138
label137:
ldc 0
label138:
ifeq label135
goto label132
goto label136
label135:
label136:
getstatic compile_test/w I
ldc 1
iadd
putstatic compile_test/w I
goto label131
label132:
ldc "TESTING fa"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should print 1, once:"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 0
istore 5
ldc 1
istore 5
label139:
iload 5
ldc 1
isub
ifgt label140
iload 5
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
iinc 5 1
goto label139
label140:
ldc " Should print 1-5:"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 0
istore 6
ldc 1
istore 6
label141:
iload 6
ldc 5
isub
ifgt label142
iload 6
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
iinc 6 1
goto label141
label142:
ldc " Should print 1-3 (testing break statement):"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 0
istore 7
ldc 1
istore 7
label143:
iload 7
ldc 5
isub
ifgt label144
iload 7
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
iload 7
ldc 3
isub
ifne label147
ldc 1
goto label148
label147:
ldc 0
label148:
ifeq label145
goto label144
goto label146
label145:
label146:
iinc 7 1
goto label143
label144:
ldc "TESTING nested breaks"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "Should print 1 then 2"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 0
istore 8
ldc 1
istore 8
label149:
iload 8
ldc 5
isub
ifgt label150
iload 8
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 0
istore 9
ldc 2
istore 9
label151:
iload 9
ldc 5
isub
ifgt label152
iload 9
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
goto label152
iinc 9 1
goto label151
label152:
goto label150
iinc 8 1
goto label149
label150:
ldc "TESTING recursive function calls"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "Should print 1 - 5, and then 5"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc 1
invokestatic compile_test/recurse(I)I
putstatic compile_test/w I
getstatic compile_test/w I
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "TESTING multiple argument function calls"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc " Should write 5, 6, foo, bar then 5"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
ldc "foo"
putstatic compile_test/z Ljava/lang/String;
ldc 5
ldc 6
ldc "foo"
ldc "bar"
invokestatic compile_test/multiarg(IILjava/lang/String;Ljava/lang/String;)I
putstatic compile_test/w I
getstatic compile_test/w I
invokestatic compile_test/print(I)V
ldc "\n"
invokestatic compile_test/print(Ljava/lang/String;)V
 
return
.end method
