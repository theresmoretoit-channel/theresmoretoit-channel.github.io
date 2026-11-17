<!-- S01 -->
Cuatro coches llegan a un cruce
exactamente en el mismo momento.
Sin semáforos. Sin señales.
Solo la regla que siguen muchos países:
cede el paso al coche de tu derecha.

<!-- S02 -->
Cada conductor mira a la derecha
y ve un coche al que tiene que esperar.
Así que todos los conductores esperan.

<!-- S03 -->
Nadie se está saltando la regla.
Todos la cumplen a la perfección.
Y nadie se moverá jamás.

<!-- S04 -->
Los informáticos lo llaman interbloqueo, o deadlock.
Y no solo pasa en las carreteras.
Pasa dentro de las bases de datos,
los sistemas operativos y el software corriente.

<!-- S05 -->
Los ordenadores suelen detectar bien
un interbloqueo una vez que ha ocurrido.
Pero ¿podría un programa leer otro programa
y decirte, con total seguridad,
si alguna vez se quedará atascado?

<!-- S06 -->
En muchos programas, sí.
Pero un método que funcione
para cualquier programa posible
no puede existir.
Y no porque los ordenadores
aún no sean lo bastante rápidos.
Ningún ordenador más rápido lo cambiará nunca.

<!-- S07 -->
Así es como se atasca un programa.
Imagina una tienda online
con dos tareas ejecutándose a la vez.

<!-- S08 -->
Antes de que una tarea cambie algo,
le echa un cerrojo,
para que nadie más pueda tocarlo.
Como coger la única llave de una habitación.

<!-- S09 -->
La primera tarea bloquea la cuenta de un cliente
y luego intenta bloquear su pedido.
La segunda bloquea el pedido
y luego intenta bloquear la cuenta.

<!-- S10 -->
Una tiene la cuenta
y espera el pedido.
La otra tiene el pedido
y espera la cuenta.
Ninguna soltará lo que tiene.

<!-- S11 -->
Y lo curioso es que
este código puede ejecutarse un millón de veces
sin ningún problema.
Solo cuando las dos tareas se solapan
exactamente en el orden equivocado
se detiene todo.

<!-- S12 -->
El fallo estuvo ahí todo el tiempo.
La coincidencia en el tiempo solo lo sacó a la luz.

<!-- S12b -->
Por cierto, si te gustan vídeos
como este, plantéate suscribirte.

Ayuda mucho al canal.

<!-- S13 -->
Las bases de datos se topan con esto constantemente,
así que vigilan.
Dibujan un mapa de quién espera a quién.

<!-- S14 -->
La primera espera a la segunda.
La segunda espera a la primera.
Cuando las flechas se cierran en un bucle,
eso es un interbloqueo.
Nada de adivinar. El bucle está ahí mismo.

<!-- S15 -->
Entonces la base de datos hace algo brutal.
Elige una de las tareas
y tira su trabajo a la basura.

<!-- S16 -->
SQL Server, de Microsoft, incluso le dice a la perdedora
que ha sido elegida
como víctima del interbloqueo
y que debe volver a intentarlo.

<!-- S17 -->
La otra tarea sigue adelante,
y la víctima puede simplemente volver a intentarlo.

<!-- S18 -->
Fíjate en lo que eso arregla y lo que no.
El interbloqueo se ha deshecho.
Pero el código que lo causó sigue ahí,
esperando el próximo momento desafortunado.

<!-- S19 -->
Así que detectar un interbloqueo
que ya ha ocurrido
es la parte fácil.
La pregunta difícil es otra.

<!-- S20 -->
No: ¿está este programa atascado ahora mismo?
Sino: dale esta entrada.
¿Podría atascarse alguna vez?

<!-- S21 -->
Lo primero es una foto del presente.
Basta con mirarla.
Lo segundo es una predicción
sobre todos los futuros posibles.

<!-- S22 -->
Y los programas lo ponen muy difícil.
Toman decisiones. Repiten cosas.
Pueden hacer cálculos que tarden
un segundo, o mil años.

<!-- S23 -->
Un programa podría atascarse enseguida,
después de un millón de pasos,
con una única entrada poco común,
o nunca.

<!-- S24 -->
Podrías simplemente ejecutarlo y observar.
Pero si no se ha atascado al cabo de una hora,
¿qué te dice eso?

<!-- S25 -->
Nada.
Podría atascarse en el siguiente segundo,
o nunca.

<!-- S26 -->
En 1936, un joven matemático
llamado Alan Turing demostró
que hay preguntas sobre programas
que ningún programa puede responder.
La más famosa suena aún más sencilla.

<!-- S27 -->
Toma cualquier programa y su entrada.
¿Acabará deteniéndose?
¿O seguirá funcionando para siempre?

<!-- S28 -->
Hoy se conoce como el problema de la parada.
Y ningún programa puede resolverlo
correctamente en todos los casos.

<!-- S29 -->
La idea de la demostración
es sorprendentemente corta.
Supón que alguien te da
un comprobador de parada perfecto.

<!-- S30 -->
Ahora escribes un pequeño programa que lleva la contraria.
Le pregunta al comprobador por sí mismo
y luego hace justo lo contrario.

<!-- S31 -->
Si el comprobador dice que se detendrá,
se queda en un bucle infinito.
Si el comprobador dice que funcionará para siempre,
se detiene al instante.

<!-- S32 -->
Diga lo que diga el comprobador sobre él,
el comprobador se equivoca.
Así que un comprobador perfecto no puede existir.

<!-- S33 -->
¿Y qué tiene que ver esto con los interbloqueos?
Todo.

<!-- S34 -->
Imagina que alguien asegura haber construido
un predictor de interbloqueos perfecto.
Le das cualquier programa y su entrada,
y siempre te dice, sin equivocarse,
si ese programa se atascará alguna vez.

<!-- S35 -->
Usémoslo
para resolver el problema de la parada.

<!-- S36 -->
Toma el programa que quieras
y envuélvelo dentro de un programa nuevo.

<!-- S37 -->
Primero, el programa nuevo
simplemente ejecuta el antiguo,
paso a paso, en un solo hilo.
Sin cerrojos. Nada compartido.
Nada que pueda atascarse nunca.

<!-- S38 -->
Luego, si el programa antiguo termina alguna vez,
el nuevo lanza dos tareas.
Cada una coge un cerrojo,
espera a que la otra haya cogido el suyo
y luego va a por el de la otra.
Un interbloqueo, a propósito, siempre.

<!-- S39 -->
Si el programa antiguo no termina nunca,
el nuevo nunca llega tan lejos.
Ningún interbloqueo. Jamás.

<!-- S40 -->
Así que el programa nuevo se atasca
si, y solo si, el antiguo se detiene.

<!-- S41 -->
Ahora pregúntale al predictor
por el programa nuevo.
«Sí, habrá interbloqueo»
significa que el programa antiguo se detiene.
«No» significa que funciona para siempre.

<!-- S42 -->
Acabamos de resolver el problema de la parada.
Y eso es exactamente lo que no se puede hacer.

<!-- S43 -->
Así que el predictor perfecto de interbloqueos
tampoco puede existir.

<!-- S44 -->
El problema no son los cerrojos,
ni las bases de datos, ni los malos programadores.
Un programa puede esconder cualquier cálculo
antes de llegar a un interbloqueo.
Para predecir el interbloqueo,
tendrías que predecir si ese cálculo termina.

<!-- S45 -->
Pero espera.
Un ordenador real no es infinito.
Su memoria tiene un número limitado de estados.
Entonces, ¿no podrías comprobarlos todos?

<!-- S46 -->
Para una máquina con una cantidad fija
de memoria, en principio, sí.
En la práctica, cuéntalos.

<!-- S47 -->
La memoria de un portátil
de ocho gigabytes
puede organizarse de tantas maneras
que solo escribir ese número
ocupa unos veinte mil millones de dígitos.

<!-- S48 -->
El número de átomos
del universo observable
tiene unos ochenta.

<!-- S49 -->
Así que en una máquina real, comprobarlo todo
es posible en teoría
e inviable en la práctica.

<!-- S50 -->
Pero ese es otro muro.
El límite de Turing no va de tener demasiados estados.
Se aplica a programas
que siempre pueden pedir más memoria.
Para esos, no puede existir ningún predictor perfecto,
por grande que sea el ordenador.

<!-- S51 -->
¿Significa eso que los interbloqueos no tienen remedio?
No.
Significa que no hay un comprobador perfecto.
Así que los programadores escriben programas
que son más fáciles de comprobar.

<!-- S52 -->
El truco más sencillo es fijar un orden.
Toda tarea debe bloquear la cuenta
antes que el pedido.
Nunca al revés.

<!-- S53 -->
Si todas las tareas respetan de verdad ese orden,
el bucle no puede formarse,
y este tipo de interbloqueo no puede ocurrir.

<!-- S54 -->
Otros sistemas se rinden tras un tiempo de espera,
cogen todos sus cerrojos de una vez,
o dejan que la base de datos elija una víctima
y simplemente vuelven a intentarlo.

<!-- S55 -->
Y para diseños pequeños y descritos con cuidado,
hay herramientas que comprueban todos los estados posibles.
Unos ingenieros de Amazon usaron una
para encontrar un fallo que necesitaba treinta y cinco pasos,
exactamente en el orden correcto, para aparecer.

<!-- S56 -->
Estas herramientas funcionan
porque el problema se ha hecho más pequeño.
Comprueban un modelo del sistema,
no cualquier programa que pudiera llegar a existir.

<!-- S57 -->
Pero con código real,
un comprobador que acepte cualquier programa
tiene que renunciar a algo.
Puede avisar de interbloqueos
que no pueden ocurrir,
pasar por alto algunos que sí,
o a veces no dar ninguna respuesta.

<!-- S58 -->
Un comprobador que nunca dé falsas alarmas,
que nunca se deje ningún interbloqueo
y que siempre dé una respuesta,
para cualquier programa,
es exactamente lo que Turing descartó.

<!-- S59 -->
Volviendo al cruce:
los cuatro conductores no se quedan ahí para siempre.

<!-- S60 -->
Alguien hace un gesto con la mano.
Un conductor renuncia a su turno,
y en unos segundos todo se resuelve.

<!-- S61 -->
Eso es lo que hace también la base de datos.
No predice el interbloqueo.
Lo detecta
y obliga a alguien a ceder el paso.

<!-- S62 -->
Algunos problemas necesitan un ordenador más rápido.
Otros, una idea mejor.

<!-- S63 -->
Y algunos, como este,
no tienen ninguna solución perfecta.
Solo buenas reglas
y alguien dispuesto a hacer ese gesto.
