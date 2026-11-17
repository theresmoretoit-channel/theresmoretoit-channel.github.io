<!-- S01 -->
Te compras un disco nuevo.
Un terabyte, completamente vacío.
Antes de que pueda guardar un solo archivo,
primero hay que formatearlo.

<!-- S02 -->
Así que lo formateas con ext4,
el sistema de archivos estándar
de muchos ordenadores con Linux.
Con la configuración predeterminada,
antes de que hayas guardado nada,
ya han desaparecido unos diecisiete gigabytes.

<!-- S03 -->
Todavía no se ha guardado nada.
Ni fotos, ni documentos.
Entonces, ¿qué ocupa todo ese espacio?

<!-- S04 -->
¿Y por qué hay que formatear un disco
en primer lugar?
Ya puede almacenar datos.
Puede leer y escribir billones de bits.

<!-- S05 -->
¿Por qué el ordenador no empieza a escribir sin más
donde haya sitio?

<!-- S06 -->
Porque guardar datos
y volver a encontrarlos
son dos problemas muy distintos.

<!-- S07 -->
Imagina una oficina que reparte
hojas en blanco en lugar de formularios.
Todo queda apuntado en algún sitio...
y nadie encuentra nada.

<!-- S08 -->
Un disco sin sistema de archivos
es ese montón de papeles.
Pero una imagen mejor
es un cuaderno.

<!-- S09 -->
Imagina un cuaderno
de mil páginas
y unas cuantas reglas para usarlo.

<!-- S10 -->
Primero, cada página tiene un número.
Así, cada sitio del cuaderno
tiene una dirección.
La página cuatrocientos doce
señala un único lugar.

<!-- S11 -->
Segundo, las primeras páginas
son un índice.
Cada entrada da un nombre
y la página donde está.
Tortitas: página doce.

<!-- S12 -->
Tercero, al final del todo,
hay una lista de las páginas
que siguen en blanco.

<!-- S13 -->
Ahora añade una receta.
Buscas al final una página en blanco.
Escribes ahí la receta.
Añades una línea al índice.
Y tachas esa página
de la lista de páginas en blanco.

<!-- S14 -->
Una receta, tres sitios.
Y los tres tienen que coincidir.

<!-- S15 -->
Luego la receta de tortitas crece.
La página doce está llena,
y la trece ya está ocupada.
Así que sigue en la página ochenta y siete,
y el índice tiene que indicarlo.

<!-- S16 -->
Y aquí está la trampa.
Si quieres sitio para mil entradas
en el índice,
tienes que reservar esas páginas
antes de escribir una sola receta.

<!-- S17 -->
Hasta aquí la analogía.
Esto es lo que hay de verdad en el disco.

<!-- S18 -->
Un disco no sabe nada de archivos,
carpetas ni nombres.
Lo único que ofrece es una larga fila
de casillas numeradas, llamadas sectores.

<!-- S19 -->
En un disco duro,
los datos están en platos que giran.
Un SSD los guarda en memoria flash.
En ambos casos, el ordenador solo pide
un sector por su número,
y el disco averigua dónde está.

<!-- S20 -->
Un sector es pequeño.
Normalmente 512 bytes,
o 4096
en los discos más nuevos.

<!-- S21 -->
Los sistemas de archivos suelen trabajar
con trozos más grandes, llamados bloques.
En ext4, un bloque son cuatro kilobytes,
el tamaño de ocho sectores de los de antes.

<!-- S22 -->
Esos bloques numerados
son las páginas del cuaderno.
Lo que aún le falta al sistema de archivos
son las otras dos partes:
un índice
y una lista de lo que está libre.

<!-- S23 -->
Eso es lo que construye el formateo.
Y ahí es adonde
fueron esos diecisiete gigabytes.

<!-- S24 -->
Ext4 reserva un registro
para cada archivo y carpeta
que el disco podrá contener a la vez.
Cada registro ocupa
256 bytes.
Se llama inodo.

<!-- S25 -->
Algún día, cada inodo dirá
cuánto ocupa un archivo,
cuándo se modificó,
quién puede abrirlo
y qué bloques guardan su contenido.

<!-- S26 -->
En un disco de un terabyte,
ext4 prepara unos
sesenta y un millones.
Todos vacíos, todos esperando.
Son casi dieciséis gigabytes
de registros en blanco.

<!-- S27 -->
¿Por qué sesenta y un millones?
Ext4 hace una suposición sencilla:
un inodo por cada dieciséis kilobytes
de espacio en el disco.
En un ordenador normal,
la mayoría de esos registros
nunca se usarán.

<!-- S28 -->
Más o menos otro gigabyte
se va en un diario (journal),
del que hablaremos luego.
El resto es más contabilidad,
incluido un mapa con un bit por bloque
que dice si está usado o libre.

<!-- S29 -->
Y ese número también es fijo.
Gasta todos los registros
con millones de archivos diminutos,
y el disco te dirá que está lleno...
aunque le queden gigabytes libres.

<!-- S30 -->
Así que veámoslo en acción.
Vamos a crear un archivo llamado hello.txt.
Dentro, una sola palabra: hello.
Cinco letras. Cinco bytes.

<!-- S31 -->
El sistema de archivos elige un inodo vacío.
Digamos el número trece.
Luego busca un bloque libre en el mapa
y lo marca como usado.

<!-- S32 -->
Escribe los cinco bytes en ese bloque.
Luego rellena el inodo:
cinco bytes de largo, creado ahora mismo
y guardado en ese único bloque.

<!-- S33 -->
Y por último, en la carpeta,
añade una línea:
el nombre hello.txt
y el número trece.

<!-- S34 -->
Fíjate dónde acabó el nombre.
No en el archivo.
No en el inodo.
El nombre vive en la carpeta,
que en realidad no es más que una lista
de nombres y números.

<!-- S35 -->
Y una carpeta es solo otro archivo.
Lo único especial es que contiene
esa lista.

<!-- S36 -->
Por eso también mover un archivo
a otra carpeta del mismo sistema de archivos
es instantáneo, por grande que sea.
Una carpeta pierde una línea,
la otra gana una,
y normalmente el contenido
no se mueve en absoluto.

<!-- S37 -->
Cinco bytes de texto...
y en el disco ocupa
4096.
Un bloque es la pieza más pequeña
que reparte el sistema de archivos,
así que hasta un archivo diminuto cuesta un bloque entero.

<!-- S38 -->
Cuando el archivo ya no cabe en su bloque,
el sistema de archivos busca otro libre.
Quizá justo al lado.
Quizá en un sitio totalmente distinto.
Y el inodo lleva la cuenta de los dos.

<!-- S39 -->
Con el tiempo, un archivo grande puede acabar
en trozos repartidos por todo el disco.
Un disco duro tiene que saltar de uno a otro.
Un SSD lo lleva mucho mejor.

<!-- S40 -->
El programa que guardó el archivo
no sabe nada de esto.
Dijo «guarda hello.txt»,
y todo lo demás pasó entre bastidores.

<!-- S41 -->
Ahora bórralo.
El nombre desaparece de la carpeta.
El inodo se marca como libre.
El bloque vuelve a la lista de bloques libres.

<!-- S42 -->
En un disco duro tradicional,
los cinco bytes en sí se quedan donde están.
Nadie los ha tocado.
Siguen ahí hasta que algo nuevo
se escribe encima.

<!-- S43 -->
Por eso un archivo borrado
a veces se puede recuperar.
Borrar normalmente no elimina
el contenido.
Solo marca el espacio como disponible.

<!-- S44 -->
En un SSD, es menos seguro.
El sistema de archivos puede decirle al disco
que esos bloques ya no hacen falta,
y el disco puede descartar lo que contienen.
Después de eso, recuperar el archivo
es mucho menos probable.

<!-- S45 -->
Así que un sistema de archivos es, en el fondo, un contable.
Crear este único archivo
supuso actualizar tres cosas:
la carpeta, el inodo
y el mapa de bloques libres.

<!-- S46 -->
Ahora corta la corriente
justo cuando se está guardando un archivo.

<!-- S47 -->
Quizá el bloque se marcó como usado,
pero aún no hay ningún inodo que apunte a él.
Ese espacio simplemente se pierde.
Molesto, pero inofensivo.

<!-- S48 -->
O quizá el inodo apunta a un bloque
que el mapa todavía da por libre.
El siguiente archivo puede escribirse
justo encima.
Y el primero queda destruido sin hacer ruido.

<!-- S49 -->
Por eso ext4 lleva un diario.
Antes de cambiar su contabilidad,
anota lo que está a punto de hacer.
Tras un fallo, repite solo los cambios
que había terminado de anotar
y marcado como completos.
Lo que quedó a medias se ignora.

<!-- S50 -->
Y hay un problema más silencioso.
A veces un disco cambia un bit
y no se lo dice a nadie.

<!-- S51 -->
Ext4 protege sus propios registros
con sumas de verificación,
así que ahí puede detectar daños.
¿Pero el contenido de tus archivos?
De eso, simplemente se fía.

<!-- S52 -->
Algunos sistemas de archivos comprueban ambas cosas.
Y algunos guardan una segunda copia,
así que, cuando una copia se daña,
pueden repararla a partir de la otra.
Detectar un problema y arreglarlo
no es lo mismo.

<!-- S53 -->
Así que todos los sistemas de archivos hacen el mismo trabajo:
bloques numerados, una lista de nombres
y un mapa de lo que está libre.

<!-- S54 -->
Pero cada uno decide distinto.
Ext4 prepara sesenta y un millones de registros
antes de que guardes nada.
NTFS, en Windows, guarda sus registros
en una gran tabla que crece sobre la marcha.

<!-- S55 -->
Y Btrfs no prepara
una tabla fija de inodos por adelantado.
Los crea a medida que llegan archivos.
Y normalmente no sobrescribe
los datos en su sitio.
Escribe una copia nueva,
y solo entonces libera la antigua.

<!-- S56 -->
Por defecto, también calcula sumas de verificación de tus archivos,
para saber cuándo se han dañado.

<!-- S57 -->
Y como la copia antigua
no se sobrescribe,
una instantánea puede mantenerla viva.
Eso cambia la respuesta
a casi todas las preguntas de este vídeo:
qué pasa tras un fallo,
qué significa borrar
e incluso qué es una copia.

<!-- S58 -->
Ahí es donde empieza el próximo vídeo.

<!-- S59 -->
Así que te dejo una pregunta.
¿Un sistema de archivos solo debería guardar tus archivos,
o también protegerlos?
Cuéntamelo en los comentarios.
