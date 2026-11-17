<!-- S01 -->
Esto es un ZX Spectrum cargando un programa.

<!-- S02 -->
Y este es el mismo programa,
en el mismo ordenador,
desde el mismo tipo de casete.

<!-- S03 -->
Termina en la mitad de tiempo.
En el hardware no ha cambiado nada.
Ni una cinta más rápida, ni una grabadora más rápida.

<!-- S04 -->
Lo único que cambió
fue la forma en que el ordenador escuchaba.

<!-- S05 -->
Entonces, ¿cómo aprendieron los ordenadores de 8 bits
a cargar juegos más rápido?
Y si era tan fácil,
¿por qué no lo hicieron desde el principio?

<!-- S06 -->
En un vídeo anterior
vimos cómo el Spectrum guarda los bits
como pulsos en la cinta.

<!-- S07 -->
Un par de pulsos cortos significa cero.
Un par el doble de largo significa uno.

<!-- S08 -->
Eso da unos mil cuatrocientos bits
por segundo.
Un juego que llena los 48K de memoria
tarda unos cinco minutos.

<!-- S09 -->
Ahora haz que cada pulso dure la mitad.

<!-- S10 -->
El ordenador sigue distinguiendo lo corto de lo largo.
Pero el doble de bits
pasa por el cabezal cada segundo.

<!-- S11 -->
Ese es todo el truco de un cargador turbo.
Y no es solo un experimento mental.

<!-- S12 -->
En 1984, el juego Skool Daze
cargaba sus datos al doble
de la velocidad normal del Spectrum.

<!-- S13 -->
Entonces, ¿por qué el Spectrum
no cargaba así de rápido por sí solo?

<!-- S14 -->
El cargador integrado está guardado en la ROM,
el chip de memoria desde el que arranca el ordenador.
No mide un pulso en segundos.

<!-- S15 -->
Cuenta.
Tras cada flanco de la señal,
espera un momento
y luego cuenta cuánto tiempo pasa hasta el siguiente.

<!-- S16 -->
Un único número en la ROM
decide dónde termina el cero
y empieza el uno.

<!-- S17 -->
Y ese número deja mucho margen.
Un cero puede estirarse
más de un cuarenta por ciento
y seguir leyéndose como cero.

<!-- S18 -->
Ese margen es lo que permite que una cinta gastada
en una grabadora barata
siga cargando.

<!-- S19 -->
Y el límite no era el ordenador.
El Spectrum comprueba la señal de la cinta
unas sesenta mil veces por segundo.

<!-- S20 -->
El límite era el casete.
Pulsos más cortos significan tonos más agudos.
A doble velocidad, un cero
pasa de dos kilohercios a cuatro.

<!-- S21 -->
Y los tonos agudos son justo lo que
una grabadora barata,
o un cabezal un poco desalineado,
pierde primero.

<!-- S22 -->
Una revista de Spectrum calculaba en 1986
que la mayoría de la gente podía llegar
al menos al doble de la velocidad normal.
Cuánto más se podía subir
dependía de la grabadora.

<!-- S23 -->
Pero el turbo tenía un problema más extraño.

<!-- S24 -->
Si el ordenador solo conoce
el formato lento,
¿cómo carga el programa
que le enseña el rápido?

<!-- S25 -->
La respuesta está al principio de la cinta.
La primera parte está grabada
en el formato normal, el lento.

<!-- S26 -->
Es corta,
y la ROM la carga como cualquier otro programa.

<!-- S27 -->
Luego ese pequeño programa toma el control.
En el caso más sencillo,
es una copia de la propia rutina de carga de la ROM,
con unos cuantos números cambiados.

<!-- S28 -->
En Skool Daze,
los cambios están en tres sitios.
Una espera más corta, un nuevo valor inicial del contador,
una nueva línea divisoria.

<!-- S29 -->
Así que la ROM carga el programa
que hace el trabajo de la ROM, solo que más rápido.

<!-- S30 -->
Es un poco como descargar
un descargador más rápido.
Con el paso lento consigues la herramienta.
La herramienta hace el resto.

<!-- S31 -->
Los juegos comerciales usaron la misma idea.
Un ejemplo muy conocido fue Speedlock,
que Ocean usó por primera vez en 1984.

<!-- S32 -->
Uno de sus autores contó que lo escribió
porque estaba harto
de lo que tardaba el cargador estándar.

<!-- S33 -->
Pero aquí viene la sorpresa.
Speedlock era solo una vez y media
más rápido, más o menos.

<!-- S34 -->
El primer día
de Daley Thompson's Decathlon
tardaba tres minutos y veinte segundos,
cuando los mismos datos a velocidad normal
habrían tardado cuatro minutos y cuarenta y siete.

<!-- S35 -->
Las versiones posteriores solo eran
alrededor de un quinto más rápidas que la ROM.
Porque la velocidad no era su única tarea.

<!-- S36 -->
Desde 1983, los programas de copia
podían leer la cabecera de un juego
y copiar el juego entero en otra cinta.

<!-- S37 -->
Un formato propio
dejaba a esos programas sin nada que leer.

<!-- S38 -->
El primer Speedlock incluso partía su tono guía
en ráfagas cortas,
para que el propio cargador de la ROM
ni siquiera lo reconociera.

<!-- S39 -->
Y se podía oír.
Una cinta con Speedlock cargaba entre chasquidos,
con franjas dando tirones alrededor de la pantalla.

<!-- S40 -->
A nadie le impidió copiar
una cinta de una pletina a otra.
Pero sí dio a las editoras
un motivo para escribir sus propios cargadores.

<!-- S41 -->
En el Commodore 64,
el motivo para cambiar era mucho mayor.

<!-- S42 -->
Su rutina integrada
lo grababa todo dos veces,
como copia de seguridad.
Un juego de cuarenta kilobytes tardaba
unos doce minutos y medio.

<!-- S43 -->
Y aquí, la grabadora
no hacía casi nada inteligente.
Solo convertía el sonido
en pulsos limpios de encendido y apagado.

<!-- S44 -->
El propio ordenador cronometraba cada pulso,
por software.

<!-- S45 -->
Así que un cargador más rápido
era simplemente otro programa.

<!-- S46 -->
En 1985, la revista Compute!
probó uno llamado TurboTape.

<!-- S47 -->
Una vez encontrado el programa en la cinta,
cargó doce kilobytes
en veintiocho segundos.

<!-- S48 -->
La propia disquetera de Commodore
necesitó treinta y cuatro segundos.

<!-- S49 -->
Un casete
ganándole a un disquete.

<!-- S50 -->
Y como era el ordenador
el que escuchaba la cinta él solo,
podía hacer otras cosas entretanto.

<!-- S51 -->
Cargadores como Freeload
daban prioridad a la lectura de la cinta.
El tiempo de procesador que sobraba
iba a música, scroll suave,
e incluso pequeños juegos.

<!-- S52 -->
Con Invade-a-Load, de Mastertronic,
jugabas a un clon de Space Invaders
mientras se cargaba el juego de verdad.

<!-- S53 -->
Los ordenadores Atari de 8 bits
eran otra historia.

<!-- S54 -->
Aquí, quien escuchaba era la grabadora.
Dentro llevaba dos filtros,
uno para cada tono,
y un circuito que le entregaba al ordenador
unos y ceros ya listos.

<!-- S55 -->
El estándar era de seiscientos bits por segundo,
y los filtros limitaban
cuánto más rápido se podía ir.

<!-- S56 -->
Un software ingenioso podía subirlo
un poco, como mucho a unos mil doscientos.
Pero para ir mucho más rápido,
había que abrir la grabadora.

<!-- S57 -->
Y en Checoslovaquia, la gente la abrió.

<!-- S58 -->
Allí, una disquetera
costaba entre dos y tres veces
lo que el propio ordenador.
Así que la mayoría de los dueños de Atari de allí siguieron con la cinta.

<!-- S59 -->
En 1987, un estudiante de Praga
del club Atari local
diseñó Turbo 2000.

<!-- S60 -->
Añadía un nuevo camino para la señal.
Un cable dentro de la grabadora tomaba el sonido
directamente de su amplificador,
antes de los filtros,
lo pasaba por un pequeño chip
y lo llevaba a la línea hacia el ordenador.

<!-- S61 -->
Un conmutador, accionado por el ordenador,
elegía entre el camino viejo y el nuevo.

<!-- S62 -->
Ahora el propio ordenador cronometraba los pulsos.
Unos dos mil trescientos bits
por segundo.
Casi cuatro veces más rápido.

<!-- S63 -->
El turbo no era un único formato universal.

<!-- S64 -->
A veces cambiabas el programa.
A veces, tenías que cambiar la máquina.

<!-- S65 -->
Y la velocidad no salía gratis.

<!-- S66 -->
Compute! advertía que una grabación de TurboTape
a veces se negaba a cargar
en otra grabadora,
con el cabezal alineado de forma algo distinta.

<!-- S67 -->
La grabación estándar, decía,
era mucho más lenta,
pero extremadamente fiable.

<!-- S68 -->
Grabarlo todo dos veces
no era pereza de Commodore.
Era el precio de cargar de forma fiable.

<!-- S69 -->
Pero un cargador distinto
también podía hacer algo inesperado.
Podía leer una cinta
que el integrado rechazaba.

<!-- S70 -->
En el Sharp MZ-800,
un ordenador que llegó
a Checoslovaquia a finales de los 80,
los usuarios conocían un programa llamado Turbo Copy.

<!-- S71 -->
Un juego no cargaba
y daba un error de suma de verificación.
Los usuarios descubrieron que Turbo Copy
muchas veces conseguía cargarlo igualmente.

<!-- S72 -->
Luego lo grababas a velocidad normal
en un casete nuevo,
y el ordenador
volvía a cargarlo con normalidad.
Era como reparar un juego roto.

<!-- S73 -->
Entonces, ¿cómo podía un cargador leer
lo que el otro no podía?

<!-- S74 -->
La ROM del Sharp grababa cada bloque dos veces,
a unos mil doscientos bits por segundo.

<!-- S75 -->
Y nunca medía un pulso.
Después de que empezara cada pulso,
esperaba un intervalo fijo
y miraba una sola vez.

<!-- S76 -->
¿Sigue alto?

<!-- S76b -->
Es un uno.

<!-- S76c -->
¿Ya está bajo?

<!-- S76d -->
Es un cero.

<!-- S77 -->
Un cronómetro, ajustado de antemano.

<!-- S78 -->
En una cinta vieja, o en otra grabadora,
los pulsos volvían un poco más redondeados.
Y entonces esa única mirada
podía ver el nivel equivocado.

<!-- S79 -->
Un solo bit erróneo estropea la suma de verificación.
Si fallan las dos copias,
falla la carga.

<!-- S80 -->
Turbo Copy escuchaba de otra manera.
Cronometraba cada pulso
con el chip temporizador del ordenador.

<!-- S81 -->
Y antes de cada bloque,
escuchaba el tono guía
y fijaba su línea divisoria
según los pulsos que de verdad estaba oyendo.

<!-- S82 -->
Su cronómetro estaba ajustado
a la cinta que tenía delante.

<!-- S83 -->
Y la reparación no era una copia del sonido.
Turbo Copy se quedaba con los bytes
y escribía una señal totalmente nueva,
con pulsos de duración precisa.

<!-- S84 -->
Los datos no se habían perdido.
Es que la forma habitual de leerlos
no era lo bastante buena.

<!-- S84b -->
Turbo Copy también podía grabar el juego en turbo,
a dos o tres veces la velocidad normal,
con su propio cargador pequeño delante.

<!-- S85 -->
Y eso es lo que todos estos trucos
tienen en común.

<!-- S86 -->
El casete siguió siendo el mismo.
Lo que cambió fue la forma de leerlo.

<!-- S87 -->
Hoy esperamos que los juegos carguen al instante.
En los años 80, la carga era parte del juego.
Escuchabas la cinta.
Mirabas las franjas.
Esperabas.

<!-- S88 -->
Y a veces, un cargador distinto
hacía que el mismo casete se comportara
como una máquina completamente distinta.

<!-- S89 -->
El ordenador no necesitaba una cinta más rápida.
Necesitaba una forma mejor de escuchar.

<!-- S90 -->
Así que aquí va una pregunta para ti.
¿Usaste cargadores turbo en su día?
¿Cómo los recuerdas?
¿Fallaban más a menudo?
Cuéntamelo en los comentarios.

<!-- S91 -->
Y por último, la cinta turbo entera,
de principio a fin.
Primero la parte a velocidad normal,
luego el turbo.
Para un programa tan pequeño,
el turbo no compensa.
El cargador tarda más
que el tiempo que ahorra.
Con un juego entero, podía ahorrar minutos.
