"""
Link del modulo: https://docs.python.org/es/3/library/re.html

"""

import re

def revisar_sintaxis(codigo):

    ## lista constantes
    
    comandos = r'\((=|move|skip|turn|face|put|pick|move-dir|run-dirs|move-face|null)\s+(.*?)\)'
    funcion = r'\((defun)\s+(\w+)\s+([a-zA-Z]+|\d+)\)'
    estructuras = r'\((if|loop|repeat|defun)\s+(.*?)\)'
    llamar_funciones = r'\((.?)\s+(.?)\)'
    condiciones = r'\((facing\?|blocked\?|can-put\?|can-pick\?|can-move\?|isZero\?|not)\s+(.*?)\)'    
    variable = r'\((defvar)\s+(\w+)\s+(\w+)+|\d+\)'
    constantes = r'\((=|Dim|myXpos|myChips|myYpos|myBalloons|balloonsHere|ChipsHere|Spaces)\b'
   

    ##funcion =  r'\((defun)\s+(\w+)\s*\(([^)]*)\)\s*(.*?)\)'
    ##direcciones = {"left", "right", "back", "north", "south","west", "front","east"}

    listaTokens = []
    
    expRegular = re.findall(r'\((.*?)\)', codigo)

    
    for tipo in expRegular:
        
        
        if re.match(comandos,tipo):
            listaTokens.append(("comando", tipo))
            continue
        elif re.match(funcion,tipo):
            listaTokens.append(("funcion", tipo))
            continue
        elif re.match(estructuras,tipo):
            listaTokens.append(("estructura", tipo))
            continue
        elif re.match(llamar_funciones,tipo):
            listaTokens.append(("llamar_funcion", tipo))
            continue
        elif re.match(condiciones,tipo):
            listaTokens.append(("condicion", tipo))
            continue        
        elif re.match(variable,tipo):
            listaTokens.append(("variable", tipo))
            continue
        elif re.match(constantes,tipo):
            listaTokens.append(("constante", tipo))
            continue
        else:
            return "no"



    print(listaTokens)
    return "yes"
           
    
    
            
def  main():
    with open("archivo.txt", 'r') as archivo:
        codigo = archivo.read()

        ## Remover 
        codigo = re.sub(r'\s+', '', codigo)

        ## poner en miniuscula el codigo no es case sensitive
        codigo = codigo.lower() 

        ## Llama la funcion revisar_sintaxis
        sintaxis = revisar_sintaxis(codigo)
        print(sintaxis)
    
main()