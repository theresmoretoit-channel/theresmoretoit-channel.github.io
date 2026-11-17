<!-- S01 -->
En septiembre de 2026, un solo lote
de actualizaciones de Windows rompió
cuatro cosas a la vez.

<!-- S02 -->
El audio dejó de funcionar.
Remote Desktop dejó de funcionar.
Las carpetas compartidas en máquinas
virtuales dejaron de funcionar.

<!-- S03 -->
Y algunos equipos dejaron de confiar
en la red de la empresa
a la que pertenecían,
así que nadie pudo iniciar sesión.

<!-- S04 -->
Un lote.
Un martes.

<!-- S05 -->
Y si estás pensando
que esto es solo otra
mala actualización de Windows...

<!-- S06 -->
no lo es.

<!-- S07 -->
Porque esto ha pasado
una y otra y otra vez.

<!-- S08 -->
¿Qué hace exactamente su QA?

<!-- S09 -->
¿Cómo puede una empresa tan enorme
publicar una actualización del sistema
y no ver algo tan evidente?

<!-- S10 -->
Empecemos por lo más pequeño.

<!-- S11 -->
Microsoft publicó una actualización
que cambiaba algunas cosas
de la barra de tareas.
Y poco después admitió
que había un problema
con la configuración del cursor.

<!-- S12 -->
A algunos, su cursor personalizado
volvía a una gran flecha blanca.
De esas que te hacen comprobar
si has arrancado sin querer
un ordenador de 1998.

<!-- S13 -->
¿Tu cursor cuidadosamente elegido?
Desaparecido.
Y volver a ponerlo
tampoco funcionaba.

<!-- S14 -->
Ahora quizá estés pensando:
todo software tiene errores.
Exacto.

<!-- S15 -->
Pero hay diferencia entre:
«Encontramos un fallo raro
en una configuración
de hardware poco habitual».

<!-- S16 -->
Y:
«Tras nuestra actualización,
tu ratón no se parece al ratón
que elegiste».

<!-- S17 -->
Porque alguien tiene que instalarla.
Alguien tiene que iniciar sesión.
Alguien tiene que mover el ratón.
Y por lo visto no bastó.

<!-- S18 -->
Luego está el audio.
Instalas una actualización.
Reinicias.
Sin sonido.

<!-- S19 -->
Algunos dispositivos de audio USB
se paran, y Windows informa
de que el dispositivo no puede iniciarse.

<!-- S20 -->
Y el audio no es precisamente
una función exótica.
Uno diría que una de las pruebas básicas
de un sistema operativo sería:

<!-- S21 -->
¿el ordenador todavía suena?

<!-- S22 -->
Por lo visto es más complicado
de lo que suena.
Literalmente.

<!-- S23 -->
En casa todo esto es molesto.
El cursor queda ridículo.
Los altavoces callan.
Pero sobrevivirás.

<!-- S24 -->
Pero un servidor que deja de confiar
en la red a la que pertenece
significa que nadie inicia sesión,
y alguien del departamento de TI
está teniendo una mañana pésima.

<!-- S25 -->
Y aquí deja de ser
una colección de anécdotas.

<!-- S26 -->
Porque podemos mirar el historial
de actualizaciones de Microsoft.
Microsoft lo publica.
Cada mes enumeran
qué rompieron sus actualizaciones.

<!-- S27 -->
Y si pones en fila
un solo año de esa lista,
el mismo patrón
se repite una y otra vez.

<!-- S28 -->
Enero rompió dispositivos de audio
y cámaras web.
Febrero hizo girar el cursor
y el equipo parecía colgado.

<!-- S29 -->
Marzo dio pantallas azules
e instalaciones
atascadas a medio camino.
Abril rompió el inicio de sesión
con la cara.

<!-- S30 -->
En mayo el Explorador dejó
de responder al ratón.
Y octubre rompió las conexiones
al propio ordenador.

<!-- S31 -->
No a internet.
A la dirección que dice «esta máquina».

<!-- S32 -->
Y dos de ellas
son realmente notables.

<!-- S33 -->
Una actualización rompió el botón
que restablece el PC.
Otra, la pantalla de recuperación,
donde los ratones y teclados USB
dejaron de responder.

<!-- S34 -->
Léelo otra vez.

<!-- S35 -->
Dos veces en tres meses,
una actualización rompió la herramienta
con la que se repara un ordenador.

<!-- S36 -->
Y un detalle más,
quizá el más importante.
Ese fallo de audio, en el que Windows
dice que el dispositivo no arranca.

<!-- S37 -->
Apareció en enero.
Y luego volvió a aparecer
veinte meses después.

<!-- S38 -->
El mismo síntoma.
El mismo tipo de dispositivo.
El mismo mensaje.

<!-- S39 -->
Esa no es una historia
sobre escribir mal el código.
Es una historia sobre pruebas.

<!-- S40 -->
Y nada de esto es nuevo.

<!-- S41 -->
En 2024 hubo una actualización
que impidió que Linux arrancara
en equipos con arranque dual.
El mensaje de error decía literalmente:

<!-- S42 -->
«Algo ha ido
gravemente mal».

<!-- S43 -->
Que es, francamente, el mensaje de error
más certero que Windows ha mostrado.

<!-- S44 -->
Y en 2018 hubo una versión
que se retiró por completo,
después de que la gente informara
de que sus archivos habían desaparecido.

<!-- S45 -->
Así que a estas alturas
puedes concluir razonablemente:
Microsoft simplemente no sabe
escribir software.

<!-- S46 -->
Y eso lo explicaría todo.
Los errores.
Las regresiones.
Las actualizaciones que arreglan una cosa
y rompen otra.

<!-- S47 -->
Pero esa explicación
tiene un problema.
Microsoft no hace solo Windows.

<!-- S48 -->
Hacen Office.
Visual Studio.
Exchange.
Teams.
Y una nube muy grande.

<!-- S49 -->
Y todo eso ha tenido
sus propios errores, sus regresiones
y sus caídas espectaculares.

<!-- S50 -->
Y eso importa.
Porque la explicación habitual para
Windows es que arrastra
treinta años de código viejo.

<!-- S51 -->
Un servicio en la nube moderno
no arrastra treinta años
de nada.
Se construyó hace poco,
por gente que sabía
lo que estaba construyendo.

<!-- S52 -->
Y aun así se rompe.

<!-- S53 -->
Así que el problema nunca fue
solo el código viejo.
El problema es la complejidad
a la escala de Microsoft.

<!-- S54 -->
Y Windows es el sitio
donde esa complejidad
se ve mejor.

<!-- S55 -->
Porque Windows no es realmente
un sistema operativo.
Abajo del todo hay una arquitectura
que viene de principios de los noventa.

<!-- S56 -->
Luego décadas de interfaces.
Luego capas de compatibilidad.
Luego controladores.
Luego servicios.

<!-- S57 -->
Luego frameworks más nuevos,
sobre frameworks más antiguos.
Luego un aspecto nuevo.
Luego otro aspecto nuevo.

<!-- S58 -->
Es menos un sistema operativo
y más una excavación arqueológica
que de algún modo sigue funcionando.

<!-- S59 -->
Y a Microsoft no se le permite
arrasar el yacimiento,
porque hay empresas que dependen
de lo que hay debajo.
Hay un vídeo entero sobre eso.

<!-- S60 -->
Lo que importa aquí
es qué le hace eso a los errores.
Cada capa tiene que seguir funcionando
con cada capa de debajo.

<!-- S61 -->
Así que un cambio aquí arriba
puede romper algo
que nadie ha mirado en años.

<!-- S62 -->
Y hay otra pista más
sobre cómo va esto,
y no trata de errores en absoluto.

<!-- S63 -->
Es un patrón.
Microsoft quita algo.
Los usuarios se quejan.
Microsoft tarda años
en reconsiderarlo.

<!-- S64 -->
Y mientras tanto,
otra persona hace una herramienta
que lo devuelve.

<!-- S65 -->
Y lo gracioso es
que no son proyectos
de aficionados perdidos.

<!-- S66 -->
Hay aplicaciones enteras
cuyo único trabajo es hacer que Windows
se comporte más como...

<!-- S67 -->
bueno...
Windows.

<!-- S68 -->
Devuelven un menú Inicio antiguo.
Restauran la barra de tareas.
Cambian cómo se comporta el Explorador.

<!-- S69 -->
Y algunas te dan más control
sobre Windows que el propio Windows.

<!-- S70 -->
Microsoft tiene una cantidad enorme
de ingenieros en este sistema.
Y entonces alguien de fuera dice:
vale.
Me devuelvo la barra yo mismo.

<!-- S71 -->
Y ahora ha cambiado otra cosa.
Microsoft usa cada vez más la IA
para escribir su software.

<!-- S72 -->
Su propio director ejecutivo ha dicho
que del veinte al treinta por ciento
del código de sus repositorios
ya lo escribe software.

<!-- S73 -->
Y eso debería significar
más productividad.
Más correcciones.
Desarrollo más rápido.

<!-- S74 -->
Pero hay un cuello de botella evidente.
Escribir código puede acelerarse.

<!-- S75 -->
Probar un sistema heredado enorme
no se acelera necesariamente.

<!-- S76 -->
Y si puedes producir cambios
más rápido de lo que puedes probar
cómo interactúan con décadas
de código existente...

<!-- S77 -->
puede que acabes simplemente
produciendo regresiones más rápido.

<!-- S78 -->
Y aquí conviene ser prudente.
Esa cifra es de Microsoft entera,
no de Windows en particular.
Y nadie ha demostrado
que la IA causara ninguno de estos fallos.

<!-- S79 -->
Quizá la IA no hizo a Microsoft
peor a la hora de probar.

<!-- S80 -->
Quizá solo aceleró
el problema que ya estaba.

<!-- S80b -->
Por cierto, si quieres ver
adónde lleva el resto de esto,
puedes suscribirte.

Al canal le ayuda de verdad.

<!-- S81 -->
La mayor parte de este vídeo ha
sostenido que Microsoft tiene
un problema real de calidad.
Y ese argumento se sostiene.

<!-- S82 -->
Pero aquí viene la parte
que sorprende a la gente.
¿Por qué el núcleo
podría ser distinto?

<!-- S83 -->
Porque casi todo
lo descrito hasta ahora
no es el núcleo.

<!-- S84 -->
El cursor.
La barra de tareas.
El menú Inicio.
La configuración.
La pantalla de recuperación.

<!-- S85 -->
Todo eso va encima.

<!-- S86 -->
El núcleo es la parte de debajo.
Decide qué programa se ejecuta
en qué núcleo del procesador.
Reparte la memoria.
Habla con el hardware.

<!-- S87 -->
Y si esa parte fallara de verdad,
el síntoma no sería
un ratón con pinta ridícula.

<!-- S88 -->
El síntoma sería una máquina
que se para, corrompe tus datos
o deja entrar a alguien en silencio.

<!-- S88b -->
Y el núcleo tiene algo
que el resto de Windows no tiene.
Restricciones estrictas.

<!-- S88c -->
Un planificador no puede decidir
comportarse de otra manera
porque alguien haya rediseñado
el menú Inicio.

<!-- S88d -->
La gestión de memoria no se moderniza
moviendo un botón.
Y un controlador no puede dar por hecho
que el hardware se portará bien.

<!-- S88e -->
Y sobre todo: el núcleo no tiene dónde
esconder un error, detrás de
una página de configuración confusa.

<!-- S88f -->
Que es una razón para sospechar
que es un asunto técnico
completamente distinto
del resto de Windows.

<!-- S89 -->
Pero sospechar no es probar.
Así que mira lo que esta cosa
ha tenido que aguantar de verdad.

<!-- S90 -->
Esa arquitectura de abajo es vieja.
Muy vieja.
Y sobrevivió.

<!-- S91 -->
Se convirtió en Windows 2000.
Luego XP.
Luego Vista.
Luego 7, 8, 10 y 11.

<!-- S92 -->
Los procesadores cambiaron.
El número de núcleos se disparó.
El tamaño de la memoria se disparó.
Las máquinas virtuales pasaron de exóticas
a completamente normales.

<!-- S93 -->
Y la misma familia de código
acabó ejecutándose en servidores
de todo el mundo.

<!-- S94 -->
Servidores de archivos.
Inicios de sesión de empresa.
Máquinas virtuales.
Cargas que nadie imaginó
cuando se diseñó.

<!-- S95 -->
Si la parte que decide
qué se ejecuta y cuándo,
y que reparte la memoria,
estuviera irremediablemente rota...
la factura sería imposible de ocultar.

<!-- S96 -->
Ahora una confesión honesta.
Nadie fuera de Microsoft puede leer
el código fuente del núcleo actual,
así que nadie puede llamarlo bello.

<!-- S96b -->
Aunque a una versión más antigua
sí que alguien la miró.

<!-- S96c -->
Parte del código de Windows 2000
se filtró en 2004,
y el año pasado un investigador
se lo repasó entero.

<!-- S96d -->
Los hallazgos no fueron halagüeños.
Fallos que estuvieron en ese código
dieciséis años
antes de que alguien los parcheara.

<!-- S96e -->
Pero ese es el abuelo
del núcleo de hoy,
y solo se filtró una parte.
Nos dice algo de Windows 2000,
no de ahora.

<!-- S97 -->
Y sobrevivir no es lo mismo
que ser excelente.

<!-- S98 -->
Así que esto no afirma
que el núcleo de Windows sea genial.
Eso no lo sabe nadie.

<!-- S99 -->
Pero sí tenemos décadas de pruebas
de que hace bien su trabajo.

<!-- S100 -->
Y esa es una conclusión mucho más rara
que «Windows es malo».

<!-- S101 -->
Porque significa que la respuesta
a «qué hace su QA»
probablemente no es
«Microsoft no sabe escribir software».

<!-- S102 -->
Es que llevan décadas
construyendo cosas nuevas sobre viejas,
sin que nunca se les permitiera
tirar las viejas.

<!-- S103 -->
El resultado es enorme.
Potente.
Compatible.
Y de vez en cuando ridículo.

<!-- S104 -->
Instalas una actualización.
Se te va el sonido.
El cursor parece de Windows 98.

<!-- S105 -->
Y debajo de todo eso,
algo decide en silencio
qué programa se ejecuta después.
Reparte memoria.
Habla con el hardware.

<!-- S106 -->
Haciendo exactamente
lo que debe hacer.

<!-- S107 -->
Al menos...
eso creemos.

<!-- S108 -->
Porque, a diferencia de la barra...
a él no lo vemos.
