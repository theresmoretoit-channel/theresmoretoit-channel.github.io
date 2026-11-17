<!-- S01 -->
A cada poucos dias, mais um bug sério
aparece nas notícias.
Um bug que deixa alguém pular o login.
Um bug que vaza dados privados.
Um bug que entrega seu computador a um invasor.

<!-- S02 -->
Às vezes é o Windows. Às vezes o Linux.
Um navegador, um banco de dados, um serviço na nuvem...
ou uma pequena biblioteca
da qual milhões de desenvolvedores dependem.

<!-- S03 -->
E a reação é quase sempre a mesma.
Como os programadores deixaram isso passar?

<!-- S04 -->
São profissionais.
Têm revisões de código, testes automatizados,
auditorias de segurança, fuzzing...
e mesmo assim os bugs continuam aparecendo.

<!-- S05 -->
Então é sequer possível
escrever software complexo sem bugs?

<!-- S06 -->
Vamos começar com um número.
Imagine um programa com apenas cem configurações,
cada uma ligada ou desligada.

<!-- S07 -->
Cem decisões simples de sim ou não.
Quantas combinações são essas?

<!-- S08 -->
Dois elevado a cem.
Isso é mais ou menos um milhão de trilhões de trilhões.

<!-- S09 -->
Agora imagine que você pudesse testar
um bilhão de combinações por segundo.
E que começasse no Big Bang.

<!-- S10 -->
Até hoje, você teria testado
cerca de uma combinação em três mil.

<!-- S11 -->
E cem chaves não é nada.
Um programa de verdade tem milhões delas.
Então "é só testar tudo"
não é caro. É impossível.

<!-- S12 -->
E essas chaves não têm nada de exótico.
Pegue uma das coisas mais simples
que um programa faz.
Um usuário pede a própria conta pelo número.
A gente encontra no banco de dados.
E devolve pra ele.

<!-- S13 -->
Mas e se o usuário não existir?
E se alguém mandar texto em vez de um número?
Ou um número negativo? Ou um número enorme?

<!-- S14 -->
E se essa pessoa não puder ver a conta?
E se alguém apagar a conta
no exato momento em que a estamos carregando?
E se a mesma requisição chegar duas vezes?

<!-- S15 -->
Cada uma dessas perguntas é simples.
O problema é como elas se combinam.
Cada uma é mais uma chave.

<!-- S15b -->
Aliás, se você gosta de vídeos
como este, pense em se inscrever.

Isso ajuda muito o canal.

<!-- S16 -->
E um computador não resolve isso pra gente.
Ele faz exatamente o que a gente manda.
Não o que a gente quis dizer.

<!-- S17 -->
Por isso inventamos as linguagens de programação.
Elas nos deixam descrever coisas complexas
sem pensar em cada detalhe.

<!-- S18 -->
Mas algumas delas cuidam de menos
do que você gostaria.
Pegue o C. É rápido, é simples,
e dá a você um enorme controle sobre a memória.

<!-- S19 -->
Então você pode escrever isto.
Reservamos espaço para dezesseis caracteres.
Depois dizemos: copie a entrada aqui.

<!-- S20 -->
E se a entrada tiver
quinhentos caracteres?
O C não pergunta.
Ele simplesmente continua escrevendo além do fim.

<!-- S21 -->
E o que fica logo depois desses dezesseis caracteres?
Muitas vezes, algo muito importante.

<!-- S22 -->
Quando um programa chama uma função,
ele anota para onde voltar
quando a função terminar.
Um endereço de retorno.
Num layout clássico, ele fica
um pouco depois do fim do nosso buffer.

<!-- S23 -->
Então um invasor manda uma entrada
com exatamente o tamanho certo.
Primeiro, as instruções dele.
Depois, bem no fim, um novo endereço de retorno...
apontando de volta para essas instruções.

<!-- S24 -->
A função termina.
O processador procura para onde retornar...
e salta direto para o código do invasor.

<!-- S25 -->
Agora ele está rodando o programa dele,
com todas as permissões do seu.
É isso que "executar código arbitrário" significa.

<!-- S26 -->
E o processador não fez nada de errado.
Ele seguiu as instruções.

<!-- S27 -->
Em 1988, um erro exatamente como este
deixou o worm Morris se espalhar
pela internet dos primórdios.
E o mesmo truque vem sendo usado
em ataques desde então.

<!-- S28 -->
Então linguagens mais novas passam parte do trabalho
para o compilador.
O Rust, por exemplo, se recusa a compilar
muitos programas que poderiam usar a memória de forma errada.

<!-- S29 -->
O programador diz:
mas eu sei exatamente o que estou fazendo!
E o compilador diz:
é o que todo mundo diz.

<!-- S30 -->
E é certo desconfiar.
A Microsoft e o time do Chrome, do Google,
relataram, os dois,
que cerca de setenta por cento
dos bugs de segurança que estudaram
vêm de problemas de segurança de memória.

<!-- S31 -->
Mas um programa pode usar a memória de forma totalmente segura
e ainda assim completamente errado.

<!-- S32 -->
Imagine que um usuário faz login.
A senha dele é verificada corretamente.
Nada trava. Nenhuma memória é corrompida.

<!-- S33 -->
E então o programa mostra a ele
os dados de outra pessoa.
Porque a verificação de permissão
foi escrita um pouco errada.

<!-- S34 -->
Nenhuma linguagem pega isso sozinha.
A linguagem não sabe
o que o programa deveria fazer.
Só nós sabemos.

<!-- S35 -->
Então, de volta aos testes.
Um teste pode dizer a você:
para esta entrada, obtive este resultado.

<!-- S36 -->
Ele não pode dizer a você:
o programa está certo para toda entrada.
E já vimos
por que não dá para tentar todas.

<!-- S37 -->
Em 1970, o cientista da computação
Edsger Dijkstra resumiu numa frase.
Testar pode mostrar a presença de bugs,
mas nunca a ausência deles.

<!-- S38 -->
Tudo bem. Então, em vez de testar,
por que não escrever um programa
que confere outros programas
e prova que estão corretos?
Dê a ele qualquer código, e ele diz
se aquele código faz o que deveria.

<!-- S39 -->
Essa pergunta foi respondida
antes mesmo de o primeiro computador de verdade existir.
Em 1936, Alan Turing provou
que um programa desses não pode existir.

<!-- S40 -->
Não que ninguém tenha construído ainda.
Que ele não pode existir de jeito nenhum.

<!-- S41 -->
Ele mostrou que nenhum programa consegue decidir,
para todo outro programa,
se ele algum dia vai parar de rodar.

<!-- S42 -->
E em 1953, Henry Rice foi ainda mais longe.
O mesmo vale para toda pergunta não trivial
sobre o que um programa de fato faz.

<!-- S43 -->
É seguro? Vaza dados?
Dá a resposta certa?
Não existe método geral
que resolva isso para todo programa.

<!-- S44 -->
Então software sem bugs é impossível?
Não exatamente.
Para um programa específico,
às vezes dá para provar que está correto,
com um esforço enorme.

<!-- S45 -->
Em 2009, uma equipe na Austrália provou
que um pequeno núcleo de sistema operacional,
chamado seL4,
faz exatamente o que sua especificação diz.

<!-- S46 -->
Ele tinha menos de dez mil linhas de código.
Construir o núcleo levou
cerca de dois anos-pessoa.
Provar que estava correto levou cerca de vinte.
Um navegador web moderno
tem dezenas de milhões de linhas.

<!-- S47 -->
E até essa prova tem um porém.
Ela mostra que o programa bate com sua especificação.
Não mostra que a especificação
é o que a gente realmente queria.

<!-- S48 -->
E a especificação é escrita por pessoas.
Então a pergunta volta pra gente.

<!-- S49 -->
E não é só o nosso próprio código.
Um programador hoje se apoia em frameworks,
bibliotecas e centenas de dependências.
Cada camada nos poupa uma quantidade enorme de trabalho.
Mas cada camada é algo
que a gente tem que entender...
ou pelo menos confiar.

<!-- S50 -->
O que significa que você não precisa escrever um bug
para ter um no seu software.
Basta instalá-lo.

<!-- S51 -->
Depois some a pressão.
Ninguém quer um produto perfeito em dez anos.
Querem um que funcione no mês que vem.
E uma invasão que nunca aconteceu
é muito difícil de mostrar numa apresentação.

<!-- S52 -->
E aqui vem a parte mais estranha.
Nossas ferramentas só melhoram.
Linguagens mais seguras, fuzzing, bug bounties...

<!-- S53 -->
E mesmo assim o número de vulnerabilidades conhecidas
não para de crescer.
Só em 2024, cerca de quarenta mil
receberam um número oficial.

<!-- S54 -->
Em parte porque também estamos escrevendo
muito mais software do que nunca.
É como tornar cada estrada mais segura...
enquanto construímos milhões de vezes mais estradas.

<!-- S55 -->
Então os programadores são ruins no que fazem?
Não.
A gente vem pedindo a eles uma coisa
que nenhum método geral consegue garantir.

<!-- S56 -->
Então talvez
"como escrevemos software sem bugs?"
seja a pergunta errada.

<!-- S57 -->
A pergunta melhor é:
como construímos sistemas que continuam seguros
mesmo quando o software tem bugs?

<!-- S58 -->
E é exatamente para lá que a segurança está indo.
Ela não diz: nunca cometa um erro.
Ela diz: assuma que você já cometeu.

<!-- S59 -->
Lembra daquele endereço de retorno?
Hoje, o sistema o protege.
Ele embaralha onde as coisas ficam na memória.
E se recusa a executar instruções
escondidas em dados.

<!-- S60 -->
O bug no nosso código em C ainda está lá.
Só que é muito mais difícil transformá-lo num ataque.

<!-- S61 -->
E a mesma ideia está em toda parte.
Sandboxes, permissões limitadas,
processos isolados, criptografia,
backups, monitoramento...
camada após camada,
para que um bug não vire um desastre.

<!-- S62 -->
E isso tem uma consequência bem prática.
Se os bugs são inevitáveis,
corrigi-los não é opcional.

<!-- S63 -->
O software que você está usando hoje
pode muito bem conter uma vulnerabilidade
que ninguém achou ainda.

<!-- S64 -->
E quando alguém achar,
a atualização é a diferença entre
"uma vulnerabilidade foi descoberta"
e "fomos hackeados".

<!-- S65 -->
O mesmo vale para os sistemas que construímos.
Bibliotecas antigas e plataformas sem suporte
não ficam mais seguras por serem ignoradas.
Elas viram dívida técnica.

<!-- S66 -->
E por que essa dívida precisa ser paga
é o que o meu vídeo
"Ainda funciona. Então por que atualizar?"
aborda.

<!-- S67 -->
Porque, em software,
"ainda funciona"
e "ainda é seguro"
são duas coisas muito diferentes.
