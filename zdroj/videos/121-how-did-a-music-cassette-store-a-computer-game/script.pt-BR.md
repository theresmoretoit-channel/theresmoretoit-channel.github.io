<!-- S01 -->
Você aperta o play num gravador de fita.
E isto sai do alto-falante.

<!-- S02 -->
Não é música.
E também não é a trilha sonora de um jogo.

<!-- S03 -->
É o próprio jogo.
Cada guincho é parte de um programa,
e o computador está escutando.

<!-- S04 -->
O toca-fitas não faz ideia.
Até onde ele sabe, está tocando uma música.

<!-- S05 -->
Então, como uma música vira um jogo?
E por que uma única nota errada
podia jogar fora cinco minutos de espera?

<!-- S06 -->
O truque é este,
numa máquina específica:
o ZX Spectrum,
um computador doméstico britânico de 1982.

<!-- S07 -->
Ele usa dois tipos de pulso.
Um par de pulsos curtos significa zero.

<!-- S08 -->
O um é o mesmo par,
só que cada pulso dura o dobro,
então o tom dele soa uma oitava mais grave.

<!-- S09 -->
Mande cerca de mil e quatrocentos bits
por segundo,
e você tem o barulho que acabou de ouvir.

<!-- S09b -->
Isso também quer dizer que um programa cheio de zeros
carrega mais rápido que um cheio de uns.
Cada "um" leva o dobro do tempo para ser enviado.

<!-- S10 -->
Agora, se você cresceu nos Estados Unidos,
talvez nunca tenha ouvido isso.

<!-- S11 -->
O que é estranho,
porque a ideia em si era americana.

<!-- S12 -->
Em 1975, num encontro em Kansas City,
entusiastas de computação combinaram um jeito
de guardar dados como som
em fitas cassete comuns.

<!-- S12b -->
Para o um, eram oito ciclos rápidos
de um tom agudo;
para o zero, quatro ciclos mais lentos de um tom grave.
Trezentos bits por segundo.

<!-- S13 -->
Máquinas pioneiras como o Apple II
e o TRS-80
gravavam seus programas
em gravadores de fita comuns.

<!-- S14 -->
Mas a computação doméstica americana
evoluiu rápido.

<!-- S15 -->
Em 1983, uma revista publicou uma pesquisa:
nove em cada dez novos donos de Commodore 64
estavam comprando um drive de disquete
junto com o computador.

<!-- S16 -->
Na Grã-Bretanha, a história foi no sentido contrário.

<!-- S17 -->
O Spectrum custava cento
e vinte e cinco libras,
e não vinha com armazenamento nenhum.
Você usava o toca-fitas
que já tinha em casa.

<!-- S18 -->
Então, para milhões de crianças pela Europa,
esse barulho era o som
de um jogo prestes a começar.

<!-- S18b -->
Depois de carregar muitas vezes,
dava até para saber qual era o jogo
só pelo guincho.

<!-- S19 -->
Então vamos seguir um jogo
da fita até o computador.

<!-- S20 -->
Você digita LOAD, aperta enter
e dá o play.

<!-- S21 -->
Primeiro vem um zumbido constante,
de oitocentos ciclos por segundo,
por uns cinco segundos.

<!-- S22 -->
Ele não carrega dado nenhum.
Está ali para que o computador
encontre o sinal
e pegue o ritmo dele.

<!-- S23 -->
Depois, dois pulsos rápidos: a sincronização.
Eles querem dizer: daqui em diante, são dados.

<!-- S24 -->
A primeira coisa a chegar
é um cabeçalho curto.
Dezenove bytes:
um nome de até dez letras,
que tipo de arquivo é
e qual vai ser o tamanho dele.

<!-- S25 -->
Depois, um segundo zumbido, mais curto,
dessa vez de dois segundos,
e então o jogo em si.

<!-- S26 -->
Cada byte são oito dessas notas,
uma atrás da outra,
sem nenhum intervalo entre os bytes.

<!-- S27 -->
E o computador não ouve notas.
Ele mede o tempo entre uma borda
do sinal e a seguinte.

<!-- S28 -->
Par curto é zero.
Par longo é um.

<!-- S28a -->
E o decodificador é só isso.

<!-- S28b -->
E o barulho do começo deste vídeo
não é efeito sonoro.
Nós o geramos exatamente com essas regras,
e tem um programa de Spectrum de verdade lá dentro.

<!-- S28c -->
Vamos tocá-lo inteiro bem no final.
Grave, e um Spectrum vai carregá-lo.

<!-- S29 -->
A maioria dos jogos mostrava uma imagem primeiro,
e ela carregava numa ordem estranha.

<!-- S30 -->
Surgiam listras finas, a oito linhas uma da outra,
depois se preenchiam, linha por linha,
um terço da tela de cada vez.
E as cores vinham por último,
descendo por cima de tudo.

<!-- S31 -->
Só essa imagem
levava uns quarenta segundos.
O jogo inteiro, uns cinco minutos.

<!-- S32 -->
E no fim de cada bloco
vem mais um byte.

<!-- S33 -->
Ao gravar, o Spectrum passa
cada byte do bloco
por uma regra simples chamada XOR,
e grava o resultado como mais um byte.

<!-- S34 -->
Ao carregar, ele repete o cálculo.
Se os resultados batem,
o bloco chegou intacto.

<!-- S35 -->
Se não batem, o Spectrum diz isto.

<!-- S36 -->
Cinco minutos de espera,
e um único byte decide
que foi tudo em vão.
Rebobina e começa tudo de novo.

<!-- S37 -->
Curiosamente, um cabeçalho danificado
não gera erro nenhum.
O Spectrum simplesmente o ignora
e continua escutando, à espera do próximo.

<!-- S38 -->
Outros computadores fizeram outras apostas.

<!-- S39 -->
O Commodore 64 gravava
cada bloco duas vezes,
para que um trecho danificado numa cópia
pudesse ser recuperado da outra.

<!-- S40 -->
Mais seguro, mas lento.
Com a rotina embutida do Commodore,
um programa de quarenta kilobytes
levava uns doze minutos e meio.

<!-- S41 -->
Por isso, as editoras de jogos escreveram
seus próprios carregadores, mais rápidos,
alguns até umas dez vezes mais rápidos.

<!-- S42 -->
E aí tinha o próprio toca-fitas.

<!-- S43 -->
Baixo demais,
e as bordas afundam no chiado.
Alto demais,
e elas se borram umas nas outras.

<!-- S44 -->
Uma fita rodando um pouco rápido ou devagar demais
estica cada pulso,
e o computador está medindo tempo.

<!-- S45 -->
O pior de tudo era o azimute,
o ângulo do cabeçote.
Uma fita gravada num aparelho
podia não se alinhar com outro.

<!-- S46 -->
Então o pessoal enfiava uma chave de fenda minúscula
num furinho ao lado do cabeçote
e girava aos pouquinhos,
escutando.

<!-- S47 -->
Parecia superstição.
Era ajuste de sinal.

<!-- S48 -->
Mas repare no que o toca-fitas
nunca precisou fazer.

<!-- S49 -->
Ele nunca entendeu um único bit.
Gravava som
e depois reproduzia.

<!-- S50 -->
Ou seja, um programa
não precisava de fato de uma fita cassete.
Qualquer coisa que transportasse som
podia transportar software.

<!-- S50b -->
Também queria dizer que copiar um jogo
era tão fácil quanto copiar um álbum.
Dois decks de fita e um cabo.

<!-- S51 -->
A Atari usou as duas faixas estéreo.
O programa numa,
e uma voz na outra,
falando com você pela TV
enquanto o jogo carregava.

<!-- S52 -->
Na Iugoslávia, um programa da Rádio Belgrado
transmitia software pelas ondas do rádio.

<!-- S53 -->
Os ouvintes gravavam tudo em fita,
cerca de cento e cinquenta programas
entre 1983 e 1986.

<!-- S54 -->
Na Tchecoslováquia, foi a televisão.
Um programa tocava como som
por baixo dos créditos finais.

<!-- S55 -->
E em 1983, o cantor Pete Shelley
escondeu um programa de Spectrum
no fim de um álbum de vinil.

<!-- S56 -->
Você copiava para a fita, carregava,
e as letras apareciam na tela
sincronizadas com as músicas.

<!-- S57 -->
Mas tinha um porém.

<!-- S58 -->
O rádio conseguia levar o som
a todos os computadores do país.
Só o certo conseguia entendê-lo.

<!-- S59 -->
Toque um jogo de Spectrum para um Commodore,
e o Commodore ouve ruído.
Os bits só significam alguma coisa
para uma máquina que conhece o formato.

<!-- S60 -->
Então a rádio holandesa tentou resolver isso.
Em 1982, criou o BASICODE:
um só formato de som,
com um pequeno programa tradutor
para cada tipo de computador.

<!-- S61 -->
E esse problema nunca foi embora.
Um arquivo só serve para alguma coisa
se algo ainda conseguir lê-lo.

<!-- S62 -->
As fitas perderam, claro.
Os disquetes eram mais rápidos,
depois os discos rígidos, depois a memória flash.

<!-- S63 -->
Só que a fita nunca saiu de cena de verdade.
Os data centers ainda guardam
seus arquivos em fita magnética.

<!-- S64 -->
Um cartucho LTO-9 moderno
armazena dezoito terabytes.

<!-- S65 -->
Na velocidade do Spectrum,
essa capacidade encheria mais ou menos
vinte e nove milhões de fitas,
e levaria mais de três mil
anos para carregar.

<!-- S66 -->
Mas ainda é a mesma ideia.
Padrões numa tira de fita em movimento,
que voltam a virar números
quando você precisa deles.

<!-- S67 -->
Então, da próxima vez que ouvir esse guincho,
lembre-se do que ele é.
Não é ruído.
É um programa viajando em forma de som.

<!-- S68 -->
E em 1985, em algum lugar,
uma criança está sentada diante da televisão,
esperando aquilo parar.
Porque, quando parar,
o jogo começa.

<!-- S69 -->
Então, aqui vai uma pergunta para você.
Se você já carregou um jogo de uma fita cassete,
do que você mais se lembra?
Conta aqui nos comentários.

<!-- S70 -->
E, como prometido, aqui está aquele programa.
Assim como a televisão tchecoslovaca,
nós o colocamos por baixo dos créditos finais.
