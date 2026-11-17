<!-- S01 -->
Esto es un código QR.
Guarda una línea corta de texto.

<!-- S02 -->
El móvil lo lee al instante.

<!-- S03 -->
Ahora vamos a arrancarle un trozo.

<!-- S04 -->
Y lo escaneamos otra vez.
El mismo texto.
Letra por letra.

<!-- S05 -->
Una parte del código ha desaparecido.
No es que cueste leerla.
Ha desaparecido.

<!-- S06 -->
Entonces, ¿cómo puede un móvil leer algo
que ya no está ahí?

<!-- S07 -->
Aquí tienes el mismo problema, en pequeño.
Alguien te envía ocho bits.
Por el camino, se pierden tres.

<!-- S08 -->
Cada bit que falta es un cero o un uno,
así que hay ocho formas de llenar los huecos.
Y nada de lo que ha llegado
te dice cuál es la correcta.

<!-- S09 -->
Y aun así, el móvil acaba de hacer justo eso.
No estaba adivinando.
La respuesta se envió
antes de que se perdiera nada.

<!-- S10 -->
El truco es enviar más
que el propio mensaje.

<!-- S11 -->
La forma más sencilla
es decirlo todo tres veces.
Un cero se envía como tres ceros,
y un uno, como tres unos.

<!-- S12 -->
El ruido invierte uno de ellos,
y recibes uno, cero, uno.
Dos votos contra uno.
Casi seguro que era un uno.

<!-- S13 -->
Si el ruido invierte un bit de cada diez,
al azar y de forma independiente,
una votación de tres falla
menos de tres veces de cada cien.

<!-- S14 -->
Pero has triplicado
todo lo que envías.
Para acercarte a la perfección,
repetirías cinco veces, luego nueve,
luego cien...
y el mensaje avanzaría a paso de tortuga.

<!-- S15 -->
Durante mucho tiempo,
ese parecía ser el precio.
Menos errores, mensajes más lentos.
No lo olvides.

<!-- S16 -->
A finales de los años 40,
Richard Hamming, en los Bell Labs,
tenía su propio problema.

<!-- S17 -->
Solía conseguir tiempo en un ordenador de relés
los fines de semana,
cuando no había nadie para vigilarlo.

<!-- S18 -->
La máquina se daba cuenta
de cuándo se había equivocado.
Repetía el paso,
tres veces...
y luego descartaba su cálculo.
Dos fines de semana seguidos,
perdió todo lo que había hecho.

<!-- S20 -->
Su pregunta, en sus propias palabras:
"Si la máquina puede detectar
que hay un error,
¿por qué no puede localizar dónde está?"
Las palabras exactas, admitió,
seguramente fueron algo más fuertes.

<!-- S22 -->
Su respuesta toma cuatro bits de mensaje
y añade tres bits de control.
Siete bits en total.

<!-- S23 -->
Cada bit de control vigila
un grupo distinto de posiciones
y se asegura de que ese grupo
tenga un número par de unos.

<!-- S24 -->
Los grupos se solapan con un patrón muy pensado.
Cada posición pertenece
a su propia combinación de grupos.

<!-- S25 -->
Ahora invierte un bit.
Por ejemplo, el de la posición seis.

<!-- S26 -->
El receptor vuelve a hacer las tres comprobaciones.
La primera sale bien.
La segunda falla.
La tercera falla.

<!-- S27 -->
Escribe una comprobación fallida como uno,
una correcta como cero,
y léelas de la última a la primera.
Uno, uno, cero.
En binario, eso es seis.

<!-- S28 -->
Las comprobaciones no solo dicen
que algo ha ido mal.
Señalan el bit exacto.

<!-- S29 -->
Lo vuelves a invertir,
y el mensaje vuelve a estar entero.
Nadie tuvo que enviar nada dos veces.

<!-- S30 -->
Esa es la respuesta.
El receptor no reconstruye
información perdida de la nada.
El emisor ya la había metido dentro,
por adelantado.

<!-- S32 -->
No todas las comprobaciones pueden hacer eso.
Una suma de verificación, como la de nuestro vídeo
sobre Btrfs,
puede decirte que un bloque está dañado,
pero no cuáles eran los datos originales.

<!-- S33 -->
Y hay un segundo tipo de daño.
A veces un bit no está mal.
Simplemente falta,
y sabes exactamente dónde está el hueco.

<!-- S34 -->
Eso se llama borrado,
y los borrados son más fáciles.

<!-- S35 -->
Envía cuatro números,
4, 7, 2 y 9,
y un quinto:
su suma, 22.

<!-- S36 -->
Si falta uno cualquiera,
los demás te dicen cuál era.
4, 7, algo, 9,
22.
Tiene que ser un 2.

<!-- S37 -->
Los servidores protegen sus discos
con un tipo de comprobación parecido,
repartido entre las unidades.
Cuando una unidad muere,
su contenido se calcula a partir del resto.

<!-- S38 -->
Entonces, ¿cuánto extra necesitas?
La repetición dice:
para reducir los errores a cero,
tienes que reducir la velocidad a cero.

<!-- S39 -->
Dos años antes de que saliera
el artículo de Hamming,
su colega Claude Shannon
había publicado una respuesta más extraña.

<!-- S40 -->
Todo canal,
un enlace de radio, un cable, un disco,
tiene un límite.
Una velocidad máxima para la información.

<!-- S41 -->
Por debajo de ese límite,
los errores pueden ser tan raros como quieras,
sin ir más despacio.
No repitiendo más.
Codificando de forma más inteligente.

<!-- S42 -->
Por encima,
ningún código del mundo sirve de nada.

<!-- S43 -->
Pero había un problema.
Shannon demostró que esos códigos existen.
No mostró cómo construir uno
que alguien pudiera usar.

<!-- S44 -->
Según su demostración, un código al azar
casi seguro que sería bueno.
Pero la forma obvia de decodificarlo
implica comparar lo que ha llegado
con todos los mensajes posibles...
y para un bloque de 1000 bits,
hay más mensajes posibles
que átomos en el universo.

<!-- S46 -->
Así que el artículo de Shannon no era una solución.
Era una promesa.
Y los ingenieros pasaron los siguientes
45 años intentando cumplirla.

<!-- S47 -->
El código de Hamming fue un primer paso.
Corrige un bit erróneo de cada siete.

<!-- S48 -->
Pero los daños reales llegan en ráfagas.
Un arañazo o un chasquido de estática
se lleva cientos de bits seguidos.

<!-- S49 -->
En 1960, Irving Reed y Gustave Solomon,
en el Lincoln Laboratory del MIT,
publicaron un artículo de cinco páginas.

<!-- S50 -->
Sus códigos trabajan con bytes enteros,
no con bits sueltos.
Si una ráfaga destroza los ocho bits
de un byte,
sigue siendo un solo byte erróneo.

<!-- S51 -->
Una versión habitual añade
32 bytes de control
a 223
bytes de datos.

<!-- S52 -->
Puede corregir 16 bytes cualesquiera
que lleguen mal...
o reconstruir 32
que no lleguen nunca.

<!-- S53 -->
Así es como un CD rayado sigue sonando.
Sus dos códigos de Reed-Solomon
pueden reparar por completo un hueco
de unos 4000 bits,
2,5 milímetros de pista.

<!-- S54 -->
Y por eso el código QR rasgado
seguía funcionando.
En su nivel más alto,
un código QR puede reconstruir
hasta alrededor del 30 % de sus bytes
y aun así devolver cada letra.

<!-- S56 -->
La Voyager 2 salió de la Tierra en 1977
llevando ya un codificador Reed-Solomon.

<!-- S57 -->
Pero en Júpiter y Saturno,
protegía todo menos las imágenes
con un código más antiguo, de Marcel Golay,
que enviaba un bit extra
por cada bit de datos.

<!-- S58 -->
Para Urano y Neptuno,
con la señal cada vez más débil,
los ingenieros activaron Reed-Solomon,
además de un segundo código
por el que ya pasaba cada bit.

<!-- S59 -->
Solo con ese segundo código,
unos cinco bits de cada mil
seguían llegando mal.
Al añadir Reed-Solomon,
más o menos uno de cada millón.

<!-- S60 -->
El ruido también llega en ráfagas,
así que la Voyager mezclaba
los bytes de cuatro bloques
antes de enviarlos.

<!-- S61 -->
Una ráfaga que habría destrozado un bloque
ahora se lleva unos pocos bytes de cada uno...
tan pocos que cada bloque
puede repararse solo.

<!-- S62 -->
El resto del viaje de las imágenes de Neptuno
hasta casa
está en nuestro vídeo sobre la Voyager.

<!-- S63 -->
Pero ni siquiera esto
alcanzaba el límite de Shannon...
y un código que podía acercarse mucho más
ya existía.

<!-- S65 -->
En 1960, en su tesis doctoral en el MIT,
Robert Gallager describió códigos
formados por muchas comprobaciones sencillas,
cada una mirando solo unos pocos bits.

<!-- S66 -->
Para decodificarlos, las comprobaciones
se pasaban conjeturas de un lado a otro,
ronda tras ronda...
demasiado
para los ordenadores de los años 60.
Así que la idea se guardó en un cajón
y quedó casi olvidada durante 30 años.

<!-- S68 -->
En 1993,
un equipo dirigido por dos ingenieros franceses,
Claude Berrou y Alain Glavieux,
presentó los turbocódigos
en un congreso en Ginebra.

<!-- S69 -->
Sus resultados estaban tan cerca
del límite de Shannon
que muchos expertos supusieron
que se habían equivocado.
Seguramente en un factor de dos,
en algún punto de sus cálculos.

<!-- S70 -->
En menos de un año,
otros laboratorios lo habían confirmado.

<!-- S71 -->
Los turbocódigos también funcionaban
pasándose conjeturas de un lado a otro,
y eso hizo que los investigadores volvieran a Gallager.

<!-- S72 -->
En 1995 y 1996,
David MacKay y Radford Neal
redescubrieron sus códigos
y demostraron que podían llegar
igual de cerca.

<!-- S73 -->
En 2001,
una versión refinada de los códigos de Gallager
se quedó a 0,04 decibelios
del límite de Shannon.

<!-- S74 -->
Eso es menos del uno por ciento
más de potencia de señal
que el mínimo teórico.
La promesa de 1948 se había cumplido.

<!-- S75 -->
Hoy, los códigos de Gallager transportan
gran parte de los datos en los móviles 5G,
en el wifi moderno
y en la televisión por satélite.

<!-- S77 -->
Ahora, volvamos a nuestros ocho bits.
Se perdieron tres,
y hay ocho formas
de llenar los huecos.

<!-- S78 -->
Pero esos ocho bits
nunca fueron solo un mensaje.
Llevaban cuatro bits de datos,
las tres comprobaciones de Hamming
y una comprobación más sobre los ocho.

<!-- S79 -->
De los 256
patrones posibles de ocho bits,
solo 16 cumplen esas reglas.

<!-- S80 -->
Prueba los ocho candidatos.
Uno tras otro, fallan.
Solo queda uno.

<!-- S81 -->
Los bits que faltaban nunca desaparecieron del todo.
Su información seguía ahí,
en los bits que sobrevivieron.

<!-- S82 -->
Así que aquí va una pregunta para ti.
¿Alguna vez has notado la corrección de errores
funcionando en algo que usas a diario?
Cuéntamelo en los comentarios.
