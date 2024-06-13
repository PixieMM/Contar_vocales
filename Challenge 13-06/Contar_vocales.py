#Definir funcion para contar vocales
def contar_vocales(cadena):
    #Definir vocales
    vocales = 'aeiouAEIOU'
    #Iniciar contador de vocales
    contador = 0

    #Recorrer cada letra de la cadena
    for letra in cadena:
        # Condicional: si letra es vocal, aumentar contador
        if letra in vocales:
            contador += 1

    #Retornar numero de vocales
    return contador

#Pedir al usuario que ingrese una palabra o frase
cadena_usuario = input("Ingresar cadena de texto: ")

#Llamar a funcion contar vocales y guardar resultado
numero_vocales = contar_vocales(cadena_usuario)

#Imprimir resultado
print(f"El numero de vocales en la cadena es: {numero_vocales}")
