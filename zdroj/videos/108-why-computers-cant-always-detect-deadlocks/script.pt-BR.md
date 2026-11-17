<!-- S01 -->
Quatro carros chegam a um cruzamento
exatamente no mesmo instante.
Sem semáforos. Sem placas.
Só a regra que muitos países usam:
dê a preferência ao carro à sua direita.

<!-- S02 -->
Cada motorista olha para a direita
e vê um carro pelo qual precisa esperar.
Então todos os motoristas esperam.

<!-- S03 -->
Ninguém está desrespeitando a regra.
Todos a seguem à risca.
E ninguém nunca vai sair do lugar.

<!-- S04 -->
Os cientistas da computação chamam isso de deadlock.
E isso não acontece só nas ruas.
Acontece dentro de bancos de dados,
sistemas operacionais e softwares comuns.

<!-- S05 -->
Computadores costumam ser bons em detectar
um deadlock depois que ele acontece.
Mas será que um programa conseguiria ler outro programa
e te dizer, com certeza,
se ele vai travar algum dia?

<!-- S06 -->
Para muitos programas, sim.
Mas um método que funcione
para qualquer programa possível
não pode existir.
E não porque os computadores
ainda não sejam rápidos o bastante.
Nenhum computador mais rápido vai mudar isso.

<!-- S07 -->
Veja como um programa trava.
Imagine uma loja online
com duas tarefas rodando ao mesmo tempo.

<!-- S08 -->
Antes de uma tarefa alterar qualquer coisa,
ela coloca um bloqueio nisso,
para que ninguém mais possa mexer.
É como pegar a única chave de uma sala.

<!-- S09 -->
A primeira tarefa bloqueia a conta de um cliente
e depois tenta bloquear o pedido dele.
A segunda bloqueia o pedido
e depois tenta bloquear a conta.

<!-- S10 -->
Uma segura a conta
e espera pelo pedido.
A outra segura o pedido
e espera pela conta.
Nenhuma vai soltar o que está segurando.

<!-- S11 -->
E o mais estranho é que
esse código pode rodar um milhão de vezes
sem nenhum problema.
Só quando as duas tarefas se sobrepõem
exatamente na ordem errada
é que tudo para.

<!-- S12 -->
O bug sempre esteve lá.
O timing só o deixou à mostra.

<!-- S12b -->
Aliás, se você gosta de vídeos
como este, pense em se inscrever.

Isso ajuda muito o canal.

<!-- S13 -->
Bancos de dados esbarram nisso o tempo todo,
então ficam de olho.
Eles desenham um mapa de quem está esperando quem.

<!-- S14 -->
A primeira espera pela segunda.
A segunda espera pela primeira.
Quando as setas se fecham em um ciclo,
isso é um deadlock.
Nada de adivinhação. O ciclo está bem ali.

<!-- S15 -->
Aí o banco de dados faz algo brutal.
Escolhe uma das tarefas
e joga o trabalho dela fora.

<!-- S16 -->
O SQL Server, da Microsoft, chega a dizer à perdedora
que ela foi escolhida
como vítima do deadlock
e que deve tentar de novo.

<!-- S17 -->
A outra tarefa segue em frente,
e a vítima pode simplesmente tentar de novo.

<!-- S18 -->
Repare no que isso resolve e no que não resolve.
O deadlock foi desfeito.
Mas o código que o causou continua lá,
esperando o próximo momento de azar.

<!-- S19 -->
Então detectar um deadlock
que já aconteceu
é a parte fácil.
A pergunta difícil é outra.

<!-- S20 -->
Não: este programa está travado agora?
Mas sim: dê esta entrada a ele.
Ele poderia travar algum dia?

<!-- S21 -->
A primeira é uma foto do presente.
Basta olhar para ela.
A segunda é uma previsão
sobre todos os futuros possíveis.

<!-- S22 -->
E os programas tornam isso muito difícil.
Eles tomam decisões. Repetem coisas.
Podem fazer cálculos que levam
um segundo, ou mil anos.

<!-- S23 -->
Um programa pode travar na hora,
depois de um milhão de passos,
com uma única entrada rara,
ou nunca.

<!-- S24 -->
Você poderia simplesmente rodá-lo e observar.
Mas se ele não travou depois de uma hora,
o que isso te diz?

<!-- S25 -->
Nada.
Ele pode travar no segundo seguinte,
ou nunca.

<!-- S26 -->
Em 1936, um jovem matemático
chamado Alan Turing mostrou
que algumas perguntas sobre programas
não podem ser respondidas por nenhum programa.
A mais famosa parece ainda mais simples.

<!-- S27 -->
Pegue qualquer programa e a entrada dele.
Ele vai acabar parando?
Ou vai rodar para sempre?

<!-- S28 -->
Hoje isso se chama problema da parada.
E nenhum programa consegue resolvê-lo
corretamente em todos os casos.

<!-- S29 -->
A ideia por trás da prova
é surpreendentemente curta.
Suponha que alguém te entregue
um verificador de parada perfeito.

<!-- S30 -->
Agora você escreve um programinha do contra.
Ele pergunta ao verificador sobre si mesmo
e depois faz o contrário.

<!-- S31 -->
Se o verificador disser que ele vai parar,
ele entra em loop para sempre.
Se o verificador disser que ele vai rodar para sempre,
ele para na hora.

<!-- S32 -->
Não importa o que o verificador diga sobre ele,
o verificador erra.
Então um verificador perfeito não pode existir.

<!-- S33 -->
E o que isso tem a ver com deadlocks?
Tudo.

<!-- S34 -->
Imagine que alguém diga ter construído
um previsor de deadlocks perfeito.
Você dá a ele qualquer programa e a entrada dele,
e ele sempre te diz, corretamente,
se esse programa vai travar algum dia.

<!-- S35 -->
Vamos usá-lo
para resolver o problema da parada.

<!-- S36 -->
Pegue qualquer programa que quiser
e coloque-o dentro de um programa novo.

<!-- S37 -->
Primeiro, o programa novo
simplesmente executa o antigo,
passo a passo, em uma única thread.
Sem bloqueios. Nada compartilhado.
Nada que possa travar, nunca.

<!-- S38 -->
Depois, se o programa antigo terminar,
o novo inicia duas tarefas.
Cada uma pega um bloqueio,
espera até a outra pegar o seu
e então tenta pegar o da outra.
Um deadlock, de propósito, toda vez.

<!-- S39 -->
Se o programa antigo nunca terminar,
o novo nunca chega até ali.
Nenhum deadlock. Nunca.

<!-- S40 -->
Então o programa novo trava
se, e somente se, o antigo parar.

<!-- S41 -->
Agora pergunte ao previsor
sobre o programa novo.
“Sim, vai dar deadlock”
significa que o programa antigo para.
“Não” significa que ele roda para sempre.

<!-- S42 -->
Acabamos de resolver o problema da parada.
E isso é exatamente o que não dá para fazer.

<!-- S43 -->
Então o previsor de deadlocks perfeito
também não pode existir.

<!-- S44 -->
O problema não são os bloqueios,
nem os bancos de dados, nem programadores ruins.
Um programa pode esconder qualquer cálculo
antes de um deadlock.
Para prever o deadlock,
você teria que prever se esse cálculo termina.

<!-- S45 -->
Mas espere aí.
Um computador de verdade não é infinito.
A memória dele tem um número limitado de estados.
Então não daria para verificar todos?

<!-- S46 -->
Para uma máquina com uma quantidade fixa
de memória, em princípio, sim.
Na prática, tente contá-los.

<!-- S47 -->
A memória de um notebook
com oito gigabytes
pode ser organizada de tantas maneiras
que só escrever esse número
exige uns vinte bilhões de dígitos.

<!-- S48 -->
O número de átomos
no universo observável
tem uns oitenta.

<!-- S49 -->
Então, numa máquina real, verificar tudo
é possível na teoria
e inviável na prática.

<!-- S50 -->
Mas esse é outro muro.
O limite de Turing não tem a ver com estados demais.
Ele vale para programas
que sempre podem pedir mais memória.
Para esses, nenhum previsor perfeito pode existir,
por maior que seja o computador.

<!-- S51 -->
Isso quer dizer que não há nada a fazer contra deadlocks?
Não.
Quer dizer que não existe verificador perfeito.
Então os programadores escrevem programas
que são mais fáceis de verificar.

<!-- S52 -->
O truque mais simples é definir uma ordem.
Toda tarefa tem que bloquear a conta
antes do pedido.
Nunca o contrário.

<!-- S53 -->
Se toda tarefa realmente seguir essa ordem,
o ciclo não se forma,
e esse tipo de deadlock não pode acontecer.

<!-- S54 -->
Outros sistemas desistem depois de um tempo limite,
pegam todos os bloqueios de uma vez
ou deixam o banco de dados escolher uma vítima
e simplesmente tentam de novo.

<!-- S55 -->
E, para projetos pequenos e descritos com cuidado,
existem ferramentas que verificam todos os estados possíveis.
Engenheiros da Amazon usaram uma delas
para achar um bug que levava trinta e cinco passos,
exatamente na ordem certa, para aparecer.

<!-- S56 -->
Essas ferramentas funcionam
porque o problema foi reduzido.
Elas verificam um modelo do sistema,
não todo programa que poderia existir.

<!-- S57 -->
Mas, para código de verdade,
um verificador que aceita qualquer programa
tem que abrir mão de alguma coisa.
Ele pode alertar sobre deadlocks
que não podem acontecer,
deixar passar alguns que podem
ou, às vezes, não dar resposta nenhuma.

<!-- S58 -->
Um verificador que nunca dá alarme falso,
nunca deixa passar nenhum deadlock
e sempre dá uma resposta,
para qualquer programa,
é exatamente o que Turing descartou.

<!-- S59 -->
De volta ao cruzamento:
os quatro motoristas não ficam ali para sempre.

<!-- S60 -->
Alguém acena.
Um motorista abre mão da vez,
e em segundos tudo se resolve.

<!-- S61 -->
É isso que o banco de dados faz também.
Ele não prevê o deadlock.
Ele percebe que aconteceu
e faz alguém dar a vez.

<!-- S62 -->
Alguns problemas precisam de um computador mais rápido.
Outros, de uma ideia melhor.

<!-- S63 -->
E alguns, como este,
não têm solução perfeita nenhuma.
Só boas regras
e alguém disposto a acenar.
