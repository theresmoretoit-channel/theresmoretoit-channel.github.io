<!-- S01 -->
Haces clic en un botón.
No pasa nada.
Vuelves a hacer clic.
Sigue sin pasar nada.

<!-- S02 -->
Mueves el ratón.
Nada.
Durante unos segundos,
el ordenador parece muerto.

<!-- S03 -->
Y entonces pasa todo de golpe.
La ventana se mueve.
El menú se abre.
Todos tus clics llegan,
todos juntos.

<!-- S04 -->
Y aquí viene lo raro.
El ordenador sabía que habías hecho clic.
Lo supo en microsegundos.

<!-- S05 -->
No es una suposición.
Ahora mismo, mientras
no haces nada en particular,
tu máquina atiende miles
de eventos de hardware por segundo.

<!-- S06 -->
Una tecla que se pulsa.
Un paquete que llega.
Un temporizador que salta.
Un disco que termina.

<!-- S07 -->
Cada uno de ellos es una interrupción,
y los ordenadores lo hacen así
desde los años cincuenta,
exactamente para esto:

<!-- S08 -->
para que un procesador pueda reaccionar
al mundo que hay fuera de él.

<!-- S09 -->
El hardware avisó de tu clic.
El procesador se enteró.
Y tú seguiste cinco segundos
mirando una pantalla muerta.

<!-- S10 -->
¿No debería ir primero el usuario?

<!-- S11 -->
Hay una respuesta,
y no es
que tu ordenador sea lento.

<!-- S12 -->
Es que ser advertido
y ser atendido
son dos cosas completamente distintas.

<!-- S13 -->
Empecemos por lo de advertir.
Imagina un ordenador sin interrupciones.

<!-- S14 -->
El procesador tendría
que preguntar una y otra vez:
¿ha llegado algo del teclado?
¿ha terminado el disco?

<!-- S15 -->
¿Ha llegado un paquete?
¿Se ha movido el ratón?
Y volver a preguntar.
Y otra vez.

<!-- S16 -->
Casi todas las respuestas serían no,
y el propio preguntar
se comería la máquina viva.

<!-- S17 -->
Así que los aparatos consiguieron
levantar la mano. El ratón se mueve,
el hardware lanza una interrupción,

<!-- S18 -->
y el procesador suelta
lo que estuviera haciendo,
salta a un trozo corto de código
que se llama manejador,

<!-- S19 -->
y el sistema operativo se entera
de que ha pasado algo.

<!-- S20 -->
Es una idea genial.
Y lleva a una suposición
de lo más razonable.

<!-- S21 -->
Si se puede arrancar al procesador
de cualquier cosa, al instante,
entonces mi clic también
se atenderá al instante.

<!-- S22 -->
Salvo que el manejador no tiene
permiso para hacer casi nada.

<!-- S23 -->
Mientras el procesador está dentro,
todo lo demás espera.
Incluida la siguiente interrupción.
Y esa ya viene de camino.

<!-- S24 -->
La regla es justo la contraria
de lo que uno esperaría.
El manejador hace lo mínimo
que puede hacer.

<!-- S25 -->
Anota lo que ha pasado.
Le confirma al aparato
que el mensaje ha llegado.
Deja el evento en una cola.
Y se va.

<!-- S26 -->
Quienes escriben núcleos incluso
parten el trabajo en dos mitades:
lo que tiene que ocurrir ahora,
y lo que puede esperar.

<!-- S27 -->
Todo lo interesante,
todo lo que llegarás a ver,
está en la segunda mitad.

<!-- S28 -->
Y ahí está la primera respuesta.
Una interrupción consigue
la atención del ordenador.

<!-- S29 -->
No mete tu programa
en un procesador.

<!-- S30 -->
Vale, dirás. Pues arréglalo.
Haz que la entrada sea lo más
importante de toda la casa.

<!-- S31 -->
¿El ratón? Prioridad máxima.
¿El teclado? Prioridad máxima.
¿La ventana que tienes delante?
Prioridad máxima.

<!-- S32 -->
Todo lo demás que espere su turno.
Suena de lo más razonable.

<!-- S33 -->
Y la mejor objeción a eso
ocurrió en Marte.

<!-- S34 -->
En 1997 el módulo Pathfinder
aterrizó y se puso a trabajar.
Luego, unos días después,
empezó a reiniciarse solo.

<!-- S35 -->
No fue un rayo cósmico.
No fue una pieza rota.
Fue un problema de planificación.

<!-- S36 -->
Había una tarea de prioridad alta
que repartía datos
por toda la sonda,
y necesitaba memoria compartida.

<!-- S37 -->
Una tarea de prioridad baja,
que recogía datos meteorológicos,
había llegado antes
y la tenía cogida.

<!-- S38 -->
Lo cual, por un momento,
no habría pasado nada.
Pero entonces una tarea de prioridad
media se llevó el procesador,

<!-- S39 -->
y la de prioridad baja
nunca llegó a terminar.
Así que nunca la soltó.

<!-- S40 -->
La tarea más importante
de toda la sonda
estaba ahora atascada detrás
de la menos importante de todas.

<!-- S41 -->
Tiene nombre.
Inversión de prioridad.

<!-- S42 -->
Un temporizador de vigilancia vio
que la tarea importante
llevaba demasiado sin ejecutarse,
dio por hecho un desastre

<!-- S43 -->
y reinició la sonda entera.
Luego volvió a pasar.
Y otra vez.

<!-- S44 -->
Unos ingenieros en la Tierra
lo entendieron y mandaron un arreglo.

<!-- S45 -->
Y la lección no nos cuesta
absolutamente nada.
Prioridad alta no significa
que te atiendan.

<!-- S46 -->
Solo significa que te preguntan antes.
Si lo que necesitas
lo tiene alguien más lento,
tu importancia no te compra nada.

<!-- S47 -->
Y la prioridad tiene un segundo límite.
Decide el orden.
No crea ni un solo
ciclo de más.

<!-- S48 -->
Supongamos que todos tus núcleos
están al cien por cien.
Dirás que eso significa congelado.
Normalmente no lo significa.

<!-- S49 -->
El planificador reparte trozos de tiempo
tan deprisa
que no notas las transiciones.

<!-- S50 -->
Por eso puedes compilar
algo enorme
y a la vez desplazar
una página web.

<!-- S51 -->
Con carga, lo que cambia
no es tanto la velocidad.
El ordenador no es lento.

<!-- S52 -->
Llega tarde.

<!-- S53 -->
Haces clic y la respuesta llega
medio segundo después.
Luego un segundo.
Luego cinco.

<!-- S54 -->
Y la gente se da cuenta de eso
extraordinariamente bien.
Medio segundo parece una máquina
que está pensando.

<!-- S55 -->
Cinco segundos parecen una máquina
que se ha muerto.

<!-- S56 -->
Y hay una versión de esto
que sorprende todavía más.
A veces el problema no está
en el procesador.

<!-- S57 -->
Abre demasiadas cosas a la vez
y la memoria física se llena.
El sistema empieza a mover
páginas de memoria al disco.

<!-- S58 -->
Que se junte bastante de eso
y la máquina se pasa el tiempo
moviendo memoria
en vez de hacer tu trabajo.

<!-- S59 -->
Esto también tiene nombre.
Hiperpaginación.

<!-- S60 -->
Y aquí viene lo confuso,
porque el procesador
puede no parecer ocupado.

<!-- S61 -->
No está trabajando.
Está esperando.

<!-- S62 -->
Puedes darle a una tarea que espera
la prioridad más alta del sistema
y esperará exactamente
lo mismo que antes.

<!-- S63 -->
Y luego está la versión
más humana de todo esto.
El evento llegó.
El núcleo lo tiene.

<!-- S64 -->
Está en una cola
con el nombre de tu programa.
Y tu programa
no lo está recogiendo.

<!-- S65 -->
A lo mejor está haciendo un cálculo
largo en el mismo hilo
que debería estar vigilando
su propia ventana.

<!-- S66 -->
Así que el ratón funciona.
El teclado funciona.
Los demás programas funcionan.

<!-- S67 -->
Y esa ventana se atenúa
y dice que no responde.

<!-- S68 -->
Y eso no es un diagnóstico.
Windows le pone ese cartel
al cabo de unos cinco segundos
sin que nadie recoja los mensajes.

<!-- S69 -->
El sistema está perfectamente vivo.
Es la aplicación
la que no ha salido a la puerta.

<!-- S70 -->
Que el ordenador reciba tu clic
y que la aplicación te conteste
no son el mismo evento.

<!-- S70b -->
Por cierto, si quieres ver
adónde nos lleva la próxima pregunta,
plantéate suscribirte.

Ayuda mucho al canal.
<!-- S71 -->
Queda un eslabón más,
y es justo aquel
en el que nunca pensamos.
Nada de esto ha puesto todavía
nada en tu pantalla.

<!-- S72 -->
La aplicación cambia su estado.
Alguien tiene que armar el fotograma.
La tarjeta gráfica tiene que dibujarlo.
La pantalla tiene que mostrarlo.

<!-- S73 -->
En una pantalla corriente
aparece una imagen nueva
cada dieciséis milisegundos.

<!-- S73b -->
Así que hay diferencia entre
que el ordenador atienda tu clic
y que tú lo veas.

<!-- S74 -->
Y debajo de todo esto
está la parte
que no arregla ninguna ingeniería.
El sistema operativo sabe
que el ratón se ha movido.
No tiene ni idea de por qué.

<!-- S75 -->
A lo mejor estás apuntando
en un juego.
O editando un documento.
O has dado un golpe a la mesa.

<!-- S76 -->
Para el hardware
son el mismo evento.
Un sistema sabe ordenar trabajos.
Adivinar, no sabe.

<!-- S77 -->
Así que hace un compromiso.
Bastante rápido para ti,
casi siempre,
sin dejar a lo demás esperando sin fin.

<!-- S78 -->
Lo que nos devuelve
a aquella pantalla muerta.
Tu clic nunca fue un solo evento.

<!-- S79 -->
El hardware tiene que avisarlo.
El núcleo tiene que guardarlo.
La cola tiene que llegar al programa.

<!-- S80 -->
Tu programa tiene que ejecutarse.
La interfaz tiene que cambiar.
Alguien tiene que dibujar el fotograma,
y la pantalla tiene que enseñártelo.

<!-- S81 -->
Cada uno de esos pasos
es pequeño y rápido.

<!-- S82 -->
Retrasa cualquiera de ellos
y no vivirás
una ventana lenta.

<!-- S83 -->
Vivirás un ordenador muerto.

<!-- S84 -->
Y lo más extraño de todo esto
es lo poco
que llega a pasar.

<!-- S85 -->
Esperamos que una máquina
que hace miles de millones
de operaciones por segundo
responda a un gesto mínimo de la mano.

<!-- S86 -->
Y casi siempre responde.

<!-- S87 -->
Así que la próxima vez que hagas clic
y no pase nada,
dale un momento.

<!-- S88 -->
Te ha oído.

<!-- S89 -->
Solo que tenía una cola,
y tú estabas en ella.
