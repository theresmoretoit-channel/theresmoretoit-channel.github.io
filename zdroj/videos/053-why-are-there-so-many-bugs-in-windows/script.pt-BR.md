<!-- S01 -->
Em setembro de 2026, um único lote
de atualizações do Windows quebrou
quatro coisas de uma vez.

<!-- S02 -->
O áudio parou de funcionar.
O Remote Desktop parou de funcionar.
As pastas compartilhadas em máquinas
virtuais pararam de funcionar.

<!-- S03 -->
E alguns computadores deixaram de
confiar na rede da empresa
à qual pertenciam,
e ninguém conseguiu fazer login.

<!-- S04 -->
Um lote.
Uma terça-feira.

<!-- S05 -->
E se você está achando
que isso é só mais uma
atualização ruim do Windows...

<!-- S06 -->
não é.

<!-- S07 -->
Porque isso vem acontecendo
de novo, e de novo, e de novo.

<!-- S08 -->
Afinal, o que o QA deles faz?

<!-- S09 -->
Como uma empresa desse tamanho
lança uma atualização do sistema
e não percebe algo tão óbvio?

<!-- S10 -->
Vamos começar pela menor delas.

<!-- S11 -->
A Microsoft lançou uma atualização
que mudou algumas coisas
na barra de tarefas.
E logo depois admitiu
que havia um problema
nas configurações do cursor.

<!-- S12 -->
Para algumas pessoas, o cursor escolhido
virava uma seta branca grande.
Daquelas que fazem você conferir
se não ligou por engano
um computador de 1998.

<!-- S13 -->
O cursor que você escolheu com cuidado?
Sumiu.
E colocá-lo de volta
pelo visto também não funcionava.

<!-- S14 -->
Agora você deve estar pensando:
todo software tem bugs.
Exatamente.

<!-- S15 -->
Mas há diferença entre:
“Encontramos uma falha rara
numa configuração de hardware
pouco comum.”

<!-- S16 -->
E:
“Depois da nossa atualização,
seu mouse não se parece com
o mouse que você escolheu.”

<!-- S17 -->
Porque alguém precisa instalar.
Alguém precisa fazer login.
Alguém precisa mexer o mouse.
E pelo visto isso não bastou.

<!-- S18 -->
Depois tem o áudio.
Instala uma atualização.
Reinicia.
Sem som.

<!-- S19 -->
Alguns dispositivos de áudio USB
simplesmente param, e o Windows avisa
que não é possível iniciar o dispositivo.

<!-- S20 -->
E áudio não é exatamente
um recurso exótico.
Você pensaria que um dos testes básicos
de um sistema operacional seria:

<!-- S21 -->
o computador ainda emite som?

<!-- S22 -->
Pelo visto é mais complicado
do que soa.
Literalmente.

<!-- S23 -->
Em casa, isso tudo é irritante.
O cursor fica ridículo.
As caixas de som ficam mudas.
Mas você sobrevive.

<!-- S24 -->
Já um servidor que deixa de confiar
na rede à qual pertence
significa que ninguém entra,
e alguém do departamento de TI
está tendo uma manhã péssima.

<!-- S25 -->
E é aqui que isso deixa de ser
uma coleção de casos engraçados.

<!-- S26 -->
Porque dá para olhar o histórico
de atualizações da própria Microsoft.
A Microsoft publica isso.
Todo mês eles listam
o que as atualizações quebraram.

<!-- S27 -->
E se você enfileirar
um único ano dessa lista,
o mesmo padrão
se repete sem parar.

<!-- S28 -->
Janeiro quebrou dispositivos de áudio
e webcams.
Fevereiro fez o cursor girar,
e a máquina parecia travada.

<!-- S29 -->
Março trouxe telas azuis
e instalações
que emperravam no meio.
Abril quebrou o login
por reconhecimento facial.

<!-- S30 -->
Em maio o Explorador parou
de responder ao mouse.
E outubro quebrou as conexões
com o próprio computador.

<!-- S31 -->
Não com a internet.
Com o endereço que diz “esta máquina”.

<!-- S32 -->
E duas delas
são realmente notáveis.

<!-- S33 -->
Uma atualização quebrou o botão
que redefine o PC.
Outra, a tela de recuperação,
onde mouses e teclados USB
pararam de responder.

<!-- S34 -->
Leia de novo.

<!-- S35 -->
Duas vezes em três meses,
uma atualização quebrou a ferramenta
que conserta um computador quebrado.

<!-- S36 -->
E mais um detalhe,
talvez o mais importante.
Aquele bug de áudio, em que o Windows
diz que o dispositivo não inicia.

<!-- S37 -->
Ele apareceu em janeiro.
E depois apareceu de novo,
vinte meses mais tarde.

<!-- S38 -->
O mesmo sintoma.
O mesmo tipo de dispositivo.
A mesma mensagem.

<!-- S39 -->
Essa não é uma história
sobre escrever código ruim.
É uma história sobre testes.

<!-- S40 -->
E nada disso é novo.

<!-- S41 -->
Em 2024 houve uma atualização
que impediu o Linux de iniciar
em máquinas com dois sistemas.
A mensagem de erro dizia, literalmente:

<!-- S42 -->
“Alguma coisa deu
muito errado.”

<!-- S43 -->
O que é, sinceramente, a mensagem de erro
mais precisa que o Windows já exibiu.

<!-- S44 -->
E em 2018 houve uma versão
que precisou ser retirada por completo,
depois que as pessoas relataram
que seus arquivos tinham sumido.

<!-- S45 -->
Então, a esta altura,
você pode razoavelmente concluir:
a Microsoft simplesmente não sabe
escrever software.

<!-- S46 -->
E isso explicaria tudo.
Os bugs.
As regressões.
As atualizações que consertam uma coisa
e quebram outra.

<!-- S47 -->
Mas essa explicação
tem um problema.
A Microsoft não faz só o Windows.

<!-- S48 -->
Eles fazem Office.
Visual Studio.
Exchange.
Teams.
E uma nuvem bem grande.

<!-- S49 -->
E tudo isso já teve
os próprios bugs, as próprias regressões
e as próprias quedas espetaculares.

<!-- S50 -->
E isso importa.
Porque a explicação de sempre para o
Windows é que ele carrega
trinta anos de código velho.

<!-- S51 -->
Um serviço de nuvem moderno
não carrega trinta anos
de coisa nenhuma.
Foi construído há pouco,
por gente que sabia
exatamente o que estava construindo.

<!-- S52 -->
E mesmo assim quebra.

<!-- S53 -->
Então o problema nunca foi
só código velho.
O problema é a complexidade
na escala da Microsoft.

<!-- S54 -->
E o Windows é o lugar
onde essa complexidade
aparece melhor.

<!-- S55 -->
Porque o Windows não é bem
um sistema operacional.
Lá embaixo há uma arquitetura
que remonta ao início dos anos noventa.

<!-- S56 -->
Depois décadas de interfaces.
Depois camadas de compatibilidade.
Depois drivers.
Depois serviços.

<!-- S57 -->
Depois frameworks mais novos,
construídos sobre frameworks mais velhos.
Depois um visual novo.
Depois outro visual novo.

<!-- S58 -->
É menos um sistema operacional
e mais uma escavação arqueológica
que, de algum jeito, ainda roda.

<!-- S59 -->
E a Microsoft não pode
aplainar o sítio,
porque há empresas que dependem
do que está embaixo.
Tem um vídeo inteiro sobre isso.

<!-- S60 -->
O que importa aqui
é o efeito disso nos bugs.
Cada camada precisa continuar funcionando
com cada camada abaixo dela.

<!-- S61 -->
Então uma mudança aqui em cima
pode quebrar alguma coisa
que ninguém olha há anos.

<!-- S62 -->
E há mais uma pista
sobre como isso funciona,
e ela não é sobre bugs.

<!-- S63 -->
É um padrão.
A Microsoft remove alguma coisa.
Os usuários reclamam.
A Microsoft leva anos
para reconsiderar.

<!-- S64 -->
E, enquanto isso,
outra pessoa faz uma ferramenta
que devolve aquilo.

<!-- S65 -->
E o engraçado é
que não são projetos
de hobby obscuros.

<!-- S66 -->
Existem aplicativos inteiros
cuja única função é fazer o Windows
se comportar mais como...

<!-- S67 -->
bem...
Windows.

<!-- S68 -->
Trazem de volta um menu Iniciar antigo.
Restauram a barra de tarefas.
Mudam o comportamento do Explorador.

<!-- S69 -->
E alguns dão a você mais controle
sobre o Windows do que o próprio Windows.

<!-- S70 -->
A Microsoft tem um número enorme
de engenheiros nesse sistema.
E aí alguém de fora diz:
tudo bem.
Eu mesmo devolvo a barra antiga.

<!-- S71 -->
E agora mudou mais uma coisa.
A Microsoft usa cada vez mais IA
na forma como escreve seu software.

<!-- S72 -->
O próprio presidente-executivo disse
que de vinte a trinta por cento
do código nos repositórios deles
hoje é escrito por software.

<!-- S73 -->
E isso deveria significar
mais produtividade.
Mais correções.
Desenvolvimento mais rápido.

<!-- S74 -->
Mas há um gargalo evidente.
Escrever código pode ficar mais rápido.

<!-- S75 -->
Testar um sistema legado enorme
não fica necessariamente mais rápido.

<!-- S76 -->
E se você consegue produzir mudanças
mais rápido do que consegue testar
como elas interagem com décadas
de código já existente...

<!-- S77 -->
talvez você acabe simplesmente
produzindo regressões mais rápido.

<!-- S78 -->
E aqui é bom ter cuidado.
Esse número é da Microsoft inteira,
não do Windows em particular.
E ninguém demonstrou
que a IA causou qualquer um desses bugs.

<!-- S79 -->
Talvez a IA não tenha deixado
a Microsoft pior em testes.

<!-- S80 -->
Talvez só tenha acelerado
o problema que já existia.

<!-- S80b -->
A propósito, se você quer ver
aonde o resto disso leva,
pode se inscrever no canal.

Isso ajuda muito o canal.

<!-- S81 -->
A maior parte deste vídeo argumentou
que a Microsoft tem
um problema real de qualidade.
E esse argumento se sustenta.

<!-- S82 -->
Mas aqui vem a parte
que surpreende as pessoas.
Por que o kernel
poderia ser diferente?

<!-- S83 -->
Porque quase tudo
que foi descrito até agora
não é o kernel.

<!-- S84 -->
O cursor.
A barra de tarefas.
O menu Iniciar.
As configurações.
A tela de recuperação.

<!-- S85 -->
Tudo isso fica por cima.

<!-- S86 -->
O kernel é a parte de baixo.
Ele decide qual programa roda
em qual núcleo do processador.
Ele distribui memória.
Ele conversa com o hardware.

<!-- S87 -->
E se essa parte desse muito errado,
o sintoma não seria
um mouse com cara ridícula.

<!-- S88 -->
O sintoma seria uma máquina
que para, corrompe seus dados
ou deixa alguém entrar em silêncio.

<!-- S88b -->
E o kernel tem uma coisa
que o resto do Windows não tem.
Restrições rígidas.

<!-- S88c -->
Um escalonador não pode decidir
se comportar de outro jeito
porque alguém redesenhou
o menu Iniciar.

<!-- S88d -->
O gerenciamento de memória não se
moderniza mudando um botão de lugar.
E um driver não pode presumir
que o hardware vai se comportar bem.

<!-- S88e -->
E, acima de tudo: o kernel não tem onde
esconder um erro, atrás de
uma página de configurações confusa.

<!-- S88f -->
O que é um motivo para suspeitar
que essa é uma história técnica
completamente diferente
do resto do Windows.

<!-- S89 -->
Mas suspeitar não é evidência.
Então olhe o que essa coisa
de fato teve que aguentar.

<!-- S90 -->
Aquela arquitetura lá embaixo é velha.
Muito velha.
E sobreviveu.

<!-- S91 -->
Ela virou o Windows 2000.
Depois XP.
Depois Vista.
Depois 7, 8, 10 e 11.

<!-- S92 -->
Os processadores mudaram.
O número de núcleos explodiu.
A capacidade de memória explodiu.
As máquinas virtuais deixaram de ser
exóticas e viraram o normal.

<!-- S93 -->
E a mesma família de código
acabou rodando em servidores
do mundo inteiro.

<!-- S94 -->
Servidores de arquivos.
Logins corporativos.
Máquinas virtuais.
Cargas que ninguém imaginou
quando aquilo foi projetado.

<!-- S95 -->
Se a parte que decide
o que roda e quando,
e que distribui a memória,
estivesse irremediavelmente quebrada...
a conta seria impossível de esconder.

<!-- S96 -->
Agora, uma confissão honesta.
Ninguém fora da Microsoft consegue ler
o código do kernel atual,
então ninguém pode chamá-lo de belo.

<!-- S96b -->
Embora alguém tenha olhado
uma versão mais antiga.

<!-- S96c -->
Parte do código do Windows 2000
vazou em 2004,
e no ano passado um pesquisador
passou o pente-fino nele.

<!-- S96d -->
As descobertas não foram lisonjeiras.
Bugs que ficaram naquele código
por dezesseis anos
até alguém corrigi-los.

<!-- S96e -->
Mas aquilo é o avô
do kernel de hoje,
e só uma fração vazou.
Diz algo sobre o ano 2000,
não sobre agora.

<!-- S97 -->
E sobreviver não é a mesma coisa
que ser excelente.

<!-- S98 -->
Então isto não é uma afirmação
de que o kernel do Windows é genial.
Ninguém sabe disso.

<!-- S99 -->
Mas temos décadas de evidências
de que ele dá conta do recado.

<!-- S100 -->
E essa é uma conclusão bem mais estranha
que “Windows ruim”.

<!-- S101 -->
Porque significa que a resposta
para “o que o QA deles faz”
provavelmente não é
“a Microsoft não sabe fazer software”.

<!-- S102 -->
É que eles passaram décadas
construindo coisas novas sobre velhas,
sem nunca poderem
jogar fora as velhas.

<!-- S103 -->
O resultado é enorme.
Poderoso.
Compatível.
E, de vez em quando, ridículo.

<!-- S104 -->
Você instala uma atualização.
Seu som some.
O cursor parece o do Windows 98.

<!-- S105 -->
E embaixo de tudo isso,
alguma coisa decide em silêncio
qual programa roda em seguida.
Distribui memória.
Conversa com o hardware.

<!-- S106 -->
Fazendo exatamente
o que deveria fazer.

<!-- S107 -->
Pelo menos...
é o que a gente acha.

<!-- S108 -->
Porque, diferente da barra de tarefas...
a gente não consegue ver.
