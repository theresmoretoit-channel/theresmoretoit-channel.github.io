<!-- S01 -->
Imagine que você tem uma ideia maluca.
Você quer construir seu próprio satélite.
Não um satélite de comunicações
de um bilhão de dólares.
Algo pequeno.

<!-- S02 -->
Uma caixa mais ou menos do tamanho
de um pão de forma.
Dentro: um computador, painéis solares,
um rádio, alguns sensores.
Talvez até uma câmera.

<!-- S03 -->
Você a constrói na sua garagem.
E aí, de algum jeito...
você a coloca em órbita.
Parece impossível.
Mas não é.

<!-- S04 -->
As pessoas fazem quase
exatamente isso há anos.
São chamados de CubeSats.

<!-- S05 -->
E o surpreendente
é que a coisa mais difícil
não é construir o satélite.
É todo o resto.

<!-- S06 -->
A unidade básica se chama 1U:
um cubo de uns dez centímetros.
Empilhe unidades
e você tem 2U, 3U, 6U
e maiores.

<!-- S07 -->
A ideia é simples.
Em vez de projetar uma nave nova
do zero,
você reutiliza tamanhos padronizados
e interfaces padronizadas.
E de repente, o espaço se abre
para universidades, startups
e talvez até para você.

<!-- S07b -->
Aliás, se você gosta
de vídeos como este, se inscreva.

Isso ajuda muito o canal.

<!-- S08 -->
O que o nosso pequeno satélite
conteria de fato?
Primeiro, ele precisa de um computador.
Algo tem que rodar o software,
controlar o hardware
e decidir o que fazer.

<!-- S09 -->
Depois, a energia.
Os painéis solares geram eletricidade.
As baterias a armazenam
para quando o satélite
entra na sombra da Terra.

<!-- S10 -->
Depois, a comunicação.
Um rádio. Uma antena.
E, de volta na Terra,
uma estação terrestre escutando.

<!-- S11 -->
Depois, os sensores.
Temperatura. Tensão. Corrente.
Aceleração. Campo magnético.
E algum jeito de saber
para onde o satélite está apontando.
Porque em órbita,
dizer "para cima" é surpreendentemente difícil.

<!-- S12 -->
Mas antes de construir um,
tem uma pergunta incômoda.
Quanto custa essa caixinha?
A resposta é...
mais do que parece.

<!-- S13 -->
Um simples CubeSat 1U
pode facilmente custar
dezenas de milhares de dólares,
só em hardware de voo.
O sistema de energia. Os painéis solares.
As baterias. O computador. O rádio.
O controle de atitude. A estrutura.
E a carga útil.

<!-- S14 -->
Depois vêm as coisas
que não estão na lista de peças.
Testes. Integração.
Documentação.
Operação da estação terrestre.
Licenciamento.
E, por fim...
o lançamento.

<!-- S15 -->
Uma carona para um CubeSat minúsculo
pode custar dezenas de milhares.
Missões maiores e CubeSats maiores
chegam a centenas de milhares.
E isso é só
colocar a coisa no espaço.

<!-- S16 -->
E agora,
um problema ainda mais ridículo.
Lembra de todas aquelas peças?
Como é que tudo isso
cabe dentro de uma caixinha?

<!-- S17 -->
No espaço, não tem espaço
para uma pilha qualquer de eletrônicos.
Cada centímetro importa.
Cada grama importa.
Cada watt importa.
O satélite é um quebra-cabeça tridimensional
que tem que sobreviver ao lançamento de um foguete.

<!-- S18 -->
Então, onde você consegue
todas essas peças?
Você não precisa projetar
tudo sozinho.
Existe toda uma indústria
que vende componentes para satélites pequenos:
computadores, sistemas de energia,
rádios, antenas e painéis solares.
Existem até plataformas de venda
só de peças de CubeSat.

<!-- S18b -->
E as peças também são padronizadas.
Muitas compartilham um formato de placa
e simplesmente se empilham,
então peças de fabricantes diferentes
se encaixam numa única unidade.
Empresas como a EnduroSat
e a GomSpace as vendem,
e um único subsistema pode custar
de alguns milhares
a dezenas de milhares de dólares.

<!-- S19 -->
E não são
processadores exóticos.
Um computador atual de CubeSat
usa um ARM Cortex-M7,
com interfaces conhecidas:
SPI, I²C, UART e CAN.

<!-- S19b -->
E não é um chip espacial sob medida.
É uma placa real, de prateleira,
que você poderia segurar na mão.

<!-- S20 -->
Uma nave precisa de algo
mais importante que velocidade bruta:
comportamento previsível,
baixo consumo e confiabilidade.
Missões mais exigentes
podem usar processadores ARM Cortex-A,
e até Linux.

<!-- S20b -->
Mas ele não é rápido.
Um computador típico de CubeSat
roda a algumas centenas de megahertz.
Seu notebook roda a
quatro ou cinco gigahertz,
com muito mais núcleos.
Ele troca velocidade bruta
por quase não gastar energia.

<!-- S21 -->
E se você é programador,
é aqui que fica interessante.
Você não escreve
nenhuma misteriosa "linguagem espacial".
Você escreve software embarcado.
Muitas vezes em C ou C++.

<!-- S22 -->
Ele pode rodar direto
no hardware,
ou num sistema operacional de tempo real
como FreeRTOS, Zephyr ou RTEMS.
Existem até frameworks abertos
feitos para naves espaciais.
O F Prime, da NASA, por exemplo,
é um framework de software de voo
para sistemas embarcados e espaciais.

<!-- S23 -->
Então seu código pode ser
mais ou menos assim.

<!-- S24 -->
Mas tem uma diferença enorme
em relação a um computador normal.
Você não faz SSH nele.
Você não conecta um depurador.
E se o seu software travar...
seu computador está
a algumas centenas de quilômetros de altura.

<!-- S25 -->
Então ele precisa de watchdogs,
modos seguros, detecção de falhas
e recuperação automática.
Ele tem que resolver alguns problemas
sem você ali para ajudar.

<!-- S25b -->
E um grande motivo pelo qual ele precisa disso tudo
é a radiação.
No espaço, os raios cósmicos
podem inverter um bit na memória,
ou até derrubar um chip.
Não há blindagem pesada:
pesaria demais.
Em vez disso, o computador se monitora,
corrige erros
e se reinicia quando algo dá errado.

<!-- S26 -->
Mas se você realmente
quer lançá-lo...
a coisa fica séria.
Uma peça que funciona na sua mesa
não está pronta automaticamente
para um foguete.
Ela tem que sobreviver à vibração,
ao vácuo, a temperaturas extremas
e à radiação.

<!-- S27 -->
Agora, de volta àquele problema
de saber para onde
o satélite está apontando.
Imagine ele girando
pelo espaço.
Sem chão. Sem teto.
O GPS pode dizer
onde você está...
mas não para onde
você está virado.

<!-- S28 -->
Então os satélites combinam
giroscópios, magnetômetros
e sensores solares
para descobrir sua atitude.
E aí eles têm que mudá-la.
Um truque comum
é um magnetorquer.

<!-- S29 -->
Ele se apoia
no campo magnético da Terra
e cria um pequeno torque.
Não é um motor de foguete.
Ele não desloca o satélite.
Só o gira.
E isso basta
para apontar o satélite
exatamente para onde você quer.

<!-- S30 -->
Mas nada disso
é o motivo
pelo qual construímos o satélite.
Precisamos de uma missão.
Essa é a carga útil.
Medir radiação.
Fotografar a Terra.
Estudar a atmosfera.
Testar um sensor novo.
Ou simplesmente provar
que uma nova tecnologia funciona.

<!-- S31 -->
O satélite em si
está ali principalmente
para manter a carga útil viva.
Alimentá-la. Apontá-la.
Mantê-la aquecida.
Guardar seus dados.
E enviá-los para casa.

<!-- S32 -->
Quando seu computador trava,
você reinicia.
Quando seu satélite trava...
você tem um objeto caríssimo
orbitando a Terra em silêncio.

<!-- S33 -->
Digamos que a gente construiu.
Tudo funciona...
O computador inicializa...
O rádio fala.
Os painéis geram energia.
A carga útil roda...
Podemos lançar?
...Ainda não.

<!-- S34 -->
Um satélite tem que provar
que consegue sobreviver ao lançamento.
Isso significa testes.
Muitos testes.

<!-- S35 -->
Primeiro, parafuse ele
numa mesa vibratória gigante.
Depois sacuda, com força...
Isso é o teste de vibração.
Lançamentos de foguete não são suaves.
Ele tem que sobreviver
a ruído, vibração e choque
sem que nada
se solte ou quebre.
Cada parafuso importa.
Cada conector importa.
Cada pedaço de cabo importa.

<!-- S36 -->
Depois vem o vácuo.
Na Terra, o ar leva o calor embora.
No espaço, não tem ar.
Um lado pode ficar muito quente,
o outro muito frio,
e a eletrônica
ainda tem que ficar
dentro dos seus limites.
Então o satélite precisa
de tiras térmicas, revestimentos,
isolamento
e materiais cuidadosamente escolhidos.
Satélites não têm
ar-condicionado.
Eles têm física.

<!-- S37 -->
E com a bateria,
a coisa fica interessante.
Carregue com luz solar.
Depois o satélite
entra na sombra da Terra,
e os painéis quase não geram nada.
A bateria o mantém vivo.
Depois, de volta à luz solar.
Carregar. Descarregar.
Carregar. Descarregar.
De novo e de novo.
Por anos.
Um erro no gerenciamento de energia
poderia encerrar a missão em silêncio.

<!-- S38 -->
E agora, como você fala com ele?
Você precisa de um rádio.
Uma antena.
E uma frequência
que você tenha permissão legal de usar.
E uma estação terrestre.
O satélite
não tem internet.
Ele só passa por cima
e transmite.

<!-- S39 -->
Sua estação terrestre
capta o sinal.
O computador o decodifica.
E de repente você tem dados
da sua própria nave espacial.
Imagine abrir um terminal
e ver isto.

Só que a máquina
que imprime esses números...
está a centenas de quilômetros
acima da sua cabeça.

<!-- S40 -->
Então, como a gente
leva ele lá para cima de verdade?
Você poderia construir um foguete...
Por favor, não...
Você não precisa de um.
Os CubeSats voam
como cargas secundárias.

<!-- S41 -->
Um foguete já vai subir.
Ele tem espaço sobrando.
Seu satélite pega carona
num ejetor padrão.
Não precisa de foguete próprio.

<!-- S42 -->
E agora ele está
no topo de um foguete.
Você não pode tocá-lo.
Você não pode abrir a caixa.
Você não pode plugar um cabo.
O foguete decola.
Cerca de nove minutos depois,
você está em órbita.

<!-- S43 -->
O ejetor
libera seu satélite.
Ele é lançado para fora
e começa a girar.

<!-- S43b -->
Mas como ele sabe que saiu?
...
Chaves com mola, pressionadas
enquanto ele estava no ejetor,
saltam no instante em que é ejetado,
e o computador inicializa.
Depois, pelas regras,
ele fica em silêncio por cerca de meia hora.
Só então liga o rádio,
desdobra as antenas
e finalmente liga para casa.
E em algum lugar da Terra...
sua estação terrestre o ouve.

<!-- S44 -->
Você construiu uma máquina.
E agora essa máquina
está orbitando o planeta.

<!-- S44b -->
Só que a gente não terminou.
Um satélite morto não pode
simplesmente ficar lá em cima para sempre.
Deixado em órbita por séculos,
ele vira lixo espacial.

<!-- S45 -->
Isso significa que missões modernas
cada vez mais precisam planejar
o fim
da vida da nave.
Idealmente, a fina atmosfera superior
o arrasta lentamente para baixo.
Sua órbita decai.
Ele reentra.
E acaba queimando.
O fim da missão...
faz parte da missão.

<!-- S46 -->
Então... você conseguiria construir
seu próprio satélite?
Tecnicamente, sim.
Você não precisa ser a NASA.
Você não precisa
ter um foguete.
Você nem precisa necessariamente
de uma empresa enorme.

<!-- S47 -->
O satélite tem que
sobreviver ao lançamento.
Sobreviver ao espaço.
Se comunicar dentro da lei.
Funcionar sozinho.
E, no fim,
sair de órbita.
Tudo isso
tem que ser provado
antes de alguém
colocá-lo num foguete.

<!-- S48 -->
Os CubeSats não tornaram fácil chegar ao espaço.
Tornaram esse acesso padronizado.
Em vez de construir tudo
do zero,
você pode construir algo
que se encaixa num padrão existente.
E essa é uma mudança surpreendentemente grande.

<!-- S49 -->
Então, em algum lugar, agora mesmo,
tem pequenas máquinas
orbitando a Terra.
Construídas por universidades,
equipes de pesquisa,
empresas e estudantes.

<!-- S50 -->
Algumas levam câmeras.
Algumas medem radiação.
Algumas testam
tecnologia totalmente nova.
E algumas são só experimentos
com uma única pergunta:
"a gente consegue fazer isso
funcionar no espaço?"

<!-- S51 -->
E é isso que torna
construir seu próprio satélite
tão fascinante.
Porque a distância
entre você e o espaço
não é mais um foguete.
Pode ser...
uma caixa de dez centímetros.
E uma lista de tarefas
muito, muito longa.
