<!-- S01 -->
En algún lugar de tu casa
quizá haya un reloj
que nadie ha puesto nunca en hora.

<!-- S02 -->
Sobrevive a los cortes de luz.
Se adapta al cambio de hora
él solo, en mitad de la noche.

<!-- S03 -->
No tiene conexión a internet.
Ni wifi, ni GPS,
ni una app en tu teléfono.

<!-- S04 -->
Solo tiene un diminuto receptor de radio.
Y una vez por segundo,
oye un único pulso.

<!-- S05 -->
Entonces, ¿cómo convierte un reloj
un pulso por segundo
en la hora exacta, la fecha
e incluso el día de la semana?

<!-- S06 -->
En Europa, esos pulsos llegan
de DCF77, cerca de Fráncfort.
En Norteamérica, de WWVB, en Colorado.
Emisoras distintas, la misma idea.

<!-- S07 -->
Tomemos la alemana.
Emite una onda de radio constante,
de día y de noche.
Y al comienzo de cada segundo,
la baja durante un instante.

<!-- S08 -->
El truco está en cuánto
dura esa bajada.

<!-- S09 -->
Una bajada de una décima de segundo
significa cero.
Una de dos décimas significa uno.

<!-- S10 -->
Esa es toda la idea.
Sin paquetes, sin red.
Solo una onda de radio que baja
durante un rato corto, o uno más largo.

<!-- S11 -->
Un bit cada segundo.
Eso significa que haría falta un minuto entero
para enviar solo 60 bits.

<!-- S12 -->
Y, de hecho, envía solo 59.

<!-- S13 -->
En el último segundo de cada minuto,
la onda no baja en absoluto.
Y esa bajada que falta
es la parte más importante
de toda la señal.

<!-- S14 -->
Porque cuando llega la siguiente bajada,
el reloj sabe
que acaba de empezar un minuto nuevo.

<!-- S15 -->
El hueco funciona como un punto.
Todo lo que hay entre dos huecos
es una frase completa.

<!-- S16 -->
Entonces, ¿qué cabe en una frase
de 59 bits?

<!-- S17 -->
El minuto. La hora.
El día del mes, el día de la semana,
el mes y el año.

<!-- S18 -->
La mayoría de los números se envían cifra a cifra.
47 minutos
no se envían como 47.
Se envían como dos cifras separadas,
un cuatro y un siete.

<!-- S19 -->
Cuatro bits bastan para cualquier cifra
del cero al nueve.
Las decenas de minutos nunca pasan de cinco,
así que les bastan tres.

<!-- S20 -->
Y el año recibe solo dos cifras.
Para la emisora,
2026 es simplemente 26.
El siglo lo pone el propio reloj.

<!-- S21 -->
Pero la radio no es un canal limpio.
Un motor, un cargador de teléfono,
una bombilla LED barata...
cualquiera de ellos puede emborronar una bajada.

<!-- S22 -->
Por eso, después de cada bloque de números
viene un bit extra, llamado bit de paridad.

<!-- S23 -->
Se elige de modo que el número de unos
del bloque siempre salga par.

<!-- S24 -->
Si una interferencia invierte un solo bit,
la cuenta sale impar,
y el reloj sabe
que algo ha ido mal.

<!-- S25 -->
Pero si se invierten dos bits,
la cuenta vuelve a ser par,
y el error se cuela.

<!-- S26 -->
Por eso muchos relojes
no se fían de un solo minuto.
Esperan a otro válido.

<!-- S27 -->
Y por eso ponerse en hora
puede llevar varios minutos,
y en un mal día, mucho más.

<!-- S28 -->
Lo que deja un problema curioso.

<!-- S29 -->
El reloj pasa un minuto entero
recogiendo la hora de las 10:48.
Pero mientras recoge ese mensaje,
todavía son las 10:47.

<!-- S30 -->
Entonces, ¿cuándo cambia de verdad?

<!-- S31 -->
Porque el mensaje es un aviso.
Dice qué hora será
cuando empiece el siguiente minuto.

<!-- S32 -->
El reloj lee la frase entera,
deja pasar la bajada que falta,
y cuando llega la siguiente bajada,
esa bajada es el momento exacto.

<!-- S33 -->
Los bits le dicen al reloj qué hora es.
La bajada le dice cuándo.

<!-- S34 -->
Pero la frase tiene algunas palabras más
aparte de la hora.

<!-- S35 -->
Dos bits indican si Alemania
está en horario de invierno o de verano.

<!-- S36 -->
Y un tercero es un aviso.
Durante toda la hora anterior al cambio de hora,
se pone a uno.

<!-- S37 -->
Así que tu reloj no necesita saber
qué domingo de marzo
se adelantan los relojes,
ni qué domingo de octubre se atrasan.
Nadie le enseñó nunca la regla.
Simplemente se lo dicen con una hora de antelación.

<!-- S38 -->
Si algún día Europa deja de cambiar la hora,
el aviso simplemente no volverá a llegar.

<!-- S39 -->
Otro bit avisaba antes de un segundo intercalar,
un segundo extra que se añadía de vez en cuando,
porque la rotación de la Tierra
no lleva un ritmo perfecto.
Ese minuto podía tener 61 segundos.

<!-- S40 -->
El último se añadió
a finales de 2016.
Pero en octubre de 2026,
las autoridades de metrología del mundo
decidieron acabar con los segundos intercalares.
A partir del 20 de mayo de 2027,
el UTC correrá de forma continua.

<!-- S41 -->
Y los primeros 14 bits
de cada minuto
no tienen nada que ver con la hora.

<!-- S42 -->
Desde 2006 también se usan
para transmitir previsiones meteorológicas cifradas,
para estaciones meteorológicas compatibles.

<!-- S43 -->
Así que la señal que pone en hora tu despertador
también podía decirle
a la estación meteorológica de otra persona
si iba a llover el jueves.

<!-- S44 -->
Y, sin embargo, la mayoría de estos relojes
no escuchan todo el tiempo.
Escuchar gasta batería,
así que muchos lo intentan una vez por noche,
de madrugada.

<!-- S45 -->
Las ondas largas llegan a un reloj por dos caminos:
por el suelo
y rebotando en la alta atmósfera.
Al anochecer, ese camino superior cambia,
y la señal a menudo llega más lejos.

<!-- S46 -->
Y a las tres de la madrugada,
suele haber menos máquinas, cargadores y luces
funcionando cerca que la tapen.

<!-- S47 -->
Entre esas comprobaciones,
el reloj funciona con un cristal de cuarzo,
que puede desviarse más o menos un segundo al día.

<!-- S48 -->
En la siguiente comprobación con éxito,
la radio corrige esa desviación.

<!-- S49 -->
Hasta el lugar donde escucha importa.
La antena es una pequeña varilla de ferrita
envuelta en hilo.

<!-- S50 -->
Recibe mejor cuando la varilla queda perpendicular
a la dirección de la emisora,
no cuando apunta hacia ella.
Gira el reloj,
y una señal débil puede desaparecer por completo.

<!-- S51 -->
Por eso un reloj funciona en una estantería,
y el mismo reloj, dos metros más allá,
detrás de un muro de hormigón armado, no se pone nunca en hora.

<!-- S52 -->
Entonces, ¿de dónde saca la emisora
su hora?

<!-- S53 -->
Del PTB,
el instituto nacional de metrología de Alemania,
que tiene relojes atómicos.

<!-- S54 -->
El propio segundo se define
mediante átomos de cesio.
Un segundo son exactamente
9 192 631 770 oscilaciones
de la radiación que emiten.

<!-- S55 -->
Así que un despertador barato en la mesilla
está, literalmente,
siguiendo un patrón de tiempo
definido por átomos de cesio.

<!-- S56 -->
Aunque no a la perfección.
La señal viaja a la velocidad de la luz,
e incluso así tarda unos 3 milisegundos
por cada 1000 kilómetros.

<!-- S57 -->
El receptor añade un retraso propio,
y tu reloj no corrige nada de eso.
No le hace falta.
Solo muestra segundos.

<!-- S58 -->
Desde un único punto cerca de Fráncfort,
la señal llega a relojes
situados hasta a unos 2000 kilómetros.
Eso es la mayor parte de Europa.

<!-- S59 -->
Suiza tenía su propia emisora,
llamada HBG, hasta finales de 2011.
Había que sustituir sus antenas,
la usaba demasiado poca gente,
y los relojes suizos podían simplemente escuchar
a Alemania en su lugar.

<!-- S60 -->
Otros conservaron la suya.
Reino Unido, Francia, Japón y China
tienen todos la suya propia.

<!-- S61 -->
Y en Norteamérica, WWVB
emite desde Fort Collins desde 1963,
con código horario desde 1965.

<!-- S62 -->
Mismo principio, distinto dialecto.
Un cero es una bajada de dos décimas de segundo.
Un uno dura medio segundo.

<!-- S63 -->
Y en lugar de un hueco por minuto,
cada 10 segundos llega una marca más larga,
como comas en la frase.
Dos seguidas indican un minuto nuevo.

<!-- S64 -->
La mayor diferencia
es qué hora envía.
Alemania emite la hora oficial de Europa Central,
compartida por gran parte del continente.

<!-- S65 -->
Pero Estados Unidos
abarca varias zonas horarias.
Así que WWVB envía la hora universal, el UTC,
y tú le dices al reloj dónde estás.

<!-- S66 -->
Ni siquiera envía el mes.
Solo el día del año,
del 1 al 366.

<!-- S67 -->
Ninguna de estas emisoras
habla el mismo idioma.
Un reloj hecho para Alemania
no entiende a Colorado.

<!-- S68 -->
Pero a ambos lados del Atlántico,
es la misma rutina silenciosa.
Noche tras noche, un pequeño receptor
se sincroniza con un patrón de tiempo atómico,
a cientos o miles de kilómetros.

<!-- S69 -->
Así que aquí va una pregunta.
Si todas las señales horarias de radio
desaparecieran esta noche,
¿te darías cuenta siquiera?
Cuéntamelo en los comentarios.
