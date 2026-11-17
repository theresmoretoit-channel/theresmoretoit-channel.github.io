<!-- S01 -->
Aquí tienes un requisito completo
para un programa de gestión empresarial.
Un usuario puede cancelar un pedido.

<!-- S02 -->
Seis palabras.
Cualquier desarrollador asentiría.
Cualquier cliente lo firmaría.

<!-- S03 -->
Entonces, ¿puede un usuario cancelar un pedido
cuando ya se ha emitido la factura?
¿Y cuando ya se ha enviado?

<!-- S04 -->
¿Cancelarlo cancela también
la reserva con el proveedor?
¿Y si una persona lo cancela
y otra aprueba ese mismo pedido
en el mismo segundo?

<!-- S05 -->
La frase no responde a nada de eso.
El código tiene que responderlo todo.
Y ese hueco entre la frase
y el código es, en realidad,
por lo que se paga a los programadores.
O al menos así era antes.

<!-- S06 -->
Hoy circula una idea tentadora.
Escribir solo las frases.
Guardarlas en documentos,
revisarlas, versionarlas.
Y que una IA escriba el código.

<!-- S07 -->
La especificación se convierte
en el código fuente.
Y el código pasa a ser lo que hoy
es el ensamblador: algo que se ejecuta
y que nadie lee.

<!-- S08 -->
Es una buena idea.
Pero tampoco es nueva.

<!-- S09 -->
Desde hace casi setenta años se intenta
subir el nivel
al que le decimos al ordenador qué hacer.
Las herramientas eran distintas,
y también sus objetivos.
Pero cada una pasó más trabajo
de las personas a las máquinas.

<!-- S10 -->
En 1957, un equipo de IBM
publicó un artículo sobre FORTRAN.
Su título lo presentaba
como un sistema de codificación automática.

<!-- S11 -->
En aquella época, el nombre era exacto.
Tú escribías fórmulas,
y las instrucciones de máquina,
la parte que la gente escribía a mano,
ahora las producía la propia máquina.

<!-- S12 -->
Hoy a FORTRAN lo llamamos código.

<!-- S13 -->
En los años ochenta, las herramientas CASE
y los lenguajes de cuarta generación
subieron un nivel más.
Dibujas los diagramas, rellenas los formularios
y gran parte de la aplicación
se genera sola.

<!-- S14 -->
En 2001, el Object Management Group,
la organización detrás de UML,
anunció Model Driven Architecture.

<!-- S15 -->
La promesa te sonará.
Describes el sistema una sola vez,
como un modelo, independiente de cualquier tecnología.
Luego las herramientas generan la implementación
para la plataforma que necesites.

<!-- S16 -->
Las mismas reglas de negocio.
Tecnología intercambiable.

<!-- S17 -->
Y en 2014, los analistas de Forrester
le pusieron nombre a las plataformas
para crear aplicaciones empresariales
con la menor cantidad posible
de código escrito a mano.
Lo llamaron low-code.

<!-- S18 -->
Entonces, ¿funcionó algo de todo eso?

<!-- S19 -->
En parte.
En 2014, investigadores de la Universidad de Lancaster
publicaron una encuesta
a 450 personas
que de verdad usaban
el desarrollo dirigido por modelos.

<!-- S20 -->
Funcionaba,
y en más ámbitos de lo que muchos creían.
Pero rara vez para un sistema entero.
La gente lo usaba en partes clave
y construía el resto de otras formas.

<!-- S21 -->
Los mayores obstáculos que encontraron
eran las personas y las organizaciones,
no las herramientas.
Pero también hay un límite técnico,
y los programadores tienen un chiste sobre él.

<!-- S22 -->
Una especificación tan precisa
que se pueda generar a partir de ella todo el programa...
ya tiene nombre.
Se llama código.

<!-- S23 -->
Para generarlo todo,
el modelo tenía que decirlo todo.
Cada estado, cada excepción,
cada «¿y si dos personas lo hacen a la vez?».

<!-- S24 -->
En ese punto
no te has librado de programar.
Solo lo has trasladado a un diagrama,
que a menudo es más difícil de leer,
de comparar y de revisar.

<!-- S25 -->
Ya a finales de los años setenta,
Edsger Dijkstra resumió la otra mitad
en una nota breve con un título tajante.
Sobre la insensatez
de programar en lenguaje natural.

<!-- S26 -->
Para él, la notación formal
no es una carga que hay que aguantar.
La llamó una herramienta asombrosamente eficaz
para descartar todo tipo de disparates.

<!-- S27 -->
El lenguaje corriente no los descarta.
Los esconde.
Un usuario puede cancelar un pedido.

<!-- S28 -->
Entonces, si nada de eso sustituyó al código,
¿por qué volver a intentarlo?

<!-- S29 -->
Porque hay una cosa que de verdad es distinta.

<!-- S30 -->
Los generadores de antes no podían llenar un hueco
por su cuenta.
Si el modelo no decía qué pasa
con un pedido ya enviado,
alguien tenía que añadir esa regla explícitamente.
Hasta que lo hacía, el hueco seguía ahí,
y se podía encontrar.

<!-- S31 -->
Una IA no se detiene.
Dale el requisito de seis palabras
y responderá a todas las preguntas
que hicimos al principio.

<!-- S32 -->
Decidirá que un pedido enviado
se puede cancelar. O que no.
Decidirá sobre la factura
y sobre el proveedor.
Producirá código que funciona,
parece razonable
y pasa las pruebas que ella misma escribió.

<!-- S33 -->
Eso es justo lo que la hace útil.
Y justo lo que la hace peligrosa.
Porque una suposición verosímil
no es una decisión de negocio.

<!-- S34 -->
Antes, los huecos eran errores.

<!-- S35 -->
Ahora son decisiones
que se tomaron sin que nadie se diera cuenta.

<!-- S36 -->
Así que, si la especificación de verdad
va a ser el código fuente,
no puede ser un par de párrafos informales.

<!-- S37 -->
Imagina el repositorio.
Un documento describe los pedidos
y todos los estados en que pueden estar.
Otro dice quién puede aprobarlos
y quién puede cancelarlos.

<!-- S38 -->
Un tercero dice cuándo se emite una factura
y cuándo hay que anularla.
Otro describe el sistema de contabilidad,
incluido qué pasa cuando se cae.

<!-- S39 -->
Una parte es prosa normal.
Pero donde la prosa sería ambigua,
hay algo más estricto:
una lista de estados y las transiciones entre ellos,
un esquema, una regla que una máquina puede comprobar.

<!-- S40 -->
Y junto a eso, pruebas de aceptación
que dicen exactamente qué debe pasar.

<!-- S41 -->
Todo eso vive en Git.
Los cambios se revisan.
Cada requisito se puede rastrear
hasta la prueba que lo comprueba.

<!-- S42 -->
Entonces, ¿cómo es un cambio?
Pongamos que el cliente decide
que un pedido enviado aún se puede cancelar,
siempre que no se haya entregado.
Y que entonces hay que anular la factura.

<!-- S43 -->
Nadie abre el backend.
Un desarrollador cambia una regla
en el documento sobre los pedidos.

<!-- S44 -->
Luego el sistema busca
todo lo que esa regla toca.
Los estados del pedido.
Las reglas de facturación.
Las pruebas de cancelación.
La reserva con el proveedor.

<!-- S45 -->
Y ahí debería detenerse y preguntar.
La especificación nunca dijo
qué pasa con la reserva con el proveedor
una vez que la mercancía está en camino.
Eso es una decisión,
así que le toca a una persona.

<!-- S46 -->
Solo entonces se genera
la nueva implementación.
Y se comprueba en ambas direcciones.
Las pruebas de la nueva regla deben pasar.
Y todas las demás deben seguir pasando,
sin cambios.

<!-- S47 -->
Porque un cambio en la cancelación
no debe cambiar nada más sin avisar.
Eso sí, que las pruebas pasen solo demuestra
lo que esas pruebas comprueban.

<!-- S48 -->
Y como las reglas
no están atadas a la tecnología,
la misma especificación podría producir
hoy una aplicación en PHP
y mañana algo totalmente distinto.

<!-- S49 -->
Que es justo lo que
prometía Model Driven Architecture
hace veinticinco años.
La diferencia es que, esta vez,
el generador quizá sea lo bastante bueno.

<!-- S50 -->
Queda la pregunta más difícil.
¿Cómo sabes que la IA
siguió de verdad la especificación?

<!-- S51 -->
Un código que funciona en situaciones normales
puede fallar igualmente en las inusuales.
Y las inusuales son justo
los casos que a nadie se le ocurre probar.

<!-- S52 -->
Amazon se topó con esto
en sus propios sistemas en la nube.
En 2014, sus ingenieros describieron
cómo habían empezado a escribir
descripciones precisas y matemáticas
de sus diseños,
en un lenguaje llamado TLA+.

<!-- S53 -->
No del código. Del propio diseño.
Luego, una herramienta tomaba un modelo del sistema,
limitado a un tamaño fijo,
y probaba todos los órdenes posibles
de fallos y recuperaciones.

<!-- S54 -->
En DynamoDB, el servicio de bases de datos de Amazon,
encontró un error que podía hacer perder datos.

<!-- S55 -->
La forma más corta de provocarlo
requería 35 pasos,
exactamente en el orden correcto.
Había superado revisiones de diseño,
revisiones de código y pruebas.

<!-- S56 -->
Así que la versión honesta de la idea
no es que la IA escriba el código
y nos fiemos de ella.
Es que la IA escriba el código
y algo independiente lo compruebe.

<!-- S57 -->
Ahora mira lo que hemos construido.

<!-- S58 -->
Estados precisos.
Reglas formales.
Pruebas comprobables.
Versionado, revisado, guardado en un repositorio.

<!-- S59 -->
Eso no parece
el fin de la programación.
Parece programación
en un lenguaje nuevo.

<!-- S60 -->
Y eso es lo que pasó cada vez.
FORTRAN era codificación automática,
hasta que se convirtió en el código.
Cada vez que la máquina asumía
el «cómo», la gente subía al «qué».

<!-- S61 -->
Y el «qué» siempre fue la parte difícil.
No teclear, sino decidir.
Qué pasa con un pedido enviado.
Quién puede tocar qué datos.
Qué no debe hacer nunca el sistema.

<!-- S62 -->
Quizá el programador del futuro
no escriba miles de líneas de código.

<!-- S63 -->
Pero alguien tendrá que seguir entendiendo
un problema lo bastante bien como para decir
exactamente qué debe hacer un ordenador,
y comprobar que lo hizo.

<!-- S64 -->
Y si la especificación
se convierte en el código fuente,
la habilidad más importante
quizá ya no sea saber
cómo escribir un programa.

<!-- S65 -->
Quizá sea saber
cómo describirlo.

<!-- S66 -->
Así que te dejo una pregunta,
y me gustaría leer tu respuesta.
Si escribes una especificación
tan precisa
como para que una máquina genere con ella el programa...
¿sigues programando?
