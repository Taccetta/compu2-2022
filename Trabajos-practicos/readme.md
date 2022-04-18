 #**Trabajos de clase:**

----


***1. Argumentos (ej 1 y 2) - [args]:***
   - tp1_args1.py
   - tp1_args2.py

***2. Argumentos - [Popen]:***
   - tp2_popen.py

 ***3. Procesos - [fork]:***
   - tp3_fork.py

***4. Procesos - [fork_fd]:***
   - tp4_fork_fd.py

 ***5. Inversor de caracteres - [pipe]:***
   - tp5_pipe.py

----

**Enunciados:**

##### Ejercicio 1 - Getopt

Crear una calculadora, donde se pase como argumentos luego de la opción -o el operador que se va a ejecutar (+,-,*,/), luego de -n el primer número de la operación, y de -m el segundo número.

Ejemplo:

python3 calc.py -o + -n 5 -m 6

5 + 6 = 11

Considerar que el usuario puede ingresar los argumentos en cualquier orden. El programa deberá verificar que los argumentos sean válidos (no repetidos, números enteros, y operaciones válidas.

----
##### Ejercicio 2 - Argparse

Escribir un programa que reciba dos nombres de archivos por línea de órdenes utilizando los parámetros “-i” y “-o” procesados con argparse.

El programa debe verificar que el archivo pasado a “-i” exista en el disco. De ser así, lo abrirá en modo de solo lectura, leerá su contenido, y copiará dicho contenido en un archivo nuevo cuyo nombre será el pasado a “-o”. Si el archivo nuevo ya existe, deberá sobreescribirlo.

Ejemplo:
python3 copiar.py -i existente.txt -o nuevo.txt

----
##### Argumentos - [Popen]

Basándose en estos ejemplos, escribir un programa que reciba por argumentos de línea de comandos los siguientes modificadores:

    -c command

    -f output_file

    -l log_file

El código deberá crear los archivos pasados por los argumentos -f y -l en el caso de que no existan.

El código deberá ejecutar el comando haciendo uso de subprocess.Popen, y almacenar su salida en el archivo pasado en el parámetro -f. En el archivo pasado por el modificador -l deberá almacenar el mensaje “fechayhora: Comando XXXX ejecutado correctamente” o en su defecto el mensaje de error generado por el comando si este falla.

Por ejemplo:

python ejecutor.py -c “ip a” -o /tmp/salida -l /tmp/log

El archivo /tmp/salida deberá contener la salida del comando, y /tmp/log deberá contener:

fechayhora: Comando “ip a” ejecutado correctamente.

Otro ejemplo:

python ejecutor.py -c “ls /cualquiera” -o /tmp/salida -l /tmp/log

El archivo /tmp/salida no contendrá nada nuevo, ya que el comando fallará. El archivo /tmp/log contendrá:

fechayhora: ls: cannot access '/cualquiera': No such file or directory

Notas

    fechayhora debe ser la fecha y la hora del sistema en el momento de ejecutar el comando.
    Si los archivos ya tienen contenido, las nuevas ejecuciones agregarán mensajes al final de los mismos, sin limpiar salidas anteriores.
    Los mensajes de error almacenados en el log_file serán los mensajes que genera el comando en su intérprete de comandos, no deberá generarlos el programa escrito en python.
    Los argumentos de la línea de comandos deberán ser manejados por argparse o getopt.
    Puede tomar como base los ejemplos disponibles en el repo git de la cátedra.
----
##### Procesos - [fork]

Escribir un programa en Python que reciba los siguientes argumentos por línea de comandos:

-n numero>

-h

-v

El programa debe generar numero> procesos hijos, y cada proceso calculará la suma de todos los números enteros pares entre 0 y su número de PID.

El programa deberá mostrar por pantalla:

PID – PPID : suma_pares>

El proceso padre debe esperar a que todos sus hijos terminen.

La opción -h mostrará ayuda de uso, y la opción -v habilitará el modo verboso de la aplicación. El modo verboso debe mostrar, además de la suma, un mensaje al inicio y al final de la ejecución de cada proceso hijo, que indique su inicio y fin.

Ejemplos 1:

./sumapares.py -n 2

32803 – 4658: 269009202

32800 – 4658: 268943600

Ejemplos 2:

./sumapares.py -n 2 -v

Starting process 32800

Starting process 32803

Ending process 32803

32803 – 4658: 269009202

Ending process 32800

32800 – 4658: 268943600

----

##### Procesos - [fork_fd]

Escribir un programa en Python que reciba los siguientes argumentos por línea de comandos:

-n <N>
-r <R>
-h
-f <ruta_archivo>
-v

El programa deberá abrir (crear si no existe) un archivo de texto cuyo path ha sido pasado por argumento con -f.

El programa debe generar <N> procesos hijos. Cada proceso estará asociado a una letra del alfabeto (el primer proceso con la "A", el segundo con la "B", etc). Cada proceso almacenará en el archivo su letra <R> veces con un delay de un segundo entre escritura y escritura (realizar flush() luego de cada escritura).

El proceso padre debe esperar a que los hijos terminen, luego de lo cual deberá leer el contenido del archivo y mostrarlo por pantalla.

La opción -h mostrará ayuda. La opción -v activará el modo verboso, en el que se mostrará antes de escribir cada letra en el archivo: Proceso <PID> escribiendo letra 'X'.
Ejemplo 1:

./escritores.py -n 3 -r 4 -f /tmp/letras.txt

ABCACBABCBAC

Ejemplo 2:

./escritores.py -n 3 -r 5 -f /tmp/letras.txt -v

Proceso 401707 escribiendo letra 'A'
Proceso 401708 escribiendo letra 'B'
Proceso 401709 escribiendo letra 'C'
Proceso 401708 escribiendo letra 'B'
Proceso 401707 escribiendo letra 'A'
Proceso 401709 escribiendo letra 'C'
Proceso 401707 escribiendo letra 'A'
Proceso 401708 escribiendo letra 'B'
Proceso 401709 escribiendo letra 'C'
Proceso 401707 escribiendo letra 'A'
Proceso 401708 escribiendo letra 'B'
Proceso 401709 escribiendo letra 'C'
Proceso 401707 escribiendo letra 'A'
Proceso 401708 escribiendo letra 'B'
Proceso 401709 escribiendo letra 'C'
ABCBACABCABCABC

----

##### Inversor de caracteres - [pipe]

Escriba un programa que abra un archvo de texto pasado por argumento utilizando el modificador -f.

    El programa deberá generar tantos procesos hijos como líneas tenga el archivo de texto.
    El programa deberá enviarle, vía pipes (os.pipe()), cada línea del archivo a un hijo.
    Cada hijo deberá invertir el orden de las letras de la línea recibida, y se lo enviará al proceso padre nuevamente, también usando os.pipe().
    El proceso padre deberá esperar a que terminen todos los hijos, y mostrará por pantalla las líneas invertidas que recibió por pipe.

Ejemplo:

Contenido del archivo /tmp/texto.txt

Hola Mundo

que tal

este es un archivo

de ejemplo.

Ejecución:

python3 inversor.py -f /tmp/texto.txt

ovihcra nu se etse

.olpmeje ed

lat euq

odnuM aloH

----
