<!-- S01 -->
Em 19 de julho de 2024,
uma empresa de segurança chamada CrowdStrike
enviou uma atualização de rotina.

<!-- S02 -->
Não era um programa novo.
Só um pequeno arquivo de configuração.

<!-- S03 -->
Em poucas horas, 8,5 milhões
de computadores com Windows tinham travado
numa tela azul.

<!-- S04 -->
Companhias aéreas suspenderam voos.
Hospitais cancelaram cirurgias.
Um canal de notícias saiu do ar.

<!-- S05 -->
E o erro por trás disso
era bem comum.
O programa esperava 20 dados.
A atualização entregou 21.

<!-- S06 -->
Seus jogos e apps cometem
erros assim o tempo todo.
Quando acontece, o jogo fecha
e você abre de novo.

<!-- S07 -->
O mesmo tipo de bug.
Um fecha uma janela.
O outro para
8,5 milhões de máquinas.

<!-- S08 -->
A diferença não está no erro.
Está em onde o código estava rodando.

<!-- S09 -->
Então por que um programa não consegue
tomar conta do seu computador...
e por que este conseguiu?

<!-- S10 -->
Nem sempre foi assim.

<!-- S11 -->
Num PC com DOS nos anos 1980,
nada no processador impedia um programa.
Ele podia escrever em qualquer parte da memória
e falar direto com o hardware.

<!-- S12 -->
Bastava um programa escrever
onde não devia
para sobrescrever o sistema operacional,
e a máquina inteira travava.

<!-- S13 -->
A solução foi parar de confiar nos programas
e deixar a desconfiança
por conta do processador.

<!-- S14 -->
Em 1982, o processador 80286 da Intel
introduziu o modo protegido,
com quatro níveis de privilégio.

<!-- S15 -->
Eles costumam ser desenhados
como quatro anéis, um dentro do outro.

<!-- S16 -->
O anel 0 fica no centro.
O anel 3 fica do lado de fora.

<!-- S17 -->
E a numeração vai ao contrário.
Quanto menor o número,
mais o código pode fazer.

<!-- S18 -->
O anel 0 pertence ao kernel,
o núcleo do sistema operacional.
Ele distribui a memória,
decide qual programa roda em seguida
e fala com o hardware.

<!-- S19 -->
No anel 3 rodam o seu navegador,
seus jogos e seu editor de texto.
Isso se chama modo usuário.

<!-- S19b -->
Windows, macOS e Linux
dividem o trabalho desse jeito.
O kernel no anel 0,
seus apps no anel 3.

<!-- S19c -->
Celulares e os Macs mais novos da Apple
usam chips ARM no lugar.
Lá, os níveis se chamam exception levels.
Outro nome, a mesma divisão:
um para o kernel, um para os seus apps.

<!-- S20 -->
O processador sempre sabe
em que anel está rodando.
E ele confere.

<!-- S21 -->
Algumas instruções só funcionam no anel 0.
Desligar as interrupções, por exemplo,
ou mudar como a memória é mapeada.

<!-- S22 -->
Quando um programa no anel 3 tenta uma delas,
o processador se recusa.
Ele dispara uma exceção
e passa o controle para o kernel,
que normalmente encerra o programa.

<!-- S23 -->
A memória recebe o mesmo tratamento.
Cada página de memória é marcada
como user ou como supervisor.

<!-- S24 -->
Um programa no anel 3
que toca numa página supervisor
não recebe os dados.
Ele é parado.

<!-- S25 -->
Seu navegador e seu jogo
rodam os dois no anel 3.
O que mantém os dois separados
é que cada um tem o seu próprio mapa da memória.
A memória do outro programa
simplesmente não está nele.

<!-- S26 -->
Então, quando um jogo trava,
o estrago fica dentro do jogo.
O kernel faz a limpeza.
Todo o resto continua.

<!-- S27 -->
Agora olhe de novo para a CrowdStrike.
O driver dela rodava no anel 0,
bem ao lado do kernel.

<!-- S28 -->
Não há nada acima do anel 0
que consiga pegar um erro desses.

<!-- S29 -->
Então o Windows fez a única coisa segura que restava.
Parou a máquina inteira, de propósito,
em vez de continuar com uma memória
em que já não podia confiar.

<!-- S30 -->
É isso que é a tela azul.

<!-- S31 -->
E como o driver iniciava
toda vez que o Windows iniciava,
cada reinício trazia a falha de volta.

<!-- S32 -->
Mas isso levanta uma pergunta.
Se o seu navegador não pode tocar no hardware,
como ele consegue salvar um arquivo
ou mandar qualquer coisa pela rede?

<!-- S33 -->
Ele pede.

<!-- S34 -->
O programa coloca o pedido
nos registradores do processador.
Qual arquivo. Para onde vão os dados.
Quantos.

<!-- S35 -->
Depois executa uma instrução especial.
Num PC moderno, ela se chama SYSCALL.

<!-- S36 -->
Nesse instante, o processador muda
do anel 3 para o anel 0...

<!-- S37 -->
mas não pula
para onde o programa quiser.
Ele pula para um único ponto de entrada
que o kernel escolheu antes.

<!-- S38 -->
O kernel confere o pedido,
faz o trabalho
e volta para o anel 3.
O programa nunca tocou no disco por conta própria.

<!-- S39 -->
Isso é uma chamada de sistema,
e acontece o tempo todo.

<!-- S40 -->
Nós contamos num notebook.
Um programa que não faz absolutamente nada
mesmo assim faz 30.

<!-- S41 -->
O Firefox, ao abrir
e carregar uma página da Wikipédia,
fez cerca de 670 mil
em 20 segundos...
e isso com a nossa contagem deixando ele mais lento.

<!-- S42 -->
Cada uma delas
é uma ida e volta através do muro.

<!-- S43 -->
O que deixa uma coisa estranha.
Quatro anéis,
e só precisamos de dois.

<!-- S44 -->
O que aconteceu com os anéis 1 e 2?

<!-- S45 -->
A ideia dos anéis é mais antiga que o PC.
O Multics, um sistema operacional
do fim dos anos 1960,
tinha oito.

<!-- S46 -->
A ideia era ter camadas de confiança.
O núcleo do sistema no meio,
serviços menos confiáveis em volta
e os programas do lado de fora.

<!-- S46b -->
A Intel desenhou o mesmo esquema.
Os anéis 1 e 2 eram para
as camadas do meio,
como drivers e serviços do sistema.
Mais confiáveis que os seus apps,
menos que o kernel.

<!-- S47 -->
Duas coisas atrapalharam.

<!-- S48 -->
Primeiro, sistemas como Unix e Windows NT
foram feitos para rodar
em vários tipos de processador.

<!-- S49 -->
E a única divisão
que todo processador oferecia
eram dois níveis.
Um para o kernel,
um para todo o resto.

<!-- S50 -->
Segundo, o próprio processador x86.
Quando ele mapeia a memória,
cada página só conhece dois estados.
User ou supervisor.

<!-- S51 -->
Os anéis 1 e 2 contam como supervisor.
Então um driver no anel 1
ainda poderia mexer na memória do kernel.
O anel a mais não protegeria grande coisa.

<!-- S51b -->
Alguns sistemas usaram mesmo assim.
O OS/2 deixava alguns programas entrar no anel 2,
só para falar direto com o hardware.

<!-- S51c -->
E antes de os processadores terem suporte
para rodar máquinas virtuais,
o Xen e o VirtualBox colocavam o kernel do sistema convidado
no anel 1,
para que o sistema por baixo
pudesse ficar com o anel 0 só para si.

<!-- S52 -->
Em 2023, a Intel propôs
eliminar de vez os anéis 1 e 2.

<!-- S53 -->
Em dezembro de 2024, ela desistiu do plano.
Eles continuam no seu processador.
Quase nada usa.

<!-- S54 -->
Até aqui, isso parece tranquilizador.
As regras estão no hardware,
e o hardware confere cada acesso.

<!-- S55 -->
Em 2017, três equipes de pesquisadores,
trabalhando separadamente,
acharam um jeito de atravessar esse muro.

<!-- S56 -->
Chamaram de Meltdown.
E para acompanhar,
você precisa conhecer um truque
que os processadores modernos usam.

<!-- S57 -->
Um processador não espera
uma instrução terminar
antes de começar a próxima.
Ele se adianta
com instruções que provavelmente vai precisar.

<!-- S58 -->
Se ele errou o palpite,
joga os resultados fora,
como se nada tivesse acontecido.

<!-- S59 -->
Aqui está a falha.
Nos chips da Intel afetados,
um programa no anel 3 podia pedir
um byte da memória do kernel...

<!-- S60 -->
e o processador buscava esse byte
e passava para as próximas instruções
antes de terminar de conferir
se aquilo era permitido.

<!-- S61 -->
A conferência falhava, sim.
O resultado era jogado fora.

<!-- S62 -->
Mas essas próximas instruções
já tinham usado o byte secreto
para puxar um pedaço
da própria memória do programa
para o cache do processador.

<!-- S63 -->
E o cache não esquece
só porque o resultado foi cancelado.

<!-- S64 -->
Então o programa cronometra
a rapidez com que cada pedaço da sua memória responde.
O que volta rápido
entrega o byte secreto.

<!-- S65 -->
Um byte de cada vez,
um programa comum podia ler
a memória do kernel,
e qualquer segredo que estivesse nela.
Senhas e chaves de criptografia inclusive.

<!-- S66 -->
O Meltdown afetava processadores Intel
desde 1995.

<!-- S67 -->
Ele foi divulgado
em 3 de janeiro de 2018.

<!-- S68 -->
A correção não podia mudar o silício.
Então os sistemas operacionais mudaram o mapa.

<!-- S69 -->
Enquanto o seu programa roda,
a memória do kernel agora é tirada
quase por completo do mapa dele.
Não há nada ali para buscar.

<!-- S70 -->
Mas lembre das chamadas de sistema.
Cada passagem pelo muro
agora também precisa trocar o mapa.

<!-- S71 -->
A Red Hat mediu as correções para o Meltdown
e uma falha parecida, o Spectre.
Menos de 1% em algumas tarefas...
até 19% em bancos de dados sobrecarregados.

<!-- S72 -->
A regra estava certa o tempo todo.
O processador só conferia tarde demais.

<!-- S73 -->
O que nos traz de volta à CrowdStrike,
e a uma pergunta mais difícil.

<!-- S74 -->
Por que um programa de segurança
estava no anel 0, para começo de conversa?

<!-- S75 -->
Porque de lá ele vê tudo.
Ele inicia antes dos outros softwares.
E um malware com direitos de administrador
tem mais dificuldade para desligá-lo.

<!-- S76 -->
A própria lista da Microsoft
termina com um aviso.
Drivers no kernel oferecem isso à custa da resiliência.

<!-- S77 -->
Depois do apagão,
a Microsoft começou a criar um jeito
de os antivírus
rodarem fora do kernel.

<!-- S78 -->
No segundo semestre de 2026,
isso ainda está só nas versões de teste do Windows.
E o kernel não foi fechado
para as empresas de segurança.

<!-- S79 -->
Seus jogos enfrentam o mesmo dilema.

<!-- S80 -->
Cheats que rodam no kernel
são invisíveis para um anti-cheat
que roda no anel 3.

<!-- S81 -->
Então o anti-cheat se mudou para lá também.
O Vanguard, da Riot, usado no Valorant,
coloca um driver no anel 0.
Na maioria dos PCs, ele carrega quando o Windows inicia...
mesmo que você nunca abra o jogo.

<!-- S82 -->
Isso não faz dele um programa com defeito.
Mas ele fica no mesmo lugar
onde ficava o driver da CrowdStrike,
onde um único erro para a máquina inteira.

<!-- S83 -->
Então por que um programa não consegue
tomar conta do seu computador?

<!-- S84 -->
Porque o processador mantém
quase todos os programas longe do centro
e confere cada um toda vez que eles batem na porta.

<!-- S85 -->
Mas o processador não pode decidir
quem pode entrar.
Quem decide são as pessoas...
toda vez que instalam um driver.

<!-- S86 -->
Então aqui vai uma pergunta para os comentários.
Quem deveria decidir quais programas
entram no anel 0:
você, a Microsoft
ou as empresas que fazem esses programas?
