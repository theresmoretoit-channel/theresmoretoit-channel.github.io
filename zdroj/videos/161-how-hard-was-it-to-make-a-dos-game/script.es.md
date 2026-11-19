<!-- S01 -->
En 1993, un juego llamado Doom
funcionaba en un ordenador
con 4 megabytes de memoria.

<!-- S02 -->
Eso es más o menos el tamaño
de una sola foto en tu móvil.

<!-- S03 -->
No había acelerador 3D.
El procesador principal
se encargaba de todo el renderizado.

<!-- S04 -->
Hoy, un desarrollador empieza con un motor,
como Unity o Unreal,
que se ocupa de los gráficos, el sonido,
la memoria y el hardware.

<!-- S05 -->
En DOS, todo eso
era problema del desarrollador.
Y muy a menudo, también del jugador.

<!-- S06 -->
Entonces, ¿qué tan difícil era
hacer un juego para DOS?

<!-- S07 -->
Empecemos por la memoria,
porque la memoria era un lío.

<!-- S08 -->
El IBM PC original, de 1981,
podía direccionar 1 megabyte de memoria.

<!-- S09 -->
Pero solo los primeros
640 kilobytes
estaban pensados para los programas.

<!-- S10 -->
Los otros 384 kilobytes
estaban reservados para la memoria de vídeo,
las tarjetas de expansión y la BIOS.

<!-- S11 -->
Durante más de una década,
DOS ejecutaba normalmente los programas
dentro de ese espacio.
Ir más allá exigía trabajo extra.

<!-- S12 -->
De ahí viene la famosa frase:
640 K deberían bastarle a cualquiera.

<!-- S13 -->
Se suele atribuir a Bill Gates.
No hay constancia de que la dijera nunca,
y él lo niega.

<!-- S14 -->
A principios de los noventa,
un PC venía con 4 megabytes,
u 8.

<!-- S15 -->
Y aun así un juego podía detenerse
con las palabras
«no hay suficiente memoria».

<!-- S16 -->
Tener la memoria
y poder usarla
eran dos cosas distintas.

<!-- S17 -->
Una salida era la memoria expandida,
o EMS.

<!-- S18 -->
Una ventana de 64 kilobytes
estaba en la parte superior
de ese primer megabyte.
A través de ella, un programa podía ver
4 páginas de memoria extra,
de 16 kilobytes cada una,

<!-- S19 -->
y cambiarlas por otras,
como pasar las páginas de un libro
a través de un agujero en una hoja de papel.

<!-- S20 -->
Otra vía era la memoria extendida,
a la que se accedía con un controlador llamado HIMEM.

<!-- S21 -->
Y aquí es donde
el problema del desarrollador
se convirtió en el del jugador.

<!-- S22 -->
Los controladores del ratón, del lector de CD
o de la tarjeta de sonido
le daban un bocado a esa preciada memoria,
a menos que consiguieras cargarlos en la memoria superior.

<!-- S23 -->
Así que los jugadores aprendieron a editar dos archivos,
CONFIG.SYS y AUTOEXEC.BAT.

<!-- S24 -->
Un juego quería EMS.
Otro la quería desactivada,
con una opción llamada NOEMS.
Y un tercero necesitaba cada kilobyte libre.

<!-- S25 -->
En 1993, MS-DOS 6 añadió
un menú de arranque.

<!-- S26 -->
Elegías la configuración
para el juego al que querías jugar,
y el ordenador arrancaba para ese juego.

<!-- S27 -->
Algunos acabaron
con una entrada aparte
para casi cada juego que tenían.

<!-- S28 -->
Pero para entonces,
los juegos más grandes ya habían encontrado
una forma de esquivar los límites de DOS.

<!-- S29 -->
Desde el 386,
el propio procesador podía funcionar
en modo protegido de 32 bits,
con espacio para hasta 4 gigabytes.

<!-- S30 -->
Ya hablamos del modo protegido
en un vídeo anterior.
DOS, sin embargo, no podía usarlo.

<!-- S31 -->
Así que los juegos traían su propio ayudante,
un extensor de DOS.
El más conocido era DOS/4GW.

<!-- S32 -->
Venía incluido con un compilador popular,
Watcom C.

<!-- S33 -->
Cuando un juego arrancaba,
DOS/4GW pasaba el procesador
a modo protegido,
lo que daba al juego acceso
a la memoria más allá del límite de DOS.

<!-- S34 -->
DOS seguía ahí debajo,
ofreciendo servicios como el acceso a archivos.
Pero el juego ahora funcionaba en modo protegido,
no como un programa de DOS tradicional.

<!-- S35 -->
Si jugaste a juegos de DOS en los noventa,
habrás visto su nombre
pasar fugazmente por la pantalla.

<!-- S37 -->
Ahora, la imagen.
En uno de los modos VGA más usados,
llamado Mode 13h,
la pantalla tenía 320
por 200 píxeles,
con 256 colores.

<!-- S38 -->
Cada píxel era un byte.
Para colorear un píxel,
escribías un número en la memoria.
Sin biblioteca gráfica. Solo memoria.

<!-- S39 -->
La pantalla entera ocupaba
64 000 bytes.

<!-- S40 -->
Eso es justo por debajo de 64 kilobytes,
lo bastante pequeño para caber en un segmento,
el bloque que un programa de 16 bits
podía direccionar de una vez.
Por una vez, la memoria jugaba a tu favor.

<!-- S41 -->
Pero si dibujas directamente
en la pantalla visible,
el jugador ve imágenes a medio hacer,
y la imagen parpadea.

<!-- S42 -->
Así que los juegos dibujaban cada fotograma
primero en un búfer oculto,
y luego copiaban la imagen terminada
a la memoria de vídeo.

<!-- S43 -->
En 1991, Michael Abrash,
programador y escritor,
publicó una forma mejor.
La llamó Mode X.

<!-- S44 -->
Usaba una parte de la VGA
que la mayoría de los programadores
nunca había tocado.

<!-- S45 -->
Daba píxeles cuadrados
y espacio para varias pantallas
en la memoria de vídeo.

<!-- S46 -->
El juego dibujaba en una pantalla
que nadie podía ver,
y luego simplemente cambiaba a esa pantalla.
Pero era mucho más difícil de programar.

<!-- S47 -->
Luego estaba el sonido.
Y el sonido era una lotería.

<!-- S48 -->
El altavoz propio del PC
estaba hecho para pitar.

<!-- S49 -->
Luego llegaron las tarjetas de sonido
y otros dispositivos de sonido.
No había dos
que funcionaran igual.

<!-- S50 -->
AdLib, con un chip de Yamaha
que sintetizaba música.
Sound Blaster, que además podía reproducir
sonido grabado.

<!-- S51 -->
La Roland MT-32,
una caja cara con instrumentos más ricos.
La Gravis UltraSound.

<!-- S52 -->
Darles soporte a todas
significaba escribir controladores distintos.

<!-- S53 -->
Y el juego tenía que saber
dónde estaba la tarjeta.
Su puerto, su IRQ
y su canal DMA.

<!-- S54 -->
La respuesta habitual, para una Sound Blaster,
era puerto 220, IRQ 7, DMA 1.
Normalmente.

<!-- S55 -->
Si fallabas en uno,
el juego se quedaba mudo.
O se colgaba.

<!-- S56 -->
En 1991, un programador llamado John Miles
lanzó una biblioteca
que hablaba con muchas tarjetas de sonido
a través de una sola interfaz.

<!-- S57 -->
Un juego podía escribir su código de sonido una vez
y dejar que la biblioteca se ocupara de la tarjeta.

<!-- S58 -->
Era otra capa más
entre el juego y el hardware.
Tenlo en cuenta.

<!-- S59 -->
Y luego estaba la velocidad.
Los programadores contaban
cada paso que daba el procesador.

<!-- S63 -->
Para encontrar un píxel en la pantalla,
multiplicas su fila
por 320.

<!-- S63b -->
En los procesadores antiguos,
multiplicar podía salir caro.

<!-- S64 -->
Pero 320
es 256
más 64.
Ambos son potencias de dos.

<!-- S65 -->
Así que puedes sustituir la multiplicación
por dos desplazamientos de bits y una suma.

<!-- S67 -->
Chris Sawyer programó pegado al hardware.
Escribió Transport Tycoon, en 1994,
casi entero en lenguaje ensamblador,

<!-- S68 -->
las instrucciones
que entiende el propio procesador,
una a una.

<!-- S69 -->
Y a veces,
ni siquiera todo eso bastaba.

<!-- S70 -->
En 1990, Wing Commander tenía un fallo
que el equipo no lograba encontrar,
con la fecha de entrega encima.

<!-- S71 -->
Al salir del juego,
se colgaba el gestor de memoria
con un mensaje de error.

<!-- S72 -->
Así que un programador, Ken Demarest,
abrió el gestor de memoria
en un editor hexadecimal
y cambió el texto de ese mensaje.

<!-- S73 -->
Ahora decía:
«Gracias por jugar a Wing Commander».

<!-- S74 -->
Luego el equipo encontró el fallo real,
y la broma nunca llegó a publicarse.

<!-- S74b -->
Algunos jugadores siguen convencidos de haberla visto.
Y juegos posteriores de Origin
sí se despedían así.

<!-- S75 -->
Lo que nos devuelve a Doom.

<!-- S76 -->
Doom usaba DOS/4GW
y funcionaba como un programa de 32 bits.

<!-- S77 -->
No todos los PC tenían garantizado
hardware de coma flotante.

<!-- S78 -->
Así que Doom usaba aritmética de coma fija.
Números enteros,
en los que los 16 bits menos significativos
representaban la parte fraccionaria.

<!-- S79 -->
Y su mundo no era
realmente tridimensional.

<!-- S80 -->
Cada nivel es un plano visto desde arriba,
con una altura para cada suelo
y cada techo.

<!-- S81 -->
Una sala nunca puede estar encima de otra.
Y no puedes mirar bien hacia arriba ni hacia abajo.

<!-- S82 -->
Antes de poder jugar un nivel,
una herramienta dividía el mapa
en un árbol binario, un BSP.

<!-- S83 -->
El motor recorre ese árbol
de delante hacia atrás,
empezando por el lado del jugador,
y se salta las zonas que no se ven.

<!-- S84 -->
Y Doom ni siquiera se escribió en DOS.

<!-- S85 -->
id Software lo desarrolló
en estaciones de trabajo NeXT
y compiló el resultado para DOS.

<!-- S86 -->
Doom no era un motor 3D general.
Estaba hecho para exactamente
un tipo de mundo.
Esa especialización
lo ayudó a funcionar en un 386.

<!-- S87 -->
Y otros estudios querían ese mundo.

<!-- S88 -->
Raven Software licenció el motor de Doom
para Heretic, en 1994,
y Hexen, en 1995.

<!-- S89 -->
Doom ayudó a consolidar
una nueva forma de hacer juegos.
Los estudios podían licenciar un motor existente
en lugar de construirlo todo desde cero.

<!-- S90 -->
Un extensor de memoria.
Una biblioteca de sonido.
Un motor con licencia.

<!-- S91 -->
Cada uno le quitó al desarrollador
un problema de encima.
Y las capas siguieron creciendo,
hasta convertirse en los motores
con los que los desarrolladores empiezan hoy.

<!-- S92 -->
Entonces, ¿era más difícil hacer juegos antes?
En muchos sentidos, sí.

<!-- S93 -->
Pero la dificultad no desapareció.
Se desplazó.

<!-- S94 -->
Hoy, los desarrolladores lidian
con gigabytes de recursos
y millones de polígonos,
en lugar de unos pocos cientos de kilobytes.

<!-- S95 -->
En DOS, hasta el jugador
tenía que saber adónde se iba su memoria.

<!-- S96 -->
Así que te dejo una pregunta.
¿Recuerdas montar
un menú de arranque solo para que funcionara un juego?
¿Y era un suplicio
o la mitad de la diversión?
Cuéntamelo en los comentarios.
