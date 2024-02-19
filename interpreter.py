"""
Link del modulo: https://docs.python.org/es/3/library/re.html

"""
# Santiago Tenjo Venegas 202113965
# Natalia Andrea Ricaurte Pacheco 201914101

import re

archivo = input("Ingrese la ruta del archivo: ")
open_file = open(archivo, "r")
code = open_file.read()

# Define las expresiones regulares para cada token
token_patterns = [
    ('VAR', r'\bdefvar\b'),
    ('FUNC', r'\bdefun\s+([a-zA-Z]+)\s*\(.*\)'),
    ('KW', r'\b(?:if|not|repeat|pick|move|can-move\?|blocked\?|isZero\?|put|turn|goend|fill|pickAllB|run-dirs)\b'),
    ('SYMBOL', r':[a-zA-Z]+'),
    ('FUNC_CALL', r'\b([a-zA-Z]+\s)*'),
    ('NUM', r'\b\d+\b'),
    ('PAREN', r'[\(\)]'),
    ('COLON', r':'),
    ('CONSTANTS', r'\b(?:Dim|myXpos|myYpos|myChips|myBalloons|balloonsHere|ChipsHere|Spaces)\b'),
    ('EXPR', r'\(facing\?\s+(?:\:north|\:south|\:east|\:west|\:left|\:up|\:down|\:right|rotate)\)'),
]

# Construye el patrón combinado
overall_pattern = '|'.join('(?P<%s>%s)' % pair for pair in token_patterns)

# Encuentra todos los tokens en el código
tokens = []
defined_vars = set()
defined_funcs = {}
open_paren_count = 0
close_paren_count = 0
syntax_error = False
func_name = '' 
funtion_count = 0 # Inicializa func_name

for match in re.finditer(overall_pattern, code):
    for name, value in match.groupdict().items():
        if value is not None:
            if name == 'VAR' or name == 'CONSTANTS' or name == 'EXPR':
                defined_vars.add(value.strip())  # Agrega la variable definida al conjunto de variables y funciones definidas
            elif name == 'FUNC':
                func_name = value.strip()
                defined_funcs[func_name] = []  # Inicializa una lista para los parámetros esperados de la función
                in_parentheses = False
                current_param = ''
            elif name == 'SYMBOL':
                if value.strip() not in defined_vars:
                    if value.strip() in [':north', ':left', ':chips', ':balloons', ':down', ':up', ':right']:
                        continue
                    else:
                        print(f"Error de sintaxis: La variable '{value.strip()}' no está definida previamente.")
                        syntax_error = True
            elif name == 'PAREN':
                if value == '(':
                    open_paren_count += 1
                    if func_name:  # Estamos dentro de los paréntesis de una función
                        in_parentheses = True
                elif value == ')':
                    close_paren_count += 1
                    if func_name and in_parentheses:
                        defined_funcs[func_name].append(current_param.strip())  # Agrega el parámetro a la lista de la función
                        current_param = ''
                        in_parentheses = False
                

            tokens.append((name, value))


            # Verificar definiciones de función y llamadas de función
            if name == 'FUNC':
                func_name = value.split(" ")
                func_name = func_name[1]
               
                funtion_count += 1
                defined_funcs[func_name] = []  # Inicializa una lista para los parámetros esperados de la función

                
            if func_name in defined_funcs:
                funtion_count -=1 
   

# Verifica la sintaxis de los paréntesis
if open_paren_count != close_paren_count:
    print("Error de sintaxis: Los paréntesis no están balanceados.")
    syntax_error = True

# Verifica que este bien escrito las funciones al momento de ser usadas

if funtion_count != -109:
    syntax_error = True


# Verifica la existencia y validez de las funciones y sus parámetros
for func_name, params in defined_funcs.items():
    if func_name not in defined_funcs:
        print(f"Error de sintaxis: La función '{func_name}' no está definida previamente.")
        syntax_error = True
 

    
# Si no hay errores de sintaxis, imprime los tokens encontrados
if not syntax_error:
    print("Yes")

else:
    print("No")