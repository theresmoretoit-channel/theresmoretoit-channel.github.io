# Internet Explorer 6 — Los errores que tenían nombre

<!-- S01 -->
Esta es la segunda parte.

Si no has visto la primera,
el enlace está abajo.

De todos modos te doy el resumen.

<!-- S02 -->
En 2001
Microsoft lanzó
Internet Explorer 6,
y llegó con Windows XP.

En un par de años
tenía más del noventa por ciento
del mercado de navegadores.

<!-- S03 -->
Microsoft usó eso
para convertir el navegador
en una plataforma de aplicaciones.

Era una idea de verdad.

Solo que la pagaron
los desarrolladores web.

<!-- S04 -->
Esa fue la primera parte.

Pero dejé algo fuera.

Dejé fuera la parte
donde los errores tenían nombre.

<!-- S05 -->
Un error de navegador normalmente
es un número en un gestor de incidencias.

Issue 4172.

Nadie lo recuerda.

Nadie habla de él en la comida.

<!-- S06 -->
En Internet Explorer 6
los errores tenían nombres propios.

Y resulta que eso es
lo más revelador
de toda aquella época.

<!-- S07 -->
Empecemos por uno suave.

Flotas una imagen a la izquierda
y pones un párrafo al lado.

El texto debería quedar
justo pegado a la imagen.

En vez de eso queda
a tres píxeles.

<!-- S08 -->
No cuatro.

<!-- S08b -->
No dos.

<!-- S08c -->
Tres.

<!-- S08d -->
Siempre.

Tenía nombre.

The Three Pixel Jog.

<!-- S09 -->
Ahora flota esa imagen a la izquierda
y dale un margen izquierdo
de diez píxeles.

Internet Explorer 6
le da veinte.

Duplica el margen,
pero solo en el lado
hacia el que la flotaste.

<!-- S10 -->
The Double Margin Bug.

Y el arreglo aceptado
era declarar
un elemento flotante como inline.

<!-- S11 -->
Lo cual no tiene sentido.

Un flotante es un bloque.

Llamarlo inline
no significa absolutamente nada.

Funcionaba, así que se escribía.

<!-- S12 -->
El siguiente es mejor.

Cargas una página,
y parte del contenido
sencillamente no está.

Bajas.

Vuelves a subir.

Y aparece.

<!-- S13 -->
No se cargó nada.

No cambió nada.

Solo era tímido.

Y tenía el nombre correcto.

The Peekaboo Bug.

<!-- S14 -->
El remedio era decirle
al elemento que faltaba
que su posición era relativa.

Nadie supo explicar del todo
por qué eso lo devolvía.

<!-- S15 -->
Luego está aquel
en el que pasas por encima de un enlace
y el fondo
de la caja de abajo
queda cortado en línea recta.

The Guillotine Bug.

<!-- S16 -->
Había un error donde el texto
se alejaba de donde lo habías puesto.

Magic Creeping Text.

Había otro donde los bordes
salían en el sitio equivocado,
del color equivocado,
o no salían.

Border Chaos.

<!-- S17 -->
Mi favorito es más silencioso.

Colocas una fila de cajas,
y letras de la última
reaparecen debajo.

No siempre.

No de forma predecible.

The Duplicate Character Bug.

<!-- S18 -->
Y lo que decidía
si te tocaba a ti,
y cuántas letras
salían duplicadas,
era el número de comentarios HTML
que habías dejado en el código.

Comentarios.

Lo único del archivo
que el navegador
debe tirar.

<!-- S19 -->
Hay uno más,
y es distinto,
porque este la gente
lo usaba a propósito.

Si fijas una altura
y el contenido es más alto,
la caja debería desbordarse.

Internet Explorer 6
agrandaba la caja.

<!-- S20 -->
Lo cual está mal.

Y es también exactamente
lo que hace una altura mínima.

E Internet Explorer 6
no tenía altura mínima.

Así que los desarrolladores dejaron
de reportar ese error
y empezaron a depender de él.

<!-- S21 -->
Para y mira esa lista.

The Three Pixel Jog.

The Double Margin Bug.

Peekaboo.

The Guillotine.

A un error que te encuentras una vez
no le pones nombre.

<!-- S22 -->
Estos tenían nombre
porque se los encontraba todo el mundo.

Y aquí viene la parte
que lo empeora.

La mayoría tenía
la misma causa debajo.

<!-- S23 -->
Dentro de Internet Explorer 6,
cada elemento tenía
o no tenía
algo llamado layout.

<!-- S24 -->
Decidía si el elemento
fijaba su tamaño y su posición,
o se lo dejaba a su padre.

Y no se podía activar.

<!-- S25 -->
No existía ninguna propiedad
llamada layout,
ni forma de pedirla.

No estaba en ninguna especificación.

Era una bandera interna
del motor de renderizado.

<!-- S26 -->
Pero podías activarla
sin querer.

Poner un ancho lo hacía.

Poner una altura lo hacía.

Flotar un elemento lo hacía.

Así que la mitad de los arreglos de este vídeo
era gente accionando un interruptor
que no podía ver.

<!-- S27 -->
Por eso se buscó
la manera más barata
de accionarlo a propósito.

Una era poner una altura
del uno por ciento.

<!-- S28 -->
Había que mantener a todos
los demás navegadores lejos de eso,
así que fue dentro de un truco
al que llegaremos en un minuto.

<!-- S29 -->
Y en Internet Explorer 6
no hacía daño,
porque una altura en la que no cabe
es una altura que rebasa igualmente.

El error de hace dos minutos
es lo que hace seguro el arreglo.

<!-- S30 -->
Tenía nombre.

The Holly Hack.

<!-- S31 -->
La otra manera
era una propiedad de Microsoft
llamada zoom, puesta a uno.

Zoom uno significa
no hagas zoom.

<!-- S32 -->
No cambiaba nada que pudieras ver.

De eso se trataba.

Estaba en las hojas de estilo
únicamente para poner
una bandera invisible
que hacía desaparecer los errores.

<!-- S33 -->
Lo que nos lleva a los trucos,
y es con los trucos
donde esto se pone raro.

Para arreglar un navegador
primero tienes que poder hablarle
solo a ese.

<!-- S34 -->
E Internet Explorer 6
se comportaba como si hubiera
otro elemento
por encima del elemento html.

Ningún otro navegador lo hacía.

No estaba documentado.

Simplemente actuaba así.

<!-- S35 -->
Así que escribías una regla
que coincidía con el fantasma,
y solo ese navegador
podía verla.

Asterisco, espacio, html.

<!-- S36 -->
Todos los demás navegadores la miraban,
no encontraban nada que coincidiera,
y seguían.

Ese es el star hack,
y durante años estuvo
en casi todas las hojas de estilo
de la web.

<!-- S37 -->
También estaba
el underscore hack.

Pones un guion bajo
delante de un nombre de propiedad.

<!-- S38 -->
Un navegador que cumple los estándares
tira la línea
por inválida.

Internet Explorer 6
ignora el guion bajo
y la aplica.

<!-- S39 -->
Así que rompías a propósito
tu propia hoja de estilo,
y la rotura
era la instrucción.

<!-- S40 -->
Y luego está el que
Microsoft construyó a propósito.

Podías escribir un comentario
que solo obedecía Internet Explorer.

<!-- S41 -->
Para todos los demás navegadores
era un comentario corriente,
ignorado como se ignoran los comentarios.

Para Internet Explorer 6
era una puerta
a una segunda versión
de la página.

<!-- S42 -->
Lo que significa que el fabricante
miró la situación,
estuvo de acuerdo en que este navegador
necesitaba su propia hoja de estilo,
y entregó una función
para hacerlo más fácil.

<!-- S43 -->
Parte del daño
no necesitaba ningún error.

Internet Explorer 6
tenía dos modos.

En el moderno
seguía el estándar.

<!-- S44 -->
En el antiguo,
el ancho de una caja
incluía su relleno
y su borde,
que es un número
completamente distinto.

<!-- S45 -->
Qué modo te tocaba
dependía de la primera línea
del documento.

Y la versión de HTML
a la que todos se movían
te decía que pusieras
una declaración XML ahí arriba.

<!-- S46 -->
Esa línea empujaba
a Internet Explorer 6
al modo antiguo.

Lo que lo rompía
era seguir el estándar más nuevo.

<!-- S47 -->
Luego está la transparencia.

Internet Explorer 6 no sabía
mostrar un PNG con bordes suaves.

Donde la imagen debía desvanecerse,
ponía gris.

<!-- S48 -->
La respuesta de Microsoft fue un filtro
con nombre de número de serie.

Funcionaba.

<!-- S49 -->
Pero pintaba fuera
del proceso de renderizado
normal del navegador,
así que los enlaces que ponías encima
solían dejar de funcionar.

Arreglabas la imagen
y rompías el enlace.

<!-- S50 -->
Y desvanecer cualquier otra cosa
era un segundo filtro,
con su propia sintaxis,
puesto en la hoja de estilo
justo al lado de la propiedad corriente
que entendían todos los demás navegadores.

<!-- S51 -->
Parte de esto es más antiguo
que los errores mismos.

Antes de todo eso,
las maquetaciones se construían
con tablas anidadas.

<!-- S52 -->
Y para mantener un hueco abierto
usabas una imagen transparente
de un píxel,
estirada al tamaño
que el hueco necesitara.

Eso también tenía nombre.

The spacer gif.

<!-- S53 -->
El hover era otra.

En Internet Explorer 6
el hover funcionaba en los enlaces.

Solo en los enlaces.

<!-- S54 -->
Así que un menú que se abría
cuando movías el ratón
sobre cualquier otra cosa
necesitaba un pequeño programa
enganchado a la hoja de estilo.

<!-- S55 -->
No un script en la página.

Un archivo aparte,
referenciado desde el CSS,
con código cuyo trabajo
era enseñarle al navegador
un solo selector.

Ese archivo se lo pasó la gente
durante años.

<!-- S56 -->
La primera parte mencionó
que se podía meter JavaScript
dentro de una hoja de estilo.

Lo que no mencionó
es con qué frecuencia se ejecutaba.

<!-- S57 -->
En cada movimiento del ratón.

En cada tecla.

En cada desplazamiento.

Una y otra vez,
para calcular un ancho.

<!-- S58 -->
Y el navegador tenía techos
que no tenía nadie más.

Una hoja de estilo dejaba de aplicarse
en algún punto pasadas
las cuatro mil reglas.

Todo lo que venía después
de la hoja de estilo treinta y uno
de una página se ignoraba.

<!-- S59 -->
Lo que suena a un número
al que nunca llegas,
hasta que tu sitio es tan grande
que alguien tiene que escribir
un paso de compilación cuyo único trabajo
es fusionar hojas de estilo
antes de que el navegador las vea.

<!-- S60 -->
Y parte de esto no era
nada cosmético.

Internet Explorer 6
contaba sus objetos de página
y sus objetos de script
de dos maneras distintas,
y ninguno de los dos lados
veía el bucle entero.

<!-- S61 -->
Así que si un script apuntaba
a una parte de la página,
y esa parte de la página
apuntaba de vuelta al script,
ninguno se liberaba nunca.

Deja esa ventana abierta bastante rato
y el navegador se comía la máquina.

<!-- S62 -->
Pero el mejor
no es un error de maquetación.

Escribes una etiqueta input.

Le das un tipo.

Y olvidas el signo igual.

<!-- S63 -->
Eso es un atributo mal formado.

Todo analizador jamás escrito
tiene una respuesta para eso.

Ignóralo.

Adivina qué se quiso decir.

Sigue adelante.

<!-- S64 -->
Internet Explorer se caía.

Por dentro quería saber
si el campo estaba oculto,
así que comparaba lo que habías escrito
con la palabra hidden.

No habías escrito nada.

<!-- S65 -->
Así que fue a buscar
lo que no habías escrito
a la dirección cero.

Lo cual sería
una caída de navegador corriente,
salvo que el código que lo hacía
no estaba en el navegador.

<!-- S66 -->
Estaba en una biblioteca compartida del sistema.

Así que esas tres palabras
tumbaban también el cliente de correo,
y el panel de vista previa
del gestor de archivos.

<!-- S67 -->
Una ventana con la lista de archivos
de tu propia máquina,
cerrada por una página web.

Ese es el argumento de la primera parte
llegando como informe de fallo.

El navegador no era un programa
que corría sobre el sistema.

Era parte del sistema.

<!-- S68 -->
Y no podías simplemente
probar el arreglo en otro sitio.

Internet Explorer estaba soldado
al sistema operativo,
así que un ordenador
ejecutaba exactamente una versión.

<!-- S69 -->
Por eso un puesto de front-end
en 2006
venía con una estantería
de máquinas de repuesto.

<!-- S70 -->
Y más tarde con una carpeta
de máquinas virtuales,
cada una cargando un sistema
operativo entero
para que una sola página
pudiera abrirse dentro.

<!-- S71 -->
Y entonces alguien hizo
lo evidente.

Si puedes enseñarle al navegador
una característica que le falta,
puedes enseñárselas todas.

<!-- S72 -->
Un desarrollador llamado Dean Edwards
escribió una biblioteca
cuyo único propósito
era hacer que Internet Explorer 6
se comportara como una versión
posterior de sí mismo.

La gente puso eso en marcha.

En producción.

<!-- S73 -->
Y ahí es donde deja
de tener gracia.

Durante casi una década,
una parte seria
del trabajo de front-end del mundo
se fue en los fallos de un navegador.

No en funciones.

No en productos.

En compensación.

<!-- S74 -->
Y duró por
aquello de lo que iba la primera parte.

Había empresas que habían construido
aplicaciones de verdad sobre él,
de las que solo corrían allí,
y esas aplicaciones
tenían que seguir funcionando el lunes.

<!-- S75 -->
Así que el navegador del que todos
querían deshacerse
era el que nadie
tenía permitido quitar.

<!-- S76 -->
En 2010,
Google anunció que sus propias
aplicaciones dejarían de funcionar en él.

Y un estudio de diseño de Denver
decidió que eso merecía un funeral.

<!-- S77 -->
Uno de verdad.

Un ataúd.

Un panegírico.

Entre ochenta y cien personas
vinieron a ver cómo se enterraba
un navegador.

Habían contado con treinta.

<!-- S78 -->
Y Microsoft mandó flores.

La tarjeta decía:
gracias por los buenos ratos,
Internet Explorer 6.

<!-- S79 -->
Un año después, día por día,
Microsoft lanzó una web.

Seguía cuánto del mundo
seguía usando
Internet Explorer 6,
país por país.

<!-- S80 -->
En ese momento
todavía era el doce por ciento.

El objetivo era bajarlo
por debajo del uno.

La empresa que construyó el navegador
llevaba una cuenta atrás pública
hasta la muerte de su propio producto.

<!-- S81 -->
Entonces, ¿por qué tenían nombre los errores?

Porque le pones nombre a lo que
no puedes rodear.

<!-- S82 -->
Nadie le pone nombre al tiempo
de un país
por el que solo pasa.

Se lo pones donde vives.

Y durante unos diez años,
ahí es donde vivía la web.

<!-- S83 -->
Pero sacar Internet Explorer 6
de la web es otra historia.

Y ahí es adonde vamos después.

Si la quieres,
hay un botón de suscripción,
y la primera parte está enlazada abajo.
