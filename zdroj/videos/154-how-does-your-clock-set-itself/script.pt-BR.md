<!-- S01 -->
Em algum lugar da sua casa,
talvez exista um relógio
que ninguém nunca acertou.

<!-- S02 -->
Ele sobrevive a quedas de energia.
Ele muda para o horário de verão
sozinho, no meio da noite.

<!-- S03 -->
Ele não tem conexão com a internet.
Nada de Wi-Fi, nada de GPS,
nenhum aplicativo no celular.

<!-- S04 -->
Tudo o que ele tem é um minúsculo receptor de rádio.
E uma vez por segundo,
ele ouve um único pulso.

<!-- S05 -->
Então como um relógio
transforma um pulso por segundo
na hora exata, na data
e até no dia da semana?

<!-- S06 -->
Na Europa, esses pulsos vêm
do DCF77, perto de Frankfurt.
Na América, do WWVB, no Colorado.
Transmissores diferentes, a mesma ideia.

<!-- S07 -->
Pegue o transmissor alemão.
Ele envia uma onda de rádio constante,
dia e noite.
E no começo de cada segundo,
ele reduz essa onda por um instante.

<!-- S08 -->
O truque é por quanto tempo
ela fica abaixada.

<!-- S09 -->
Uma queda de um décimo de segundo
significa zero.
Uma queda de dois décimos significa um.

<!-- S10 -->
Essa é toda a ideia.
Nada de pacotes, nada de rede.
Só uma onda de rádio que cai
por um tempo curto, ou um pouco mais longo.

<!-- S11 -->
Um bit por segundo.
Ou seja, levaria um minuto inteiro
para enviar só 60 bits.

<!-- S12 -->
E, na verdade, ele envia só 59.

<!-- S13 -->
No último segundo de cada minuto,
a onda não cai nenhuma vez.
E essa queda que falta
é a parte mais importante
de todo o sinal.

<!-- S14 -->
Porque quando a próxima queda chega,
o relógio sabe
que um novo minuto acabou de começar.

<!-- S15 -->
A lacuna funciona como um ponto final.
Tudo entre duas lacunas
é uma frase completa.

<!-- S16 -->
Então o que cabe numa frase
de 59 bits?

<!-- S17 -->
O minuto. A hora.
O dia do mês, o dia da semana,
o mês e o ano.

<!-- S18 -->
A maioria dos números é enviada dígito por dígito.
47 minutos
não são enviados como 47.
São enviados como dois dígitos separados,
um quatro e um sete.

<!-- S19 -->
4 bits bastam para qualquer dígito
de zero a nove.
As dezenas de minutos nunca passam de cinco,
então ganham só 3.

<!-- S20 -->
E o ano ganha só dois dígitos.
Para o transmissor,
2026 é simplesmente 26.
O relógio completa o século sozinho.

<!-- S21 -->
Mas o rádio não é um canal limpo.
Um motor, um carregador de celular,
uma lâmpada de LED barata...
qualquer um deles pode distorcer uma queda.

<!-- S22 -->
Por isso, depois de cada bloco de números
vem um bit extra, chamado bit de paridade.

<!-- S23 -->
Ele é escolhido para que o número de uns
no bloco sempre dê par.

<!-- S24 -->
Se uma interferência inverter um único bit,
o número de uns fica ímpar,
e o relógio sabe
que algo deu errado.

<!-- S25 -->
Mas se dois bits se inverterem,
a contagem volta a ser par,
e o erro passa despercebido.

<!-- S26 -->
É por isso que muitos relógios
não confiam num único minuto.
Eles esperam por outro minuto válido.

<!-- S27 -->
E é por isso que acertar a hora sozinho
pode levar vários minutos,
e, num dia ruim, muito mais.

<!-- S28 -->
O que cria um problema curioso.

<!-- S29 -->
O relógio passa um minuto inteiro
coletando a hora de 10:48.
Mas enquanto ele coleta essa mensagem,
ainda são 10:47.

<!-- S30 -->
Então, quando ele muda de verdade?

<!-- S31 -->
Porque a mensagem é um aviso.
Ela diz que horas vão ser
quando o próximo minuto começar.

<!-- S32 -->
O relógio lê a frase inteira,
espera passar a queda que falta,
e quando a próxima queda chega,
essa queda é o momento exato.

<!-- S33 -->
Os bits dizem ao relógio que horas são.
A queda diz quando.

<!-- S34 -->
Mas a frase tem algumas palavras a mais
do que só a hora.

<!-- S35 -->
Dois bits dizem se a Alemanha
está no horário de inverno ou de verão.

<!-- S36 -->
E um terceiro é um aviso.
Durante uma hora inteira antes da mudança,
ele fica em um.

<!-- S37 -->
Então seu relógio não precisa saber
em que domingo de março
os relógios avançam uma hora,
nem em que domingo de outubro voltam uma hora.
Ninguém nunca ensinou essa regra a ele.
Ele simplesmente é avisado, com uma hora de antecedência.

<!-- S38 -->
Se a Europa um dia parar de mudar os relógios,
o aviso simplesmente nunca mais vai chegar.

<!-- S39 -->
Outro bit servia para avisar de um segundo intercalar,
um segundo extra acrescentado de vez em quando,
porque a rotação da Terra
não marca o tempo com perfeição.
Aquele minuto podia ter 61 segundos.

<!-- S40 -->
O último foi acrescentado
no fim de 2016.
Mas em outubro de 2026,
as autoridades de metrologia do mundo
decidiram acabar com os segundos intercalares.
A partir de 20 de maio de 2027,
o UTC vai correr sem interrupções.

<!-- S41 -->
E os primeiros 14 bits
de cada minuto
nem são sobre a hora.

<!-- S42 -->
Desde 2006, eles também são usados
para levar previsões do tempo criptografadas
a estações meteorológicas compatíveis.

<!-- S43 -->
Então o sinal que acerta o seu despertador
também podia dizer
à estação meteorológica de outra pessoa
se ia chover na quinta-feira.

<!-- S44 -->
E, mesmo assim, a maioria desses relógios
não fica ouvindo o tempo todo.
Ouvir gasta bateria,
então muitos tentam uma vez por noite,
de madrugada.

<!-- S45 -->
As ondas longas chegam a um relógio por dois caminhos:
ao longo do solo
e refletidas pela alta atmosfera.
Depois que escurece, esse caminho de cima muda,
e o sinal muitas vezes vai mais longe.

<!-- S46 -->
E às três da manhã,
normalmente há menos máquinas, carregadores e luzes
ligados por perto para abafá-lo.

<!-- S47 -->
Entre essas verificações,
o relógio funciona com um cristal de quartzo,
que pode fazer o relógio errar cerca de um segundo por dia.

<!-- S48 -->
Na próxima verificação bem-sucedida,
o rádio corrige esse desvio.

<!-- S49 -->
Até o lugar onde ele escuta importa.
A antena é uma pequena barra de ferrite
enrolada com fio.

<!-- S50 -->
Ela ouve melhor quando a barra fica atravessada
em relação à direção do transmissor,
e não apontando para ele.
Gire o relógio,
e um sinal fraco pode sumir completamente.

<!-- S51 -->
É por isso que um relógio funciona numa prateleira,
e o mesmo relógio, dois metros adiante,
atrás de uma parede de concreto armado, nunca acerta a hora.

<!-- S52 -->
Então de onde o transmissor
tira a hora dele?

<!-- S53 -->
Do PTB,
o instituto nacional de metrologia da Alemanha,
que opera relógios atômicos.

<!-- S54 -->
O próprio segundo é definido
por átomos de césio.
Um segundo é exatamente
9.192.631.770 oscilações
da radiação que eles emitem.

<!-- S55 -->
Então um despertador barato na mesa de cabeceira
está, literalmente,
seguindo um padrão de tempo
definido por átomos de césio.

<!-- S56 -->
Mas não perfeitamente.
O sinal viaja à velocidade da luz,
e mesmo assim leva cerca de 3 milissegundos
a cada 1.000 quilômetros.

<!-- S57 -->
O receptor acrescenta um atraso próprio,
e seu relógio não corrige nada disso.
Nem precisa.
Ele só mostra segundos.

<!-- S58 -->
De um único local perto de Frankfurt,
o sinal chega a relógios
a até cerca de 2.000 quilômetros.
Isso é a maior parte da Europa.

<!-- S59 -->
A Suíça tinha o próprio transmissor,
chamado HBG, até o fim de 2011.
As antenas precisavam ser trocadas,
pouca gente o usava,
e os relógios suíços podiam simplesmente
ouvir a Alemanha.

<!-- S60 -->
Outros mantiveram os seus.
Reino Unido, França, Japão e China
têm, todos, o seu próprio.

<!-- S61 -->
E na América do Norte, o WWVB
transmite de Fort Collins desde 1963,
com um código horário desde 1965.

<!-- S62 -->
Mesmo princípio, outro sotaque.
Um zero é uma queda de dois décimos de segundo.
O 1 dura meio segundo.

<!-- S63 -->
E em vez de uma lacuna por minuto,
vem um marcador mais longo a cada 10 segundos,
como vírgulas na frase.
Dois seguidos indicam um novo minuto.

<!-- S64 -->
A maior diferença
é qual horário ele transmite.
A Alemanha transmite a hora civil da Europa Central,
compartilhada por boa parte do continente.

<!-- S65 -->
Mas os Estados Unidos
abrangem vários fusos horários.
Então o WWVB transmite o tempo universal, o UTC,
e você diz ao relógio onde está.

<!-- S66 -->
Ele nem envia o mês.
Só o dia do ano,
de 1 a 366.

<!-- S67 -->
Nenhuma dessas estações
fala a mesma língua.
Um relógio feito para a Alemanha
não entende nada do Colorado.

<!-- S68 -->
Mas dos dois lados do Atlântico,
é a mesma rotina silenciosa.
Noite após noite, um pequeno receptor
se alinha a um padrão de tempo atômico
a centenas ou milhares de quilômetros.

<!-- S69 -->
Então, uma pergunta para você.
Se todos os sinais horários de rádio
sumissem esta noite,
você sequer perceberia?
Conte para mim nos comentários.
