<!-- S01 -->
Imagina que diriges una de las mayores
empresas tecnológicas del mundo.

<!-- S02 -->
Miles de ingenieros.
Miles de millones de dólares.

<!-- S03 -->
Y una de las piezas más importantes
de tu infraestructura
la controla un hombre
que no trabaja para ti.

<!-- S04 -->
No puedes despedirlo.
No puedes desautorizarlo.

<!-- S05 -->
Cuando tus ingenieros quieren cambiar
ese software, le envían su trabajo
y esperan su respuesta.

<!-- S06 -->
Ese hombre es Linus Torvalds.
Y el software es Linux.

<!-- S07 -->
Google lo hace.
Y también Microsoft, Intel, Amazon y Meta.

<!-- S08 -->
Entonces, ¿por qué las grandes tecnológicas no lo han sustituido?

<!-- S09 -->
Linux nació como el hobby de un estudiante
en Helsinki en 1991.
Hoy funciona en los móviles Android,
en servidores en la nube y en los quinientos
superordenadores más rápidos del mundo.

<!-- S10 -->
La última versión trajo
casi diecinueve mil cambios,
de unos tres mil desarrolladores
y más de doscientas empresas.

<!-- S11 -->
¿Y cuántos de esos cambios
escribió el propio Linus?

<!-- S12 -->
Nueve.

<!-- S13 -->
Y ocho de ellos
solo cambiaban el número de versión.

<!-- S14 -->
En dos semanas, integró
unos doscientos cuarenta lotes
de cambios, cada uno enviado
por alguien de su confianza.

<!-- S15 -->
Él manda
porque el código acaba en sus manos.

<!-- S16 -->
Y esa es justo la parte
que una empresa como Google
podría saltarse sin más.

<!-- S17 -->
Linux es de código abierto.
Cualquiera puede coger el código
y hacer su propia versión.

<!-- S18 -->
Se llama fork,
y no necesitas el permiso de Linus.

<!-- S19 -->
Google hizo exactamente eso.

<!-- S20 -->
No un Linux completamente nuevo.
Cogió el núcleo,
la parte central que habla con el hardware,
y mantuvo su propia rama
para Android.

<!-- S21 -->
En diciembre de 2009, el código de Android
se eliminó del núcleo principal.

<!-- S22 -->
Greg Kroah-Hartman,
uno de los mantenedores veteranos,
explicó por qué:
a nadie le importaba ese código,
así que se eliminó.

<!-- S23 -->
Así que el núcleo de Android se fue alejando.

<!-- S24 -->
Los fabricantes de chips y de móviles
le añadieron sus propios cambios encima.

<!-- S25 -->
Según reconoce la propia Google,
hasta la mitad del código
del núcleo de un móvil
podía venir de fuera del núcleo principal.

<!-- S26 -->
Y cada corrección de seguridad
que aparecía en Linux
había que trasladarla
a cada una de esas versiones.

<!-- S27 -->
La documentación de Google lo califica
de «prohibitivamente caro».

<!-- S28 -->
Una nueva versión del núcleo podía tardar
hasta dieciocho meses
en llegar a un móvil.

<!-- S29 -->
Dos años después de borrar
el código de Android,
Greg lo volvió a meter.

<!-- S30 -->
Su nota decía:
«Resulta que me equivocaba,
queremos esto en el árbol».

<!-- S31 -->
Y desde Android 12,
los móviles que salen con un núcleo más reciente
tienen que usar un núcleo común de Google,
el Generic Kernel Image.

<!-- S32 -->
Sigue siendo Linux
con los cambios propios de Android encima.
Pero se mantiene cerca de la versión principal,
porque ahí es donde están las correcciones.

<!-- S33 -->
Hacer tu propia versión es fácil.
Lo caro es mantenerla viva.

<!-- S34 -->
Por eso las empresas envían su código
al núcleo principal.

<!-- S35 -->
No es por hacer un favor.
Una vez dentro,
todos los demás ayudan a cuidarlo.

<!-- S36 -->
Pero Linus no puede leerse
diecinueve mil cambios.
Nadie podría.

<!-- S37 -->
Linux está dividido en áreas.
Redes. Memoria. Sistemas de archivos.
Controladores gráficos. Cada familia de procesadores.

<!-- S38 -->
Cada área tiene sus propios mantenedores.
La lista tiene unas
tres mil quinientas entradas.

<!-- S39 -->
Un cambio va primero
al mantenedor que le toca.

<!-- S40 -->
Lo revisan, discuten sobre él,
piden correcciones
y reúnen lo que está listo.

<!-- S41 -->
Luego lo mandan hacia arriba.

<!-- S42 -->
En lo más alto,
más de cien de ellos
le mandan a Linus lo que han reunido.

<!-- S43 -->
Linux se construye en todas partes.
Pero se ensambla en un solo lugar.

<!-- S44 -->
Ahora bien, las empresas
que envían todo ese código
no son organizaciones benéficas.

<!-- S45 -->
Estas empresas compiten
entre sí todos los días.

<!-- S46 -->
¿Dejaría Google que Microsoft decidiera
qué entra en el software
con el que funcionan sus servidores?

<!-- S47 -->
Linus no trabaja para ninguna de ellas.

<!-- S48 -->
Entonces, ¿quién le paga?

<!-- S49 -->
La Linux Foundation.

<!-- S50 -->
Y la fundación no es una organización benéfica
al margen del mundo empresarial.

<!-- S51 -->
Es una asociación de empresas.

<!-- S52 -->
Google, Microsoft, Intel,
Meta, Amazon y otras
pagan por ser socios del máximo nivel,
y cada una de ellas
tiene un asiento en su junta directiva.

<!-- S53 -->
La fundación dice
que le paga a Linus
para que pueda seguir siendo independiente.

<!-- S54 -->
Es un propósito declarado,
no una garantía publicada.

<!-- S55 -->
La fundación acoge
más de mil proyectos.
El núcleo se lleva alrededor del tres por ciento
de su presupuesto.

<!-- S56 -->
O sea, las empresas no están poniendo
a uno de los suyos en lo más alto.

<!-- S57 -->
Están apoyando un lugar
donde pueden trabajar juntas
sin que ninguna de ellas mande.

<!-- S58 -->
Pero ¿de verdad Linus
tiene la última palabra?

<!-- S59 -->
Veamos cómo funciona en la práctica.

<!-- S60 -->
En 2024, Linux recibió
un nuevo sistema de archivos llamado bcachefs,
una nueva forma de guardar archivos en un disco.

<!-- S61 -->
Cada nueva versión tiene una regla.
Las funciones nuevas entran
durante las dos primeras semanas.
Después, solo correcciones.

<!-- S62 -->
Su desarrollador siguió enviando
cambios grandes pasadas esas dos semanas.

<!-- S63 -->
En agosto de 2024, Linus escribió:

<!-- S64 -->
«En algún momento,
"arreglar algo" se convierte sin más en desarrollo.
Y este es ese momento».

<!-- S65 -->
Las discusiones siguieron un año más.

<!-- S66 -->
En 2025, Linus sacó bcachefs
del núcleo.

<!-- S67 -->
Sigue existiendo,
como un complemento aparte.
Solo que no en la versión compartida.

<!-- S68 -->
Linus tiene poder
porque la gente que le envía código
sigue confiando en él.

<!-- S69 -->
Entonces, ¿qué pasará cuando Linus ya no esté?

<!-- S70 -->
Algo ya sabemos.

<!-- S71 -->
En septiembre de 2018, Linus se apartó.

<!-- S72 -->
Pidió perdón por atacar a gente
en sus correos,
y dijo que necesitaba tiempo
para cambiar su forma de comportarse.

<!-- S73 -->
Greg Kroah-Hartman,
el mismo mantenedor
de la historia de Android,
tomó el relevo
y terminó la siguiente versión, la 4.19.

<!-- S74 -->
Linux siguió adelante.
Unas semanas después, Linus volvió.

<!-- S75 -->
Desde 2026 hay incluso un plan por escrito.

<!-- S76 -->
Si Linus no puede continuar,
los mantenedores veteranos empiezan a hablar,
en un plazo de setenta y dos horas,
sobre quién toma el relevo.

<!-- S77 -->
No nombra a ningún sucesor.
Describe cómo encontrarlo.

<!-- S78 -->
Así que Linux puede sobrevivir sin Linus.

<!-- S79 -->
Lo que no puede sustituir tan fácilmente
es la confianza que, en su día,
lo llevó al centro.

<!-- S80 -->
Entonces, ¿por qué las grandes tecnológicas
no han sustituido a Linus Torvalds?

<!-- S81 -->
Porque lo que estarían sustituyendo
no es un programador.

<!-- S82 -->
Es el único lugar
donde se junta todo el código
de empresas que compiten entre sí,
cuidado por alguien
que no pertenece a ninguna de ellas.

<!-- S83 -->
Linus no es el dueño del reino.
Simplemente, todos coinciden en que, por ahora,
él es la persona adecuada para custodiarlo.

<!-- S84 -->
Así que te dejo una pregunta.
Cuando Linus se retire,
¿debería una sola persona
volver a tener la última palabra,
o debería ser un grupo?

<!-- S85 -->
Cuéntamelo en los comentarios.
