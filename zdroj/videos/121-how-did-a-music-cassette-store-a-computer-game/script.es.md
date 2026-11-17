<!-- S01 -->
Le das al play en un radiocasete.
Y del altavoz sale esto.

<!-- S02 -->
No es música.
Y tampoco es la banda sonora de un juego.

<!-- S03 -->
Es el juego.
Cada chirrido es parte de un programa,
y el ordenador lo está escuchando.

<!-- S04 -->
El radiocasete no tiene ni idea.
Por lo que a él respecta, suena una canción.

<!-- S05 -->
Entonces, ¿cómo se convierte una canción en un juego?
¿Y por qué una sola nota equivocada
podía tirar a la basura cinco minutos de espera?

<!-- S06 -->
Este es el truco,
en una máquina concreta:
el ZX Spectrum,
un ordenador doméstico británico de 1982.

<!-- S07 -->
Usa dos tipos de pulso.
Un par de pulsos cortos significa cero.

<!-- S08 -->
Un uno es el mismo par,
pero cada pulso dura el doble,
así que su tono suena una octava más grave.

<!-- S09 -->
Envía unos mil cuatrocientos bits
por segundo,
y obtienes el ruido que acabas de oír.

<!-- S09b -->
También significa que un programa lleno de ceros
carga más rápido que uno lleno de unos.
Cada «uno» tarda el doble en enviarse.

<!-- S10 -->
Ahora bien, si creciste en Estados Unidos,
puede que nunca lo hayas oído.

<!-- S11 -->
Lo cual es curioso,
porque la idea en sí era estadounidense.

<!-- S12 -->
En 1975, en una reunión en Kansas City,
aficionados a la informática acordaron una forma
de guardar datos como sonido
en casetes de audio corrientes.

<!-- S12b -->
Un uno eran ocho ciclos rápidos
de un tono agudo,
y un cero, cuatro ciclos más lentos de uno grave.
Trescientos bits por segundo.

<!-- S13 -->
Las primeras máquinas, como el Apple II
y el TRS-80,
guardaban sus programas
en grabadoras de casete normales y corrientes.

<!-- S14 -->
Pero la informática doméstica estadounidense
pasó página muy deprisa.

<!-- S15 -->
En 1983, una revista publicó una encuesta:
nueve de cada diez nuevos dueños de un Commodore 64
se compraban una disquetera
junto con el ordenador.

<!-- S16 -->
En Gran Bretaña, la historia fue justo al revés.

<!-- S17 -->
El Spectrum costaba ciento
veinticinco libras,
y no traía ningún tipo de almacenamiento.
Usabas el radiocasete
que ya tuvieras en casa.

<!-- S18 -->
Así que para millones de niños de toda Europa,
este ruido era el sonido
de un juego a punto de empezar.

<!-- S18b -->
Después de cargar tantos juegos,
hasta podías saber qué juego era
solo por el chirrido.

<!-- S19 -->
Así que sigamos un juego
desde la cinta hasta el ordenador.

<!-- S20 -->
Escribes LOAD, pulsas Enter
y le das al play.

<!-- S21 -->
Primero llega un zumbido constante,
de ochocientos ciclos por segundo,
durante unos cinco segundos.

<!-- S22 -->
No lleva ningún dato.
Está ahí para que el ordenador
encuentre la señal
y se enganche a su ritmo.

<!-- S23 -->
Luego, dos pulsos rápidos: la sincronización.
Significan: a partir de aquí, son datos.

<!-- S24 -->
Lo primero que llega
es una cabecera corta.
Diecinueve bytes:
un nombre de hasta diez letras,
qué tipo de archivo es
y cuánto va a ocupar.

<!-- S25 -->
Luego, un segundo zumbido, más corto,
esta vez de dos segundos,
y después el juego en sí.

<!-- S26 -->
Cada byte son ocho de esas notas,
una detrás de otra,
sin ningún hueco entre un byte y el siguiente.

<!-- S27 -->
Y el ordenador no oye notas.
Mide el tiempo entre un flanco
de la señal y el siguiente.

<!-- S28 -->
Un par corto es un cero.
Un par largo es un uno.

<!-- S28a -->
Y ese es todo el decodificador.

<!-- S28b -->
Y el ruido del principio de este vídeo
no es un efecto de sonido.
Lo generamos exactamente con estas reglas,
y dentro hay un programa real de Spectrum.

<!-- S28c -->
Lo pondremos entero al final del todo.
Grábalo, y un Spectrum lo cargará.

<!-- S29 -->
La mayoría de los juegos mostraban primero una imagen,
y se cargaba en un orden extraño.

<!-- S30 -->
Aparecían rayas finas, separadas ocho líneas,
luego se rellenaban, línea a línea,
un tercio de la pantalla cada vez.
Y los colores llegaban al final,
cubriéndolo todo de arriba abajo.

<!-- S31 -->
Solo esa imagen
tardaba unos cuarenta segundos.
El juego entero, unos cinco minutos.

<!-- S32 -->
Y al final de cada bloque
llega un byte más.

<!-- S33 -->
Al guardar, el Spectrum pasa
cada byte del bloque
por una regla sencilla llamada XOR,
y graba el resultado como un byte más.

<!-- S34 -->
Al cargar, repite el cálculo.
Si los resultados coinciden,
el bloque ha llegado intacto.

<!-- S35 -->
Si no, el Spectrum te dice esto.

<!-- S36 -->
Cinco minutos de espera,
y un solo byte decide
que todo ha sido en vano.
Rebobinar y vuelta a empezar.

<!-- S37 -->
Curiosamente, una cabecera dañada
no da ningún error.
El Spectrum simplemente la ignora
y sigue escuchando a la espera de la siguiente.

<!-- S38 -->
Otros ordenadores apostaron por otras cosas.

<!-- S39 -->
El Commodore 64 grababa
cada bloque dos veces,
para que una zona dañada en una copia
pudiera rescatarse de la otra.

<!-- S40 -->
Más seguro, pero lento.
Con la rutina integrada de Commodore,
un programa de cuarenta kilobytes
tardaba unos doce minutos y medio.

<!-- S41 -->
Así que las editoras de juegos escribieron
sus propios cargadores, más rápidos,
algunos hasta unas diez veces más rápidos.

<!-- S42 -->
Y luego estaba el propio radiocasete.

<!-- S43 -->
Demasiado bajo,
y los flancos se hunden en el siseo.
Demasiado alto,
y se emborronan unos con otros.

<!-- S44 -->
Una cinta que va un poco rápida o lenta
estira cada pulso,
y el ordenador está midiendo tiempo.

<!-- S45 -->
Lo peor de todo era el azimut,
el ángulo del cabezal.
Una cinta grabada en un aparato
podía no cuadrar con otro.

<!-- S46 -->
Así que la gente metía un destornillador diminuto
en un agujerito junto al cabezal,
y lo giraba poquito a poco,
escuchando.

<!-- S47 -->
Parecía superstición.
En realidad, estaban ajustando la señal.

<!-- S48 -->
Pero fíjate en lo que el radiocasete
nunca tuvo que hacer.

<!-- S49 -->
Nunca entendió ni un solo bit.
Grababa sonido
y lo volvía a reproducir.

<!-- S50 -->
Lo que significa que un programa
en realidad no necesitaba un casete.
Cualquier cosa capaz de llevar sonido
podía llevar software.

<!-- S50b -->
También significaba que copiar un juego
era tan fácil como copiar un álbum.
Dos pletinas y un cable.

<!-- S51 -->
Atari usó las dos pistas estéreo.
El programa en una,
y una voz en la otra,
que te hablaba desde la tele
mientras cargaba el juego.

<!-- S52 -->
En Yugoslavia, un espacio de Radio Belgrado
emitía programas informáticos por las ondas.

<!-- S53 -->
Los oyentes los grababan en cinta,
unos ciento cincuenta programas
entre 1983 y 1986.

<!-- S54 -->
En Checoslovaquia, fue la televisión.
Un programa sonaba como audio
bajo los créditos finales.

<!-- S55 -->
Y en 1983, el cantante Pete Shelley
escondió un programa de Spectrum
al final de un álbum en vinilo.

<!-- S56 -->
Lo pasabas a cinta, lo cargabas,
y las letras aparecían en pantalla
sincronizadas con las canciones.

<!-- S57 -->
Pero había una pega.

<!-- S58 -->
La radio podía llevar el sonido
a todos los ordenadores del país.
Solo el adecuado podía entenderlo.

<!-- S59 -->
Ponle un juego de Spectrum a un Commodore,
y el Commodore oye ruido.
Los bits solo significan algo
para una máquina que conoce el formato.

<!-- S60 -->
Así que la radio neerlandesa intentó arreglarlo.
En 1982 creó BASICODE:
un único formato de sonido,
con un pequeño programa traductor
para cada tipo de ordenador.

<!-- S61 -->
Y ese problema nunca desapareció.
Un archivo solo sirve
si algo todavía puede leerlo.

<!-- S62 -->
Los casetes perdieron, claro.
Los disquetes eran más rápidos,
luego los discos duros, luego la memoria flash.

<!-- S63 -->
Solo que la cinta nunca se fue del todo.
Los centros de datos siguen guardando
sus archivos en cinta magnética.

<!-- S64 -->
Un cartucho moderno LTO-9
almacena dieciocho terabytes.

<!-- S65 -->
A la velocidad del Spectrum,
esa capacidad llenaría unos
veintinueve millones de casetes,
y tardaría más de tres mil
años en cargar.

<!-- S66 -->
Pero sigue siendo la misma idea.
Patrones en una tira de cinta en movimiento,
que vuelven a convertirse en números
cuando los necesitas.

<!-- S67 -->
Así que la próxima vez que oigas ese chirrido,
recuerda lo que es.
No es ruido.
Es un programa que viaja en forma de sonido.

<!-- S68 -->
Y en 1985, en algún lugar,
un niño está sentado delante de la tele,
esperando a que pare.
Porque cuando pare,
empieza el juego.

<!-- S69 -->
Así que aquí va una pregunta para ti.
Si alguna vez cargaste un juego desde un casete,
¿qué es lo que más recuerdas?
Cuéntamelo en los comentarios.

<!-- S70 -->
Y como prometimos, aquí está ese programa.
Igual que la televisión checoslovaca,
lo hemos puesto bajo los créditos finales.
