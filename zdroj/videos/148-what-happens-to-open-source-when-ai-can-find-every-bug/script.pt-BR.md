<!-- S01 -->
948.
Foi o número de formas diferentes que uma IA encontrou
de assumir o controle de um computador Linux por dentro.

<!-- S02 -->
Nenhuma senha roubada. Nenhuma invasão remota.
Cada uma começa com um usuário comum
sem nenhum privilégio especial,
e termina com root,
a conta que pode fazer qualquer coisa.

<!-- S03 -->
A OpenAI publicou o resultado em novembro de 2026.
A execução inteira custou
US$ 1,2 milhão em créditos de API.

<!-- S05 -->
Esses números são da própria OpenAI,
publicados um dia antes
de ela lançar o modelo que os produziu,
e ninguém de fora confirmou a contagem completa.
Mas centenas de relatórios e patches
já foram enviados.

<!-- S06 -->
Eis por que isso importa além do Linux.
O código-fonte do Linux é público.
Qualquer pessoa pode lê-lo.
Durante décadas, esse foi o argumento
para dizer que ele é seguro.

<!-- S07 -->
Então, se uma máquina consegue ler código público
e transformá-lo em exploits funcionais nessa escala,
o software deveria manter seu código em segredo, afinal?

<!-- S08 -->
Vamos olhar para um software que já faz isso.
Em abril de 2026, a Microsoft corrigiu
164 falhas de segurança
no seu dia mensal de atualizações.
Em outubro, corrigiu
1.413.

<!-- S09 -->
Só naquele mês, corrigiu mais
do que em qualquer ano inteiro antes dele.
Mais de 1.000 dessas correções eram no Windows,
e a Microsoft tinha avisado
que suas próprias ferramentas de IA impulsionariam o aumento.

<!-- S10 -->
Você não pode comparar os dois números diretamente.
As empresas contam de jeitos diferentes,
e a Microsoft estava vasculhando o próprio código privado.

<!-- S11 -->
Mas isso mostra uma coisa.
Manter o código privado
não tinha mantido os bugs do lado de fora.

<!-- S12 -->
Então, o que protege você de verdade?
Para responder a isso,
precisamos ver como essa máquina funciona,
porque cada etapa dela descarta alguma coisa.

<!-- S13 -->
O kernel do Linux tem
mais de 40 milhões de linhas de código.
Primeiro, agentes de reconhecimento o percorreram
e separaram as partes
que um usuário comum consegue de fato alcançar.

<!-- S14 -->
Sobraram cerca de 7%.
É a parte que eles julgaram valer a pena atacar,
não uma amostra aleatória,
então você não pode multiplicar o resultado por 14.

<!-- S15 -->
Em seguida, agentes analistas examinaram esse código
e listaram tudo o que era suspeito.
2.308 candidatos
em 12 horas.

<!-- S16 -->
Mas uma suspeita não prova nada.
Então outros agentes escreveram programas de teste
e os rodaram em máquinas virtuais isoladas.
1.724 bugs
se mostraram reais.

<!-- S17 -->
Depois veio a parte cara:
construir exploits funcionais,
com as proteções padrão
de um sistema desktop comum ativadas.
1.169
chegaram ao root.

<!-- S18 -->
Agrupe esses casos pela falha de origem,
e você chega aos 948.

<!-- S19 -->
Há um detalhe no relatório
que é difícil de esquecer.
Em uma das primeiras execuções,
os agentes relataram 200 sucessos.
Depois, humanos verificaram como eles tinham chegado lá.

<!-- S20 -->
Vinte deles tinham chegado ao root
por outro bug desconhecido,
não pelo que tinham recebido ordem de usar.
Enviados para abrir uma porta,
encontraram outra que ninguém conhecia.

<!-- S21 -->
Numa amostra dos seus exploits,
a OpenAI identificou dez técnicas de exploração
que especialistas externos nunca tinham visto.

<!-- S22 -->
Em julho, um modelo anterior
encontrou 166 dessas falhas.
Três meses de correções depois,
o modelo mais novo encontrou 948.
Os bugs não tinham acabado.
A execução posterior encontrou muito mais.

<!-- S23 -->
Agora, existe um limite importante.
Nada disso invade o seu computador
pela internet.
O atacante já precisa estar na máquina,
como um usuário comum.

<!-- S24 -->
Isso tranquiliza menos do que parece,
porque ataques reais muitas vezes acontecem em duas etapas.
Primeiro você entra,
por uma falha no navegador ou um download malicioso.
Depois você precisa de root.
Esta é a segunda etapa.

<!-- S25 -->
O conselho da OpenAI é direto.
Num sistema sem os patches mais recentes,
trate qualquer conta comum como root,
pelo menos diante de um atacante com muitos recursos.

<!-- S26 -->
Então, onde fica
o velho argumento a favor do código aberto?
No fim dos anos noventa,
Eric Raymond deu a ele um slogan:
"Com olhos suficientes, todos os bugs são superficiais."

<!-- S27 -->
Ele chamou isso de Lei de Linus.
É uma ideia bonita, com uma suposição embutida:
a de que alguém está realmente olhando.

<!-- S28 -->
Em 2014, um bug chamado Heartbleed
apareceu no OpenSSL,
o código que protegia uma enorme parte da web.
Estimava-se que cerca de meio milhão de servidores seguros
estivessem expostos.

<!-- S29 -->
O bug estava em código público havia dois anos.
O projeto recebia
cerca de US$ 2.000 por ano em doações
e tinha um único desenvolvedor em tempo integral.

<!-- S30 -->
Qualquer um podia ler.
Quase ninguém leu.

<!-- S31 -->
Essa sempre foi a verdadeira fraqueza do código aberto.
Não olhos demais sobre o código. Olhos de menos.

<!-- S32 -->
E é essa a parte que a IA muda.
Uma máquina pode continuar varrendo o código
e investigar muito mais candidatos
do que um pesquisador humano daria conta sozinho.
A velha promessa finalmente está sendo cumprida,
para todo mundo, atacantes incluídos.

<!-- S33 -->
Então o código público agora é examinado de verdade.
Escondê-lo ajuda?

<!-- S34 -->
Um programa fechado ainda precisa rodar,
então o código de máquina dele fica
em todo computador que o usa.
Ferramentas como o Ghidra transformam isso de volta
em algo parecido com código-fonte.

<!-- S35 -->
E existe um truque clássico.
Compare um programa
antes e depois de uma atualização de segurança.
O que mudou mostra onde estava a brecha.

<!-- S35b -->
Isso diz aos atacantes onde mirar,
bem antes de todos os sistemas
terem instalado a atualização.

<!-- S36 -->
A Anthropic testou isso no kernel do Windows,
com 21 falhas
que a Microsoft tinha corrigido havia pouco,
e sem código-fonte.
A IA provocou o primeiro travamento em 31 minutos.
Em seis horas, já eram 18.

<!-- S37 -->
Oito viraram exploits funcionais
capazes de assumir o controle total da máquina,
por cerca de US$ 2.000 cada.

<!-- S38 -->
Mas esses não eram bugs desconhecidos.
Os patches já apontavam
onde estavam os problemas.
Encontrar uma falha nova do zero é mais difícil.

<!-- S39 -->
Então o sigilo ainda custa algo ao atacante.
É uma lombada, não um muro.
Qual é a altura da lombada?
Não existe um número público.

<!-- S40 -->
E o outro lado?
O que ser aberto realmente traz para você?
A resposta está num pequeno detalhe
do relatório da OpenAI.

<!-- S41 -->
Durante os dez dias daquela varredura e análise,
mais de 100 dessas falhas do Linux
foram corrigidas, ou estavam prestes a ser,
por outras pessoas.
Cerca de 300 outras
já estavam sendo discutidas em público.

<!-- S42 -->
Outras pessoas estavam encontrando os mesmos bugs
ao mesmo tempo.

<!-- S43 -->
Linus Torvalds já tinha descrito isso em maio.
Ele disse que os relatórios gerados por IA
tinham deixado a lista de e-mails de segurança do kernel
"quase totalmente impossível de gerenciar",
porque pessoas diferentes viviam encontrando
as mesmas coisas com as mesmas ferramentas.

<!-- S44 -->
E o conselho dele foi este:
"Se você encontrou um bug usando ferramentas de IA,
é bem provável que outra pessoa também tenha encontrado."

<!-- S45 -->
As regras do kernel agora dizem isso com todas as letras.
Um bug encontrado com IA deve ser tratado como público,
porque esses bugs aparecem
para vários pesquisadores,
muitas vezes no mesmo dia.

<!-- S46 -->
Pense no que isso faz
com a ideia de um bug secreto.
Se foi barato para você encontrar,
foi barato para todo mundo.

<!-- S47 -->
Com código aberto,
qualquer um pode examinar o relatório,
verificar a correção e contestar o resultado.
Com software fechado,
na maioria das vezes você precisa confiar no fornecedor.

<!-- S49 -->
Mas a abertura tem um custo,
e não é o que você esperaria.
É tentador dizer
que um projeto pequeno não pode pagar pela varredura.
Empresas de IA já estão
oferecendo acesso gratuito aos mantenedores.

<!-- S50 -->
O que falta são pessoas.
O kernel costumava registrar
cerca de 500 problemas de segurança por versão.
Este ano, passou de 1.500.
Muitos são pequenos,
mas alguém ainda precisa analisar cada um.

<!-- S51 -->
Em janeiro, o projeto curl
encerrou seu programa pago de recompensa por bugs,
para parar de premiar uma enxurrada de relatórios inúteis.

<!-- S52 -->
Mesmo bons relatórios só passam o trabalho para a próxima etapa.
Patches gerados por IA ainda precisam de revisão humana.
Algumas das primeiras correções acrescentavam código desnecessário
ou deixavam passar outras versões do mesmo bug.

<!-- S53 -->
Você pode pagar por mais varredura.
Não dá para pagar por mais pessoas
que entendam um trecho de código tão bem.
Aqui, uma empresa com uma equipe de segurança paga
tem, sim, uma vantagem.

<!-- S54 -->
E aí vem o último problema.
Corrigido não é o mesmo que instalado.

<!-- S55 -->
Em março de 2017,
a Microsoft corrigiu uma falha no Windows.
Código fechado, um fornecedor, um sistema de atualização.
Dois meses depois,
o WannaCry passou por essa mesma brecha
e entrou em cerca de 200.000 computadores
em uns 150 países.

<!-- S56 -->
Aquele patch teve dois meses para se espalhar,
e não foi suficiente.
Um atacante talvez já não dê dois meses a você.
No mesmo estudo da Anthropic,
a IA pegou uma correção pública
do motor JavaScript do Firefox
e tinha um exploit funcional em menos de uma hora.

<!-- S57 -->
A versão corrigida do Firefox
ainda estava a 18 dias de sair.

<!-- S58 -->
Esse é o perigo de publicar uma correção.
A informação pode chegar aos atacantes
antes que a atualização chegue a você.

<!-- S59 -->
Uma correção do Linux tem um longo caminho a percorrer,
do kernel para uma versão estável,
para a sua distribuição, para o seu dispositivo.
Um celular pode esperar meses, ou para sempre.

<!-- S60 -->
E o software fechado não escapa disso.
Acabamos de ver: o patch do Windows foi suficiente.
Toda atualização agora também é um mapa.

<!-- S60b -->
Então mantenha tudo atualizado,
seu computador, seu celular, até o seu roteador,
e instale as atualizações assim que chegarem.
À medida que a IA fica melhor em transformar correções em ataques,
cada dia de espera vai pesar mais.

<!-- S61 -->
Então, o código aberto ainda é mais seguro?
Sinceramente, ninguém sabe.
Até onde se sabe publicamente,
ninguém fez o mesmo teste nos dois lados,
com as mesmas regras.

<!-- S62 -->
O que dá para dizer é mais modesto.
Esconder o código rende menos do que antes.
Mostrá-lo permite que qualquer um confira o trabalho,
e joga uma pilha maior desse trabalho
nas mãos de quem mantém o código.

<!-- S64 -->
Mesmo que a IA nunca encontre todos os bugs,
ela já mudou o custo de encontrá-los.

<!-- S65 -->
O que importa agora é quanto tempo uma brecha fica aberta
entre o momento em que alguém a encontra
e o momento em que ela é fechada na sua máquina.

<!-- S66 -->
Então, aqui vai uma pergunta para você.
Se qualquer bug pode ser encontrado por qualquer um,
você prefere confiar em código que pode ler,
ou numa empresa que é paga para corrigi-lo?
Conta aqui nos comentários.
