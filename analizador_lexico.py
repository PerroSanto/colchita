import ply.lex as lex
import ply.yacc as yacc

error = False

# Lista de tokens
tokens = ['CHARS', 'LPAREN', 'RPAREN', 'COMMA', 'EQUAL', 'FUN', 'VAL', 'IN', 'END', 'TURN', 'SEW', 'LET']

# Reglas de Expresiones regulares
def t_LPAREN(t):
    r'\('
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_COMMA(t):
    r','
    return t

def t_EQUAL(t):
    r'='
    return t

def t_FUN(t):
    r'fun'
    return t

def t_VAL(t):
    r'val'
    return t

def t_IN(t):
    r'in'
    return t

def t_END(t):
    r'end'
    return t

def t_TURN(t):
    r'turn'
    return t

def t_SEW(t):
    r'sew'
    return t

def t_LET(t):
    r'let'
    return t

def t_CHARS(t):
    r'[a-zA-Z][a-zA-Z]*'
    return t

# Ignorar salto de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios y tabs
t_ignore = ' \t'

# Ignorar comentarios
def t_COMMENT(t):
    r'\#.*'
    pass

# Manejo de errores
def t_error(t):
    global error
    print("Token error: Linea {:4}, Valor {:16}, Posicion {:4}".format(str(t.lineno), str(t.value[0]), str(t.lexpos)))
    t.lexer.skip(1)
    error = True

# Definición del analizador léxico
lexer = lex.lex()

# Función para analizar una cadena de entrada
def analizador_lexico_log(input_string):
    lexer.input(input_string)
    print("")
    print("******* ANALISIS LEXICO *******")
    print("")
    for token in lexer:
        print(token)
    print("")
    print("******************************")
    print("")

def analizador_lexico(input_string):
    global error
    error = False
    lexer.input(input_string)
    for token in lexer:
        pass
    if error:
        print("- No se puede compilar debido a errores lexicos")
        return False
    else:
        print("- Analisis Lexico exitoso")
        return True
    

