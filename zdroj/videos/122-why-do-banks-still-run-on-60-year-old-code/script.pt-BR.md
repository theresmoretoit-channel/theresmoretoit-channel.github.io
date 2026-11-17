<!-- S01 -->
Novecentas e noventa e nove libras
e noventa e nove pence.
Some um penny.

<!-- S02 -->
O resultado é zero.

<!-- S03 -->
Nenhuma mensagem de erro. Nenhum travamento.
Só um zero, gravado em silêncio na conta.

<!-- S04 -->
Em COBOL, quando o campo do resultado
é pequeno demais para guardá-lo,
o dígito que sobra pode simplesmente sumir.
A menos que o programa peça um aviso,
o cálculo segue em frente.

<!-- S05 -->
E ele também não arredonda.
Duas libras e trinta e quatro pence e meio,
guardadas com precisão de um penny,
viram duas e trinta e quatro.

<!-- S06 -->
Escreva uma palavra a mais, ROUNDED,
e vira duas e trinta e cinco.

<!-- S07 -->
Nenhuma das duas coisas é um bug.
São regras.
E muitos bancos do mundo
ainda funcionam com regras assim.

<!-- S08 -->
COBOL é uma linguagem de programação
de 1959.
Nem todo programa escrito nela é tão antigo.
Mas a linguagem é,
e os hábitos dela também.

<!-- S09 -->
Então por que os bancos não a substituíram?
Dinheiro eles têm.
Engenheiros também.

<!-- S10 -->
Para descobrir, vamos ver três casos reais.
Um banco que tentou deixar seu sistema antigo,
outro que conseguiu,
e uma crise em que todo mundo culpou o COBOL.

<!-- S11 -->
Mas antes, aquele meio penny que sumiu.

<!-- S12 -->
Digamos que você reescreva esse programa bancário
numa linguagem moderna.
Você provavelmente corrigiria essas regras.
O estouro vira um erro.
O meio penny é arredondado para cima.

<!-- S13 -->
Mais limpo. Mais seguro.
E agora, sempre que aparece meio penny,
o seu programa discorda do antigo.

<!-- S14 -->
Linguagens modernas conseguem fazer contas decimais exatas.
Java tem um tipo feito para isso.
Mas mesmo ali,
a regra de arredondamento é uma escolha.

<!-- S15 -->
Uma configuração comum, quando dá exatamente no meio, arredonda para cima:
duas e trinta e cinco.
Outra arredonda para o dígito par mais próximo:
duas e trinta e quatro.
As duas estão certas. Só uma bate.

<!-- S16 -->
E com o ponto flutuante comum,
o que a maior parte do código usa por padrão,
fica ainda mais estranho.
Zero vírgula um mais zero vírgula dois
não dá zero vírgula três.

<!-- S17 -->
Então substituir o COBOL não é tradução.
É encontrar cada regra como essa,
em milhões de linhas,
e manter cada uma exatamente como era.

<!-- S18 -->
E como ele foi parar lá, para começo de conversa?

<!-- S19 -->
Em maio de 1959,
o Departamento de Defesa dos EUA
convocou uma reunião no Pentágono.
Fabricantes de computadores, órgãos do governo
e grandes empresas compareceram,
todos com o mesmo problema.

<!-- S20 -->
Cada computador tinha sua própria linguagem.
Um programa de folha de pagamento feito para uma máquina
não servia em outra.

<!-- S21 -->
Um comitê projetou uma linguagem comum
para os negócios.
Sua maior influência foi o FLOW-MATIC,
da equipe de Grace Hopper na Remington Rand.

<!-- S22 -->
E em dezembro de 1960,
praticamente o mesmo programa em COBOL
rodou em dois computadores
de fabricantes rivais.
A ideia era exatamente essa.

<!-- S23 -->
Ela foi feita para que as pessoas conseguissem entendê-la.
ADD PAYMENT TO ACCOUNT-BALANCE.
Você provavelmente adivinha o que isso faz.

<!-- S24 -->
E guardava dinheiro do jeito que as pessoas escrevem:
como dígitos decimais.
A vírgula decimal
nem precisa ser guardada.
A descrição do campo diz onde ela fica:
os dois últimos dígitos são os pence.

<!-- S25 -->
Em 1964, a IBM lançou o System/360.
O projeto dele incluía instruções
para aritmética decimal.

<!-- S26 -->
E desde então a IBM projeta seus mainframes
para que continuem compatíveis.
Muitos programas antigos ainda podem rodar
nas máquinas de hoje
sem precisar ser reescritos.

<!-- S27 -->
Então raramente houve um momento
que obrigasse alguém a mudar.
Todo ano o código continuava funcionando,
e todo ano acumulava mais regras.
Novos produtos, novos impostos, novas regulamentações,
novas exceções.

<!-- S28 -->
Ninguém contou quanto COBOL
ainda roda no mundo.
Mas a IBM diz que quarenta e cinco
dos cinquenta maiores bancos do mundo
ainda usam seus mainframes.

<!-- S29 -->
E alguns donos contaram.
Em 2017, a Administração da Seguridade Social
dos EUA disse que seus sistemas tinham
mais de sessenta milhões de linhas de COBOL.

<!-- S30 -->
Em 2025, auditores do governo dos EUA
listaram os onze sistemas federais
que mais precisavam ser substituídos.

<!-- S31 -->
Eles tinham entre vinte e três
e sessenta anos,
e custavam cerca de setecentos e cinquenta
milhões de dólares por ano para manter funcionando.

<!-- S32 -->
Então o código é velho, está em toda parte
e cheio de regras que ninguém pôs no papel.
O perigo, com certeza, está em mantê-lo.

<!-- S33 -->
Vamos ver o que acontece
quando um banco sai.

<!-- S34 -->
Em 2018, um banco britânico chamado TSB
tinha cerca de cinco milhões de clientes,
e um problema.

<!-- S35 -->
Os sistemas dele eram alugados
do Lloyds Banking Group,
um concorrente,
e as tarifas iam subir muito.

<!-- S36 -->
Então o TSB decidiu levar tudo
para uma plataforma nova,
criada pelo seu novo dono,
o banco espanhol Sabadell.

<!-- S37 -->
Um fim de semana em abril.
No domingo à noite,
o novo sistema foi ligado.

<!-- S38 -->
Na segunda, houve cerca de
novecentas mil tentativas de login.
Só cerca de um login no internet banking
em cada dez deu certo.

<!-- S39 -->
Pagamentos falharam.
Alguns clientes entraram na conta
e viram contas de outras pessoas.

<!-- S40 -->
O pior durou cerca de uma semana.
O TSB só voltou à normalidade
em dezembro.

<!-- S41 -->
As consequências custaram cerca de
trezentos e trinta milhões de libras
só em 2018.
Depois, os reguladores somaram
quase quarenta e nove milhões em multas.

<!-- S42 -->
E aqui vem a parte estranha.
Os dados dos clientes chegaram intactos.
Os dois relatórios oficiais dizem isso.

<!-- S43 -->
O que falhou foi a nova plataforma em volta deles.
Dois data centers, configurados de forma diferente.
Desempenho testado em só um deles,
com as metas reduzidas
depois que os testes não passaram.

<!-- S44 -->
E não tinha volta.
Depois que os dados foram transferidos,
voltar ao sistema antigo era,
nas palavras do regulador,
“praticamente impossível”.

<!-- S45 -->
O TSB não estava fugindo de um sistema quebrado.
Estava deixando um que funcionava,
por causa de quem era o dono
e de quanto custava.
O perigoso foi sair.

<!-- S46 -->
Então sair é sempre um desastre?

<!-- S47 -->
Em 2008, o Commonwealth Bank da Austrália
decidiu substituir os sistemas centrais
que o serviam
havia mais de quarenta e cinco anos.

<!-- S48 -->
O plano: cerca de quinhentos e oitenta
milhões de dólares australianos,
e quatro anos.

<!-- S49 -->
Levou cinco.
Mais tarde, a imprensa estimou o total
em cerca de um bilhão e cem milhões,
à medida que o projeto crescia.

<!-- S50 -->
Mas ele não mudou tudo
num só fim de semana.
As contas de depósito foram primeiro, em 2010.
As contas empresariais vieram em 2011,
e os empréstimos, em 2012.

<!-- S51 -->
O banco podia acompanhar cada etapa,
conferir os resultados e aprender com eles
antes de passar para a próxima.

<!-- S52 -->
No fim, segundo o próprio banco,
ele se tornou o primeiro grande banco australiano
com operações bancárias em tempo real,
vinte e quatro horas por dia.

<!-- S53 -->
Então dá para fazer.
Mas veja o que foi preciso.
Cinco anos, uma conta muito maior
e paciência.

<!-- S54 -->
Modernização não é uma compra.
É um projeto,
com riscos próprios.

<!-- S55 -->
Agora, a crise
em que todo mundo culpou o COBOL.

<!-- S56 -->
Março de 2020.
Quando a pandemia parou Nova Jersey,
os novos pedidos de seguro-desemprego saltaram
de menos de dez mil em uma semana
para mais de cento e cinquenta e cinco mil.

<!-- S57 -->
Dezesseis vezes mais,
em sete dias.
O órgão do seguro-desemprego não dava conta.

<!-- S58 -->
No início de abril, o governador
pediu voluntários.
Não só profissionais de saúde,
mas também gente que soubesse COBOL.
Os sistemas do estado, disse ele,
tinham mais de quarenta anos.

<!-- S59 -->
A história se espalhou rápido.
Um código antiquíssimo tinha desabado
com a pandemia.

<!-- S60 -->
Mas quando o auditor estadual
investigou o caso mais tarde,
não encontrou nenhuma evidência
de que os atrasos tivessem sido causados
pelos sistemas de computador.

<!-- S61 -->
Paralelamente, jornalistas que analisaram
as mensagens de erro que as pessoas viam
atribuíram muitas delas ao site que o público usava,
escrito numa linguagem bem mais nova, Java.
O código antigo por trás continuou rodando.

<!-- S62 -->
Então por que o estado precisava de programadores de COBOL?
Porque o Congresso estava mudando as regras.
Novos benefícios, novos valores,
novas pessoas com direito a eles,
e cada mudança tinha que entrar
no código, e rápido.

<!-- S63 -->
O problema não era o código ser velho.
Era que pouca gente sabia alterá-lo,
e que as linhas telefônicas e os funcionários
também estavam sobrecarregados.

<!-- S64 -->
Três casos.
Um banco que deixou um sistema que ainda funcionava,
e cuja migração fracassou.
Um banco que saiu com cuidado,
e deu certo.
E uma crise em que o código antigo levou a culpa,
e ninguém conseguiu provar que ele era a causa.

<!-- S65 -->
Isso não quer dizer que sistemas antigos nunca falhem.
Falham.
Ficam caros,
as pessoas que os entendem se aposentam,
e esperar também tem seu custo.

<!-- S66 -->
Mas a idade é fácil de ver,
e os riscos reais, não.
Regras que ninguém pôs no papel.
Conhecimento na cabeça de poucas pessoas.
E o momento da virada.

<!-- S67 -->
Por isso muitos bancos não substituem
o núcleo antigo de uma vez.
Eles o envolvem.
O app no seu celular é novo,
mas pode estar conversando com algo
muito mais antigo.

<!-- S68 -->
E o substituem peça por peça.
Em 2004, o autor de software Martin Fowler
batizou isso com o nome da figueira-estranguladora,
uma planta da floresta tropical que cresce em volta de uma árvore
até conseguir se sustentar sozinha.

<!-- S69 -->
O sistema antigo continua funcionando
enquanto o novo cresce em volta dele,
uma tarefa de cada vez,
até que nada mais dependa do antigo.

<!-- S70 -->
O que nos traz de volta àquele meio penny.
Em algum lugar, um programa ainda pode descartá-lo,
porque alguém decidiu que seria assim,
décadas atrás.
Substituir esse programa significa saber disso,
e de tudo o que for parecido.

<!-- S71 -->
O sistema antigo não é necessariamente
o que falha.
Às vezes, é o que o substitui.

<!-- S72 -->
Porque substituir a tecnologia
não é o mesmo que eliminar o risco.
Às vezes, só leva o risco
para um único fim de semana de abril.

<!-- S73 -->
Então aqui vai uma pergunta para você.
Se um sistema funciona há quarenta anos,
qual é a hora certa de substituí-lo?
E você mesmo já teve que substituir um?
Conta aqui nos comentários.
