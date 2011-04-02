def init_jasmin(cn, variables):
    string = ".class public %s\n" % cn  
    string += ".super java/lang/Object\n"
    for v in variables.values():
        string += v.jasmin()
    string += """
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
"""
    return string

def jasmin_types(t):
    if t == ():
        return "V"
    string = '['*len(t[1])
    if t[0] == 'int':
        string += 'I'
    elif t[0] == 'bool':
        string += 'I'
    elif t[0] == 'string':
        string+= "Ljava/lang/String;"
    return string

