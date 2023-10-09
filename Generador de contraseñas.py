from random import sample

def password_generator(longitud):

    # Definimos los caracteres y símbolos
    abc_minusculas = "abcdefghijklmnopqrstuvwxyz"

    # Hack: upper() transforma las letras de una cadena en mayúsculas
    abc_mayusculas = abc_minusculas.upper()

    numeros = "0123456789"
    simbolos = "{}[]()*;/,_-"

    # Definimos la secuencia
    secuencia = abc_minusculas + abc_mayusculas + numeros + simbolos

    # Llamamos la función sample() utilizando la secuencia y la longitud
    password_union = sample(secuencia, longitud)

    # Con join insertamos los elementos de una lista en una cadena
    password_result = "".join(password_union)

    # Retomamos la variable "password_result"
    return password_result

# Llamamos a la función "password_generator" y le pasamos el valor "12"

password = password_generator

#Imprimimos el resultado
print("Contraseña: ", password)