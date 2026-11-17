# Internet Explorer 6 — El navegador que se convirtió en plataforma

Traducción de `script.md`. Mismas marcas de escena, mismo número de líneas.
Una línea = una frase = un subtítulo.

<!-- S01 -->
Imagina que eres desarrollador web
a principios de los dos mil.

Has escrito
una página web perfectamente razonable.

<!-- S02 -->
Funciona en Netscape.

Funciona en Opera.

Funciona en el nuevo Firefox.

Y entonces la abres
en Internet Explorer.

Todo está roto.

<!-- S03 -->
La maquetación está mal.

Los botones se han movido.

Las imágenes PNG se ven fatal.

Y de algún modo,
un solo salto de línea en tu HTML
ha creado un hueco de tres píxeles.

<!-- S04 -->
Bienvenido al desarrollo web
en la era de Internet Explorer 6.

Pero aquí viene lo interesante.

Internet Explorer 6
no era simplemente un mal navegador.

<!-- S05 -->
Microsoft intentaba resolver problemas
que la web tenía de verdad.

Solo que tenía una ventaja enorme
sobre todos los demás.

Windows.

<!-- S06 -->
Y al final esa ventaja
le permitió convertir el navegador
en algo mucho más grande
que un navegador.

<!-- S07 -->
A mediados de los años noventa,
la web estaba dominada
por Netscape Navigator.

A Microsoft eso no le gustaba.

<!-- S08 -->
Así que Internet Explorer
se incluyó con Windows
y se ofreció gratis.

Comprabas un ordenador con Windows.

Internet Explorer ya estaba ahí.

Nada que descargar.

Nada que pagar.

<!-- S09 -->
Y lo más importante:
Microsoft controlaba
el sistema operativo.

Poco después del año 2000,
Internet Explorer tenía
más del noventa por ciento
del mercado de navegadores.

<!-- S10 -->
Internet Explorer 6 llegó
en 2001,
junto con Windows XP.

Y durante un tiempo pareció
que Microsoft había ganado
la guerra de los navegadores.

<!-- S11 -->
Microsoft tenía un problema.

La web era enormemente limitada.

HTML podía mostrar documentos.

CSS podía darles estilo.

JavaScript podía hacerlos interactivos.

<!-- S12 -->
Y poco más.

Cualquier cosa más complicada
chocaba de frente
con los límites del navegador.

<!-- S13 -->
¿Y si querías escanear un documento?

¿O comunicarte con una tarjeta inteligente?

¿O hablar con algún
componente del hardware de Windows?

<!-- S14 -->
El navegador no podía
hacer nada de eso.

Así que Microsoft propuso una solución.

ActiveX.

<!-- S15 -->
La idea básica era simple.

¿Por qué limitar una aplicación web
a lo que el navegador sabe hacer?

Déjala usar
componentes nativos de Windows.

<!-- S16 -->
Y de pronto una página web
podía hacer cosas
con las que el HTML corriente
ni siquiera podía soñar.

<!-- S17 -->
Hoy ActiveX suena aterrador.

Y con razón.

Un componente ActiveX podía llegar
a los archivos, a las aplicaciones,
al hardware
y al sistema operativo.

<!-- S18 -->
Desde la seguridad de hoy,
eso suena absolutamente demencial.

Pero a principios de los dos mil
tenía todo el sentido
para las aplicaciones corporativas.

<!-- S19 -->
Las empresas no querían
un bonito visor de documentos.

Querían aplicaciones.

Querían páginas web
que se comportaran
casi como programas de escritorio.

<!-- S20 -->
Y Microsoft les dio exactamente eso.

Hasta el propio Windows Update
se basaba al principio en ActiveX
para inspeccionar el sistema
y averiguar qué actualizaciones
hacían falta.

<!-- S21 -->
Así que ActiveX no fue simplemente
un error estúpido.

Fue un intento temprano
de convertir el navegador
en una plataforma de aplicaciones.

<!-- S22 -->
Y en ese sentido, Microsoft
iba de verdad por delante de su tiempo.

El problema era cuánto poder
le dio a esa plataforma.

<!-- S23 -->
ActiveX no era
la única extensión de Microsoft.

Estaba VBScript.

Estaba DHTML.

Y hasta CSS expression.

Sí.

<!-- S24 -->
Internet Explorer podía evaluar
JavaScript directamente dentro del CSS.

Se podía escribir algo así.

<!-- S25 -->
Era ridículo.

Y a veces también
sorprendentemente útil.

Y nada de eso tenía garantizado
funcionar en ningún otro sitio.

<!-- S26 -->
Microsoft no estaba simplemente
implementando la web.

Microsoft estaba extendiendo la web
en su propia dirección.

Y con el noventa por ciento
del mercado
tenía poder suficiente
para salirse con la suya.

<!-- S27 -->
Uno de los ejemplos más famosos
fue el modelo de caja de CSS.

El modelo estándar decía
que si un elemento
medía 200 píxeles de ancho,
con 20 píxeles de relleno
y 5 píxeles de borde,

<!-- S28 -->
el ancho total
era de 250 píxeles.

<!-- S29 -->
Las versiones antiguas de Internet Explorer
lo leían de otra manera.

En modo quirks, el ancho declarado
podía incluir el relleno
y el borde.

<!-- S30 -->
No era necesariamente
una forma demencial de pensar el ancho.

De hecho, hoy pedimos a menudo
ese mismo comportamiento a propósito.

Se llama border-box.

<!-- S31 -->
El problema de verdad era
que los distintos navegadores
se comportaban de forma distinta.

Y eso significaba
que al desarrollador tenía que importarle.

Mucho.

<!-- S32 -->
Existía algo llamado hasLayout.

No era una propiedad normal de CSS.

No formaba parte del estándar.

Pero decidía
cómo Internet Explorer
colocaba los elementos.

<!-- S33 -->
Y a veces una maquetación rota
se arreglaba misteriosamente
añadiendo una sola línea.

zoom: 1

¿Por qué?

Porque zoom: 1 podía activar
el mecanismo interno hasLayout.

<!-- S34 -->
Había problemas
con la transparencia de los PNG.

Había problemas con los elementos select,
que aparecían por encima
de menús posicionados de forma absoluta,
por muy alto
que pusieras el z-index.

<!-- S35 -->
El desarrollo web no consistía solo
en implementar tu diseño.

Consistía en aprenderte los fallos
de un motor de navegador concreto.

<!-- S36 -->
Otro ejemplo maravilloso.

Los espacios en blanco.

Y de este Internet Explorer
ni siquiera tenía la culpa.

Podías poner dos imágenes
justo una al lado de la otra
en el marcado,
sin nada entre las etiquetas,
y obtener un resultado.

<!-- S37 -->
Luego alguien formateaba bien el HTML
y ponía cada etiqueta en su propia línea.

Y de pronto aparecía
un hueco de unos píxeles entre las imágenes.

El salto de línea pasaba a significar algo.

<!-- S38 -->
Tu formateador de código
podía romperte literalmente la página.

Y si usabas
una versión antigua de Visual Studio,
te formateaba el HTML
encantado, él solo.

Gracias, Microsoft.

<!-- S39 -->
Los desarrolladores acumularon
toda una caja de herramientas de apaños.

Comentarios condicionales.

<!-- S40 -->
Y a veces HTML
de aspecto completamente disparatado
cuyo único propósito era
que Internet Explorer se portara bien.

<!-- S41 -->
No escribías código feo
por ser mal programador.

Escribías código feo
porque el navegador te obligaba.

<!-- S42 -->
Internet Explorer también se colgaba
de forma espectacular, y a menudo se llevaba
por delante todas las ventanas abiertas.

<!-- S43 -->
Lo que dio lugar a una categoría estupenda
de entretenimiento de oficina.

Oye, mira este enlace.

Y veinte ventanas de Internet Explorer
desaparecen.

<!-- S44 -->
Esta era la web antes de que
los navegadores tuvieran aislamiento.

El navegador de hoy dice esto.

Este sitio no es de fiar.

Lo voy a aislar.

<!-- S45 -->
Internet Explorer 6
sonaba más bien así.

¿Eres una página web?

Claro.

Aquí tienes las llaves del edificio.

<!-- S46 -->
¿Por qué usaban los desarrolladores
estos apaños?

Porque no les quedaba otra.

<!-- S47 -->
Imagina una empresa
con quinientos empleados.

En cada ordenador corre Windows XP.

En cada uno está Internet Explorer.

<!-- S48 -->
El desarrollador tiene dos opciones.

Opción uno.

Hacerlo para Internet Explorer,
que ya tiene todo el mundo.

<!-- S49 -->
Opción dos.

Hacerlo para todos los navegadores,
probarlo todo en todas partes
y explicarle al departamento de informática
por qué todos necesitan un segundo.

La respuesta solía ser obvia.

<!-- S50 -->
No elegían
tecnología de Microsoft
porque amaran a Microsoft.

Elegían lo que resolvía
el problema del cliente.

Y a veces ActiveX
era la mejor herramienta disponible.

<!-- S51 -->
Y al final alguien se hartó.

Las bibliotecas de JavaScript empezaron
a esconder las diferencias entre navegadores.

Una de las más importantes
fue jQuery.

<!-- S52 -->
En vez de escribir
manejo de eventos específico por navegador,
podías escribir una sola línea
que funcionaba en todas partes.

<!-- S53 -->
En vez de pelearte a mano
con distintas implementaciones de AJAX,
usabas una abstracción común.

<!-- S54 -->
jQuery no hizo
desaparecer a Internet Explorer.

Pero hizo mucho más fácil
fingir que no existía.

Y para los desarrolladores web de la época,
eso era una maravilla.

<!-- S55 -->
Apareció Firefox.

Opera siguió desarrollándose.

Llegó Safari.

Y al final Google lanzó Chrome.

<!-- S56 -->
La guerra de los navegadores volvió,
y esta vez
la competencia era distinta.

Los motores de JavaScript
mejoraron muchísimo.

Llegó HTML5.

<!-- S57 -->
El propio navegador empezó a aprender
todo aquello para lo que antes
hacían falta complementos.

<!-- S58 -->
Vídeo.

Audio.

Canvas.

SVG.

WebGL.

WebSockets.

Y al final WebRTC.

La web se estaba convirtiendo
en una plataforma de aplicaciones.

<!-- S59 -->
Que era exactamente
lo que Microsoft había intentado
conseguir con ActiveX.

Solo que ahora ocurría
a través de estándares abiertos.

<!-- S60 -->
Microsoft lo intentó una vez más.

Silverlight permitía crear
aplicaciones ricas en el navegador
con C# y .NET.

Incluso el primer streaming
de Netflix funcionaba con él.

<!-- S61 -->
Pero la web no quería complementos para siempre.

Apple se negó a admitir Flash
en el iPhone.

Y de pronto el futuro no era esto.

Navegador más complemento.

Era esto.

El navegador en sí.

<!-- S62 -->
Silverlight desapareció.

Flash desapareció.

ActiveX desapareció.

Y al final desapareció
también Internet Explorer.

<!-- S63 -->
Y aquí es donde
la historia se pone interesante.

Porque Microsoft
no se equivocaba del todo.

Había predicho correctamente
que el navegador se convertiría
en una plataforma de aplicaciones.

<!-- S64 -->
Solo que intentaba llegar allí
con tecnologías propietarias.

La web llegó al mismo destino
con estándares.

<!-- S65 -->
El navegador ganó.

Pero ganó convirtiéndose
en algo mucho más potente
que el navegador
de 2001.

<!-- S66 -->
¿Era Microsoft entonces el villano?

En realidad no.

Y eso es lo que hace
la historia más interesante.

<!-- S67 -->
Microsoft tenía ingenieros brillantes.

Tenía recursos enormes.

Y construyó muchas tecnologías
que iban de verdad por delante de su tiempo.

<!-- S68 -->
Pero Microsoft tenía además
una posición de mercado aplastante.

Y eso creó
un incentivo peligroso.

<!-- S69 -->
Si casi todo el mundo
usa tu navegador,
¿para qué esperar a los estándares?

¿Por qué no implementar
directamente tu propia solución?

Durante un tiempo funcionó.

Hasta que el resto de la web le alcanzó.

<!-- S70 -->
Hoy Internet Explorer ya no está.

Las viejas guerras de navegadores
parecen historia antigua.

Pero mira
el mercado de navegadores actual.

Chrome.

Edge.

Opera.

Brave.

Vivaldi.

<!-- S71 -->
Y muchos más
están basados en Chromium.

Productos distintos.

A menudo el mismo
motor por debajo.

<!-- S72 -->
Así que quizá hayamos cambiado esto.

Un navegador al que todos tenían que atender.

Por esto.

Un motor sobre el que todos construyen.

¿No te suena de algo?

<!-- S73 -->
Porque un motor dominante
no decide solo
cómo se muestran las páginas.

<!-- S74 -->
Influye en lo que construyen los desarrolladores.

En qué tecnologías se popularizan.

Y en última instancia,
en qué acaba siendo la propia web.

<!-- S75 -->
Hay, sin embargo,
una diferencia muy importante.

La web de hoy se apoya
en estándares abiertos.

Firefox sigue teniendo su propio motor.

Safari tiene WebKit.

Chromium es de código abierto.

<!-- S76 -->
Y los navegadores modernos
se actualizan solos.

No estamos ni de lejos
en la situación
de 2003.

<!-- S77 -->
Pero la pregunta de fondo sigue ahí.

¿Cuánta influencia
debería tener una sola empresa
sobre una plataforma
que usa casi todo el mundo?

Esa es la pregunta
que nunca llegó a desaparecer.

<!-- S78 -->
Entonces, ¿era Internet Explorer 6 terrible?

Sí.

A veces espectacularmente terrible.

<!-- S79 -->
Pero esa no es toda la historia.

También era un producto de su época.

<!-- S80 -->
El problema era
que Microsoft había ganado
las guerras de navegadores tan del todo
que podía dictar las reglas.

<!-- S81 -->
Y lo pagaron los desarrolladores web.

Aprendieron los misterios
de hasLayout.

Descubrieron que zoom: 1
arreglaba cosas por arte de magia.

Y rezaron.

<!-- S82 -->
Y al final Internet Explorer
se convirtió en aquello que llevaba
veinte años construyendo.

Una plataforma heredada
que ya nadie quería
seguir manteniendo.

<!-- S83 -->
La web no rechazó
la visión de Microsoft.

Simplemente construyó
una versión mejor de ella.

Y si aquella época
debe enseñarnos una cosa,
es esta.

<!-- S84 -->
Una tecnología no se convierte en estándar
solo porque sea buena.

<!-- S85 -->
A veces se convierte en estándar
porque una empresa tiene poder suficiente
para que la use todo el mundo.

<!-- S86 -->
Y a veces,
veinte años después,
nos damos cuenta de que lo hemos vuelto a hacer.
