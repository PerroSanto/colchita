import ply.yacc as yacc
from analizador_lexico import tokens


# Este es el BNF de colchita
# <exp> ::= <name> | <name> (<actuals>) | turn (<exp>) | sew (<exp>,<exp>) | let <decls> in <exp> end 
# <actuals> ::= <exp> | <exp> , <actuals>
# <decls> ::= <decl> | <decl> <decls>
# <decl> ::= fun <name> (<formals>) = <exp> | val <name> = <exp>
# <formals> ::= <name> | <name> , <formals>
# <name> ::= chars | <name> chars


# Resultado del analisis
resultado_gramatica = []

# Reglas de precedencia
precedence = (
    ('left', 'LPAREN', 'RPAREN'),
    ('left', 'LET', 'IN', 'END'),
    ('left', 'FUN', 'EQUAL'),
    ('left', 'VAL', 'EQUAL'),
)
    

# Reglas de produccion 
def p_exp(p):
    '''exp : name 
            | name LPAREN actuals RPAREN 
            | TURN LPAREN exp RPAREN 
            | SEW LPAREN exp COMMA exp RPAREN 
            | LET decls IN exp END''' 
    if len(p) == 2:
        p[0] = p[1]

    elif len(p) == 5 and p[1] == "name":
        p[0] = p[1] + p[3]

    elif len(p) == 5 and p[1] == "turn":
        p[0] = p[3]

    elif len(p) == 7:
        p[0] = p[3] + p[5]

    elif len(p) == 6:
        p[0] = p[2] + p[4]

        
def p_actuals(p):
    '''actuals : exp
                | exp COMMA actuals'''
    if len(p) == 2:
        p[0] = p[1]

    elif len(p) == 4:
        p[0] = p[1] + p[3]

        
def p_decls(p):
    '''decls : decl
            | decl decls'''
    if len(p) == 2:
        p[0] = p[1]

    elif len(p) == 3:
        p[0] = p[1] + p[2]


def p_decl(p):
    '''decl : FUN name LPAREN formals RPAREN EQUAL exp
            | VAL name EQUAL exp'''
    if len(p) == 8:
        p[0] = p[2] + p[4] + p[7]

    elif len(p) == 5:
        p[0] = p[2] + p[4] 


        
def p_formals(p):
    '''formals : name
                | name COMMA formals'''
    if len(p) == 2:
        p[0] = p[1]

    elif len(p) == 4:
        p[0] = p[1] + p[3]   


def p_name(p):
    '''name : CHARS
            | name CHARS'''
    if len(p) == 2:
        p[0] = p[1]

    elif len(p) == 3:
        p[0] = p[1] + p[2]

            
            
# Manejo de errores  
def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de: Tipo {}, Linea {}, Valor {}".format( str(t.type),str(t.lineno),str(t.value))
        #print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        #print(resultado)
    resultado_gramatica.append(resultado)
  
# instancia del analizador sintactico
parser = yacc.yacc()

# Funcion para probar el analizador sintactico
def analizador_sintactico_log(data):
    global resultado_gramatica
    resultado_gramatica.clear()
    print("")
    print("******* ANALISIS SINTACTICO *******")
    print("")
    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else: print("data vacia")
    print("resultado: ", resultado_gramatica)
    print("")
    print("******************************")
    print("")
    return resultado_gramatica

def analizador_sintactico(data):
    global resultado_gramatica
    resultado_gramatica.clear()
    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        #else: print("data vacia")
    for err in resultado_gramatica:
        if "Error" in err:
            print("- No se puede compilar debido a errores sintacticos")
            return False
        else:
            print("- Analisis Sintactico exitoso")
            return True

