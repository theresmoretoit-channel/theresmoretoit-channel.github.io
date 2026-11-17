<!-- S01 -->
El 19 de julio de 2024,
una empresa de seguridad llamada CrowdStrike
envió una actualización rutinaria.

<!-- S02 -->
No era un programa nuevo.
Solo un pequeño archivo de configuración.

<!-- S03 -->
En pocas horas, 8,5 millones
de ordenadores con Windows se habían quedado parados
en una pantalla azul.

<!-- S04 -->
Las aerolíneas suspendieron vuelos.
Los hospitales cancelaron operaciones.
Un canal de noticias dejó de emitir.

<!-- S05 -->
Y el error que había detrás
era de lo más corriente.
El programa esperaba 20 datos.
La actualización le dio 21.

<!-- S06 -->
Tus juegos y tus apps cometen
errores así todo el tiempo.
Cuando pasa, el juego se cierra
y lo vuelves a abrir.

<!-- S07 -->
El mismo tipo de fallo.
Uno cierra una ventana.
El otro detiene
8,5 millones de máquinas.

<!-- S08 -->
La diferencia no está en el error.
Está en dónde se ejecutaba el código.

<!-- S09 -->
Entonces, ¿por qué un programa no puede
apoderarse de tu ordenador...
y por qué este sí pudo?

<!-- S10 -->
No siempre fue así.

<!-- S11 -->
En un PC con DOS en los años 80,
nada en el procesador detenía a un programa.
Podía escribir en cualquier parte de la memoria
y hablar directamente con el hardware.

<!-- S12 -->
Bastaba con que un programa escribiera
donde no debía
para sobrescribir el sistema operativo,
y la máquina entera se colgaba.

<!-- S13 -->
La solución fue dejar de fiarse de los programas
y hacer que fuera el procesador
el que desconfiara.

<!-- S14 -->
En 1982, el procesador 80286 de Intel
introdujo el modo protegido,
con cuatro niveles de privilegio.

<!-- S15 -->
Suelen dibujarse
como cuatro anillos, uno dentro de otro.

<!-- S16 -->
El anillo 0 está en el centro.
El anillo 3, por fuera.

<!-- S17 -->
Y la numeración va al revés.
Cuanto más bajo el número,
más puede hacer el código.

<!-- S18 -->
El anillo 0 es del kernel,
el núcleo del sistema operativo.
Reparte la memoria,
decide qué programa se ejecuta a continuación
y habla con el hardware.

<!-- S19 -->
En el anillo 3 se ejecutan tu navegador,
tus juegos y tu editor de texto.
Esto se llama modo usuario.

<!-- S19b -->
Windows, macOS y Linux
reparten el trabajo de esta manera.
El kernel en el anillo 0,
tus apps en el anillo 3.

<!-- S19c -->
Los móviles y los Mac más nuevos de Apple
usan en cambio chips ARM.
Allí, los niveles se llaman exception levels.
Otro nombre, la misma división:
uno para el kernel, otro para tus apps.

<!-- S20 -->
El procesador siempre sabe
en qué anillo se está ejecutando.
Y lo comprueba.

<!-- S21 -->
Algunas instrucciones solo funcionan en el anillo 0.
Desactivar las interrupciones, por ejemplo,
o cambiar cómo se mapea la memoria.

<!-- S22 -->
Cuando un programa del anillo 3 intenta usar una,
el procesador se niega.
Lanza una excepción
y pasa el control al kernel,
que normalmente cierra el programa.

<!-- S23 -->
Con la memoria pasa lo mismo.
Cada página de memoria está marcada
como user o como supervisor.

<!-- S24 -->
Un programa del anillo 3
que toca una página de supervisor
no recibe los datos.
Lo detienen.

<!-- S25 -->
Tu navegador y tu juego
se ejecutan los dos en el anillo 3.
Lo que los mantiene separados
es que cada uno tiene su propio mapa de memoria.
La memoria del otro programa
simplemente no aparece en él.

<!-- S26 -->
Así que cuando un juego se cuelga,
el daño se queda dentro del juego.
El kernel lo limpia todo.
Todo lo demás sigue funcionando.

<!-- S27 -->
Ahora vuelve a mirar CrowdStrike.
Su driver se ejecutaba en el anillo 0,
justo al lado del kernel.

<!-- S28 -->
Por encima del anillo 0 no hay nada
que pueda atrapar un error así.

<!-- S29 -->
Así que Windows hizo lo único seguro que quedaba.
Detuvo la máquina entera, a propósito,
en lugar de seguir con una memoria
de la que ya no podía fiarse.

<!-- S30 -->
Eso es la pantalla azul.

<!-- S31 -->
Y como el driver arrancaba
cada vez que arrancaba Windows,
cada reinicio traía de vuelta el fallo.

<!-- S32 -->
Pero esto plantea una pregunta.
Si tu navegador no puede tocar el hardware,
¿cómo consigue guardar un archivo
o enviar algo por la red?

<!-- S33 -->
Lo pide.

<!-- S34 -->
El programa pone su petición
en los registros del procesador.
Qué archivo. Adónde van los datos.
Cuántos son.

<!-- S35 -->
Luego ejecuta una instrucción especial.
En un PC moderno, se llama SYSCALL.

<!-- S36 -->
En ese instante, el procesador pasa
del anillo 3 al anillo 0...

<!-- S37 -->
pero no salta
adonde quiera el programa.
Salta a un único punto de entrada
que el kernel eligió de antemano.

<!-- S38 -->
El kernel comprueba la petición,
hace el trabajo
y vuelve al anillo 3.
El programa nunca tocó el disco por sí mismo.

<!-- S39 -->
Esto es una llamada al sistema,
y ocurre constantemente.

<!-- S40 -->
Las contamos en un portátil.
Un programa que no hace absolutamente nada
aun así hace 30.

<!-- S41 -->
Firefox, al arrancar
y cargar una página de Wikipedia,
hizo unas 670 000
en 20 segundos...
y eso que nuestro recuento lo ralentizaba.

<!-- S42 -->
Cada una de ellas
es un viaje a través del muro, de ida y vuelta.

<!-- S43 -->
Y aquí queda algo raro.
Cuatro anillos,
y solo hemos necesitado dos.

<!-- S44 -->
¿Qué pasó con los anillos 1 y 2?

<!-- S45 -->
La idea de los anillos es anterior al PC.
Multics, un sistema operativo
de finales de los años 60,
tenía ocho.

<!-- S46 -->
La idea eran capas de confianza.
El núcleo del sistema en el centro,
servicios menos fiables a su alrededor
y los programas por fuera.

<!-- S46b -->
Intel dibujó el mismo esquema.
Los anillos 1 y 2 estaban pensados
para las capas intermedias,
como los drivers y los servicios del sistema.
Más confianza que tus apps,
menos que el kernel.

<!-- S47 -->
Dos cosas se interpusieron.

<!-- S48 -->
Primero, sistemas como Unix y Windows NT
estaban diseñados para funcionar
en muchos tipos de procesador.

<!-- S49 -->
Y la única división
que ofrecían todos los procesadores
eran dos niveles.
Uno para el kernel,
otro para todo lo demás.

<!-- S50 -->
Segundo, el propio procesador x86.
Cuando mapea la memoria,
cada página solo conoce dos estados.
User o supervisor.

<!-- S51 -->
Los anillos 1 y 2 cuentan como supervisor.
Así que un driver en el anillo 1
podría tocar igualmente la memoria del kernel.
El anillo extra no protegería gran cosa.

<!-- S51b -->
Aun así, algunos sistemas los usaron.
OS/2 dejaba que algunos programas pasaran al anillo 2,
solo para hablar directamente con el hardware.

<!-- S51c -->
Y antes de que los procesadores tuvieran ayuda
para ejecutar máquinas virtuales,
Xen y VirtualBox movían el kernel del sistema invitado
al anillo 1,
para que el sistema de debajo
pudiera quedarse el anillo 0 para sí.

<!-- S52 -->
En 2023, Intel propuso
eliminar del todo los anillos 1 y 2.

<!-- S53 -->
En diciembre de 2024, abandonó el plan.
Siguen estando en tu procesador.
Casi nada los usa.

<!-- S54 -->
Hasta aquí, suena tranquilizador.
Las reglas están en el hardware,
y el hardware comprueba cada acceso.

<!-- S55 -->
En 2017, tres equipos de investigadores,
trabajando por separado,
encontraron una forma de atravesar ese muro.

<!-- S56 -->
Lo llamaron Meltdown.
Y para entenderlo,
necesitas conocer un truco
que usan los procesadores modernos.

<!-- S57 -->
Un procesador no espera
a que termine una instrucción
para empezar la siguiente.
Se adelanta
con instrucciones que probablemente va a necesitar.

<!-- S58 -->
Si se equivocó,
tira los resultados,
como si no hubiera pasado nada.

<!-- S59 -->
Aquí está el fallo.
En los chips de Intel afectados,
un programa del anillo 3 podía pedir
un byte de la memoria del kernel...

<!-- S60 -->
y el procesador lo traía
y se lo pasaba a las siguientes instrucciones
antes de terminar de comprobar
si eso estaba permitido.

<!-- S61 -->
La comprobación sí fallaba.
El resultado se descartaba.

<!-- S62 -->
Pero esas siguientes instrucciones
ya habían usado el byte secreto
para traer un trozo
de la propia memoria del programa
a la caché del procesador.

<!-- S63 -->
Y la caché no olvida
solo porque el resultado se haya cancelado.

<!-- S64 -->
Así que el programa mide
lo rápido que responde cada trozo de su memoria.
El que responde rápido
delata el byte secreto.

<!-- S65 -->
Byte a byte,
un programa normal podía leer
la memoria del kernel
y cualquier secreto que hubiera en ella.
Contraseñas y claves de cifrado incluidas.

<!-- S66 -->
Meltdown afectaba a procesadores Intel
fabricados desde 1995.

<!-- S67 -->
Se hizo público
el 3 de enero de 2018.

<!-- S68 -->
El arreglo no podía cambiar el silicio.
Así que los sistemas operativos cambiaron el mapa.

<!-- S69 -->
Mientras tu programa se ejecuta,
la memoria del kernel ahora se quita
casi por completo de su mapa.
Ahí ya no hay nada que traer.

<!-- S70 -->
Pero acuérdate de las llamadas al sistema.
Cada viaje a través del muro
ahora tiene que cambiar también el mapa.

<!-- S71 -->
Red Hat midió los parches contra Meltdown
y un fallo relacionado, Spectre.
Menos del 1 % en algunas tareas...
hasta un 19 % en bases de datos con mucha carga.

<!-- S72 -->
La regla era correcta desde el principio.
El procesador solo la comprobaba demasiado tarde.

<!-- S73 -->
Lo que nos devuelve a CrowdStrike
y a una pregunta más difícil.

<!-- S74 -->
¿Por qué estaba un programa de seguridad
en el anillo 0, para empezar?

<!-- S75 -->
Porque desde ahí lo ve todo.
Arranca antes que el resto del software.
Y al malware con permisos de administrador
le cuesta más desactivarlo.

<!-- S76 -->
La propia lista de Microsoft
termina con una advertencia.
Los drivers del kernel lo dan a costa de la resiliencia del sistema.

<!-- S77 -->
Después del apagón,
Microsoft empezó a desarrollar una forma
de que los antivirus
funcionen fuera del kernel.

<!-- S78 -->
En otoño de 2026,
sigue estando solo en versiones de prueba de Windows.
Y el kernel no se ha cerrado
a las empresas de seguridad.

<!-- S79 -->
Tus juegos se enfrentan al mismo dilema.

<!-- S80 -->
Los trucos que se ejecutan en el kernel
son invisibles para un anticheat
que se ejecuta en el anillo 3.

<!-- S81 -->
Así que el anticheat también se mudó allí.
Vanguard, de Riot, el que usa Valorant,
mete un driver en el anillo 0.
En la mayoría de los PC, se carga al arrancar Windows...
aunque nunca abras el juego.

<!-- S82 -->
Eso no lo convierte en defectuoso.
Pero está en el mismo sitio
donde estaba el driver de CrowdStrike,
donde un solo error detiene la máquina entera.

<!-- S83 -->
Entonces, ¿por qué un programa no puede
apoderarse de tu ordenador?

<!-- S84 -->
Porque el procesador mantiene
a casi todos los programas fuera del centro
y los comprueba cada vez que llaman a la puerta.

<!-- S85 -->
Pero el procesador no puede decidir
a quién se deja entrar.
Eso lo deciden las personas...
cada vez que instalan un driver.

<!-- S86 -->
Así que aquí va una pregunta para los comentarios.
¿Quién debería decidir qué programas
entran en el anillo 0:
tú, Microsoft
o las empresas que los fabrican?
