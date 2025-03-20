import random
import sys
 # Preguntas para el juego
questions = [ 
 "¿Qué función se usa para obtener la longitud de una cadena en Python?",
 "¿Cuál de las siguientes opciones es un número entero en Python?",
 "¿Cómo se solicita entrada del usuario en Python?",
 "¿Cuál de las siguientes expresiones es un comentario  válido en Python?",
 "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
 ]
 # Respuestas posibles para cada pregunta, en el mismo orden  que las preguntas
answers = [
 ("size()", "len()", "length()", "count()"),
 ("3.14", "'42'", "10", "True"),
 ("input()", "scan()", "read()", "ask()"),
 (
 "// Esto es un comentario",
 "/* Esto es un comentario */",
 "-- Esto es un comentario",
 "# Esto es un comentario",
 ),
 ("=", "==", "!=", "==="),
 ]
 # Índice de la respuesta correcta para cada pregunta, el el  mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
6. 
7. 
1. 
2. 
3. 

puntaje= 0

# El usuario deberá contestar 3 preguntas
for _ in range(3):
 
# Guardamos los elementos de manera aleatoria en una variable
    test = random.sample(list(zip(questions, answers, correct_answers_index)), 3)
    for q, a, c in test:
        que = q
        ans = a
        cor = c

 # Se muestra la pregunta y las respuestas posibles
    print(que)
    for i, ans in enumerate(ans):
        print(f"{i + 1}. {ans}")

 # El usuario tiene 2 intentos para responder  correctamente
    for intento in range(2):
            user_answer = int(input("Respuesta: "))-1

# Verificar si la respuesta está dentro del rango 
            if user_answer < 0 or user_answer >= 4:
                print ("Respuesta no válida")
                sys.exit(1)
 # Se verifica si la respuesta es correcta
            if user_answer == cor:
               print("¡Correcto!")
               puntaje += 1
               break
            else:
              print("Incorrecto. La respuesta correcta es:")
              print(ans, cor)
              puntaje -= 0.5
              break

 # Se imprime un blanco al final de la pregunta
    print()

print("Tu puntaje final es:", puntaje,)
