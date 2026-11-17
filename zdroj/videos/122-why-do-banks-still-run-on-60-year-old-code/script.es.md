<!-- S01 -->
Novecientas noventa y nueve libras
y noventa y nueve peniques.
Súmale un penique.

<!-- S02 -->
El resultado es cero.

<!-- S03 -->
Ningún mensaje de error. Ningún bloqueo.
Solo un cero, escrito en silencio en la cuenta.

<!-- S04 -->
En COBOL, cuando el campo del resultado
es demasiado pequeño para contenerlo,
el dígito que sobra puede desaparecer sin más.
Salvo que el programa pida un aviso,
el cálculo sigue adelante.

<!-- S05 -->
Y tampoco redondea.
Dos libras con treinta y cuatro peniques y medio,
guardadas con precisión de un penique,
se quedan en dos con treinta y cuatro.

<!-- S06 -->
Escribe una palabra más, ROUNDED,
y pasa a ser dos con treinta y cinco.

<!-- S07 -->
Ninguna de las dos cosas es un fallo.
Son reglas.
Y muchos bancos del mundo
siguen funcionando con reglas así.

<!-- S08 -->
COBOL es un lenguaje de programación
de 1959.
No todo programa escrito en él es tan antiguo.
Pero el lenguaje sí,
y también sus costumbres.

<!-- S09 -->
Entonces, ¿por qué no lo han sustituido los bancos?
Dinero tienen.
Ingenieros, también.

<!-- S10 -->
Para averiguarlo, veremos tres casos reales.
Un banco que intentó dejar su sistema antiguo,
otro que lo consiguió,
y una crisis en la que todos culparon a COBOL.

<!-- S11 -->
Pero antes, ese medio penique que falta.

<!-- S12 -->
Supón que reescribes ese programa bancario
en un lenguaje moderno.
Seguramente corregirías esas reglas.
El desbordamiento pasa a ser un error.
El medio penique se redondea hacia arriba.

<!-- S13 -->
Más limpio. Más seguro.
Y ahora, cada vez que aparece medio penique,
tu programa no coincide con el antiguo.

<!-- S14 -->
Los lenguajes modernos saben calcular con decimales exactos.
Java tiene un tipo pensado para eso.
Pero incluso ahí,
la regla de redondeo es una elección.

<!-- S15 -->
Un ajuste habitual, si cae justo en medio, redondea hacia arriba:
dos con treinta y cinco.
Otro redondea al dígito par más cercano:
dos con treinta y cuatro.
Los dos son correctos. Solo uno coincide.

<!-- S16 -->
Y con la coma flotante de toda la vida,
la que usa por defecto la mayor parte del código,
la cosa se vuelve aún más rara.
Cero coma uno más cero coma dos
no da cero coma tres.

<!-- S17 -->
Así que sustituir COBOL no es traducir.
Es encontrar cada regla como esta,
entre millones de líneas,
y conservar cada una exactamente como estaba.

<!-- S18 -->
¿Y cómo acabó ahí, para empezar?

<!-- S19 -->
En mayo de 1959,
el Departamento de Defensa de EE. UU.
convocó una reunión en el Pentágono.
Acudieron fabricantes de ordenadores, organismos públicos
y grandes empresas,
todos con el mismo problema.

<!-- S20 -->
Cada ordenador tenía su propio lenguaje.
Un programa de nóminas escrito para una máquina
no servía en otra.

<!-- S21 -->
Un comité diseñó un lenguaje común
para los negocios.
Su mayor influencia fue FLOW-MATIC,
del equipo de Grace Hopper en Remington Rand.

<!-- S22 -->
Y en diciembre de 1960,
prácticamente el mismo programa en COBOL
funcionó en dos ordenadores
de fabricantes rivales.
De eso se trataba precisamente.

<!-- S23 -->
Se diseñó para que cualquiera pudiera seguirlo.
ADD PAYMENT TO ACCOUNT-BALANCE.
Seguramente adivinas qué hace.

<!-- S24 -->
Y guardaba el dinero tal como lo escribe la gente:
como dígitos decimales.
La coma decimal
ni siquiera hace falta guardarla.
La descripción del campo indica dónde va:
los dos últimos dígitos son peniques.

<!-- S25 -->
En 1964, IBM lanzó el System/360.
Su diseño incluía instrucciones
de aritmética decimal.

<!-- S26 -->
Y desde entonces, IBM ha diseñado sus mainframes
para que sigan siendo compatibles.
Muchos programas antiguos todavía pueden funcionar
en las máquinas actuales
sin tener que reescribirse.

<!-- S27 -->
Así que rara vez hubo un momento
que obligara a nadie a cambiar.
Cada año el código seguía funcionando,
y cada año acumulaba más reglas.
Nuevos productos, nuevos impuestos, nuevas normativas,
nuevas excepciones.

<!-- S28 -->
Nadie ha calculado cuánto COBOL
sigue funcionando en el mundo.
Pero IBM dice que cuarenta y cinco
de los cincuenta mayores bancos del mundo
siguen usando sus mainframes.

<!-- S29 -->
Y algunos propietarios sí lo han contado.
En 2017, la Administración del Seguro Social
de EE. UU. dijo que sus sistemas tenían
más de sesenta millones de líneas de COBOL.

<!-- S30 -->
En 2025, los auditores del Gobierno de EE. UU.
enumeraron los once sistemas federales
que más necesitaban ser sustituidos.

<!-- S31 -->
Tenían entre veintitrés
y sesenta años,
y mantenerlos en marcha costaba unos setecientos cincuenta
millones de dólares al año.

<!-- S32 -->
Así que el código es viejo, está por todas partes
y está lleno de reglas que nadie dejó por escrito.
Seguro que el peligro está en conservarlo.

<!-- S33 -->
Veamos qué pasa
cuando un banco se va.

<!-- S34 -->
En 2018, un banco británico llamado TSB
tenía unos cinco millones de clientes,
y un problema.

<!-- S35 -->
Tenía sus sistemas alquilados
a Lloyds Banking Group,
un competidor,
y las tarifas iban a subir mucho.

<!-- S36 -->
Así que TSB decidió trasladarlo todo
a una plataforma nueva,
construida por su nuevo dueño,
el banco español Sabadell.

<!-- S37 -->
Un fin de semana de abril.
El domingo por la noche,
se encendió el nuevo sistema.

<!-- S38 -->
El lunes hubo unos
novecientos mil intentos de iniciar sesión.
Solo alrededor de uno de cada diez accesos
a la banca por internet salió bien.

<!-- S39 -->
Los pagos fallaban.
Algunos clientes iniciaron sesión
y vieron las cuentas de otras personas.

<!-- S40 -->
Lo peor duró más o menos una semana.
TSB no volvió a la normalidad
hasta diciembre.

<!-- S41 -->
Las consecuencias costaron unos
trescientos treinta millones de libras
solo en 2018.
Más tarde, los reguladores añadieron
casi cuarenta y nueve millones en multas.

<!-- S42 -->
Y aquí viene lo raro.
Los datos de los clientes llegaron intactos.
Lo dicen los dos informes oficiales.

<!-- S43 -->
Lo que falló fue la plataforma nueva que los rodeaba.
Dos centros de datos, configurados de forma distinta.
Rendimiento probado solo en uno de ellos,
y los objetivos rebajados
cuando las pruebas no se superaron.

<!-- S44 -->
Y no había vuelta atrás.
Una vez trasladados los datos,
volver al sistema antiguo era,
en palabras del regulador,
«prácticamente imposible».

<!-- S45 -->
TSB no huía de un sistema roto.
Dejaba uno que funcionaba,
por quién era su dueño
y por lo que costaba.
Lo peligroso fue irse.

<!-- S46 -->
Entonces, ¿irse siempre es un desastre?

<!-- S47 -->
En 2008, el Commonwealth Bank de Australia
se propuso sustituir los sistemas centrales
que le habían servido
durante más de cuarenta y cinco años.

<!-- S48 -->
El plan: unos quinientos ochenta
millones de dólares australianos,
y cuatro años.

<!-- S49 -->
Tardó cinco.
Más tarde, la prensa cifró el total
en alrededor de mil cien millones,
a medida que el proyecto crecía.

<!-- S50 -->
Pero no lo trasladó todo
en un solo fin de semana.
Primero fueron las cuentas de depósito, en 2010.
Las cuentas de empresa siguieron en 2011,
y los préstamos, en 2012.

<!-- S51 -->
En cada paso, el banco podía
vigilar los resultados, comprobarlos y aprender
antes de pasar al siguiente.

<!-- S52 -->
Al final, según el banco,
se convirtió en el primer gran banco australiano
con banca en tiempo real,
las veinticuatro horas.

<!-- S53 -->
Así que se puede hacer.
Pero mira lo que hizo falta.
Cinco años, una factura mucho mayor
y paciencia.

<!-- S54 -->
Modernizar no es una compra.
Es un proyecto,
con sus propios riesgos.

<!-- S55 -->
Y ahora, la crisis
en la que todos culparon a COBOL.

<!-- S56 -->
Marzo de 2020.
Cuando la pandemia paralizó Nueva Jersey,
las nuevas solicitudes de subsidio por desempleo saltaron
de menos de diez mil en una semana
a más de ciento cincuenta y cinco mil.

<!-- S57 -->
Dieciséis veces más,
en siete días.
La oficina de desempleo no daba abasto.

<!-- S58 -->
A principios de abril, el gobernador
pidió voluntarios.
No solo sanitarios,
sino también gente que supiera COBOL.
Los sistemas del estado, dijo,
tenían más de cuarenta años.

<!-- S59 -->
La historia corrió como la pólvora.
Un código antiquísimo se había venido abajo
con la pandemia.

<!-- S60 -->
Pero cuando el auditor del estado
lo investigó más tarde,
no encontró ninguna prueba
de que los retrasos se debieran
a los sistemas informáticos.

<!-- S61 -->
Por otro lado, los periodistas que examinaron
los mensajes de error que veía la gente
atribuyeron muchos de ellos a la web pública,
escrita en un lenguaje mucho más nuevo, Java.
El código antiguo que había detrás siguió funcionando.

<!-- S62 -->
Entonces, ¿por qué necesitaba el estado programadores de COBOL?
Porque el Congreso estaba cambiando las reglas.
Nuevas prestaciones, nuevas cuantías,
nuevas personas con derecho a ellas,
y cada cambio tenía que llegar
al código, y rápido.

<!-- S63 -->
El problema no era que el código fuera viejo.
Era que poca gente sabía modificarlo,
y que las líneas telefónicas y el personal
también estaban desbordados.

<!-- S64 -->
Tres casos.
Un banco que dejó un sistema que aún funcionaba,
y cuya migración fracasó.
Un banco que se fue con cuidado,
y lo logró.
Y una crisis en la que se culpó al código antiguo,
y nadie pudo demostrar que fuera la causa.

<!-- S65 -->
Eso no significa que los sistemas antiguos nunca fallen.
Fallan.
Se encarecen,
la gente que los entiende se jubila,
y esperar también tiene su coste.

<!-- S66 -->
Pero la edad se ve fácilmente,
y los riesgos reales, no.
Reglas que nadie dejó por escrito.
Conocimiento en la cabeza de unas pocas personas.
Y el momento del cambio.

<!-- S67 -->
Por eso muchos bancos no sustituyen
el viejo núcleo de una sola vez.
Lo envuelven.
La app de tu móvil es nueva,
pero puede que esté hablando con algo
mucho más antiguo.

<!-- S68 -->
Y lo van sustituyendo pieza a pieza.
En 2004, el autor de software Martin Fowler
le puso el nombre de la higuera estranguladora,
una planta de la selva que crece alrededor de un árbol
hasta que puede sostenerse por sí misma.

<!-- S69 -->
El sistema antiguo sigue funcionando
mientras el nuevo crece a su alrededor,
una tarea tras otra,
hasta que nada depende del antiguo.

<!-- S70 -->
Lo que nos devuelve a ese medio penique.
En algún sitio, puede que un programa aún lo descarte,
porque alguien decidió que así fuera,
hace décadas.
Sustituir ese programa exige conocer esa regla,
y todas las que se le parezcan.

<!-- S71 -->
El sistema antiguo no es necesariamente
lo que falla.
A veces, es lo que lo sustituye.

<!-- S72 -->
Porque sustituir la tecnología
no es lo mismo que eliminar el riesgo.
A veces solo traslada el riesgo
a un único fin de semana de abril.

<!-- S73 -->
Así que aquí va una pregunta para ti.
Si un sistema lleva cuarenta años funcionando,
¿cuándo es el momento adecuado para sustituirlo?
¿Y alguna vez has tenido que sustituir uno tú?
Cuéntamelo en los comentarios.
