Este proyecto es una colección de juegos clásicos implementados en Python. Está diseñado para ejecutarse desde la terminal y permite a los usuarios elegir entre varios juegos interactivos. A continuación, se describe la estructura del proyecto, los juegos disponibles y su funcionamiento:

# Estructura del Proyecto
El proyecto tiene la siguiente estructura de archivos:

- `app.py`: Archivo principal que actúa como punto de entrada al programa. Gestiona la interacción con el usuario, permite elegir un juego y coordina la ejecución de los mismos.
- `ahorcado.py`: Implementa el juego del ahorcado.
- `tateti.py`: Implementa el juego del tateti (tres en raya).
- `ruleta.py`: Implementa el juego de la ruleta.
- `ruleta_rusa.py`: Implementa el juego de la ruleta rusa.
- `.gitignore`: Archivo que especifica qué archivos o directorios deben ser ignorados por Git (como __pycache__ y entornos virtuales).

# Descripción de los juegos

1. Ahorcado (ahorcado.py):
El usuario debe adivinar una palabra secreta letra por letra.
Tiene 6 intentos para adivinar correctamente.
Cada letra correcta revela su posición en la palabra, mientras que las incorrectas reducen los intentos disponibles.
2. Tateti (tateti.py):
Es una versión del clásico juego de tres en raya.
El usuario juega contra la computadora en un tablero de 3x3.
El objetivo es alinear tres marcas consecutivas (en fila, columna o diagonal) antes que el oponente.
3. Ruleta (ruleta.py):
El usuario intenta adivinar un número aleatorio entre 0 y 36 generado por la ruleta.
Tiene 6 intentos para acertar el número.
Se proporcionan pistas indicando si el número secreto es mayor o menor que el número ingresado.
4. Ruleta Rusa (ruleta_rusa.py):
Dos jugadores (el usuario y un oponente) se turnan para disparar un revólver con una sola bala en el tambor.
El tambor tiene 5 posiciones vacías y 1 bala, que se coloca aleatoriamente.
El juego termina si un jugador dispara y la bala está en el tambor, o si ambos sobreviven tras 5 turnos.

# Funcionamiento del Programa Principal (app.py)
1. Bienvenida:
El programa solicita el nombre del usuario y lo saluda.
2. Selección de juego:
El usuario elige un juego de una lista numerada (1: tateti, 2: ahorcado, 3: ruleta, 4: ruleta rusa).
Si la entrada es inválida, se solicita nuevamente.
3. Ejecución del juego:
Según la elección del usuario, se llama a la función correspondiente al juego seleccionado.
Cada juego tiene su propia lógica y se ejecuta de forma independiente.
4. Repetición:
Al finalizar un juego, el programa pregunta si el usuario desea jugar otro.
Si el usuario responde afirmativamente, se reinicia el proceso de selección de juego.
Si responde negativamente, el programa se despide y termina.

# Aspectos técnicos
- **Modularidad**: cada juego está implementado en un archivo separado, lo que facilita la organización y el mantenimiento del código.
- **Interactividad**: el programa utiliza funciones como `input()` para interactuar con el usuario, lo que lo hace dinámico y fácil de usar.
- **Aleatoriedad**: los juegos como la ruleta, la ruleta rusa y el tateti utilizan el módulo `random` para generar resultados impredecibles, aumentando la rejugabilidad.
- **Control de errores**: Se manejan entradas inválidas mediante validaciones y mensajes claros para el usuario.

# Posibles mejoras
1. Ampliar la Lista de Palabras en Ahorcado:
     - Utilizar una lista de palabras aleatorias en lugar de una palabra fija.
2. Persistencia de Datos:
   - Implementar un sistema de puntuación que se guarde entre sesiones.
3. Interfaz gráfica:
   - Migrar el proyecto a una interfaz gráfica para mejorar la experiencia del usuario.

[Enlace a Trello](https://trello.com/b/BVjVCjS2/juegos-python).