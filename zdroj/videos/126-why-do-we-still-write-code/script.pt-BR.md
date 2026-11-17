<!-- S01 -->
Aqui está um requisito completo
para um software empresarial.
Um usuário pode cancelar um pedido.

<!-- S02 -->
Seis palavras.
Qualquer desenvolvedor concordaria.
Qualquer cliente assinaria embaixo.

<!-- S03 -->
Então, um usuário pode cancelar um pedido
depois que a fatura já foi emitida?
E depois que ele já foi enviado?

<!-- S04 -->
Cancelar o pedido também cancela
a reserva com o fornecedor?
E se uma pessoa cancelar
e outra aprovar o mesmo pedido
no mesmo segundo?

<!-- S05 -->
A frase não responde a nada disso.
O código precisa responder a tudo.
E essa lacuna, entre a frase
e o código, é aquilo pelo que os programadores
são pagos de verdade.
Pelo menos, eram.

<!-- S06 -->
Hoje existe uma ideia tentadora.
Escrever só as frases.
Guardá-las em documentos,
revisá-las, versioná-las.
E deixar uma IA escrever o código.

<!-- S07 -->
A especificação vira
o código-fonte.
E o código vira o que o assembly
é hoje: algo que roda
e que ninguém lê.

<!-- S08 -->
É uma boa ideia.
Só que também não é nova.

<!-- S09 -->
Há quase setenta anos, as pessoas tentam
elevar o nível
em que dizemos aos computadores o que fazer.
As ferramentas eram diferentes,
e os objetivos também.
Mas cada uma passou mais trabalho
das pessoas para as máquinas.

<!-- S10 -->
Em 1957, uma equipe da IBM
publicou um artigo sobre o FORTRAN.
O título o chamava de
sistema de codificação automática.

<!-- S11 -->
Na época, o nome era exato.
Você escrevia fórmulas,
e as instruções de máquina,
a parte que as pessoas escreviam à mão,
agora eram produzidas pela própria máquina.

<!-- S12 -->
Hoje a gente chama o FORTRAN de código.

<!-- S13 -->
Nos anos 1980, as ferramentas CASE
e as linguagens de quarta geração
subiram mais um nível.
Você desenha os diagramas, preenche os formulários,
e boa parte da aplicação
é gerada para você.

<!-- S14 -->
Em 2001, o Object Management Group,
a entidade por trás da UML,
anunciou a Model Driven Architecture.

<!-- S15 -->
A proposta vai soar familiar.
Você descreve o sistema uma vez só,
como um modelo, independente de qualquer tecnologia.
Depois, as ferramentas geram a implementação
para a plataforma de que você precisar.

<!-- S16 -->
As mesmas regras de negócio.
Tecnologia substituível.

<!-- S17 -->
E em 2014, os analistas da Forrester
deram nome às plataformas
para criar aplicações empresariais
com o mínimo possível
de código escrito à mão.
Chamaram isso de low-code.

<!-- S18 -->
Então, alguma coisa disso funcionou?

<!-- S19 -->
Em parte.
Em 2014, pesquisadores da Universidade de Lancaster
publicaram uma pesquisa
com 450 pessoas
que realmente usavam
desenvolvimento orientado a modelos.

<!-- S20 -->
Funcionou, sim,
e de forma mais ampla do que muitos pensavam.
Mas raramente para um sistema inteiro.
As pessoas usavam em partes-chave
e construíam o resto de outros jeitos.

<!-- S21 -->
Os maiores obstáculos encontrados
eram pessoas e organizações,
não ferramentas.
Mas também existe um limite técnico,
e os programadores têm uma piada sobre ele.

<!-- S22 -->
Uma especificação precisa o bastante
para gerar o programa inteiro a partir dela...
já tem nome.
Se chama código.

<!-- S23 -->
Para gerar tudo,
o modelo tinha que dizer tudo.
Cada estado, cada exceção,
cada “e se duas pessoas fizerem isso ao mesmo tempo?”.

<!-- S24 -->
Nesse ponto,
você não escapou da programação.
Só a levou para dentro de um diagrama,
que muitas vezes é mais difícil de ler,
de comparar e de revisar.

<!-- S25 -->
Já no fim dos anos 1970,
Edsger Dijkstra resumiu a outra metade
numa nota curta com um título direto.
Sobre a tolice
da programação em linguagem natural.

<!-- S26 -->
Para ele, a notação formal
não é um fardo que a gente tem que aguentar.
Ele a chamou de ferramenta incrivelmente eficaz
para descartar todo tipo de absurdo.

<!-- S27 -->
A linguagem comum não descarta os absurdos.
Esconde.
Um usuário pode cancelar um pedido.

<!-- S28 -->
Então, se nada disso substituiu o código,
por que tentar de novo?

<!-- S29 -->
Porque uma coisa é realmente diferente.

<!-- S30 -->
Os geradores antigos não conseguiam preencher uma lacuna
sozinhos.
Se o modelo não dizia o que acontece
com um pedido já enviado,
alguém tinha que acrescentar essa regra explicitamente.
Enquanto ninguém fazia isso, a lacuna continuava lá,
e dava para encontrá-la.

<!-- S31 -->
Uma IA não para.
Dê a ela o requisito de seis palavras
e ela vai responder a todas as perguntas
que fizemos no começo.

<!-- S32 -->
Ela vai decidir que um pedido enviado
pode ser cancelado. Ou que não pode.
Vai decidir sobre a fatura
e sobre o fornecedor.
Vai produzir código que roda,
parece razoável
e passa nos testes que ela mesma escreveu.

<!-- S33 -->
É exatamente isso que a torna útil.
E exatamente isso que a torna perigosa.
Porque um palpite plausível
não é uma decisão de negócio.

<!-- S34 -->
Antes, as lacunas eram erros.

<!-- S35 -->
Agora são decisões
que ninguém percebeu que estavam sendo tomadas.

<!-- S36 -->
Então, se a especificação realmente
vai ser o código-fonte,
não pode ser só uns parágrafos informais.

<!-- S37 -->
Imagine o repositório.
Um documento descreve os pedidos
e todos os estados em que eles podem estar.
Outro diz quem pode aprová-los
e quem pode cancelá-los.

<!-- S38 -->
Um terceiro diz quando uma fatura é emitida
e quando ela precisa ser estornada.
Outro descreve o sistema de contabilidade,
inclusive o que acontece quando ele cai.

<!-- S39 -->
Parte disso é texto comum.
Mas onde o texto seria ambíguo,
há algo mais rigoroso:
uma lista de estados e das transições entre eles,
um esquema, uma regra que uma máquina pode verificar.

<!-- S40 -->
E, ao lado, testes de aceitação
que dizem exatamente o que deve acontecer.

<!-- S41 -->
Tudo isso fica no Git.
As mudanças são revisadas.
Cada requisito pode ser rastreado
até o teste que o verifica.

<!-- S42 -->
Então, como é uma mudança?
Digamos que o cliente decida
que um pedido enviado ainda pode ser cancelado,
desde que não tenha sido entregue.
E que, nesse caso, a fatura precisa ser estornada.

<!-- S43 -->
Ninguém abre o backend.
Um desenvolvedor muda uma regra
no documento sobre pedidos.

<!-- S44 -->
Aí o sistema vai atrás
de tudo o que essa regra afeta.
Os estados do pedido.
As regras da fatura.
Os testes de cancelamento.
A reserva com o fornecedor.

<!-- S45 -->
E aí ele deveria parar e perguntar.
A especificação nunca disse
o que acontece com a reserva com o fornecedor
quando a mercadoria já está a caminho.
Isso é uma decisão,
então cabe a uma pessoa.

<!-- S46 -->
Só então a nova implementação
é gerada.
E ela é verificada nos dois sentidos.
Os testes da nova regra devem passar.
E todos os outros testes devem continuar passando,
sem alteração.

<!-- S47 -->
Porque uma mudança no cancelamento
não pode mudar mais nada às escondidas.
Mas testes passando só mostram
aquilo que os testes verificam.

<!-- S48 -->
E como as regras
não estão presas à tecnologia,
a mesma especificação poderia gerar
hoje uma aplicação em PHP
e amanhã algo completamente diferente.

<!-- S49 -->
Exatamente o que
a Model Driven Architecture prometia
vinte e cinco anos atrás.
A diferença é que, desta vez,
o gerador pode ser bom o bastante.

<!-- S50 -->
Sobra a pergunta mais difícil.
Como você sabe que a IA
seguiu mesmo a especificação?

<!-- S51 -->
Um código que funciona em situações comuns
ainda pode falhar em casos incomuns.
E esses são justamente
os casos que ninguém pensa em testar.

<!-- S52 -->
A Amazon esbarrou nisso
nos próprios sistemas de nuvem.
Em 2014, seus engenheiros descreveram
como tinham começado a escrever
descrições precisas e matemáticas
dos seus designs,
numa linguagem chamada TLA+.

<!-- S53 -->
Não do código. Do próprio design.
Uma ferramenta então pegava um modelo do sistema,
limitado a um tamanho fixo,
e testava todas as ordens possíveis
de falhas e recuperações.

<!-- S54 -->
No DynamoDB, o serviço de banco de dados da Amazon,
ela encontrou um bug que podia causar perda de dados.

<!-- S55 -->
O caminho mais curto para dispará-lo
tinha 35 passos,
exatamente na ordem certa.
Ele tinha passado por revisões de design,
revisões de código e testes.

<!-- S56 -->
Então, a versão honesta da ideia
não é que a IA escreve o código
e a gente confia nela.
É que a IA escreve o código,
e algo independente o verifica.

<!-- S57 -->
Agora olhe o que construímos.

<!-- S58 -->
Estados precisos.
Regras formais.
Testes verificáveis.
Versionado, revisado, guardado num repositório.

<!-- S59 -->
Isso não parece
o fim da programação.
Parece programação
numa nova linguagem.

<!-- S60 -->
E foi isso que aconteceu todas as vezes.
O FORTRAN era codificação automática,
até virar o código.
Cada vez que a máquina assumiu
o “como”, as pessoas subiram para o “o quê”.

<!-- S61 -->
E o “o quê” sempre foi a parte difícil.
Não digitar, mas decidir.
O que acontece com um pedido enviado.
Quem pode mexer em quais dados.
O que o sistema nunca pode fazer.

<!-- S62 -->
Talvez o programador do futuro
não escreva milhares de linhas de código.

<!-- S63 -->
Mas alguém ainda vai ter que entender
um problema bem o bastante para dizer
exatamente o que um computador deve fazer,
e verificar que ele fez.

<!-- S64 -->
E se a especificação
virar o código-fonte,
a habilidade mais importante
talvez não seja mais saber
como escrever um programa.

<!-- S65 -->
Talvez seja saber
como descrever um.

<!-- S66 -->
Então, aqui vai a pergunta,
e eu quero muito ler a sua resposta.
Se você escrever uma especificação
precisa o bastante
para uma máquina construir o programa a partir dela...
você ainda está programando?
