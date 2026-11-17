# Como a ARM dominou a computação?

<!-- S01 -->
Em 1985, engenheiros na Grã-Bretanha
ligaram um processador novinho em folha
pela primeiríssima vez.

<!-- S02 -->
Ele funcionou.
O que já era um pequeno milagre.

<!-- S03 -->
Mas aí eles notaram algo estranho.
A alimentação do chip
não estava conectada.

<!-- S04 -->
E mesmo assim ele estava rodando.

<!-- S05 -->
Ele se virava com correntes minúsculas
que vazavam pelos pinos de entrada,
vindas dos sinais dos chips ao redor.

<!-- S06 -->
Quando mediram direito,
o processador precisava
de mais ou menos um décimo de watt.

<!-- S07 -->
Ninguém tinha mirado nisso.
Os engenheiros só queriam um chip
que fosse barato de fabricar.

<!-- S08 -->
Aquele chip foi o primeiro processador ARM.

<!-- S09 -->
Quarenta anos depois, seus descendentes
estão em quase todo smartphone.
Nos computadores da Apple.
Em alguns dos maiores data centers
do mundo.

<!-- S10 -->
Centenas de bilhões de chips.

<!-- S11 -->
Então, como um processador
de uma empresa britânica de computadores domésticos
dominou a computação?

<!-- S12 -->
A resposta não é simplesmente
que ele consumia pouquíssima energia.
Essa parte foi quase um acidente.

<!-- S12b -->
Aliás, se você gosta de vídeos
como este, pense em se inscrever.

Isso ajuda muito o canal.

<!-- S13 -->
Para entender o que aconteceu de verdade,
precisamos voltar a 1983.

<!-- S14 -->
A empresa era a Acorn Computers.
O BBC Micro dela estava nas salas de aula
de toda a Grã-Bretanha.

<!-- S15 -->
O BBC Micro usava um chip mais antigo,
de oito bits, o 6502.
Para a próxima máquina,
a Acorn precisava de algo bem mais rápido.

<!-- S16 -->
Então a equipe testou
os processadores novos do mercado.
Nenhum fazia o que a Acorn queria.

<!-- S17 -->
Eram complicados,
e nenhum deles se encaixava de verdade
no que a Acorn queria construir.

<!-- S18 -->
Aí dois engenheiros da Acorn,
Sophie Wilson e Steve Furber,
foram até o Arizona,
a uma empresa fundada por um dos
projetistas originais do 6502.

<!-- S19 -->
Eles esperavam uma grande fabricante de chips.
Em vez disso, encontraram um punhado de pessoas
trabalhando numa casa de subúrbio.

<!-- S20 -->
E voltaram para casa
com uma conclusão simples.
Se eles conseguem projetar um processador...
nós também conseguimos.

<!-- S22 -->
Na época, os processadores ganhavam
instruções cada vez mais elaboradas.

<!-- S23 -->
Uma única instrução podia buscar
um número na memória,
fazer uma conta com ele
e gravar o resultado de volta.

<!-- S24 -->
Prático para o programador.
Mas cada instrução dessas
deixa o chip mais difícil de construir.

<!-- S25 -->
Ele precisa de mais lógica
só para descobrir o que cada uma significa.
Mais transistores.
Mais tempo de projeto.

<!-- S26 -->
Pesquisadores de Berkeley e Stanford
tinham feito uma pergunta radical.

<!-- S27 -->
E se um processador
tivesse só instruções simples,
e o compilador fizesse o resto?

<!-- S28 -->
Eles chamaram isso de RISC.
Computador com conjunto reduzido de instruções.

<!-- S29 -->
Sophie Wilson projetou
as instruções da ARM nessa linha.

<!-- S30 -->
As operações aritméticas só trabalham
com os registradores do próprio chip,
pequenas gavetas rápidas dentro do processador.
Para a memória, há instruções próprias.

<!-- S31 -->
Então somar um número da memória
vira três passos.
Carregar.
Somar.
Armazenar.

<!-- S32 -->
Isso se chama arquitetura load-store.

<!-- S33 -->
Mais passos para o programa.
Mas cada passo é regular,
previsível
e fácil de decodificar.

<!-- S34 -->
E o ARM tinha registradores de sobra
para trabalhar.
Dezesseis, cada um com 32 bits.
O 6502 tinha três, pequenos.

<!-- S35 -->
O resultado foi o ARM1.

<!-- S36 -->
Ele tinha cerca de
25 mil transistores.

<!-- S37 -->
O 286 da Intel, lançado alguns anos antes,
tinha cerca de 134 mil.

<!-- S38 -->
Menos transistores significavam um chip menor.
Um chip mais barato.

<!-- S39 -->
E, quase como efeito colateral,
um chip que quase não gastava energia.

<!-- S40 -->
Foi daí que veio
aquele décimo de watt.
A Acorn queria um encapsulamento de plástico barato,
o que significava ficar abaixo de um watt.
Então eles projetaram com cuidado...
e chegaram a um valor dez vezes menor.

<!-- S41 -->
Em 1987, uma versão mais rápida do ARM
foi parar no novo computador da Acorn,
o Archimedes.

<!-- S42 -->
Ele era um dos computadores pessoais
mais rápidos da sua época.

<!-- S43 -->
E isso quase não fez diferença.

<!-- S44 -->
O mundo comprava PCs compatíveis com IBM
com processadores Intel.
Era lá que estavam os programas.
Era isso que as empresas compravam.

<!-- S45 -->
O Archimedes ficou
principalmente nas escolas britânicas.

<!-- S46 -->
E a própria Acorn estava em apuros.
Já tinha precisado ser resgatada
pela Olivetti, lá em 1985.

<!-- S48 -->
Então a ajuda veio da Apple.
Ela estava construindo um computador de mão
chamado Newton.

<!-- S49 -->
Precisava de um processador
rápido, barato
e que pudesse funcionar com pilhas.

<!-- S50 -->
O ARM caía como uma luva.
Mas a Apple não queria depender
de um chip que pertencia
a uma fabricante de computadores rival.

<!-- S51 -->
Então, em 1990, a equipe do ARM
saiu da Acorn
e virou uma empresa independente.

<!-- S52 -->
A Acorn, a Apple
e a fabricante de chips VLSI
eram donas dela em conjunto.

<!-- S53 -->
Doze engenheiros.
Um velho celeiro perto de Cambridge.

<!-- S54 -->
E um modelo de negócio
que acabou sendo o verdadeiro segredo do sucesso.

<!-- S55 -->
A Intel projetava seus processadores,
fabricava em suas próprias fábricas
e vendia.

<!-- S56 -->
A ARM não ia fabricar nada.
Ia vender o projeto.

<!-- S57 -->
Qualquer empresa podia licenciá-lo,
colocar o núcleo ARM no próprio chip
e pagar uma pequena taxa
por cada chip vendido.

<!-- S58 -->
Isso importava,
porque um chip não precisa ser
só um processador.
Em volta do núcleo ARM
você pode colocar um rádio,
uma unidade gráfica,
um processador de câmera.

<!-- S59 -->
Um único chip,
projetado por quem precisar dele,
com o ARM no centro.

<!-- S60 -->
A ARM não precisava vencer a Intel
nos computadores pessoais.
Podia acabar dentro de qualquer coisa.

<!-- S61 -->
E, nos anos 90,
"qualquer coisa" significava cada vez mais
celulares.

<!-- S62 -->
Um computador de mesa pode gastar
cem watts e ter um cooler grande.
Um celular funciona com uma bateria
no seu bolso.

<!-- S63 -->
No fim da década,
havia núcleos ARM dentro
de alguns dos celulares mais vendidos,
da Nokia e de outras marcas.

<!-- S64 -->
Depois veio o iPod.
Depois, o smartphone.

<!-- S65 -->
De repente, bilhões de pessoas carregavam
um computador que tinha que aguentar
o dia todo com uma bateria.

<!-- S66 -->
E o processador que foi criado
por ser barato
acabou sendo exatamente
o que esse mundo precisava.

<!-- S67 -->
Então essa é a nossa resposta, certo?
O ARM é simples,
simples significa eficiente,
e o eficiente vence.

<!-- S68 -->
Não exatamente.

<!-- S69 -->
Olhe dentro de um núcleo ARM moderno de ponta.

<!-- S70 -->
Caches enormes.
Várias instruções rodando ao mesmo tempo.
Predição de desvios:
adivinhar para onde o programa vai
antes de ele chegar lá.

<!-- S71 -->
Execução fora de ordem:
rodar as instruções
na ordem que for mais rápida.

<!-- S72 -->
Bilhões de transistores no chip.
Não há nada de simples nisso.

<!-- S73 -->
Então, para onde foi a simplicidade?

<!-- S74 -->
O truque é que um processador
na verdade são duas coisas diferentes.

<!-- S75 -->
O conjunto de instruções é a língua
que o software fala.
Quais instruções existem
e o que elas significam.

<!-- S76 -->
A microarquitetura é a máquina
que de fato as executa.

<!-- S77 -->
A língua pode continuar simples,
enquanto a máquina por baixo
fica enormemente complicada.

<!-- S78 -->
E a mesma coisa aconteceu
do outro lado.

<!-- S79 -->
As instruções x86 da Intel
são famosas por serem complicadas.

<!-- S80 -->
Mas, desde meados dos anos 90,
os processadores da Intel e da AMD
as quebram internamente
em operações pequenas e simples.

<!-- S81 -->
Depois executam essas operações num mecanismo
muito parecido com o que existe
dentro de um núcleo ARM moderno.

<!-- S82 -->
Por baixo dos rótulos,
os dois ficaram surpreendentemente parecidos.

<!-- S83 -->
As instruções mais limpas do ARM ainda ajudam.
Elas são mais fáceis de decodificar,
o que pode economizar um pouco de energia.

<!-- S84 -->
Mas não são uma vantagem mágica
que o x86 nunca pudesse alcançar.

<!-- S85 -->
Então o ARM não dominou tudo
por ser simples.
E também não foi projetado para consumir pouco.

<!-- S86 -->
Ele venceu porque três coisas se alinharam.
Um projeto eficiente.
Um modelo de negócio
que deixava qualquer um construir com ARM.
E um mundo que de repente precisava
de bilhões de computadores movidos a bateria.

<!-- S87 -->
E aí, em 2020,
a história voltou para a Apple.

<!-- S88 -->
A Apple tinha vendido sua participação na ARM
anos antes,
quando precisava muito de dinheiro.

<!-- S89 -->
Agora ela colocou seus próprios chips baseados em ARM
no Mac.

<!-- S90 -->
O mesmo tipo de núcleo do iPhone,
ampliado para um computador.
Núcleos rápidos, núcleos eficientes,
gráficos e muito mais,
num único chip.

<!-- S91 -->
Eles eram mais rápidos
que os chips da Intel que substituíram,
e os notebooks duravam muito mais
com uma carga.

<!-- S92 -->
O ARM já não era
só o processador dos celulares.

<!-- S93 -->
E a ARM não parou por aí.
Entrou também nos data centers,
onde cada watt custa dinheiro.
Hoje a Amazon projeta
seus próprios chips ARM para servidores.

<!-- S95 -->
O primeiro chip ARM tinha cerca de
25 mil transistores.
Os de hoje têm bilhões.

<!-- S96 -->
Quase tudo no jeito
como eles funcionam por dentro mudou.

<!-- S98 -->
Uma equipe pequena queria
um processador que pudesse de fato construir.

<!-- S99 -->
Eles não o construíram para celulares,
nem para a Apple,
nem para vencer a Intel.

<!-- S100 -->
E, no fim das contas,
a coisa mais importante que eles criaram
não foi o chip.

<!-- S101 -->
Foi uma base simples
sobre a qual todo mundo pôde construir.
