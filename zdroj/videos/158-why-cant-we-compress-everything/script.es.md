<!-- S01 -->
Aquí están todos los guiones
que se han escrito para este canal.
158 vídeos,
casi un millón y medio de bytes de texto.

<!-- S02 -->
Pásalos por un compresor corriente
llamado gzip.
Salen con poco más de medio megabyte.
Casi dos tercios menos.

<!-- S03 -->
Y no se pierde nada.
Descomprime el archivo
y todos los guiones vuelven,
letra por letra.

<!-- S04 -->
Ahora comprímelo otra vez.

<!-- S05 -->
Se hace más grande.
98 bytes más grande.

<!-- S06 -->
Una tercera vez.
98 bytes más grande.
Una cuarta.
Otra vez 98.

<!-- S07 -->
La primera pasada elimina dos tercios.
La segunda no encuentra nada de nada.
Entonces, ¿por qué no podemos seguir comprimiendo?

<!-- S08 -->
Veamos qué hay dentro de ese segundo archivo.
gzip no comprimió nada.
Copió los datos sin cambiar nada,
en dieciséis bloques.

<!-- S09 -->
Cada bloque recibió una etiqueta de cinco bytes.
Súmale una pequeña cabecera y un pie,
y te sale exactamente 98.

<!-- S10 -->
Cuando un compresor no encuentra nada que quitar,
guarda los datos tal como están
y añade solo lo que necesita para deshacerlo.

<!-- S11 -->
Entonces, ¿por qué la segunda pasada no encontró nada?
¿Y lo encontraría un programa más listo?

<!-- S12 -->
Un texto así está lleno de repeticiones.
Las mismas palabras, las mismas frases,
las mismas pequeñas marcas de escena
al principio de cada escena.

<!-- S13 -->
En 1977, Jacob Ziv y Abraham Lempel
publicaron un truco sencillo.
No vuelvas a escribir lo repetido.
Señala dónde estaba antes.

<!-- S14 -->
Retrocede 300 caracteres
y copia los doce siguientes.
Unos pocos bytes en lugar de doce.

<!-- S15 -->
El segundo truco:
dar códigos cortos a las letras frecuentes
y códigos largos a las raras.

<!-- S16 -->
En 1951, David Huffman,
estudiante de posgrado en el MIT,
podía hacer el examen final
o escribir un trabajo en su lugar.

<!-- S17 -->
El trabajo, propuesto por Robert Fano,
consistía en encontrar el código más eficiente
de exactamente este tipo.

<!-- S18 -->
Durante meses, Huffman no avanzó nada.
Se rindió
y se puso a estudiar para el examen.
Entonces se le ocurrió.

<!-- S19 -->
Toma los dos símbolos más raros,
únelos en uno solo
y repite hasta que quede un único árbol.

<!-- S20 -->
Más tarde lo llamó
«el momento más singular de mi vida».

<!-- S21 -->
Fano no le había dicho a la clase
que él mismo se había atascado con eso,
y Claude Shannon también.

<!-- S22 -->
El código de Huffman superó los métodos de ambos.
Y se puede demostrar
que ningún código de su tipo lo hace mejor.

<!-- S23 -->
A principios de los años 90,
Phil Katz juntó los dos trucos
para los archivos ZIP.
gzip usa el mismo método.

<!-- S24 -->
La primera pasada ya agotó
los patrones que gzip sabe encontrar.

<!-- S25 -->
Lo que queda no le da nada con lo que trabajar.
Para gzip, parece ruido.

<!-- S26 -->
Pero un programa más listo
podría ver patrones que a gzip se le escaparon.
¿Podría algún programa, algún día,
reducir cualquier cosa que le des?

<!-- S27 -->
No.
Y no hace falta saber cómo funciona
para estar seguro de ello.

<!-- S28 -->
Toma todos los archivos
de exactamente tres bits.
Hay ocho.

<!-- S29 -->
Ahora cuenta todos los más cortos.
Cuatro archivos de dos bits,
dos de un bit
y un archivo vacío.

<!-- S30 -->
Siete.

<!-- S30b -->
Ocho archivos y siete sitios más cortos
donde meterlos.

<!-- S31 -->
Si todos se acortaran,
dos tendrían que compartir sitio.
Y al descomprimir,
¿a cuál te referías?

<!-- S32 -->
Se llama principio del palomar
y se cumple para cualquier longitud.
Siempre falta un archivo más corto
para que quepan todos.

<!-- S33 -->
Así que cualquier compresor que acepte cualquier archivo
y reduzca algunos
tiene que agrandar otros.
No porque esté mal escrito.
Es que no tienen otro sitio adonde ir.

<!-- S34 -->
Esos 98 bytes
son el precio que paga gzip.

<!-- S35 -->
Elige el compresor que quieras.
De todos los archivos de un tamaño dado,
puede reducir en un solo byte menos de uno
de cada 250.

<!-- S36 -->
Aun así, la compresión funciona,
porque los archivos que creamos no son aleatorios.
Son textos, imágenes y programas,
llenos de patrones.

<!-- S37 -->
Eso no ha impedido que haya gente
que prometa más.

<!-- S38 -->
En 1992, WEB Technologies
anunció un software capaz de comprimir
casi cualquier dato por debajo de un kilobyte.
Incluso su propio resultado,
una y otra vez.

<!-- S39 -->
Su vicepresidente dijo que el método
«no estaba sujeto a las leyes
de la teoría de la información».
El producto nunca salió al mercado.

<!-- S40 -->
Entonces, ¿cómo es que las fotos y la música
se quedan tan pequeñas?
Es que no siguen esta regla para nada.

<!-- S41 -->
Un JPEG no vuelve idéntico.
Vuelve lo bastante parecido.
El detalle que tu ojo no echará de menos
se tira para siempre.

<!-- S42 -->
Haz zoom
y verás adónde fue a parar.

<!-- S43 -->
Eso es compresión con pérdida,
y es otro juego.
Este vídeo va del otro tipo.
Cada bit recuperado, tal cual.

<!-- S44 -->
Entonces, con los archivos que sí tienen patrones,
¿hasta dónde pueden reducirse?
¿Hay un mínimo?

<!-- S45 -->
Lo hay.
Se descubrió en 1948,
en el mismo artículo en el que se basa nuestro vídeo
sobre códigos correctores de errores.

<!-- S46 -->
Allí, Claude Shannon mostró
cómo añadir redundancia protege un mensaje.
Aquí, calculó
cuánta se puede quitar.

<!-- S47 -->
Su respuesta fue un número
que llamó entropía:
lo difícil que es adivinar
lo que viene después.

<!-- S48 -->
Ningún código sin pérdida puede bajar de ese número
de media.
Pero puedes acercarte a él
tanto como quieras.

<!-- S49 -->
Entonces, ¿cómo de impredecible es el inglés?
En 1951, Shannon lo midió
con un juego.

<!-- S50 -->
Le dio a alguien un pasaje
que nunca había visto
y le pidió que lo adivinara,
letra por letra.

<!-- S51 -->
Si fallaba,
volvía a intentarlo
hasta acertar.

<!-- S52 -->
Resultó que a la gente se le da muy bien.
Con cien letras de contexto,
el inglés salía a un bit, más o menos,
por letra.

<!-- S53 -->
Un ordenador guarda cada letra
en ocho bits.
Un lector humano necesita más o menos uno.

<!-- S54 -->
En esa diferencia es donde trabaja la compresión.
gzip dejó los guiones del canal
en menos de tres bits por carácter.

<!-- S55 -->
Entonces, ¿cuánto puede acercarse
una máquina a un bit?

<!-- S56 -->
Hay un premio justo para eso.
Se llama Hutter Prize,
y desde 2020, el reto es comprimir un solo archivo:
un gigabyte de la Wikipedia en inglés.

<!-- S57 -->
gzip lo reduce a un tercio.
Los mejores compresores de uso diario,
a más o menos un quinto.

<!-- S58 -->
El récord, de julio de 2026,
es de poco más de 100 millones de bytes.
Una décima parte.

<!-- S59 -->
Y el descompresor también cuenta.
Su tamaño se suma al total,
así que no puedes esconder la Wikipedia
dentro del programa.

<!-- S60 -->
El fondo es de 500.000 euros.
Cada 1 % de mejora
se premia con 5000.

<!-- S61 -->
Marcus Hutter, que lo financia, explica por qué:
«saber comprimir bien
está estrechamente relacionado
con actuar de forma inteligente».

<!-- S62 -->
Porque los programas que van en cabeza
no buscan repeticiones.
Predicen.

<!-- S63 -->
Antes de cada carácter,
estiman lo probable que es
cada uno de los posibles siguientes.
Una buena predicción cuesta una fracción de bit.

<!-- S64 -->
Es el juego de adivinar de Shannon,
jugado por una máquina.
Los mejores jugadores usan ahora redes neuronales,
entrenadas para predecir lo que viene después.

<!-- S65 -->
Funciona incluso con archivos ya comprimidos.
En 2016, Dropbox empezó a reempaquetar
los JPEG de sus usuarios con un mejor predictor.
De media, más de un quinto más pequeños.

<!-- S66 -->
Todos los archivos volvían bit a bit,
y para 2017
había ahorrado más de 46 petabytes.
Eso es más de 46.000 terabytes.

<!-- S67 -->
Y luego están los gigantes.
En 2023, investigadores de DeepMind
usaron un gran modelo de lenguaje
como compresor.

<!-- S68 -->
En pequeños recortes de fotos en escala de grises,
superó a PNG:
48 % del tamaño original
frente a 58.

<!-- S69 -->
En grabaciones de textos leídos en voz alta,
superó a FLAC:
21 % frente a 30.

<!-- S70 -->
Pero eso es sin contar el modelo.
Suma su tamaño
y el resultado sale
140 veces
más grande que los datos.

<!-- S71 -->
Un compresor más grande que sus datos
no ha ahorrado nada.
El programa forma parte de la descripción.

<!-- S72 -->
Y eso nos lleva a la parte más extraña.
Aquí está el primer millón de dígitos de pi.

<!-- S73 -->
Dáselos a cuatro compresores.
El mejor los deja en unos
426.000 bytes.

<!-- S74 -->
Ahora dales a esos mismos compresores
un millón de dígitos aleatorios.
El mismo resultado,
con menos de un 0,1 % de diferencia.

<!-- S75 -->
Pero pi no sale del azar.
Sigue una regla matemática.
Aquí tienes un programa que imprime
todo ese millón de dígitos, uno por uno.

<!-- S76 -->
362 bytes.
Más de 2000 veces más corto que el archivo.

<!-- S77 -->
Los compresores no podían ver
la regla matemática detrás de pi.
Solo veían los dígitos.

<!-- S78 -->
Una forma de medir la información
de unos datos es preguntarse:
¿cómo de corto puede ser un programa
que aún los imprima?

<!-- S79 -->
Esa longitud se llama
complejidad de Kolmogórov,
por uno de los hombres que la describieron.

<!-- S80 -->
La mayoría de los datos no tiene un programa corto.
Es otra vez el principio del palomar:
no hay suficientes programas cortos
para todos.

<!-- S81 -->
Un millón de dígitos aleatorios
muy probablemente no tiene nada más corto.
Pi sí.

<!-- S82 -->
Entonces, ¿por qué no encontrar sin más
el programa más corto para cualquier archivo?
Porque está demostrado
que ningún algoritmo puede hacerlo
para todos los archivos.

<!-- S83 -->
Cada programa te da un límite superior.
Pero nada puede decirte siempre
si existe uno más corto.
Nunca sabes si has llegado al mínimo.

<!-- S84 -->
gzip encontró las repeticiones en los guiones,
y nada más.
Ve bytes,
no lo que significan las palabras.

<!-- S85 -->
Para ir más allá, un programa
tiene que predecirlas mejor.
Y predecir bien un texto
empieza a parecerse mucho a entenderlo.

<!-- S86 -->
Así que aquí va una pregunta para ti.
Si un programa pudiera comprimir la Wikipedia
más que cualquier otro programa,
¿dirías que la entiende?
Deja tu respuesta en los comentarios.
