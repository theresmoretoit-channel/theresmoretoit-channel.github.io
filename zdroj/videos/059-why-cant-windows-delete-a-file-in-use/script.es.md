<!-- S01 -->
Intentas borrar un archivo.
El ordenador dice que está abierto
en otro programa.
Pero no dice en cuál.

<!-- S02 -->
Ese mensaje es el extremo visible
de una pregunta mucho más rara.
¿Qué significa en realidad
abrir un archivo?

<!-- S03 -->
Porque en otro ordenador
el mismo archivo, abierto igual,
se borra sin una sola queja.

<!-- S04 -->
El mismo archivo.
La misma acción.
Dos respuestas completamente distintas.

<!-- S05 -->
Empecemos por lo
que molesta a todo el mundo.
¿Qué programa?

<!-- S06 -->
Windows lo sabe.
Tiene un objeto del núcleo
para ese archivo abierto
y sabe qué proceso es su dueño.
Podría decir su nombre.

<!-- S07 -->
Así que cierras cosas al azar.
Abres el Administrador de tareas.
Miras una lista de procesos
y casi no reconoces ninguno.

<!-- S08 -->
Y durante años
la respuesta fue de verdad
descargar una herramienta aparte.
Unlocker salió en 2005,
y en Windows XP esa era la respuesta.

<!-- S09 -->
Luego Windows 7 trajo
el Monitor de recursos.
La pestaña CPU.
Una lista llamada Identificadores asociados.

<!-- S10 -->
Escribe el nombre del archivo.
Te da el programa
y el identificador del proceso.
Nada que instalar.
Está ahí desde 2009.

<!-- S10b -->
Pero las herramientas aparte hacían
más que solo decírtelo.
Podían cerrar el identificador
y soltar el archivo.

<!-- S11 -->
Lo que nos devuelve
a la pregunta.
¿Qué consiguió ese programa
al abrir el archivo?

<!-- S12 -->
Digamos que un reproductor abre
un archivo llamado movie.mp4.
En Windows, abrir un archivo
implica especificar dos cosas.

<!-- S13 -->
La primera es obvia.
¿Qué quiero hacer con él?
Leerlo. Escribir en él.

<!-- S14 -->
La segunda es la interesante.
¿Qué pueden hacer los demás
mientras yo lo tengo abierto?

<!-- S15 -->
Es un ajuste de verdad.
Dices lo que otros programas
pueden hacer mientras lo tienes.

<!-- S16 -->
Pueden leerlo.
También pueden escribir en él.
Pueden borrarlo o renombrarlo.

<!-- S16b -->
O nada en absoluto.
Nadie lo toca
mientras yo lo esté usando.

<!-- S17 -->
El indicador que permite borrar
se llama FILE_SHARE_DELETE.
Y la documentación de Microsoft
añade una línea debajo.

<!-- S18 -->
El permiso de borrado abarca
borrar y renombrar a la vez.

<!-- S19 -->
Así que un programa que niega
el uso compartido para borrar
ha bloqueado también el renombrado.

<!-- S20 -->
Y si el programa que abrió el archivo
no lo concedió,
ningún otro programa puede obtenerlo.

<!-- S21 -->
Por eso el error
no se llama archivo en uso.
Se llama violación de uso compartido.

<!-- S22 -->
La respuesta estuvo todo el tiempo
en el nombre
del propio error.

<!-- S23 -->
Ahora lo mismo
en una máquina Linux.
Un reproductor abre el vídeo.

<!-- S24 -->
Y escribes
rm movie.mp4.

<!-- S24b -->
Funciona.
El vídeo sigue reproduciéndose.

<!-- S25 -->
¿Qué consiguió entonces ese programa,
si no algún control sobre el archivo?

<!-- S26 -->
De esto trata
todo el vídeo.
El nombre no es el archivo.

<!-- S27 -->
movie.mp4 es una línea
en un directorio.
Esa línea apunta a un objeto
que guarda los datos reales.

<!-- S28 -->
Cuando un programa abre el archivo,
lo que obtiene es una referencia
al objeto.
No a la línea.

<!-- S29 -->
Borrar el archivo
elimina entonces la línea.
El objeto queda intacto.

<!-- S30 -->
La página del manual lo dice
en una sola frase.
El archivo seguirá existiendo
hasta que se cierre el último
descriptor que lo referencia.

<!-- S31 -->
Suena abstracto
hasta que uno lo ve pasar.
Así que hice un archivo de registro
de quinientos megabytes
y dejé un proceso con el archivo abierto.

<!-- S31b -->
Luego lo borré.

<!-- S32 -->
El listado del directorio
no muestra absolutamente nada.
La herramienta que mide
el tamaño de la carpeta dice cero.

<!-- S33 -->
Y la herramienta que mide
el espacio libre del disco
dice que quinientos megabytes
siguen faltando.

<!-- S33b -->
Una carpeta vacía.
Medio gigabyte desaparecido.

<!-- S34 -->
Pasa lo bastante a menudo
como para que haya un comando
solo para encontrar archivos así.
Borrados, invisibles, aún en el disco.

<!-- S35 -->
Y el espacio vuelve
en el momento en que ese proceso
suelta el archivo.

<!-- S36 -->
La misma lógica vale al renombrar.
Mueve el archivo mientras está abierto,
y el programa ni se entera.

<!-- S37 -->
El manual también es tajante ahí.
Los descriptores de archivo abiertos
para la ruta anterior no se ven afectados.

<!-- S37b -->
Nunca estuvo usando el nombre.

<!-- S38 -->
Lo cual tiene un límite
que conviene conocer.
Un programa en ejecución
no se puede sobrescribir directamente.

<!-- S38b -->
Linux se niega.
Text file busy.

<!-- S39 -->
Lo que sí puedes hacer
es quitarle el nombre
y poner un archivo nuevo en su lugar.

<!-- S40 -->
El proceso anterior sigue ejecutándose
a partir de un objeto
que ya no tiene nombre.
Lo que se inicie después usa el nuevo.

<!-- S41 -->
Que es otra vez la misma idea,
demostrándose a sí misma.
Muchas cosas se pueden reemplazar
sin tocar el objeto en su sitio.

<!-- S41b -->
Por eso Linux puede actualizar
un programa mientras se ejecuta.
Solo que no tienes la versión nueva
hasta que lo reinicias.

<!-- S42 -->
¿Es entonces Windows
simplemente peor diseñado?

<!-- S42b -->
No.
Y esta es la parte
que casi nadie conoce.

<!-- S43 -->
Windows tiene una forma
de hacer exactamente lo mismo.

<!-- S43b -->
En NTFS, Windows puede solicitar
una eliminación con semántica POSIX.

<!-- S44 -->
Microsoft describe
lo que pasa entonces.
El nombre se retira
del espacio de nombres visible.

<!-- S45 -->
Y las aplicaciones que ya tenían
el archivo abierto pueden seguir usándolo,
aunque el nombre
con el que lo abrieron ya no esté.

<!-- S46 -->
Ese es el comportamiento de Unix.
En NTFS.
Documentado por Microsoft.

<!-- S47 -->
Ambos sistemas saben hacer las dos cosas.
Lo que cambia es lo predeterminado.
Lo que obtienes al abrir un archivo
sin pensar en ello.

<!-- S48 -->
En Windows obtienes un contrato.
En Unix obtienes una referencia
a un objeto.

<!-- S49 -->
Lo que suena a pregunta
para programadores,
hasta que uno ha visto
este mensaje en concreto.

<!-- S50 -->
Reinicia el ordenador
para terminar de instalar las actualizaciones.

<!-- S51 -->
Supongamos que Windows debe sustituir
una biblioteca que un proceso
tiene abierta bajo esas reglas estrictas.

<!-- S52 -->
No puede cambiar el archivo
por debajo de ese proceso.
Así que algo tiene que soltarlo.

<!-- S53 -->
Cerrar la aplicación.
Detener el servicio.
O dejarle todo el trabajo
al Administrador de reinicio.

<!-- S54 -->
Que es un componente real.
Apaga las cosas por orden.
Las aplicaciones de Windows,
luego los programas de consola,

<!-- S55 -->
luego los servicios,
y el Explorador al final.
Después vuelve a arrancarlos.

<!-- S56 -->
Y existe por una sola razón,
que Microsoft dice sin rodeos
en su propia documentación.

<!-- S57 -->
La razón principal
por la que las instalaciones
y las actualizaciones exigen
reiniciar el sistema...

<!-- S58 -->
es que algunos de los archivos
que se actualizan están en uso
por una aplicación
o un servicio en ejecución.

<!-- S59 -->
Sería demasiado redondo acabar ahí.
Las reglas de uso compartido no son la única
razón por la que un ordenador pide reiniciar.

<!-- S60 -->
Actualizar el núcleo es otra cosa.
El núcleo no se puede cambiar
por debajo de sí mismo.

<!-- S61 -->
Linux tiene el mismo problema,
aunque el parcheo en caliente
a veces evita el reinicio.

<!-- S62 -->
Así que la versión honesta
afirma menos que
la versión satisfactoria.

<!-- S63 -->
Cómo trata Windows los archivos
en uso hizo que algunos componentes
fueran más difíciles de cambiar en marcha,
y eso contribuyó.

<!-- S64 -->
Porque toda decisión de diseño
tiene una consecuencia en alguna parte.

<!-- S65 -->
Windows deja que el programa
que abre un archivo decida
qué pueden hacer los demás con él.

<!-- S66 -->
El precio es que a veces
no puedes borrar tu propio archivo,
porque otro programa
no lo ha permitido.

<!-- S67 -->
Unix mantiene el nombre
y el objeto separados,
así que mucho se puede reemplazar
mientras el sistema funciona.

<!-- S68 -->
El precio es medio gigabyte
que desapareció del disco
y no pertenece a ningún archivo.

<!-- S69 -->
Y fíjate en cómo se resuelve
cada uno de los dos.
En Windows, una salida es
cerrar el programa
que tiene el archivo.

<!-- S70 -->
En Linux, una forma
de recuperar ese espacio
es reiniciar el servicio
que todavía lo tiene abierto.

<!-- S71 -->
Causas distintas.
A veces el mismo remedio.

<!-- S71b -->
Por cierto, si quieres ver
adónde nos lleva la próxima pregunta,
plantéate suscribirte.
Ayuda mucho al canal.

<!-- S72 -->
Bien. La pregunta del principio.
¿Qué significa
abrir un archivo?

<!-- S73 -->
Significa que sostienes algo.
Los dos sistemas simplemente te dan
cosas distintas que sostener.

<!-- S74 -->
Por eso ese mensaje
nunca dijo en realidad
que el archivo no se puede borrar.

<!-- S75 -->
Dijo que el programa
que lo abrió
no te dio permiso.

<!-- S75b -->
Y sí sabe cuál es.
Simplemente no lo mencionó.
