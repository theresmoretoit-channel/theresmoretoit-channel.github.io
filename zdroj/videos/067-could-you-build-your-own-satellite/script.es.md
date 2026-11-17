<!-- S01 -->
Imagina que tienes una idea loca.
Quieres construir tu propio satélite.
No un satélite de comunicaciones
de mil millones de dólares.
Algo pequeño.

<!-- S02 -->
Una caja del tamaño
de un pan de molde.
Dentro: un ordenador, paneles solares,
una radio, unos sensores.
Puede que hasta una cámara.

<!-- S03 -->
La construyes en tu garaje.
Y luego, de algún modo...
la pones en órbita.
Suena imposible.
Pero no lo es.

<!-- S04 -->
La gente lleva años haciendo
casi exactamente esto.
Se llaman CubeSats.

<!-- S05 -->
Y lo sorprendente
es que lo más difícil
no es construir el satélite.
Es todo lo demás.

<!-- S06 -->
La unidad básica se llama 1U:
un cubo de unos diez centímetros.
Apila varias unidades
y obtienes 2U, 3U, 6U
y más grandes.

<!-- S07 -->
La idea es simple.
En vez de diseñar una nave nueva
desde cero,
reutilizas tamaños estándar
e interfaces estándar.
Y de repente, el espacio se abre
a universidades, startups
y puede que hasta a ti.

<!-- S07b -->
Por cierto, si te gustan
vídeos como este, suscríbete.

Ayuda mucho al canal.

<!-- S08 -->
¿Qué contendría en realidad
nuestro pequeño satélite?
Primero, necesita un ordenador.
Algo tiene que ejecutar el software,
controlar el hardware
y decidir qué hacer.

<!-- S09 -->
Luego, la energía.
Los paneles solares generan electricidad.
Las baterías la almacenan
para cuando el satélite
entra en la sombra de la Tierra.

<!-- S10 -->
Luego, la comunicación.
Una radio. Una antena.
Y aquí, en la Tierra,
una estación terrestre escuchando.

<!-- S11 -->
Luego, los sensores.
Temperatura. Voltaje. Corriente.
Aceleración. Campo magnético.
Y alguna forma de saber
hacia dónde apunta el satélite.
Porque en órbita,
decir "arriba" es sorprendentemente difícil.

<!-- S12 -->
Pero antes de construir uno,
hay una pregunta incómoda.
¿Cuánto cuesta esta cajita?
La respuesta es...
más de lo que parece.

<!-- S13 -->
Un simple CubeSat 1U
puede costar fácilmente
decenas de miles de dólares,
solo en hardware de vuelo.
El sistema de energía. Los paneles solares.
Las baterías. El ordenador. La radio.
El control de actitud. La estructura.
Y la carga útil.

<!-- S14 -->
Luego vienen las cosas
que no están en la lista de piezas.
Pruebas. Integración.
Documentación.
Operación de la estación terrestre.
Licencias.
Y por último...
el lanzamiento.

<!-- S15 -->
Un viaje compartido para un CubeSat diminuto
puede costar decenas de miles.
Misiones mayores y CubeSats mayores
llegan a cientos de miles.
Y eso es solo
poner la cosa en el espacio.

<!-- S16 -->
Y ahora,
un problema aún más ridículo.
¿Recuerdas todas esas piezas?
¿Cómo demonios cabe todo eso
dentro de una cajita?

<!-- S17 -->
En el espacio no hay sitio
para un montón de componentes electrónicos puestos sin orden.
Cada centímetro importa.
Cada gramo importa.
Cada vatio importa.
El satélite es un rompecabezas tridimensional
que tiene que sobrevivir al lanzamiento de un cohete.

<!-- S18 -->
Entonces, ¿de dónde sacas
todas estas piezas?
No tienes que diseñarlo
todo tú mismo.
Hay toda una industria
que vende componentes para satélites pequeños:
ordenadores, sistemas de energía,
radios, antenas y paneles solares.
Hasta existen mercados
hechos específicamente para piezas de CubeSat.

<!-- S18b -->
Y las piezas también están estandarizadas.
Muchas comparten un formato de placa
y simplemente se apilan,
así que piezas de distintos fabricantes
encajan en una sola unidad.
Empresas como EnduroSat
y GomSpace las venden,
y un solo subsistema puede costar
desde unos pocos miles
hasta decenas de miles de dólares.

<!-- S19 -->
Y no son
procesadores exóticos.
Un ordenador actual de CubeSat
usa un ARM Cortex-M7,
con interfaces conocidas:
SPI, I²C, UART y CAN.

<!-- S19b -->
Y no es un chip espacial a medida.
Es una placa real, comercial,
que podrías sostener en la mano.

<!-- S20 -->
Una nave necesita algo
más importante que la velocidad bruta:
comportamiento predecible,
bajo consumo y fiabilidad.
Misiones más exigentes
pueden usar procesadores ARM Cortex-A,
e incluso Linux.

<!-- S20b -->
Pero no es rápido.
Un ordenador típico de CubeSat
funciona a un par de cientos de megahercios.
Tu portátil funciona a
cuatro o cinco gigahercios,
con muchos más núcleos.
Cambia velocidad bruta
por no gastar casi nada de energía.

<!-- S21 -->
Y si eres programador,
aquí es donde se pone interesante.
No escribes
ningún misterioso "lenguaje espacial".
Escribes software embebido.
A menudo en C o C++.

<!-- S22 -->
Puede ejecutarse directamente
sobre el hardware,
o en un sistema operativo de tiempo real
como FreeRTOS, Zephyr o RTEMS.
Hasta hay frameworks abiertos
hechos para naves espaciales.
F Prime, de la NASA, por ejemplo,
es un framework de software de vuelo
para sistemas embebidos y espaciales.

<!-- S23 -->
Así que tu código podría verse
más o menos así.

<!-- S24 -->
Pero hay una diferencia enorme
con un ordenador normal.
No puedes entrar por SSH.
No puedes conectar un depurador.
Y si tu software se cuelga...
tu ordenador está
a unos cientos de kilómetros de altura.

<!-- S25 -->
Así que necesita watchdogs,
modos seguros, detección de fallos
y recuperación automática.
Tiene que arreglar algunos problemas
sin que tú estés ahí para ayudar.

<!-- S25b -->
Y una gran razón por la que necesita todo eso
es la radiación.
En el espacio, los rayos cósmicos
pueden cambiar un bit en la memoria,
o incluso inutilizar un chip.
No hay blindaje pesado:
pesaría demasiado.
En cambio, el ordenador se vigila,
corrige errores
y se reinicia cuando algo sale mal.

<!-- S26 -->
Pero si de verdad
quieres lanzarlo...
la cosa se pone seria.
Una pieza que funciona en tu mesa
no está lista automáticamente
para un cohete.
Tiene que sobrevivir a la vibración,
al vacío, a temperaturas extremas
y a la radiación.

<!-- S27 -->
Ahora, de vuelta a ese problema
de saber hacia dónde
apunta el satélite.
Imagínalo dando vueltas
por el espacio.
Sin suelo. Sin techo.
El GPS puede decirte
dónde estás...
pero no hacia dónde
estás orientado.

<!-- S28 -->
Así que los satélites combinan
giroscopios, magnetómetros
y sensores solares
para calcular su actitud.
Y luego tienen que cambiarla.
Un truco común
es un magnetorquer.

<!-- S29 -->
Se apoya
en el campo magnético de la Tierra
y crea un par diminuto.
No es un motor de cohete.
No desplaza el satélite.
Solo lo gira.
Y eso basta
para orientar el satélite
justo donde quieres.

<!-- S30 -->
Pero nada de esto
es la razón
por la que construimos el satélite.
Necesitamos una misión.
Esa es la carga útil.
Medir radiación.
Fotografiar la Tierra.
Estudiar la atmósfera.
Probar un sensor nuevo.
O simplemente demostrar
que una nueva tecnología funciona.

<!-- S31 -->
El satélite en sí
está ahí sobre todo
para mantener viva la carga útil.
Alimentarla. Orientarla.
Mantenerla caliente.
Guardar sus datos.
Y enviarlos a casa.

<!-- S32 -->
Cuando tu ordenador se cuelga,
lo reinicias.
Cuando tu satélite se cuelga...
tienes un objeto carísimo
orbitando la Tierra en silencio.

<!-- S33 -->
Digamos que lo construimos.
Todo funciona...
El ordenador arranca...
La radio habla.
Los paneles generan energía.
La carga útil funciona...
¿Podemos lanzarlo?
...Todavía no.

<!-- S34 -->
Un satélite tiene que demostrar
que puede sobrevivir al lanzamiento.
Eso significa pruebas.
Muchas pruebas.

<!-- S35 -->
Primero, atorníllalo
a un agitador gigante.
Luego sacúdelo, fuerte...
Eso es la prueba de vibración.
Los lanzamientos de cohetes no son suaves.
Tiene que sobrevivir
al ruido, la vibración y el choque
sin que nada
se suelte o se rompa.
Cada tornillo importa.
Cada conector importa.
Cada trozo de cable importa.

<!-- S36 -->
Luego viene el vacío.
En la Tierra, el aire se lleva el calor.
En el espacio no hay aire.
Un lado puede calentarse muchísimo,
otro enfriarse muchísimo,
y la electrónica
aún tiene que mantenerse
dentro de sus límites.
Así que el satélite necesita
correas térmicas, recubrimientos,
aislamiento
y materiales cuidadosamente elegidos.
Los satélites no tienen
aire acondicionado.
Tienen física.

<!-- S37 -->
Y con la batería
la cosa se pone interesante.
Cárgala con luz solar.
Luego el satélite
entra en la sombra de la Tierra,
y los paneles no generan casi nada.
La batería lo mantiene vivo.
Luego, de vuelta a la luz solar.
Cargar. Descargar.
Cargar. Descargar.
Una y otra vez.
Durante años.
Un fallo en la alimentación
podría acabar con la misión sin hacer ruido.

<!-- S38 -->
Y ahora, ¿cómo hablas con él?
Necesitas una radio.
Una antena.
Y una frecuencia
que puedas usar legalmente.
Y una estación terrestre.
El satélite
no tiene internet.
Solo pasa por encima
y transmite.

<!-- S39 -->
Tu estación terrestre
capta la señal.
El ordenador la decodifica.
Y de repente tienes datos
de tu propia nave espacial.
Imagina abrir un terminal
y ver esto.

Solo que la máquina
que imprime esos números...
está a cientos de kilómetros
sobre tu cabeza.

<!-- S40 -->
Entonces, ¿cómo lo
subimos ahí de verdad?
Podrías construir un cohete...
Por favor, no...
No necesitas uno.
Los CubeSats vuelan
como cargas secundarias.

<!-- S41 -->
Un cohete ya va a subir.
Tiene sitio de sobra.
Tu satélite viaja con él
en un desplegador estándar.
No hace falta un cohete propio.

<!-- S42 -->
Y ahora está colocado
en lo alto de un cohete.
No puedes tocarlo.
No puedes abrir la caja.
No puedes enchufar un cable.
El cohete despega.
Unos nueve minutos después,
estás en órbita.

<!-- S43 -->
El desplegador
libera tu satélite.
Sale disparado
y empieza a dar vueltas.

<!-- S43b -->
¿Pero cómo sabe que ya salió?
...
Unos interruptores con muelle, presionados
mientras estaba en el desplegador,
saltan en cuanto es expulsado,
y el ordenador arranca.
Luego, según las reglas,
se queda callado una media hora.
Solo entonces enciende su radio,
despliega sus antenas
y por fin llama a casa.
Y en algún lugar de la Tierra...
tu estación terrestre lo oye.

<!-- S44 -->
Construiste una máquina.
Y ahora esa máquina
está orbitando el planeta.

<!-- S44b -->
Solo que no hemos terminado.
Un satélite muerto no puede
quedarse ahí arriba para siempre.
Si se deja en órbita durante siglos,
se convierte en basura espacial.

<!-- S45 -->
Eso significa que las misiones modernas
cada vez más tienen que planear
el final
de la vida de la nave.
Idealmente, la fina atmósfera superior
la arrastra despacio hacia abajo.
Su órbita decae.
Reingresa.
Y se quema.
El final de la misión...
es parte de la misión.

<!-- S46 -->
Así que... ¿podrías construir
tu propio satélite?
Técnicamente, sí.
No hace falta ser la NASA.
No hace falta
tener un cohete.
Ni siquiera hace falta necesariamente
una empresa enorme.

<!-- S47 -->
El satélite tiene que
sobrevivir al lanzamiento.
Sobrevivir al espacio.
Transmitir legalmente.
Funcionar por su cuenta.
Y, al final,
salir de órbita.
Todo eso
tiene que demostrarse
antes de que alguien
lo ponga en un cohete.

<!-- S48 -->
Los CubeSats no simplificaron el acceso al espacio.
Lo estandarizaron.
En vez de construir todo
desde cero,
puedes construir algo
que encaje en un estándar existente.
Y ese es un cambio sorprendentemente grande.

<!-- S49 -->
Así que, en algún lugar, ahora mismo,
hay pequeñas máquinas
orbitando la Tierra.
Construidas por universidades,
equipos de investigación,
empresas y estudiantes.

<!-- S50 -->
Algunas llevan cámaras.
Algunas miden radiación.
Algunas prueban
tecnología totalmente nueva.
Y algunas son solo experimentos
que hacen una pregunta:
"¿podemos hacer que esto
funcione en el espacio?"

<!-- S51 -->
Y eso es lo que hace
que construir tu propio satélite
sea tan fascinante.
Porque la distancia
entre tú y el espacio
ya no es un cohete.
Podría ser...
una caja de diez centímetros.
Y una lista de comprobación
muy, muy larga.
