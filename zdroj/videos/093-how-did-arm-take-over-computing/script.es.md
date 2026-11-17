# ¿Cómo conquistó ARM la informática?

<!-- S01 -->
En 1985, unos ingenieros en Gran Bretaña
encendieron un flamante procesador
por primera vez.

<!-- S02 -->
Funcionó.
Y eso ya era un pequeño milagro.

<!-- S03 -->
Pero entonces notaron algo raro.
La alimentación del chip
no estaba conectada.

<!-- S04 -->
Y aun así, funcionaba.

<!-- S05 -->
Se las arreglaba con corrientes diminutas
que se colaban por sus pines de entrada,
desde las señales de los chips de alrededor.

<!-- S06 -->
Cuando lo midieron como es debido,
el procesador necesitaba
alrededor de una décima de vatio.

<!-- S07 -->
Nadie lo había buscado.
Los ingenieros solo querían un chip
que fuera barato de fabricar.

<!-- S08 -->
Ese chip fue el primer procesador ARM.

<!-- S09 -->
Cuarenta años después, sus descendientes
están en casi todos los smartphones.
En los ordenadores de Apple.
En algunos de los mayores centros de datos
del mundo.

<!-- S10 -->
Cientos de miles de millones de chips.

<!-- S11 -->
Entonces, ¿cómo un procesador
de una empresa británica de ordenadores domésticos
acabó conquistando la informática?

<!-- S12 -->
La respuesta no es simplemente
que consumía muy poco.
Eso fue casi un accidente.

<!-- S12b -->
Por cierto, si te gustan vídeos
como este, plantéate suscribirte.

Ayuda mucho al canal.

<!-- S13 -->
Para entender qué pasó de verdad,
tenemos que volver a 1983.

<!-- S14 -->
La empresa era Acorn Computers.
Su BBC Micro estaba en las aulas
de todo el Reino Unido.

<!-- S15 -->
El BBC Micro usaba un chip
más antiguo de ocho bits, el 6502.
Para su siguiente máquina,
Acorn necesitaba algo mucho más rápido.

<!-- S16 -->
Así que el equipo probó
los nuevos procesadores del mercado.
Ninguno hacía lo que Acorn quería.

<!-- S17 -->
Eran complicados,
y ninguno encajaba de verdad
con lo que Acorn quería construir.

<!-- S18 -->
Entonces, dos ingenieros de Acorn,
Sophie Wilson y Steve Furber,
fueron a Arizona,
a una empresa fundada por uno de
los diseñadores originales del 6502.

<!-- S19 -->
Esperaban una gran empresa de chips.
En cambio, encontraron a un puñado de personas
trabajando desde una casa en las afueras.

<!-- S20 -->
Y volvieron a casa
con una conclusión sencilla.
Si ellos pueden diseñar un procesador...
nosotros también.

<!-- S22 -->
En aquella época, los procesadores incorporaban
instrucciones cada vez más elaboradas.

<!-- S23 -->
Una sola instrucción podía traer
un número de la memoria,
hacer cálculos con él
y volver a escribir el resultado.

<!-- S24 -->
Cómodo para el programador.
Pero cada instrucción así
hace que el chip sea más difícil de construir.

<!-- S25 -->
Necesita más lógica
solo para averiguar qué significa cada una.
Más transistores.
Más tiempo de diseño.

<!-- S26 -->
Investigadores de Berkeley y Stanford
se habían hecho una pregunta radical.

<!-- S27 -->
¿Y si un procesador
solo tuviera instrucciones sencillas
y el compilador hiciera el resto?

<!-- S28 -->
Lo llamaron RISC.
Ordenador con conjunto de instrucciones reducido.

<!-- S29 -->
Sophie Wilson diseñó
las instrucciones de ARM con esa idea.

<!-- S30 -->
Las operaciones aritméticas solo trabajan
con los registros del propio chip,
pequeñas casillas rápidas dentro del procesador.
Para la memoria hay instrucciones aparte.

<!-- S31 -->
Así que sumar un número de la memoria
se convierte en tres pasos.
Cargarlo.
Sumarlo.
Guardarlo.

<!-- S32 -->
Se llama arquitectura de carga y almacenamiento.

<!-- S33 -->
Más pasos para el programa.
Pero cada paso es regular,
predecible
y fácil de decodificar.

<!-- S34 -->
Y ARM tenía muchos registros
con los que trabajar.
Dieciséis, de 32 bits cada uno.
El 6502 tenía tres pequeños.

<!-- S35 -->
El resultado fue el ARM1.

<!-- S36 -->
Tenía unos
25.000 transistores.

<!-- S37 -->
El 286 de Intel, lanzado unos años antes,
tenía unos 134.000.

<!-- S38 -->
Menos transistores significaban un chip más pequeño.
Un chip más barato.

<!-- S39 -->
Y, casi como efecto secundario,
un chip que apenas consumía energía.

<!-- S40 -->
De ahí salió
esa décima de vatio.
Acorn quería un encapsulado de plástico barato,
y eso obligaba a quedarse por debajo de un vatio.
Así que diseñaron con cuidado...
y se quedaron diez veces por debajo.

<!-- S41 -->
En 1987, una versión más rápida del ARM
llegó al nuevo ordenador de Acorn,
el Archimedes.

<!-- S42 -->
Era uno de los ordenadores personales
más rápidos de su época.

<!-- S43 -->
Y casi no sirvió de nada.

<!-- S44 -->
El mundo compraba PC compatibles con IBM
con procesadores Intel.
Ahí estaban los programas.
Eso era lo que compraban las empresas.

<!-- S45 -->
El Archimedes se quedó
sobre todo en los colegios británicos.

<!-- S46 -->
Y la propia Acorn pasaba apuros.
Ya había tenido que rescatarla
Olivetti, en 1985.

<!-- S48 -->
Entonces llegó ayuda de Apple.
Estaba construyendo un ordenador de bolsillo
llamado Newton.

<!-- S49 -->
Necesitaba un procesador
rápido, barato
y capaz de funcionar con pilas.

<!-- S50 -->
El ARM encajaba a la perfección.
Pero Apple no quería depender
de un chip que pertenecía
a un fabricante de ordenadores rival.

<!-- S51 -->
Así que en 1990, el equipo de ARM
se separó de Acorn
y formó su propia empresa.

<!-- S52 -->
Acorn, Apple
y el fabricante de chips VLSI
eran copropietarios de la empresa.

<!-- S53 -->
Doce ingenieros.
Un viejo granero cerca de Cambridge.

<!-- S54 -->
Y un modelo de negocio
que resultó ser el verdadero secreto de su éxito.

<!-- S55 -->
Intel diseñaba sus procesadores,
los fabricaba en sus propias fábricas
y los vendía.

<!-- S56 -->
ARM no iba a fabricar nada.
Iba a vender el diseño.

<!-- S57 -->
Cualquier empresa podía licenciarlo,
integrar el núcleo ARM en su propio chip
y pagar una pequeña cuota
por cada chip que vendiera.

<!-- S58 -->
Eso era importante,
porque un chip no tiene por qué ser
solo un procesador.
Alrededor del núcleo ARM
puedes poner una radio,
una unidad gráfica,
un procesador para la cámara.

<!-- S59 -->
Un solo chip,
diseñado por quien lo necesite,
con ARM en el centro.

<!-- S60 -->
ARM no tenía que ganarle a Intel
en los ordenadores personales.
Podía acabar dentro de cualquier cosa.

<!-- S61 -->
Y en los años noventa,
«cualquier cosa» significaba cada vez más
teléfonos móviles.

<!-- S62 -->
Un ordenador de sobremesa puede gastar
cien vatios y llevar un ventilador grande.
Un teléfono funciona con una batería
en tu bolsillo.

<!-- S63 -->
A finales de la década,
había núcleos ARM dentro
de algunos de los teléfonos más vendidos,
de Nokia y otros.

<!-- S64 -->
Luego llegó el iPod.
Luego, el smartphone.

<!-- S65 -->
De repente, miles de millones de personas llevaban
un ordenador que tenía que aguantar
todo el día con una batería.

<!-- S66 -->
Y el procesador que se creó
porque era barato
resultó ser justo
lo que ese mundo necesitaba.

<!-- S67 -->
Así que esa es la respuesta, ¿no?
ARM es sencillo,
sencillo significa eficiente,
y lo eficiente gana.

<!-- S68 -->
No exactamente.

<!-- S69 -->
Mira dentro de un núcleo ARM moderno de gama alta.

<!-- S70 -->
Cachés enormes.
Varias instrucciones a la vez.
Predicción de saltos:
adivinar por dónde irá el programa
antes de llegar ahí.

<!-- S71 -->
Ejecución fuera de orden:
ejecutar las instrucciones
en el orden que resulte más rápido.

<!-- S72 -->
Miles de millones de transistores en el chip.
No tiene nada de sencillo.

<!-- S73 -->
Entonces, ¿dónde quedó la sencillez?

<!-- S74 -->
El truco es que un procesador
en realidad son dos cosas distintas.

<!-- S75 -->
El conjunto de instrucciones es el idioma
que habla el software.
Qué instrucciones existen
y qué significan.

<!-- S76 -->
La microarquitectura es la máquina
que de verdad las ejecuta.

<!-- S77 -->
El idioma puede seguir siendo sencillo,
mientras la máquina que hay debajo
se vuelve enormemente complicada.

<!-- S78 -->
Y lo mismo pasó
en el otro bando.

<!-- S79 -->
Las instrucciones x86 de Intel
son famosas por lo complicadas que son.

<!-- S80 -->
Pero desde mediados de los noventa,
los procesadores de Intel y AMD
las descomponen por dentro
en operaciones pequeñas y sencillas.

<!-- S81 -->
Y luego las ejecutan en un motor
muy parecido al que hay
dentro de un núcleo ARM moderno.

<!-- S82 -->
Por debajo de las etiquetas,
los dos se han vuelto sorprendentemente parecidos.

<!-- S83 -->
Las instrucciones más limpias de ARM siguen ayudando.
Son más fáciles de decodificar,
lo que puede ahorrar un poco de energía.

<!-- S84 -->
Pero no son una ventaja mágica
que x86 nunca pudiera igualar.

<!-- S85 -->
Así que ARM no conquistó todo
por ser sencillo.
Y tampoco se diseñó para consumir poco.

<!-- S86 -->
Ganó porque coincidieron tres cosas.
Un diseño eficiente.
Un modelo de negocio
que permitía a cualquiera construir sobre ARM.
Y un mundo que de repente necesitaba
miles de millones de ordenadores con batería.

<!-- S87 -->
Y entonces, en 2020,
la historia volvió a Apple.

<!-- S88 -->
Apple había vendido su parte de ARM
años antes,
cuando necesitaba dinero con urgencia.

<!-- S89 -->
Ahora metió sus propios chips basados en ARM
en el Mac.

<!-- S90 -->
El mismo tipo de núcleos que en el iPhone,
ampliados para un ordenador.
Núcleos rápidos, núcleos eficientes,
gráficos y mucho más,
en un solo chip.

<!-- S91 -->
Eran más rápidos
que los chips de Intel a los que sustituyeron,
y los portátiles aguantaban mucho más
con una carga.

<!-- S92 -->
ARM ya no era
solo el procesador de los móviles.

<!-- S93 -->
Y ARM no se quedó ahí.
También entró en los centros de datos,
donde cada vatio cuesta dinero.
Amazon ahora diseña
sus propios chips ARM para servidores.

<!-- S95 -->
El primer chip ARM tenía unos
25.000 transistores.
Los de hoy tienen miles de millones.

<!-- S96 -->
Casi todo lo relativo a
cómo funcionan por dentro ha cambiado.

<!-- S98 -->
Un equipo pequeño quería
un procesador que de verdad pudiera construir.

<!-- S99 -->
No lo construyeron para los teléfonos,
ni para Apple,
ni para ganarle a Intel.

<!-- S100 -->
Y al final,
lo más importante que crearon
no fue el chip.

<!-- S101 -->
Fue una base sencilla
sobre la que todos los demás pudieran construir.
