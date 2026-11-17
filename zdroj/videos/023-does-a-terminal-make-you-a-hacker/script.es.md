<!-- S01 -->
Abres una terminal.
Alguien pasa por detrás.
Ve una pantalla negra
cubierta de texto misterioso.
Y de repente...

<!-- S02 -->
"¡Dios mío! ¡Estás hackeando!"

<!-- S03 -->
Bueno...
Puede ser.
O puede que solo estés intentando averiguar
por qué se ha caído el servidor.

<!-- S04 -->
Hoy vamos a ver por qué
las terminales y el hackeo se han vuelto
casi lo mismo en la cultura popular.
Y, más importante todavía...
qué aspecto tiene el hackeo de verdad.

<!-- S05 -->
Para la mayoría, un ordenador tiene botones.
Haces clic en algo.
Algo ocurre.
Y luego está la terminal.
Sin botones.
Sin mensajes amables.
Solo esto.
Y eso da miedo.

<!-- S06 -->
Una interfaz gráfica puede decir:
eliminar usuario.
Una terminal dice esto en su lugar.

<!-- S07 -->
Para un usuario de Linux con experiencia
eso es perfectamente corriente.
Para todos los demás parece
que vas a lanzar un misil.

<!-- S08 -->
En realidad hay una razón histórica
para que tenga ese aspecto.
Los primeros ordenadores no tenían interfaz gráfica.
Se hablaba con ellos por terminales de texto.

<!-- S09 -->
Y aquellas terminales tenían pantallas oscuras
con fósforo verde o ámbar.
No era un intento de parecer moderno.
Era simplemente cómo funcionaba la tecnología.

<!-- S10 -->
Pero entonces el cine y la televisión
notaron algo útil.
Una pantalla negra llena de
texto que cambia deprisa parece técnica.
Y, más importante todavía...
parece complicada.

<!-- S11 -->
No necesitas entender
qué significan los caracteres.
Simplemente ves esto.
Y tu cerebro decide:
esta persona está haciendo algo ilegal.

<!-- S12 -->
Hollywood ha desarrollado un lenguaje
notablemente uniforme para el hackeo.
El hacker está sentado en una habitación oscura.
Hay seis monitores.

<!-- S13 -->
La habitación se ilumina solo con los monitores.
Nadie ha encendido la luz.
El hacker empieza a teclear
a unas novecientas palabras por minuto.

<!-- S14 -->
El texto vuela por la pantalla.
Aparece una barra de progreso.
Noventa y siete por ciento.
Noventa y ocho.
Noventa y nueve.
Y por fin, cien.
El hacker se echa hacia atrás.
Y dice...

<!-- S15 -->
"Estoy dentro."

<!-- S16 -->
No es así como funcionan la mayoría
de los incidentes de seguridad.
Imaginemos la conversación real.
"Voy a hackear este servidor."
Y el servidor responde:
permission denied.

<!-- S17 -->
"Ah."
Lo intenta otra vez.
Permission denied.
Comprueba la contraseña.

<!-- S18 -->
Lee la documentación.
Busca el mensaje de error.
Al final descubre que el administrador
desactivó el acceso por contraseña hace medio año.

<!-- S19 -->
"Ya."

<!-- S20 -->
Los ordenadores son extraordinariamente buenos
haciéndote pasar veinte minutos para descubrir que
olvidaste un solo carácter en un archivo de configuración.

<!-- S21 -->
En un lado de la pantalla:
administrador de sistemas.
En el otro:
hacker.
Las mismas herramientas pueden aparecer en ambos.
Es porque la terminal
no es una herramienta de hackeo.
Es una interfaz.

<!-- S22 -->
Puedes usarla para llevar un servidor,
leer registros, copiar archivos, instalar programas,
o averiguar qué se rompió a las tres de la madrugada.

<!-- S23 -->
O, según lo que estés haciendo
y si tienes permiso,
puedes usarla para pruebas de seguridad.
O para un ataque.

<!-- S24 -->
La herramienta en sí no te dice
cuál de las dos cosas estás haciendo.
Un destornillador puede reparar un ordenador.
También puede destruirlo.
El destornillador no es el criminal.

<!-- S25 -->
Entonces, ¿qué es en realidad un hacker?
La palabra tiene una historia mucho más antigua
que la ciberdelincuencia moderna.

<!-- S26 -->
Originalmente, un hacker era alguien
a quien le gustaba explorar sistemas
y sabía encontrar soluciones inesperadas.

<!-- S27 -->
Con el tiempo, la palabra quedó ligada
a la seguridad informática.
Y hoy, cuando alguien dice
"es un hacker", puede referirse a

<!-- S28 -->
un investigador de seguridad,
un pentester,
un atacante de verdad,
o simplemente alguien que sabe
una cantidad inquietante sobre Linux.
Normalmente el contexto ayuda.

<!-- S29 -->
Volvamos a mirar nuestra imagen.
El texto dice:
lo has hackeado.
Y mirad sus pantallas.

<!-- S29b -->
En una, algo parecido a nmap.
En la otra, algo que parece
todavía más sospechoso.
Barra etc barra passwd.

<!-- S30 -->
Para alguien que no conoce Linux,
está claramente entrando en el Pentágono.
Para un administrador de sistemas, está revisando
la red y leyendo una lista de cuentas.

<!-- S31 -->
Y de ahí viene el chiste.
Puede que la mujer no esté hackeando nada.
Puede que simplemente esté haciendo su trabajo.

<!-- S32 -->
¿Y qué hace nmap en realidad?
Es una herramienta de descubrimiento de redes
y auditoría de seguridad.

<!-- S33 -->
En términos muy sencillos,
lo apuntas a una máquina y preguntas
qué está exponiendo
este ordenador a la red.

<!-- S34 -->
Puede decirte que ciertos puertos están abiertos.
Y los puertos corresponden a servicios de red.
Eso no es automáticamente un ataque.

<!-- S35 -->
Se parece más a mirar un edificio
y preguntar qué puertas están abiertas.
Si es tu edificio,
eso es administración normal.

<!-- S36 -->
Si es de otra persona
y estás buscando a propósito
una manera de entrar...

<!-- S37 -->
bueno, eso ya es otra cosa.

<!-- S38 -->
¿Y qué pasa con esa ruta?
Alguien podría pensar:
está leyendo el archivo de contraseñas.
Sí contiene información sobre las cuentas.

<!-- S39 -->
Pero en un sistema Linux moderno,
los hashes de las contraseñas están guardados en otro sitio.
Están en barra etc barra shadow,
que está mucho más restringido.

<!-- S40 -->
Así que ver ese archivo no es lo mismo
que descubrir las contraseñas de todos.
Hollywood, por supuesto,
lo haría mucho más dramático.

<!-- S41 -->
Un administrador de Linux diría:
es literalmente una lista de usuarios.

<!-- S42 -->
Otra escena clásica descifra una contraseña
en unos catorce segundos.
El descifrado real es más aburrido.
Tienes un hash, tienes un diccionario,
y dejas que el ordenador pruebe candidatos.

<!-- S43 -->
Quizá encuentre una en un minuto.
Quizá en una semana.
Quizá nunca.
Y mientras trabaja, el atacante
no está ahí sentado tecleando.
Igual se está comiendo un bocadillo.

<!-- S44 -->
Lo que me lleva a mi tradición
favorita de Hollywood.
Por lo visto los ordenadores no aceptan órdenes
si no las escribes rapidísimo.

<!-- S45 -->
Los programadores y administradores de verdad
no teclean sin parar.
Piensan.
Leen.
Se quedan mirando un error.

<!-- S46 -->
Luego descubren que alguien
lo resolvió hace once años.
Y entonces copian la solución.

<!-- S47 -->
Eso es la informática.

<!-- S48 -->
A veces lo más peligroso
que puedes escribir no es
una orden misteriosa de hackeo.
Es algo perfectamente legítimo.

<!-- S49 -->
El ejemplo famoso es este.

<!-- S50 -->
Lo cual es una historia estupenda,
salvo que un sistema moderno se niega.
Responde que operar de forma recursiva
sobre la barra es peligroso,
a menos que añadas una opción diciendo que lo dices en serio.

<!-- S51 -->
Las órdenes que de verdad destruyen cosas
son más aburridas.
Un borrado en el directorio equivocado.
Un disco escrito encima del disco equivocado.

<!-- S52 -->
De esas la terminal no te avisa,
porque por lo que ella puede ver
no pasa nada raro.
Solo puede preguntar: ¿estás completamente seguro?

<!-- S53 -->
Y si respondes que sí...
puede que te crea.

<!-- S54 -->
Y aquí está el mayor problema
del estereotipo de Hollywood.
Un ataque real puede no parecer
un hackeo en absoluto.

<!-- S55 -->
Puede ser una contraseña robada.
Phishing.
Un servidor sin parchear.
Una clave de API filtrada.
Una contraseña reutilizada de otro sitio.

<!-- S56 -->
El atacante puede que ni siquiera necesite
una terminal.
Puede que simplemente inicie sesión
en una interfaz web.
Usuario.
Contraseña.
Y ya está dentro.

<!-- S57 -->
Sin texto verde.
Sin gráficos estilo Matrix.
Sin música dramática.

<!-- S58 -->
Lo cual seguramente da mucho más miedo.

<!-- S59 -->
La gente imagina a un hacker como una sudadera,
una habitación oscura y un teclado que brilla.
Nada de eso tiene que ver con hackear.

<!-- S60 -->
La persona que va a tu lado en el tren,
con un portátil completamente corriente,
puede saber bastante más
sobre seguridad informática.

<!-- S61 -->
Y la persona que está sentada
delante de seis servidores
puede que solo esté intentando averiguar
por qué no arranca la base de datos.

<!-- S62 -->
Volvamos entonces a nuestra imagen original.
El hombre señala a la mujer.
Lo has hackeado.
¿Estaba hackeando?

<!-- S63 -->
Puede que sí.
Puede que no.

<!-- S64 -->
Tiene una terminal.
Tiene nmap.
Tiene una lista de cuentas.
Pero nada de eso demuestra
que haya hackeado nada.
Podría ser la administradora
o estar haciendo una auditoría de seguridad.

<!-- S65 -->
O podría estar hackeando de verdad.
No lo sabemos.
Y ahí está el chiste.

<!-- S66 -->
La verdadera diferencia entre
la administración normal y el hackeo
no es el color de tu terminal.
No es cuántos monitores tienes.

<!-- S67 -->
No es lo rápido que escribes.
Y desde luego no es
si llevas sudadera con capucha.
Es lo que estás haciendo
y si tienes permiso para hacerlo.

<!-- S68 -->
Así que la próxima vez que veas a alguien
mirando fijamente una pantalla negra
llena de texto misterioso,
no des por hecho que está hackeando.

<!-- S69 -->
Puede que solo esté arreglando el servidor.

<!-- S70 -->
Aunque...
si escribe novecientas palabras
por minuto mientras grita
"estoy dentro"...

<!-- S71 -->
quizá convenga preguntarle
qué está haciendo.
