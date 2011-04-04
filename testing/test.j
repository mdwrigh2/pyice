.class public test
.super java/lang/Object

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
.method public static sum([I)I
.limit stack 100
.limit locals 6
ldc 0
istore 1
ldc 0
istore 2
ldc 0
istore 2
label0:
iload 2
ldc 9
isub
ifgt label1
iload 1
aload 0
iload 2
iaload
iadd
istore 1
iinc 2 1
goto label0
label1:
iload 1
ireturn
.end method
 
 ; END BEGINS 
.method public static f()I
.limit stack 100
.limit locals 5
bipush 10
multianewarray [I 1
astore 1
ldc 0
istore 2
ldc 0
istore 2
label2:
iload 2
ldc 9
isub
ifgt label3
aload 1
iload 2
ldc 17
iload 2
isub
iastore
iinc 2 1
goto label2
label3:
aload 1
invokestatic test/sum([I)I
istore 0
iload 0
ireturn
.end method
 
 ; END BEGINS 
 .method public static main([Ljava/lang/String;)V 
.limit stack 100
.limit locals 100
invokestatic test/f()I
invokestatic test/print(I)V
ldc "\n"
invokestatic test/print(Ljava/lang/String;)V
 
return
.end method

