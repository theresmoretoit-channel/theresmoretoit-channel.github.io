<!-- S01 -->
Cada pocos días, otro fallo grave
sale en las noticias.
Un fallo que permite saltarse el inicio de sesión.
Un fallo que filtra datos privados.
Un fallo que le entrega tu ordenador a un atacante.

<!-- S02 -->
A veces es Windows. A veces, Linux.
Un navegador, una base de datos, un servicio en la nube...
o una pequeña biblioteca
de la que dependen millones de programadores.

<!-- S03 -->
Y la reacción casi siempre es la misma.
¿Cómo es posible que los programadores no lo vieran?

<!-- S04 -->
Son profesionales.
Tienen revisiones de código, pruebas automáticas,
auditorías de seguridad, fuzzing...
y aun así los fallos no dejan de aparecer.

<!-- S05 -->
Entonces, ¿es siquiera posible
escribir software complejo sin fallos?

<!-- S06 -->
Empecemos con un número.
Imagina un programa con solo cien opciones,
y cada una puede estar activada o desactivada.

<!-- S07 -->
Cien decisiones simples de sí o no.
¿Cuántas combinaciones son?

<!-- S08 -->
Dos elevado a cien.
Más o menos un millón de billones de billones.

<!-- S09 -->
Ahora imagina que pudieras probar
mil millones de combinaciones por segundo.
Y que hubieras empezado en el Big Bang.

<!-- S10 -->
A día de hoy, habrías probado
más o menos una combinación de cada tres mil.

<!-- S11 -->
Y cien interruptores no son nada.
Un programa real tiene millones.
Así que «probarlo todo»
no es caro. Es imposible.

<!-- S12 -->
Y esos interruptores no son nada exótico.
Pensemos en una de las cosas más sencillas
que hace un programa.
Un usuario pide los datos de su cuenta por su número.
La buscamos en la base de datos.
Se la devolvemos.

<!-- S13 -->
¿Pero y si el usuario no existe?
¿Y si alguien manda texto en vez de un número?
¿O un número negativo? ¿O uno enorme?

<!-- S14 -->
¿Y si esa persona no tiene permiso para verla?
¿Y si alguien borra la cuenta
justo en el momento en que la estamos cargando?
¿Y si la misma petición llega dos veces?

<!-- S15 -->
Cada una de estas preguntas es sencilla.
El problema es cómo se combinan.
Cada una es otro interruptor.

<!-- S15b -->
Por cierto, si te gustan vídeos
como este, plantéate suscribirte.

Ayuda mucho al canal.

<!-- S16 -->
Y el ordenador no las va a resolver por nosotros.
Hace exactamente lo que le decimos.
No lo que queríamos decir.

<!-- S17 -->
Por eso inventamos los lenguajes de programación.
Nos permiten describir cosas complejas
sin pensar en cada detalle.

<!-- S18 -->
Pero algunos se encargan de menos cosas
de las que te gustaría.
Por ejemplo, C. Es rápido, es sencillo
y te da muchísimo control sobre la memoria.

<!-- S19 -->
Así que puedes escribir esto.
Reservamos espacio para dieciséis caracteres.
Y luego decimos: copia aquí la entrada.

<!-- S20 -->
¿Y si la entrada
tiene quinientos caracteres?
C no pregunta.
Simplemente sigue escribiendo más allá del final.

<!-- S21 -->
¿Y qué hay justo después de esos dieciséis caracteres?
A menudo, algo muy importante.

<!-- S22 -->
Cuando un programa llama a una función,
apunta adónde tiene que volver
cuando la función termine.
Una dirección de retorno.
En la disposición clásica, está
poco después del final de nuestro búfer.

<!-- S23 -->
Así que un atacante manda una entrada
con la longitud exacta.
Primero, sus propias instrucciones.
Y luego, justo al final, una nueva dirección de retorno...
que apunta a esas mismas instrucciones.

<!-- S24 -->
La función termina.
El procesador mira adónde tiene que volver...
y salta directamente al código del atacante.

<!-- S25 -->
Ahora está ejecutando el programa del atacante,
con todos los permisos del tuyo.
Eso es lo que significa «ejecutar código arbitrario».

<!-- S26 -->
Y el procesador no ha hecho nada mal.
Ha seguido las instrucciones.

<!-- S27 -->
En 1988, un error exactamente como este
permitió al gusano Morris propagarse
por internet en sus primeros años.
Y el mismo truco se ha usado
en ataques desde entonces.

<!-- S28 -->
Por eso los lenguajes más nuevos le pasan parte del trabajo
al compilador.
Rust, por ejemplo, se niega a compilar
muchos programas que podrían usar mal la memoria.

<!-- S29 -->
El programador dice:
¡pero si sé perfectamente lo que hago!
Y el compilador responde:
eso dicen todos.

<!-- S30 -->
Y hace bien en desconfiar.
Tanto Microsoft como el equipo de Chrome de Google
han informado
de que alrededor del setenta por ciento
de los fallos de seguridad que han estudiado
vienen de problemas de seguridad de memoria.

<!-- S31 -->
Pero un programa puede manejar la memoria de forma totalmente segura
y aun así estar completamente mal.

<!-- S32 -->
Imagina que un usuario inicia sesión.
Su contraseña se comprueba correctamente.
Nada se cuelga. No se corrompe la memoria.

<!-- S33 -->
Y entonces el programa le muestra
los datos de otra persona.
Porque la comprobación de permisos
estaba escrita un poquito mal.

<!-- S34 -->
Ningún lenguaje puede detectar eso por sí solo.
El lenguaje no sabe
qué se suponía que tenía que hacer el programa.
Eso solo lo sabemos nosotros.

<!-- S35 -->
Así que volvamos a las pruebas.
Una prueba te puede decir:
con esta entrada, he obtenido este resultado.

<!-- S36 -->
Lo que no te puede decir es:
el programa funciona bien con cualquier entrada.
Y ya hemos visto
por qué no podemos probarlas todas.

<!-- S37 -->
En 1970, el informático
Edsger Dijkstra lo resumió en una frase.
Las pruebas pueden demostrar que hay fallos,
pero nunca que no los hay.

<!-- S38 -->
Vale. Entonces, en vez de probar,
¿por qué no escribir un programa
que revise otros programas
y demuestre que son correctos?
Le das cualquier código y te dice
si ese código hace lo que debe.

<!-- S39 -->
Esa pregunta tuvo respuesta
antes incluso de que existiera el primer ordenador de verdad.
En 1936, Alan Turing demostró
que un programa así no puede existir.

<!-- S40 -->
No que nadie lo haya construido todavía.
Que no puede existir, y punto.

<!-- S41 -->
Demostró que ningún programa puede decidir,
para cualquier otro programa,
si llegará a terminar alguna vez.

<!-- S42 -->
Y en 1953, Henry Rice fue más allá.
Lo mismo vale para cualquier pregunta no trivial
sobre lo que un programa hace de verdad.

<!-- S43 -->
¿Es seguro? ¿Filtra datos?
¿Da la respuesta correcta?
No existe ningún método general
que lo resuelva para todos los programas.

<!-- S44 -->
Entonces, ¿es imposible el software sin fallos?
No exactamente.
Para un programa concreto,
a veces se puede demostrar que es correcto,
con un esfuerzo enorme.

<!-- S45 -->
En 2009, un equipo en Australia demostró
que un pequeño núcleo de sistema operativo,
llamado seL4,
hace exactamente lo que dice su especificación.

<!-- S46 -->
Tenía menos de diez mil líneas de código.
Construir el núcleo llevó
unos dos años-persona.
Demostrar que era correcto, unos veinte.
Un navegador web moderno
tiene decenas de millones de líneas.

<!-- S47 -->
Y hasta esa demostración tiene trampa.
Demuestra que el programa cumple su especificación.
Lo que no puede demostrar es que la especificación
sea lo que de verdad queríamos.

<!-- S48 -->
Y la especificación la escriben personas.
Así que la pelota vuelve a estar en nuestro tejado.

<!-- S49 -->
Y no se trata solo de nuestro propio código.
Hoy un programador se apoya en frameworks,
bibliotecas y cientos de dependencias.
Cada capa nos ahorra muchísimo trabajo.
Pero cada capa es algo
que tenemos que entender...
o al menos, de lo que tenemos que fiarnos.

<!-- S50 -->
O sea, que no hace falta escribir un fallo
para tenerlo en tu software.
Basta con instalarlo.

<!-- S51 -->
Y luego súmale la presión.
Nadie quiere un producto perfecto dentro de diez años.
Quieren uno que funcione el mes que viene.
Y una intrusión que nunca ocurrió
es muy difícil de lucir en una presentación.

<!-- S52 -->
Y ahora viene lo más raro.
Nuestras herramientas no dejan de mejorar.
Lenguajes más seguros, fuzzing, recompensas por encontrar fallos...

<!-- S53 -->
Y aun así, el número de vulnerabilidades conocidas
no para de crecer.
Solo en 2024, unas cuarenta mil
recibieron un número oficial.

<!-- S54 -->
En parte, porque también escribimos
muchísimo más software que nunca.
Es como hacer más seguras todas las carreteras...
mientras construimos millones de veces más carreteras.

<!-- S55 -->
Entonces, ¿los programadores hacen mal su trabajo?
No.
Les hemos estado pidiendo algo
que ningún método general puede garantizar.

<!-- S56 -->
Así que quizá
«¿cómo escribimos software sin fallos?»
sea la pregunta equivocada.

<!-- S57 -->
La pregunta buena es:
¿cómo construimos sistemas que sigan siendo seguros
incluso cuando el software tiene fallos?

<!-- S58 -->
Y justo hacia ahí va la seguridad.
No dice: no te equivoques nunca.
Dice: da por hecho que ya te has equivocado.

<!-- S59 -->
¿Te acuerdas de la dirección de retorno?
Hoy el sistema la vigila.
Cambia al azar dónde se colocan las cosas en la memoria.
Y se niega a ejecutar instrucciones
escondidas entre los datos.

<!-- S60 -->
El fallo de nuestro código en C sigue ahí.
Solo que es mucho más difícil convertirlo en un ataque.

<!-- S61 -->
Y la misma idea está por todas partes.
Entornos aislados, permisos limitados,
procesos separados, cifrado,
copias de seguridad, monitorización...
capa tras capa,
para que un fallo no se convierta en un desastre.

<!-- S62 -->
Y tiene una consecuencia muy práctica.
Si los fallos son inevitables,
corregirlos no es opcional.

<!-- S63 -->
El software que usas hoy
bien puede tener una vulnerabilidad
que nadie ha encontrado todavía.

<!-- S64 -->
Y cuando alguien la encuentre,
la actualización marca la diferencia entre
«se ha descubierto una vulnerabilidad»
y «nos han hackeado».

<!-- S65 -->
Y lo mismo pasa con los sistemas que construimos.
Las bibliotecas viejas y las plataformas sin soporte
no se vuelven más seguras porque las ignoremos.
Se convierten en deuda técnica.

<!-- S66 -->
Y por qué hay que pagar esa deuda
tarde o temprano
es justo el tema de mi vídeo
«Funciona. ¿Entonces por qué actualizarlo?».

<!-- S67 -->
Porque en el software,
«todavía funciona»
y «todavía es seguro»
son dos cosas muy distintas.
