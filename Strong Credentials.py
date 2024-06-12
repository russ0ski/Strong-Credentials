
import random

letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "123456789"
simbolos = "#@=<>{[]}?¿-;}][]}"

union = f'{letras}{numeros}{simbolos}'
longitud = 20

contraseña = random.sample(union, longitud)
contraseña_final = "".join(contraseña)

print("-> Tu contraseña generada es:", contraseña_final)