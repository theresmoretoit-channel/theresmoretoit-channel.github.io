<!-- S01 -->
Em 1993, um jogo chamado Doom
rodava num computador
com 4 megabytes de memória.

<!-- S02 -->
Isso é mais ou menos o tamanho
de uma única foto no seu celular.

<!-- S03 -->
Não havia acelerador 3D.
O processador principal
fazia toda a renderização.

<!-- S04 -->
Hoje, um desenvolvedor começa com uma engine,
como Unity ou Unreal,
que cuida de gráficos, som,
memória e hardware.

<!-- S05 -->
No DOS, tudo isso
era problema do desenvolvedor.
E, muitas vezes, do jogador também.

<!-- S06 -->
Então, quão difícil era
fazer um jogo para DOS?

<!-- S07 -->
Vamos começar pela memória,
porque a memória era uma bagunça.

<!-- S08 -->
O IBM PC original, de 1981,
conseguia endereçar 1 megabyte de memória.

<!-- S09 -->
Mas só os primeiros
640 kilobytes
eram destinados aos programas.

<!-- S10 -->
Os outros 384
eram reservados para a memória de vídeo,
as placas de expansão e o BIOS.

<!-- S11 -->
Por mais de uma década,
o DOS normalmente executava os programas
dentro desse espaço.
Ir além disso dava trabalho extra.

<!-- S12 -->
É daí que vem a frase famosa:
640K deveriam ser suficientes para qualquer um.

<!-- S13 -->
Ela costuma ser atribuída a Bill Gates.
Não há registro de que ele a tenha dito,
e ele nega.

<!-- S14 -->
No começo dos anos noventa,
um PC vinha com 4 megabytes,
ou 8.

<!-- S15 -->
E um jogo ainda podia parar
com a mensagem
"memória insuficiente".

<!-- S16 -->
Ter a memória
e conseguir usá-la
eram duas coisas diferentes.

<!-- S17 -->
Uma saída era a memória expandida,
ou EMS.

<!-- S18 -->
Uma janela de 64 kilobytes
ficava na parte superior
daquele primeiro megabyte.
Por ela, um programa enxergava
4 páginas de memória extra,
de 16 kilobytes cada,

<!-- S19 -->
e podia trocá-las por outras,
como folhear um livro
por um buraco numa folha de papel.

<!-- S20 -->
Outra saída era a memória estendida,
acessada por um driver chamado HIMEM.

<!-- S21 -->
E é aqui que
o problema do desenvolvedor
virou problema do jogador.

<!-- S22 -->
Drivers do mouse, do drive de CD
ou da placa de som
comiam um pedaço daquela memória preciosa,
a não ser que você conseguisse carregá-los na memória alta.

<!-- S23 -->
Então os jogadores aprenderam a editar dois arquivos,
CONFIG.SYS e AUTOEXEC.BAT.

<!-- S24 -->
Um jogo queria EMS.
Outro queria a EMS desligada,
com uma opção chamada NOEMS.
E um terceiro precisava de cada kilobyte livre.

<!-- S25 -->
Em 1993, o MS-DOS 6 trouxe
um menu na inicialização.

<!-- S26 -->
Você escolhia a configuração
do jogo que queria jogar,
e o computador iniciava preparado para aquele jogo.

<!-- S27 -->
Algumas pessoas acabavam
com uma opção separada
para quase todos os jogos que tinham.

<!-- S28 -->
Mas, a essa altura,
os jogos maiores já tinham encontrado
um jeito de contornar os limites do DOS.

<!-- S29 -->
Desde o 386,
o próprio processador podia rodar
no modo protegido de 32 bits,
com espaço para até 4 gigabytes.

<!-- S30 -->
Já falamos do modo protegido
num vídeo anterior.
Mas o DOS não conseguia usá-lo.

<!-- S31 -->
Então os jogos traziam seu próprio ajudante,
um extensor de DOS.
O mais conhecido era o DOS/4GW.

<!-- S32 -->
Ele vinha junto com um compilador popular,
o Watcom C.

<!-- S33 -->
Quando um jogo iniciava,
o DOS/4GW colocava o processador
em modo protegido,
dando ao jogo acesso
à memória além do limite do DOS.

<!-- S34 -->
O DOS continuava lá embaixo,
oferecendo serviços como acesso a arquivos.
Mas agora o jogo rodava em modo protegido,
não como um programa de DOS tradicional.

<!-- S35 -->
Se você jogava jogos de DOS nos anos noventa,
já viu esse nome
passar rapidinho na tela.

<!-- S37 -->
Agora, a imagem.
Num dos modos VGA mais usados,
chamado Mode 13h,
a tela tinha 320
por 200 pixels,
com 256 cores.

<!-- S38 -->
Cada pixel era um byte.
Para colorir um pixel,
você escrevia um número na memória.
Nenhuma biblioteca gráfica. Só memória.

<!-- S39 -->
A tela inteira ocupava
64.000 bytes.

<!-- S40 -->
Isso é um pouco menos de 64 kilobytes,
pequeno o bastante para caber num segmento,
o bloco que um programa de 16 bits
conseguia endereçar de uma vez.
Pelo menos uma vez, a memória estava do seu lado.

<!-- S41 -->
Mas se você desenha direto
na tela visível,
o jogador vê imagens pela metade,
e a imagem pisca.

<!-- S42 -->
Então os jogos desenhavam cada quadro
primeiro num buffer escondido,
e depois copiavam a imagem pronta
para a memória de vídeo.

<!-- S43 -->
Em 1991, Michael Abrash,
programador e escritor,
publicou um jeito melhor.
Ele o chamou de Mode X.

<!-- S44 -->
Ele usava uma parte da VGA
que a maioria dos programadores
nunca tinha tocado.

<!-- S45 -->
Ele dava pixels quadrados
e espaço para várias telas
na memória de vídeo.

<!-- S46 -->
O jogo desenhava numa tela
que ninguém via,
e depois simplesmente mudava para essa tela.
Mas era muito mais difícil de programar.

<!-- S47 -->
Depois vinha o som.
E o som era uma loteria.

<!-- S48 -->
O alto-falante do próprio PC
foi feito para apitar.

<!-- S49 -->
Depois vieram as placas de som,
e outros equipamentos de som.
Não havia dois
que funcionassem do mesmo jeito.

<!-- S50 -->
AdLib, com um chip Yamaha
que sintetizava música.
Sound Blaster, que também tocava
som gravado.

<!-- S51 -->
O Roland MT-32,
uma caixa cara com instrumentos mais ricos.
A Gravis UltraSound.

<!-- S52 -->
Suportar todos eles
significava escrever drivers diferentes.

<!-- S53 -->
E o jogo precisava saber
onde a placa estava.
A porta, a interrupção
e o canal de DMA.

<!-- S54 -->
A resposta de sempre, para uma Sound Blaster,
era porta 220, IRQ 7, DMA 1.
Geralmente.

<!-- S55 -->
Errou um deles,
e o jogo ficava mudo.
Ou travava.

<!-- S56 -->
Em 1991, um programador chamado John Miles
lançou uma biblioteca
que se comunicava com muitas placas de som
por uma única interface.

<!-- S57 -->
Um jogo podia escrever o código de som uma vez
e deixar a biblioteca lidar com a placa.

<!-- S58 -->
Era mais uma camada
entre o jogo e o hardware.
Guarde isso.

<!-- S59 -->
E depois vinha a velocidade.
Os programadores contavam
cada passo que o processador dava.

<!-- S63 -->
Para achar um pixel na tela,
você multiplica a linha dele
por 320.

<!-- S63b -->
Em processadores mais antigos,
multiplicar podia sair caro.

<!-- S64 -->
Mas 320
é 256
mais 64.
Os dois são potências de dois.

<!-- S65 -->
Então dá para trocar a multiplicação
por dois deslocamentos de bits e uma soma.

<!-- S67 -->
Chris Sawyer foi ao nível mais baixo possível.
Ele escreveu Transport Tycoon, em 1994,
quase inteiramente em assembly,

<!-- S68 -->
as instruções
que o próprio processador entende,
uma por uma.

<!-- S69 -->
E às vezes
nem tudo isso bastava.

<!-- S70 -->
Em 1990, Wing Commander tinha um bug
que a equipe não conseguia achar,
com o prazo chegando.

<!-- S71 -->
Quando você saía do jogo,
o gerenciador de memória travava
com uma mensagem de erro.

<!-- S72 -->
Então um programador, Ken Demarest,
abriu o gerenciador de memória
num editor hexadecimal
e mudou o texto daquela mensagem.

<!-- S73 -->
Agora ela dizia:
"Obrigado por jogar Wing Commander."

<!-- S74 -->
Depois a equipe achou o bug de verdade,
e a piada nunca chegou à versão lançada.

<!-- S74b -->
Alguns jogadores ainda têm certeza de que a viram.
E jogos posteriores da Origin
realmente se despediam assim.

<!-- S75 -->
O que nos traz de volta ao Doom.

<!-- S76 -->
O Doom usava o DOS/4GW
e rodava como um programa de 32 bits.

<!-- S77 -->
Hardware de ponto flutuante
não era garantido em todo PC.

<!-- S78 -->
Então o Doom usava aritmética de ponto fixo.
Números inteiros,
em que os 16 bits mais baixos
representavam a parte fracionária.

<!-- S79 -->
E o mundo dele não era
realmente tridimensional.

<!-- S80 -->
Cada fase é uma planta baixa plana,
com uma altura para cada piso
e cada teto.

<!-- S81 -->
Uma sala nunca pode ficar em cima de outra.
E não dá para olhar direito para cima ou para baixo.

<!-- S82 -->
Antes que uma fase pudesse ser jogada,
uma ferramenta dividia o mapa
numa árvore binária, uma BSP.

<!-- S83 -->
A engine percorre essa árvore
de frente para trás,
começando pelo lado do jogador,
e pula as áreas que não podem ser vistas.

<!-- S84 -->
E o Doom nem foi escrito no DOS.

<!-- S85 -->
A id Software o desenvolveu
em estações de trabalho NeXT
e compilou o resultado para DOS.

<!-- S86 -->
O Doom não era uma engine 3D genérica.
Ele foi feito para exatamente
um tipo de mundo.
Essa especialização
ajudou o jogo a rodar num 386.

<!-- S87 -->
E outros estúdios queriam esse mundo.

<!-- S88 -->
A Raven Software licenciou a engine do Doom
para Heretic, em 1994,
e Hexen, em 1995.

<!-- S89 -->
O Doom ajudou a consolidar
um novo jeito de fazer jogos.
Os estúdios podiam licenciar uma engine existente,
em vez de construir tudo do zero.

<!-- S90 -->
Um extensor de memória.
Uma biblioteca de som.
Uma engine licenciada.

<!-- S91 -->
Cada um tirou um problema
das mãos do desenvolvedor.
E as camadas continuaram crescendo,
até virarem as engines
com que os desenvolvedores começam hoje.

<!-- S92 -->
Então, fazer jogos era mais difícil naquela época?
De muitas formas, sim.

<!-- S93 -->
Mas a dificuldade não desapareceu.
Ela mudou de lugar.

<!-- S94 -->
Hoje, os desenvolvedores lutam
com gigabytes de recursos
e milhões de polígonos,
em vez de algumas centenas de kilobytes.

<!-- S95 -->
No DOS, até o jogador
precisava saber para onde ia a memória.

<!-- S96 -->
Então aqui vai uma pergunta para você.
Você se lembra de montar
um menu de inicialização só para rodar um jogo?
E era um sofrimento,
ou metade da diversão?
Me conta nos comentários.
