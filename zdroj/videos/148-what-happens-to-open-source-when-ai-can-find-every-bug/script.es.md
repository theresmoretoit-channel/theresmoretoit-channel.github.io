<!-- S01 -->
948.
Tantas formas distintas encontró una IA
de tomar el control de un ordenador Linux desde dentro.

<!-- S02 -->
Sin contraseñas robadas. Sin intrusión remota.
Cada una empieza con un usuario corriente
sin ningún permiso especial,
y termina con root,
la cuenta que puede hacerlo todo.

<!-- S03 -->
OpenAI publicó el resultado en noviembre de 2026.
Toda la ejecución costó
1,2 millones de dólares en créditos de API.

<!-- S05 -->
Son cifras de la propia OpenAI,
publicadas el día antes
de lanzar el modelo que las produjo,
y nadie de fuera ha confirmado el recuento completo.
Pero ya se han enviado
cientos de informes y parches.

<!-- S06 -->
Por eso esto no solo importa para Linux.
El código fuente de Linux es público.
Cualquiera puede leerlo.
Durante décadas, ese fue el argumento
para afirmar que era seguro.

<!-- S07 -->
Así que, si una máquina puede leer código público
y convertirlo en exploits funcionales a esta escala,
¿debería el software mantener su código en secreto?

<!-- S08 -->
Veamos un software que ya lo hace.
En abril de 2026, Microsoft corrigió
164 fallos de seguridad
en su día mensual de parches.
En octubre, corrigió
1.413.

<!-- S09 -->
Solo en ese mes corrigió más
que en cualquier año completo anterior.
Más de 1.000 de esas correcciones eran de Windows,
y Microsoft había avisado
de que sus propias herramientas de IA impulsarían el aumento.

<!-- S10 -->
No puedes comparar las dos cifras directamente.
Las empresas cuentan de forma distinta,
y Microsoft buscaba en su propio código privado.

<!-- S11 -->
Pero sí demuestra una cosa.
Mantener el código privado
no había impedido que hubiera errores.

<!-- S12 -->
Entonces, ¿qué te protege de verdad?
Para responder a eso,
tenemos que ver cómo funciona esta máquina,
porque cada uno de sus pasos descarta algo.

<!-- S13 -->
El kernel de Linux tiene
más de 40 millones de líneas de código.
Primero, unos agentes exploradores lo recorrieron
y escogieron las partes
a las que un usuario corriente puede llegar de verdad.

<!-- S14 -->
Quedó alrededor del 7 %.
Es la parte que consideraron digna de atacar,
no una muestra aleatoria,
así que no puedes multiplicar el resultado por 14.

<!-- S15 -->
Después, agentes analistas revisaron ese código
y anotaron todo lo sospechoso.
2.308 candidatos
en 12 horas.

<!-- S16 -->
Pero una sospecha no prueba nada.
Así que otros agentes escribieron programas de prueba
y los ejecutaron en máquinas virtuales aisladas.
1.724 errores
resultaron ser reales.

<!-- S17 -->
Luego vino la parte cara:
construir exploits funcionales,
con las protecciones estándar
de un sistema de escritorio normal activadas.
1.169
llegaron a root.

<!-- S18 -->
Agrúpalos según el fallo de fondo
y te salen los 948.

<!-- S19 -->
Hay un detalle en el informe
que cuesta olvidar.
En una de las primeras ejecuciones,
los agentes comunicaron 200 éxitos.
Luego unos humanos comprobaron cómo lo habían logrado.

<!-- S20 -->
Veinte de ellos habían llegado a root
a través de otro error desconocido,
no del que se les había indicado usar.
Enviados a abrir una puerta,
encontraron otra que nadie conocía.

<!-- S21 -->
En una muestra de sus exploits,
OpenAI identificó diez técnicas de explotación
que los expertos externos no habían visto antes.

<!-- S22 -->
En julio, un modelo anterior
encontró 166 de estos fallos.
Tres meses de correcciones después,
el modelo más nuevo encontró 948.
Los errores no se habían agotado.
La ejecución posterior encontró muchos más.

<!-- S23 -->
Ahora bien, hay un límite importante.
Nada de esto entra en tu ordenador
a través de internet.
El atacante ya tiene que estar en la máquina,
como usuario corriente.

<!-- S24 -->
Eso tranquiliza menos de lo que parece,
porque los ataques reales suelen tener dos pasos.
Primero entras,
por un fallo del navegador o una descarga maliciosa.
Luego necesitas root.
Este es el segundo paso.

<!-- S25 -->
El consejo de OpenAI es tajante.
En un sistema sin los últimos parches,
trata cualquier cuenta de usuario normal como si fuera root,
al menos frente a un atacante con muchos recursos.

<!-- S26 -->
Entonces, ¿en qué queda
el viejo argumento a favor del código abierto?
A finales de los noventa,
Eric Raymond le puso un eslogan:
«Con suficientes ojos, todos los errores son superficiales».

<!-- S27 -->
Lo llamó la ley de Linus.
Es una idea preciosa, pero parte de una suposición:
que alguien está mirando de verdad.

<!-- S28 -->
En 2014 apareció un fallo llamado Heartbleed
en OpenSSL,
el código que protegía una enorme parte de la web.
Se calculaba que alrededor de medio millón de servidores seguros
estaban expuestos.

<!-- S29 -->
El fallo llevaba dos años en código público.
El proyecto recibía
unos 2.000 dólares al año en donaciones
y tenía un solo desarrollador a tiempo completo.

<!-- S30 -->
Cualquiera podía leerlo.
Casi nadie lo hizo.

<!-- S31 -->
Esa fue siempre la verdadera debilidad del código abierto.
No demasiados ojos sobre el código. Demasiado pocos.

<!-- S32 -->
Y esa es la parte que cambia la IA.
Una máquina puede seguir escaneando
e investigar muchos más candidatos
de los que un investigador humano podría abarcar solo.
La vieja promesa por fin se cumple,
para todo el mundo, atacantes incluidos.

<!-- S33 -->
Así que el código público ahora sí se examina.
¿Sirve de algo esconderlo?

<!-- S34 -->
Un programa cerrado tiene que ejecutarse igualmente,
así que su código máquina está
en cada ordenador que lo usa.
Herramientas como Ghidra lo convierten de nuevo
en algo parecido al código fuente.

<!-- S35 -->
Y hay un truco clásico.
Compara un programa
antes y después de una actualización de seguridad.
Lo que ha cambiado te muestra dónde estaba el agujero.

<!-- S35b -->
Eso les dice a los atacantes dónde apuntar,
mucho antes de que todos los sistemas
hayan instalado la actualización.

<!-- S36 -->
Anthropic lo probó con el kernel de Windows,
con 21 fallos
que Microsoft había parcheado hacía poco,
y sin código fuente.
La IA provocó su primer cuelgue a los 31 minutos.
En seis horas tenía 18.

<!-- S37 -->
Ocho se convirtieron en exploits funcionales
capaces de tomar el control total de la máquina,
por unos 2.000 dólares cada uno.

<!-- S38 -->
Pero no eran errores desconocidos.
Los parches ya señalaban
dónde estaban los problemas.
Encontrar un fallo nuevo desde cero es más difícil.

<!-- S39 -->
Así que el secreto todavía le cuesta algo al atacante.
Es un badén, no un muro.
¿Qué altura tiene el badén?
No hay ninguna cifra pública.

<!-- S40 -->
¿Y el otro lado?
¿Qué te aporta realmente ser abierto?
La respuesta está en un pequeño detalle
del informe de OpenAI.

<!-- S41 -->
Durante los diez días de ese escaneo y análisis,
más de 100 de estos fallos de Linux
fueron corregidos, o estaban a punto de serlo,
por otras personas.
Unos 300 más
ya se estaban discutiendo en público.

<!-- S42 -->
Otras personas encontraban los mismos errores
al mismo tiempo.

<!-- S43 -->
Linus Torvalds ya lo había descrito en mayo.
Dijo que los informes de IA
habían vuelto la lista de correo de seguridad del kernel
«casi completamente inmanejable»,
porque distintas personas no paraban de encontrar
las mismas cosas con las mismas herramientas.

<!-- S44 -->
Y su consejo fue este:
«Si encontraste un error con herramientas de IA,
lo más probable es que alguien más también lo encontrara».

<!-- S45 -->
Las normas del kernel ahora lo dicen claramente.
Un error encontrado con IA debe tratarse como público,
porque varios investigadores
descubren los mismos errores,
a menudo el mismo día.

<!-- S46 -->
Piensa en lo que eso supone
para la idea de un error secreto.
Si a ti te salió barato encontrarlo,
le salió barato a todo el mundo.

<!-- S47 -->
Con el código abierto,
cualquiera puede revisar el informe,
verificar la corrección y cuestionar el resultado.
Con el software cerrado,
casi siempre tienes que fiarte del fabricante.

<!-- S49 -->
Pero la apertura tiene una factura,
y no es la que esperarías.
Es tentador decir
que un proyecto pequeño no puede pagar el escaneo.
Las empresas de IA ya están
ofreciendo acceso gratuito a los mantenedores.

<!-- S50 -->
Lo que falta son personas.
El kernel solía registrar
unos 500 problemas de seguridad por versión.
Este año superó los 1.500.
Muchos son menores,
pero alguien tiene que revisarlos igualmente.

<!-- S51 -->
En enero, el proyecto curl
puso fin a su programa de recompensas por errores,
para dejar de premiar una avalancha de informes basura.

<!-- S52 -->
Incluso los buenos informes solo trasladan el trabajo.
Los parches generados por IA siguen necesitando revisión humana.
Algunas de las primeras correcciones añadían código innecesario
o pasaban por alto otras variantes del mismo error.

<!-- S53 -->
Puedes comprar más escaneo.
No puedes comprar más personas
que entiendan un fragmento de código así de bien.
Aquí, una empresa con un equipo de seguridad pagado
sí que tiene ventaja.

<!-- S54 -->
Y entonces llega el último problema.
Corregido no es lo mismo que instalado.

<!-- S55 -->
En marzo de 2017,
Microsoft parcheó un fallo en Windows.
Código cerrado, un fabricante, un sistema de actualizaciones.
Dos meses después,
WannaCry entró por ese mismo agujero
en unos 200.000 ordenadores
de unos 150 países.

<!-- S56 -->
Ese parche tuvo dos meses para extenderse,
y no fue suficiente.
Puede que un atacante ya no te deje dos meses.
En el mismo estudio de Anthropic,
la IA tomó una corrección pública
del motor de JavaScript de Firefox
y tuvo un exploit funcional en menos de una hora.

<!-- S57 -->
A la versión corregida de Firefox
aún le faltaban 18 días.

<!-- S58 -->
Este es el peligro de publicar una corrección.
La información puede llegar a los atacantes
antes de que la actualización te llegue a ti.

<!-- S59 -->
Una corrección de Linux tiene un largo camino por delante,
del kernel a una versión estable,
a tu distribución, a tu dispositivo.
Un teléfono puede esperar meses, o para siempre.

<!-- S60 -->
Y el software cerrado no se libra de esto.
Lo acabamos de ver: el parche de Windows bastó.
Cada actualización es ahora también un mapa.

<!-- S60b -->
Así que mantén todo actualizado,
tu ordenador, tu teléfono, incluso tu router,
e instala las actualizaciones en cuanto lleguen.
A medida que la IA mejora convirtiendo correcciones en ataques,
cada día que esperes importará más.

<!-- S61 -->
Entonces, ¿sigue siendo más seguro el código abierto?
Sinceramente, nadie lo sabe.
Hasta donde se sabe públicamente,
nadie ha hecho la misma prueba en ambos lados
con las mismas reglas.

<!-- S62 -->
Lo que podemos decir es más modesto.
Esconder el código aporta menos que antes.
Mostrarlo permite que cualquiera revise el trabajo,
y descarga todavía más de ese trabajo
sobre quienes lo mantienen.

<!-- S64 -->
Aunque la IA nunca encuentre todos los errores,
ya ha cambiado lo que cuesta encontrarlos.

<!-- S65 -->
Lo que importa ahora es cuánto tiempo sigue abierto un agujero
entre el momento en que alguien lo encuentra
y el momento en que se cierra en tu máquina.

<!-- S66 -->
Así que aquí va una pregunta para ti.
Si cualquiera puede encontrar cualquier error,
¿preferirías confiar en código que puedes leer,
o en una empresa a la que pagan por arreglarlo?
Cuéntamelo en los comentarios.
