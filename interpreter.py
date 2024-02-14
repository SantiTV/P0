def revisar_sintaxis(codigo):
    
    ##Iniciamos el estado como False
    sintaxis = False
    


    ## lista constantes
    comandos = {"defvar", "defun", "if", "loop","repeat","move", "skip", "turn", "face",
                 "put", "pick", "move-dir", "run-dirs", "move-face","null"} 
    
    caracteres = {" ","(",")","\n","\t"}

    direcciones = {"left", "right", "back", "north", "south","west", "front","east"}
    
    condiciones = {"facing?", "blocked?", "can-put?", "can-pick", "can-move?", "isZero","not"}

    constantes = {"Dim", "myXpos", "myChips", "myYpos", "myBalloons", "balloonsHere", "ChipsHere", "Spaces"}
    
    
    
    funciones= []
    parametros = []
    
    parentesis = 0
    
    for expReg in codigo:
    
        ##Revisar parentesis 
        if expReg == '(':
            parentesis += 1
            
        elif  expReg == ')':
            parentesis -= 1

        ##Verificar funciones
            
        defun_indices = [ i for i, expReg in enumerate(codigo) if expReg == 'defun']

        #if expReg == 'defun':
         #   if codigo.index(expReg) + 1 < len (codigo):
                #nombre = codigo[codigo.index(expReg) + 1] ##Nombre de la funcion
                #parametro = expReg[2:1] #Parametros de la funcion
                #funciones.append(nombre) ##Guarda el niombre en una lista

    for index in defun_indices:
        nombre = codigo[index +1] 
        if codigo[index+3] != ")" :
            parametros.append(codigo[index + 3])
            parametros.append(codigo[index+4])
        
        
        funciones.append(nombre)      

    
    
    ##Revisar parentesis y asegurar que si hay (, existe un )
    if parentesis != 0: 
        sintaxis =  False          
    
    
    print(funciones)
    print(parametros)
    

def  main():
    with open("archivo.txt", 'r') as archivo:
        codigo = archivo.read()

        ## poner en miniuscula el codigo no es case sensitive
        codigo = codigo.lower() 

        ## Guarda las palabras en una lista
        espacios =  codigo.replace('(', ' ( ').replace(')',' ) ').replace("\n","").replace("\t","").split()
        
        ## Llama la funcion revisar_sintaxis
        sintaxis = revisar_sintaxis(espacios)

 
    
    
    
main()