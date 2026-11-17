<!-- S01 -->
Este é um ZX Spectrum carregando um programa.

<!-- S02 -->
E este é o mesmo programa,
no mesmo computador,
do mesmo tipo de fita cassete.

<!-- S03 -->
Ele termina na metade do tempo.
Nada no hardware mudou.
Nem fita mais rápida, nem gravador mais rápido.

<!-- S04 -->
A única coisa que mudou
foi o jeito como o computador escutava.

<!-- S05 -->
Então, como os computadores de 8 bits
aprenderam a carregar jogos mais rápido?
E se era tão fácil assim,
por que não fizeram isso desde o começo?

<!-- S06 -->
Num vídeo anterior,
vimos como o Spectrum guarda os bits
como pulsos na fita.

<!-- S07 -->
Um par de pulsos curtos significa zero.
Um par duas vezes mais longo significa um.

<!-- S08 -->
Isso dá uns mil e quatrocentos bits
por segundo.
Um jogo que ocupa os 48K de memória
leva uns cinco minutos.

<!-- S09 -->
Agora deixe cada pulso com a metade da duração.

<!-- S10 -->
O computador ainda distingue curto de longo.
Mas o dobro de bits
passa pelo cabeçote a cada segundo.

<!-- S11 -->
Esse é todo o truque de um carregador turbo.
E não é só um experimento mental.

<!-- S12 -->
Em 1984, o jogo Skool Daze
carregava seus dados com o dobro
da velocidade normal do Spectrum.

<!-- S13 -->
Então por que o Spectrum
não carregava rápido assim sozinho?

<!-- S14 -->
O carregador embutido fica gravado na ROM,
o chip de memória com que o computador inicia.
Ele não mede um pulso em segundos.

<!-- S15 -->
Ele conta.
Depois de cada borda do sinal,
espera um instante
e aí conta o tempo até chegar a próxima.

<!-- S16 -->
Um único número na ROM
decide onde o zero termina
e o um começa.

<!-- S17 -->
E esse número deixa bastante folga.
Um zero pode se esticar
mais de quarenta por cento
e ainda ser lido como zero.

<!-- S18 -->
É essa folga que faz uma fita gasta
num gravador barato
ainda carregar.

<!-- S19 -->
E o limite não era o computador.
O Spectrum verifica o sinal da fita
umas sessenta mil vezes por segundo.

<!-- S20 -->
O limite era a fita cassete.
Pulsos mais curtos significam tons mais agudos.
Com o dobro da velocidade, um zero
passa de dois quilohertz para quatro.

<!-- S21 -->
E tons agudos são exatamente o que
um gravador barato,
ou um cabeçote meio desalinhado,
perde primeiro.

<!-- S22 -->
Uma revista de Spectrum calculou em 1986
que a maioria das pessoas conseguia
pelo menos o dobro da velocidade normal.
O quanto dava para acelerar além disso
dependia do gravador.

<!-- S23 -->
Mas o turbo tinha um problema mais estranho.

<!-- S24 -->
Se o computador só conhece
o formato lento,
como ele carrega o programa
que ensina o rápido para ele?

<!-- S25 -->
A resposta está no começo da fita.
A primeira parte é gravada
no formato comum, o lento.

<!-- S26 -->
Ela é curta,
e a ROM a carrega como qualquer outro programa.

<!-- S27 -->
Aí esse programinha assume o controle.
No caso mais simples,
é uma cópia da própria rotina de carga da ROM,
com alguns números trocados.

<!-- S28 -->
No Skool Daze,
as mudanças ficam em três lugares.
Uma espera mais curta, um novo valor inicial da contagem,
uma nova linha divisória.

<!-- S29 -->
Então a ROM carrega o programa
que faz o trabalho da ROM, só que mais rápido.

<!-- S30 -->
É meio como baixar
um gerenciador de downloads mais rápido.
O passo lento te dá a ferramenta.
A ferramenta faz o resto.

<!-- S31 -->
Os jogos comerciais usaram a mesma ideia.
Um exemplo famoso foi o Speedlock,
usado pela primeira vez pela Ocean em 1984.

<!-- S32 -->
Um dos autores disse que o escreveu
porque estava farto
da demora do carregador padrão.

<!-- S33 -->
Mas aí vem a surpresa.
O Speedlock era só cerca de uma vez e meia
mais rápido.

<!-- S34 -->
O primeiro dia
do Daley Thompson's Decathlon
levava três minutos e vinte segundos,
enquanto os mesmos dados na velocidade normal
levariam quatro minutos e quarenta e sete.

<!-- S35 -->
As versões posteriores eram só cerca
de um quinto mais rápidas que a ROM.
Porque velocidade não era a única função.

<!-- S36 -->
A partir de 1983, programas copiadores
conseguiam ler o cabeçalho de um jogo
e copiar o jogo inteiro para outra fita.

<!-- S37 -->
Um formato próprio
não deixava nada para esses programas lerem.

<!-- S38 -->
O primeiro Speedlock chegava a picotar seu tom piloto
em rajadas curtas,
para que o próprio carregador da ROM
nem chegasse a reconhecê-lo.

<!-- S39 -->
E dava para ouvir.
Uma fita com Speedlock carregava com estalos,
com faixas trepidando em volta da tela.

<!-- S40 -->
Isso não impediu ninguém de copiar
uma fita de um deck para outro.
Mas deu às editoras
um motivo para escrever seus próprios carregadores.

<!-- S41 -->
No Commodore 64,
o motivo para mudar era bem maior.

<!-- S42 -->
A rotina embutida dele
gravava tudo duas vezes,
como cópia de segurança.
Um jogo de quarenta kilobytes levava
uns doze minutos e meio.

<!-- S43 -->
E aqui o gravador
não fazia quase nada de esperto.
Só transformava o som
em pulsos limpos de liga e desliga.

<!-- S44 -->
O próprio computador cronometrava cada pulso,
por software.

<!-- S45 -->
Então um carregador mais rápido
era só um programa diferente.

<!-- S46 -->
Em 1985, a revista Compute!
testou um chamado TurboTape.

<!-- S47 -->
Depois de achar o programa na fita,
ele carregou doze kilobytes
em vinte e oito segundos.

<!-- S48 -->
O próprio drive de disquete da Commodore
precisou de trinta e quatro segundos.

<!-- S49 -->
Uma fita cassete
vencendo um disquete.

<!-- S50 -->
E como o computador fazia
toda a escuta sozinho,
ele podia fazer outras coisas nesse meio-tempo.

<!-- S51 -->
Carregadores como o Freeload
davam prioridade à leitura da fita.
O tempo de processador que sobrava
ia para música, rolagem suave,
e até pequenos jogos.

<!-- S52 -->
Com o Invade-a-Load, da Mastertronic,
você jogava um clone de Space Invaders
enquanto o jogo de verdade carregava.

<!-- S53 -->
Os computadores Atari de 8 bits
eram outra história.

<!-- S54 -->
Aqui, quem escutava era o gravador.
Dentro dele havia dois filtros,
um para cada tom,
e um circuito que entregava ao computador
uns e zeros prontinhos.

<!-- S55 -->
O padrão era de seiscentos bits por segundo,
e os filtros limitavam
o quanto dava para ir mais rápido.

<!-- S56 -->
Um software esperto conseguia subir isso
um pouco, no máximo a uns mil e duzentos.
Mas para ir muito mais rápido,
era preciso abrir o gravador.

<!-- S57 -->
E na Tchecoslováquia, o pessoal abriu.

<!-- S58 -->
Um drive de disquete lá
custava de duas a três vezes
o preço do próprio computador.
Então a maioria dos donos de Atari de lá ficou na fita.

<!-- S59 -->
Em 1987, um estudante de Praga
do clube Atari local
criou o Turbo 2000.

<!-- S60 -->
Ele acrescentava um novo caminho para o sinal.
Um fio dentro do gravador pegava o som
direto do amplificador,
antes dos filtros,
passava por um pequeno chip
e seguia para a linha que ia ao computador.

<!-- S61 -->
Uma chave, acionada pelo computador,
escolhia entre o caminho antigo e o novo.

<!-- S62 -->
Agora o próprio computador cronometrava os pulsos.
Uns dois mil e trezentos bits
por segundo.
Quase quatro vezes mais rápido.

<!-- S63 -->
O turbo não era um único formato universal.

<!-- S64 -->
Às vezes você mudava o programa.
Às vezes, tinha que mudar a máquina.

<!-- S65 -->
E velocidade não saía de graça.

<!-- S66 -->
A Compute! alertava que uma gravação em TurboTape
às vezes se recusava a carregar
num gravador diferente,
com o cabeçote alinhado de um jeito um pouco diferente.

<!-- S67 -->
A gravação padrão, segundo a revista,
era bem mais lenta,
mas extremamente confiável.

<!-- S68 -->
Gravar tudo duas vezes
não era preguiça da Commodore.
Era o preço de carregar com segurança.

<!-- S69 -->
Mas um carregador diferente
também podia fazer algo inesperado.
Podia ler uma fita
que o embutido recusava.

<!-- S70 -->
No Sharp MZ-800,
um computador que foi parar
na Tchecoslováquia no fim dos anos 80,
os donos conheciam um programa chamado Turbo Copy.

<!-- S71 -->
Um jogo não carregava
e dava erro de soma de verificação.
Os donos descobriram que o Turbo Copy
muitas vezes conseguia carregá-lo mesmo assim.

<!-- S72 -->
Aí você gravava o jogo na velocidade normal
numa fita nova,
e o computador
voltava a carregá-lo normalmente.
Parecia que você tinha consertado um jogo quebrado.

<!-- S73 -->
Então como um carregador conseguia ler
o que o outro não conseguia?

<!-- S74 -->
A ROM do Sharp gravava cada bloco duas vezes,
a uns mil e duzentos bits por segundo.

<!-- S75 -->
E ela nunca media um pulso.
Depois que cada pulso começava,
esperava um intervalo fixo
e olhava uma vez só.

<!-- S76 -->
Ainda alto?

<!-- S76b -->
Então é um.

<!-- S76c -->
Já baixo?

<!-- S76d -->
Então é zero.

<!-- S77 -->
Um cronômetro, ajustado de antemão.

<!-- S78 -->
Numa fita velha, ou num gravador diferente,
os pulsos voltavam um pouco mais arredondados.
E aí aquela única olhada
podia ver o nível errado.

<!-- S79 -->
Um bit errado estraga a soma de verificação.
Se as duas cópias falharem,
a carga falha.

<!-- S80 -->
O Turbo Copy escutava de outro jeito.
Ele cronometrava cada pulso
com o chip temporizador do computador.

<!-- S81 -->
E antes de cada bloco,
escutava o tom piloto
e definia sua linha divisória
pelos pulsos que estava ouvindo de verdade.

<!-- S82 -->
O cronômetro dele era ajustado
à fita que estava tocando ali.

<!-- S83 -->
E o conserto não era uma cópia do som.
O Turbo Copy guardava os bytes
e gravava um sinal novinho em folha,
com os pulsos na duração certa.

<!-- S84 -->
Os dados não tinham se perdido.
O jeito normal de ler é que
simplesmente não era bom o bastante.

<!-- S84b -->
O Turbo Copy também podia gravar o jogo em turbo,
a duas ou três vezes a velocidade normal,
com seu próprio carregadorzinho na frente.

<!-- S85 -->
E é isso que todos esses truques
têm em comum.

<!-- S86 -->
A fita continuou a mesma.
O que mudou foi o jeito de ler.

<!-- S87 -->
Hoje, esperamos que os jogos carreguem na hora.
Nos anos 80, carregar fazia parte do jogo.
Você escutava a fita.
Olhava as faixas.
Esperava.

<!-- S88 -->
E às vezes um carregador diferente
fazia a mesma fita se comportar
como se fosse uma máquina completamente diferente.

<!-- S89 -->
O computador não precisava de uma fita mais rápida.
Precisava de um jeito melhor de escutar.

<!-- S90 -->
Então, aqui vai uma pergunta para você.
Você usou carregadores turbo naquela época?
Como você se lembra deles?
Eles falhavam mais?
Conta aí nos comentários.

<!-- S91 -->
E, por fim, a fita turbo inteira,
do começo ao fim.
Primeiro a parte na velocidade normal,
depois o turbo.
Num programa tão pequeno assim,
o turbo não compensa.
O carregador demora mais
do que o tempo que economiza.
Num jogo inteiro, dava para economizar minutos.
