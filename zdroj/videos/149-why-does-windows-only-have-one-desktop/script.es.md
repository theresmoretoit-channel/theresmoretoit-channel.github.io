<!-- S01 -->
Imagina que enciendes un PC con Windows
y no encuentras barra de tareas, ni botón de Inicio,
ni un solo icono en el escritorio.

<!-- S02 -->
En su lugar hay una barra fina arriba,
un menú que aparece dondequiera que hagas clic
y cuatro escritorios virtuales uno al lado del otro.

<!-- S03 -->
Parece Linux.
Pero tus programas, tus controladores y tus archivos
están exactamente donde los dejaste.
Sigue siendo Windows.

<!-- S04 -->
Solo ha cambiado el escritorio.
Y el interruptor que lo cambia
es un único ajuste.

<!-- S05 -->
Windows lo guarda en el registro,
en un valor llamado Shell.
En casi todos los PC con Windows,
ahí pone explorer.exe.

<!-- S06 -->
Escribe ahí el nombre de otro programa,
cierra sesión y vuelve a iniciarla,
y Windows arrancará ese programa en su lugar.
Lo que dibuje se convierte en tu escritorio.

<!-- S07 -->
Y no es un truco que alguien descubrió el año pasado.
En 1990, Windows 3.0 ya tenía el mismo interruptor
en un simple archivo de texto llamado system.ini.
Una línea: shell=progman.exe.

<!-- S08 -->
Si cambiabas ese nombre,
el Administrador de programas, la ventana llena de grupos de iconos,
ni siquiera aparecía.

<!-- S09 -->
Así que la pregunta no es si Windows
puede tener otro escritorio.
Siempre ha podido.
La pregunta es por qué casi nadie ha visto uno.

<!-- S10 -->
Empecemos por aquello a lo que apunta de verdad esa línea.
La barra de tareas, los iconos del escritorio,
la pequeña área de notificación junto al reloj:
todo eso es un solo programa, explorer.exe.

<!-- S11 -->
Sí, el mismo explorer.exe
que abres para ver tus archivos: el Explorador de archivos.
Hace dos trabajos,
y casi todo el mundo solo se fija en uno.

<!-- S12 -->
Ese segundo trabajo tiene nombre: el shell.
Es la capa que tocas.
Debajo están el núcleo, los controladores
y los servicios que mantienen Windows en marcha.

<!-- S13 -->
Ninguno de ellos necesita una barra de tareas.
Finaliza explorer.exe en el Administrador de tareas
y la barra de tareas y los iconos desaparecen...
pero el Bloc de notas, tu navegador
y todas las demás ventanas siguen funcionando.

<!-- S14 -->
Vuelve a iniciarlo y el escritorio regresa.
Es casi la prueba más clara que existe
de que el escritorio es solo otro programa.

<!-- S14b -->
Si alguna vez has cambiado el launcher
de un móvil Android,
ya has visto una idea parecida.
Android lo convierte en un ajuste normal.
Windows también tiene el mecanismo,
pero nunca dio a los usuarios corrientes
un botón sencillo para usarlo.

<!-- S15 -->
Aquí se confunden tres términos.
El shell es desde donde abres las cosas:
la barra de tareas, los menús, el escritorio.
Un gestor de ventanas controla cómo las ventanas
se colocan, se apilan y reciben el foco.
Un entorno de escritorio
integra todas esas piezas.

<!-- S16 -->
En Linux, estas piezas se pueden combinar
de muchas maneras distintas.
En Windows, sustituir el shell
no sustituye la gestión de ventanas del sistema
ni la forma en que las aplicaciones dibujan los marcos de sus ventanas.

<!-- S17 -->
Eso no impidió que la gente lo intentara.
A principios de los 90 podías entrar en una tienda
y comprar un sustituto del Administrador de programas.

<!-- S18 -->
Norton Desktop for Windows
te daba su propio escritorio,
sus propias herramientas de archivos y su propio lanzador,
sobre el mismo Windows de siempre.

<!-- S19 -->
Algunos fabricantes lo sustituían
antes de que el cliente encendiera el ordenador.
El Navigator de Packard Bell recibía a los compradores
con una casa que se podía recorrer habitación por habitación.

<!-- S20 -->
Luego Windows 95 le pasó el trabajo a explorer.exe,
y la línea de system.ini
simplemente cambió a explorer.exe.
El interruptor siguió exactamente donde estaba.

<!-- S21 -->
A finales de los 90
creció toda una comunidad en torno a ese interruptor.
El proyecto más conocido fue LiteStep.

<!-- S22 -->
Tomó su aspecto de AfterStep,
un gestor de ventanas de Unix inspirado en NeXTSTEP,
de la empresa que Steve Jobs fundó tras dejar Apple.

<!-- S23 -->
LiteStep no tenía menú Inicio a menos que te lo montaras.
Todo era un módulo:
un dock aquí, un reloj allá,
un menú que se abría dondequiera que hicieras clic derecho.

<!-- S24 -->
Los temas se compartían como fondos de pantalla.
Algunos parecían futuristas.
Otros, una estación de trabajo Unix.
Otros apenas dejaban nada en la pantalla.

<!-- S25 -->
Blackbox for Windows fue en la dirección contraria.
Copiaba Blackbox, un gestor de ventanas minimalista de Unix,
hasta quedarse en un único menú sencillo
y una barra de herramientas fina.

<!-- S26 -->
Su sucesor, bbLean,
mantuvo viva esa idea en Windows 2000 y XP.

<!-- S27 -->
Emerge Desktop dividió el shell en partes separadas:
un lanzador, un área de notificación, una lista de tareas,
cada una un pequeño programa que podías conservar o quitar.

<!-- S28 -->
¿Por qué tomarse tantas molestias?
En parte porque el aspecto de XP
era fácil de reconocer y difícil de cambiar.
Los temas cambiaban los colores y los botones.
La distribución no cambiaba.

<!-- S29 -->
En parte, por la memoria.
En una máquina con 128 megabytes,
un shell más ligero prometía más espacio
para todo lo demás.

<!-- S30 -->
Y en parte, por Linux.
Allí, elegir el escritorio era normal,
y algunos usuarios de Windows querían
poder elegir también.

<!-- S31 -->
La mayoría de esos proyectos ya no existe.
La última versión de LiteStep fue una versión preliminar
de 2014, todavía marcada como alfa.
Emerge Desktop y SharpEnviro también se abandonaron.

<!-- S32 -->
Parte del motivo fue que los equipos de voluntarios eran pequeños.
Pero Windows también cambió.
Con los años, su escritorio pasó a ser mucho más
que un solo ejecutable.

<!-- S33 -->
Hoy la experiencia del escritorio está repartida
entre varios procesos,
componentes del sistema y aplicaciones empaquetadas.
Hasta el menú Inicio funciona como un programa aparte.

<!-- S34 -->
Sustituir explorer.exe no significa sustituir
todo lo que forma la interfaz moderna de Windows.
Y esa es una de las razones por las que construir
un escritorio alternativo completo
es más difícil que antes.

<!-- S35 -->
Y aun así, sigue funcionando.
Cairo Desktop, un proyecto de código abierto,
funciona hoy en Windows 11.

<!-- S36 -->
Trae su propia barra de menús arriba,
su propia barra de tareas
y carpetas que puedes anclar a la barra como pilas.

<!-- S37 -->
Puede funcionar junto a explorer.exe
o tomar el relevo como shell.
En ese segundo modo,
algunas partes de Windows 11 pueden fallar,
entre ellas Configuración y Seguridad de Windows.

<!-- S38 -->
Seelen UI lo hace de otra manera.
No sustituye a explorer.exe.
Oculta la barra de tareas y trae sus propias piezas:
un dock, una barra, widgets
y un gestor de ventanas que coloca tus ventanas en mosaico.

<!-- S39 -->
El resultado puede no parecerse en nada a Windows.
Pero por debajo, explorer.exe sigue funcionando.
Es una cara nueva, no un shell nuevo.

<!-- S40 -->
¿Y Microsoft?
En realidad tiene una función oficial para esto.
Se llama Shell Launcher
y está pensada para dispositivos como quioscos.

<!-- S41 -->
Probablemente hayas usado algo así
sin saberlo.
La máquina de billetes de una estación.
Una caja de autopago. Un cajero automático.

<!-- S42 -->
Muchos de ellos son PC con Windows
cuyo shell entero es una sola aplicación.
Un administrador indica el programa
y, tras iniciar sesión, ese programa es todo el escritorio.

<!-- S43 -->
Pero solo está disponible
en las ediciones Enterprise, Education
e IoT Enterprise.

<!-- S44 -->
Y el mecanismo antiguo del registro
sigue formando parte de Windows.
Lo que pasa es que Microsoft nunca lo convirtió
en un ajuste normal del escritorio
para los usuarios corrientes.

<!-- S45 -->
Entonces, ¿por qué parece que Windows solo tiene un escritorio?
No porque no pueda tener otro.
Sino porque el escritorio es el producto.

<!-- S46 -->
En Linux, el escritorio es una elección.
Algunas distribuciones te piden que elijas uno
mientras todavía estás instalando.
KDE Plasma, GNOME, Xfce, Cinnamon...

<!-- S47 -->
En Windows, el escritorio es lo que Microsoft muestra
en cada anuncio, en cada captura de pantalla
y en cada página de soporte.
Un solo escritorio significa un solo conjunto de instrucciones
para más de mil millones de equipos.

<!-- S48 -->
Es una ventaja real.
Cuando algo se rompe,
la pantalla del artículo de ayuda se parece a la tuya.
El precio es que la mayoría nunca se entera
de que había elección.

<!-- S49 -->
La gente cambiaba el escritorio de Windows
antes incluso de que existiera Windows 95.
Construyeron docks, menús mínimos
y escritorios que no se parecían a ningún otro.

<!-- S50 -->
La mayoría de esos proyectos ya no están.
La idea sí.
Bajo cada barra de tareas en la que hayas hecho clic,
sigue estando ese único ajuste, esperando otro nombre.

<!-- S51 -->
El escritorio es solo otra pieza de software.
Y el software se puede sustituir.

<!-- S52 -->
Así que aquí va una pregunta para ti.
Si Windows te dejara elegir el escritorio
al instalarlo, como hacen algunas distribuciones de Linux,
¿cambiarías o te quedarías con el que conoces?
Cuéntamelo en los comentarios.
