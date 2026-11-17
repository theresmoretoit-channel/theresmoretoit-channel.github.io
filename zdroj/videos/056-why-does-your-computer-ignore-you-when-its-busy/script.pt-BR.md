<!-- S01 -->
Você clica num botão.
Não acontece nada.
Clica de novo.
Ainda nada.

<!-- S02 -->
Você mexe o mouse.
Nada.
Por alguns segundos,
o computador parece morto.

<!-- S03 -->
E aí acontece tudo de uma vez.
A janela se move.
O menu abre.
Todos os seus cliques chegam,
todos juntos.

<!-- S04 -->
E agora a parte estranha.
O computador sabia que você clicou.
Soube em microssegundos.

<!-- S05 -->
Isso não é chute.
Agora mesmo, enquanto você
não faz nada de especial,
sua máquina dá conta de milhares
de eventos de hardware por segundo.

<!-- S06 -->
Uma tecla apertada.
Um pacote chegando.
Um temporizador disparando.
Um disco que terminou o serviço.

<!-- S07 -->
Cada um deles é uma interrupção,
e os computadores fazem assim
desde os anos cinquenta,
exatamente para isso:

<!-- S08 -->
para que o processador possa reagir
ao mundo fora dele.

<!-- S09 -->
O hardware avisou do seu clique.
O processador percebeu.
E você ficou cinco segundos
olhando para uma tela morta.

<!-- S10 -->
O usuário não deveria vir primeiro?

<!-- S11 -->
Existe uma resposta,
e não é
que o computador seja lento.

<!-- S12 -->
É que ser percebido
e ser atendido
são duas coisas bem diferentes.

<!-- S13 -->
Vamos começar pela parte de perceber.
Imagine um computador sem interrupções.

<!-- S14 -->
O processador teria
que perguntar sem parar:
chegou algo do teclado?
o disco terminou?

<!-- S15 -->
Chegou um pacote?
O mouse se mexeu?
E então perguntar de novo.
E de novo.

<!-- S16 -->
Quase toda resposta seria não,
e o próprio perguntar
devoraria a máquina.

<!-- S17 -->
Então os aparelhos ganharam um jeito
de levantar a mão. O mouse se mexe,
o hardware dispara uma interrupção,

<!-- S18 -->
e o processador larga
o que estava fazendo,
pula para um pedaço curto de código
que se chama tratador,

<!-- S19 -->
e o sistema operacional fica sabendo
que aconteceu alguma coisa.

<!-- S20 -->
É uma ideia genial.
E leva a uma suposição
bem razoável.

<!-- S21 -->
Se dá para tirar o processador
de qualquer coisa, na hora,
então o meu clique também
vai ser atendido na hora.

<!-- S22 -->
Só que o tratador não tem
permissão para fazer quase nada.

<!-- S23 -->
Enquanto o processador está lá dentro,
todo o resto espera.
Inclusive a próxima interrupção.
E ela já está a caminho.

<!-- S24 -->
A regra é justamente o contrário
do que você esperaria.
O tratador faz o mínimo
que consegue.

<!-- S25 -->
Anota o que aconteceu.
Avisa o aparelho
que a mensagem chegou.
Larga o evento numa fila.
E sai fora.

<!-- S26 -->
Quem escreve kernel chega a dividir
o trabalho em duas metades com nome:
o que precisa acontecer agora,
e o que pode esperar.

<!-- S27 -->
Tudo que é interessante,
tudo que você um dia vai ver,
está na segunda metade.

<!-- S28 -->
E aí está a primeira resposta.
Uma interrupção chama
a atenção do computador.

<!-- S29 -->
Ela não coloca o seu programa
num processador.

<!-- S30 -->
Tá bom, você diz. Então conserta.
Faz da entrada a coisa mais
importante da casa inteira.

<!-- S31 -->
Mouse? Prioridade máxima.
Teclado? Prioridade máxima.
A janela na sua frente?
Prioridade máxima.

<!-- S32 -->
Todo o resto que espere a vez.
Parece óbvio.

<!-- S33 -->
E a melhor objeção a isso
aconteceu em Marte.

<!-- S34 -->
Em 1997 o módulo Pathfinder
pousou e começou a trabalhar.
Aí, alguns dias depois,
começou a se reiniciar sozinho.

<!-- S35 -->
Não foi raio cósmico.
Não foi peça quebrada.
Foi um problema de escalonamento.

<!-- S36 -->
Havia uma tarefa de prioridade alta
que distribuía dados
pela sonda inteira,
e ela precisava de memória compartilhada.

<!-- S37 -->
Uma tarefa de prioridade baixa,
que coletava dados do tempo,
tinha chegado lá primeiro
e estava segurando ela.

<!-- S38 -->
O que, por um instante,
não teria problema nenhum.
Mas aí uma tarefa de prioridade
média tomou o processador,

<!-- S39 -->
e a de prioridade baixa
nunca chegou ao fim.
Então nunca soltou a memória.

<!-- S40 -->
A tarefa mais importante
da sonda inteira
estava agora presa atrás
da menos importante de todas.

<!-- S41 -->
Isso tem nome.
Inversão de prioridade.

<!-- S42 -->
Um temporizador watchdog percebeu
que a tarefa importante
não rodava havia tempo demais,
achou que era desastre

<!-- S43 -->
e reiniciou a sonda inteira.
Aí aconteceu de novo.
E de novo.

<!-- S44 -->
Engenheiros na Terra descobriram
e mandaram uma correção para Marte.

<!-- S45 -->
E a lição sai de graça,
é só levar para casa.
Prioridade alta não quer dizer
que alguém vai te atender.

<!-- S46 -->
Quer dizer só que perguntam primeiro.
Se aquilo de que você precisa
está com alguém mais lento,
sua importância não adianta nada.

<!-- S47 -->
E a prioridade tem um segundo limite.
Ela decide quem vai primeiro.
Não cria nem um ciclo
a mais.

<!-- S48 -->
Suponha que todos os seus núcleos
estejam a cem por cento.
Você vai achar que travou.
Geralmente não é.

<!-- S49 -->
O escalonador reparte fatias de tempo
tão depressa
que você nem percebe a troca.

<!-- S50 -->
Por isso dá para compilar
uma coisa enorme
e ao mesmo tempo rolar
uma página na web.

<!-- S51 -->
Sob carga, o que muda
não é bem a velocidade.
O computador não está lento.

<!-- S52 -->
Ele está atrasado.

<!-- S53 -->
Você clica e a resposta vem
meio segundo depois.
Depois um segundo.
Depois cinco.

<!-- S54 -->
E as pessoas percebem isso
extraordinariamente bem.
Meio segundo parece uma máquina
que está pensando.

<!-- S55 -->
Cinco segundos parecem uma máquina
que morreu.

<!-- S56 -->
E tem uma versão disso
que surpreende ainda mais.
Às vezes o problema não é
o processador.

<!-- S57 -->
Abra coisas demais de uma vez
e a memória física enche.
O sistema começa a empurrar
páginas de memória para o disco.

<!-- S58 -->
Faça isso o bastante
e a máquina passa o tempo
movendo memória de um lado para o outro
em vez de fazer o seu trabalho.

<!-- S59 -->
Isso também tem nome.
Thrashing.

<!-- S60 -->
E aqui fica confuso,
porque o processador
pode nem parecer ocupado.

<!-- S61 -->
Ele não está trabalhando.
Ele está esperando.

<!-- S62 -->
Você pode dar a uma tarefa que espera
a prioridade mais alta do sistema
e ela vai esperar exatamente
o mesmo tanto.

<!-- S63 -->
E aí tem a versão
mais humana de tudo isso.
O evento chegou.
O kernel está com ele.

<!-- S64 -->
Ele está numa fila
com o nome do seu programa.
E o seu programa
não está pegando ele.

<!-- S65 -->
Talvez esteja fazendo uma conta longa
na mesma linha de execução
que deveria estar vigiando
a própria janela.

<!-- S66 -->
Então o mouse funciona.
O teclado funciona.
Os outros programas funcionam.

<!-- S67 -->
E aquela janela desbota
e diz que não está respondendo.

<!-- S68 -->
E isso não é diagnóstico.
O Windows põe esse aviso
depois de uns cinco segundos
sem ninguém recolher as mensagens.

<!-- S69 -->
O sistema está perfeitamente vivo.
É o aplicativo
que não veio até a porta.

<!-- S70 -->
O computador receber o seu clique
e o aplicativo responder a ele
não são o mesmo evento.

<!-- S70b -->
Aliás, se você quer ver aonde
a próxima pergunta vai nos levar,
pense em se inscrever.

Isso ajuda muito o canal.
<!-- S71 -->
Falta ainda um elo,
e é justamente aquele
em que a gente nunca pensa.
Nada disso ainda colocou
coisa alguma na sua tela.

<!-- S72 -->
O aplicativo muda o seu estado.
Alguém tem que montar o próximo quadro.
A placa de vídeo tem que desenhar.
A tela tem que mostrar.

<!-- S73 -->
Numa tela comum
uma imagem nova aparece
mais ou menos a cada dezesseis ms.

<!-- S73b -->
Então tem diferença entre
o computador dar conta do seu clique
e você ver isso.

<!-- S74 -->
E por baixo de tudo isso
está a parte
que engenharia nenhuma conserta.
O sistema operacional sabe
que o mouse se mexeu.
Por quê? Não faz ideia.

<!-- S75 -->
Talvez você esteja mirando
num jogo.
Ou editando um documento.
Ou esbarrou na mesa.

<!-- S76 -->
Para o hardware
é o mesmo evento.
Um sistema sabe priorizar trabalhos.
Adivinhar, não sabe.

<!-- S77 -->
Então ele faz um meio-termo.
Rápido o bastante para você,
quase sempre,
sem deixar o resto esperando sem fim.

<!-- S78 -->
O que nos traz de volta
àquela tela morta.
Seu clique nunca foi um evento só.

<!-- S79 -->
O hardware tem que avisar.
O kernel tem que guardar.
A fila tem que entregar ao programa.

<!-- S80 -->
Seu programa tem que rodar.
A interface tem que mudar.
Alguém tem que desenhar a imagem,
e a tela tem que te mostrar.

<!-- S81 -->
Cada um desses passos
é pequeno e rápido.

<!-- S82 -->
Atrase qualquer um deles
e não vai parecer
uma janela lenta.

<!-- S83 -->
Vai parecer um computador morto.

<!-- S84 -->
E o mais estranho de tudo isso
é como raramente
isso acontece.

<!-- S85 -->
A gente espera que uma máquina
que faz bilhões de operações
por segundo
responda a um tranco da mão.

<!-- S86 -->
E quase sempre ela responde.

<!-- S87 -->
Então da próxima vez que você clicar
e não acontecer nada,
dê um tempo a ele.

<!-- S88 -->
Ele te ouviu.

<!-- S89 -->
Só tinha uma fila,
e você estava nela.
