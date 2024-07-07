# Importamos la librería Random que nos ayudará con la aleatoriedad de las contraseñas
import random

# Definimos las 3 variables donde almacenaremos los caracteres alfanuméricos y los símbolos
letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "123456789"
simbolos = "#@=<>{[]}?¿-;}][]}"

# Definimos Unión, donde combinaremos las variables anteriores
# Definimos Longitud, donde especificaremos el largo de las contraseñas
union = f'{letras}{numeros}{simbolos}'
longitud = 20

# Definimos Contraseña, donde la función random actuará sobre las variables Unión y Longitud
# Definimos Contraseña_final, donde se almacenará en una cadena vacía el resultado de Contraseña
contraseña = random.sample(union, longitud)
contraseña_final = "".join(contraseña)

# Imprimimos por pantalla la contraseña resultante junto a un mensaje descriptivo
print("-> Tu Contraseña generada es:", contraseña_final)