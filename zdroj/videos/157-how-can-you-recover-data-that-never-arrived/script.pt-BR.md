<!-- S01 -->
Este é um QR code.
Ele guarda uma linha curta de texto.

<!-- S02 -->
O celular lê na hora.

<!-- S03 -->
Agora vamos arrancar um pedaço dele.

<!-- S04 -->
E escanear de novo.
O mesmo texto.
Letra por letra.

<!-- S05 -->
Uma parte desse código sumiu.
Não é que ficou difícil de ler.
Sumiu.

<!-- S06 -->
Então, como um celular consegue ler algo
que não está mais lá?

<!-- S07 -->
Aqui está o mesmo problema, em miniatura.
Alguém envia oito bits para você.
No caminho, três deles se perdem.

<!-- S08 -->
Cada bit que falta é zero ou um,
então há oito jeitos de preencher as lacunas.
E nada do que chegou
diz qual é o certo.

<!-- S09 -->
E mesmo assim, o celular acabou de fazer exatamente isso.
Ele não estava chutando.
A resposta foi enviada
antes de qualquer coisa se perder.

<!-- S10 -->
O truque é enviar mais
do que a própria mensagem.

<!-- S11 -->
O jeito mais simples
é dizer tudo três vezes.
Um zero é enviado como três zeros,
e o bit um, como três uns.

<!-- S12 -->
O ruído inverte um deles,
e você recebe um, zero, um.
Dois votos contra um.
Quase com certeza era um.

<!-- S13 -->
Se o ruído inverte um bit em cada dez,
aleatoriamente e de forma independente,
uma votação de três erra
menos de três vezes em cada cem.

<!-- S14 -->
Mas você triplicou
tudo o que envia.
Para chegar mais perto da perfeição,
você repetiria cinco vezes, depois nove,
depois cem...
e a mensagem andaria a passo de tartaruga.

<!-- S15 -->
Por muito tempo,
esse parecia ser o preço.
Menos erros, mensagens mais lentas.
Guarde isso.

<!-- S16 -->
No fim dos anos 1940,
Richard Hamming, no Bell Labs,
tinha um problema só dele.

<!-- S17 -->
Ele quase sempre conseguia tempo num computador de relés
nos fins de semana,
quando não havia ninguém para vigiá-lo.

<!-- S18 -->
A máquina conseguia perceber
quando tinha cometido um erro.
Ela tentava a etapa de novo,
três vezes...
e depois abandonava o cálculo dele.
Dois fins de semana seguidos,
ele perdeu todo o trabalho.

<!-- S20 -->
A pergunta, nas palavras dele:
"Se a máquina consegue detectar
que há um erro,
por que não consegue localizar onde ele está?"
As palavras que ele realmente usou, admitiu,
provavelmente foram um pouco mais fortes.

<!-- S22 -->
A resposta dele pega quatro bits de mensagem
e acrescenta três bits de verificação.
Sete bits no total.

<!-- S23 -->
Cada bit de verificação cuida
de um grupo diferente de posições
e garante que esse grupo
tenha um número par de uns.

<!-- S24 -->
Os grupos se sobrepõem num padrão bem pensado.
Cada posição pertence
à sua própria combinação de grupos.

<!-- S25 -->
Agora inverta um bit.
Digamos, o da posição seis.

<!-- S26 -->
O receptor refaz as três verificações.
A primeira passa.
A segunda falha.
A terceira falha.

<!-- S27 -->
Escreva uma verificação que falhou como um,
uma que passou como zero,
e leia da última para a primeira.
Um, um, zero.
Em binário, isso dá seis.

<!-- S28 -->
As verificações não dizem só
que algo deu errado.
Elas apontam o bit exato.

<!-- S29 -->
Inverta de volta,
e a mensagem fica inteira de novo.
Ninguém precisou enviar nada duas vezes.

<!-- S30 -->
Então essa é a resposta.
O receptor não reconstrói
informação perdida do nada.
O remetente já tinha colocado essa informação ali,
com antecedência.

<!-- S32 -->
Nem toda verificação consegue fazer isso.
Uma soma de verificação, como a do nosso vídeo
sobre Btrfs,
pode dizer que um bloco está danificado,
mas não quais eram os dados originais.

<!-- S33 -->
E existe um segundo tipo de dano.
Às vezes um bit não está errado.
Ele simplesmente está faltando,
e você sabe exatamente onde está a lacuna.

<!-- S34 -->
Isso se chama apagamento,
e apagamentos são mais fáceis.

<!-- S35 -->
Envie quatro números,
4, 7, 2 e 9,
e um quinto:
a soma deles, 22.

<!-- S36 -->
Se qualquer um deles sumir,
os outros dizem qual era.
4, 7, alguma coisa, 9,
22.
Só pode ser 2.

<!-- S37 -->
Servidores protegem seus discos
com um tipo parecido de verificação,
espalhado pelos drives.
Quando um drive morre,
o conteúdo dele é calculado a partir dos outros.

<!-- S38 -->
Então, quanto a mais você precisa?
A repetição diz:
para levar os erros a zero,
você tem que levar a velocidade a zero.

<!-- S39 -->
Dois anos antes de o artigo de Hamming
sair,
seu colega Claude Shannon
tinha publicado uma resposta mais estranha.

<!-- S40 -->
Todo canal,
um link de rádio, um cabo, um disco,
tem um limite.
Uma velocidade máxima para a informação.

<!-- S41 -->
Abaixo desse limite,
os erros podem ficar tão raros quanto você quiser,
sem reduzir a velocidade.
Não repetindo mais.
Codificando de forma mais inteligente.

<!-- S42 -->
Acima dele,
nenhum código do mundo resolve.

<!-- S43 -->
Mas havia um porém.
Shannon provou que esses códigos existem.
Ele não mostrou como construir um
que alguém conseguisse usar.

<!-- S44 -->
A prova dele dizia que um código escolhido ao acaso
quase com certeza seria bom.
Mas o jeito óbvio de decodificá-lo
é comparar o que chegou
com cada mensagem possível...
e, para um bloco de 1.000 bits,
existem mais mensagens possíveis
do que átomos no universo.

<!-- S46 -->
Então o artigo de Shannon não era uma solução.
Era uma promessa.
E os engenheiros passaram os
45 anos seguintes tentando cumpri-la.

<!-- S47 -->
O código de Hamming foi um primeiro passo.
Ele corrige um bit errado em cada sete.

<!-- S48 -->
Mas danos reais vêm em rajadas.
Um arranhão ou um chiado de estática
destrói centenas de bits seguidos.

<!-- S49 -->
Em 1960, Irving Reed e Gustave Solomon,
no Lincoln Laboratory do MIT,
publicaram um artigo de cinco páginas.

<!-- S50 -->
Os códigos deles trabalham com bytes inteiros,
não com bits isolados.
Se uma rajada estraga todos os oito bits
de um byte,
continua sendo só um byte com erro.

<!-- S51 -->
Uma versão comum acrescenta
32 bytes de verificação
a 223
bytes de dados.

<!-- S52 -->
Ela consegue corrigir quaisquer 16 bytes
que cheguem errados...
ou reconstruir 32
que nunca cheguem.

<!-- S53 -->
É assim que um CD toca mesmo com um arranhão.
Seus dois códigos de Reed-Solomon
conseguem reparar por completo uma falha
de uns 4.000 bits,
2,5 milímetros de trilha.

<!-- S54 -->
E é por isso que o QR code rasgado
ainda funcionou.
No nível mais forte,
um QR code consegue reconstruir
até cerca de 30% dos seus bytes
e ainda devolver cada letra.

<!-- S56 -->
A Voyager 2 deixou a Terra em 1977
já levando um codificador Reed-Solomon.

<!-- S57 -->
Mas em Júpiter e Saturno,
ela protegia tudo, menos as imagens,
com um código mais antigo, de Marcel Golay,
que enviava um bit extra
para cada bit de dados.

<!-- S58 -->
Para Urano e Netuno,
com o sinal ficando mais fraco,
os engenheiros ligaram o Reed-Solomon,
por cima de um segundo código
pelo qual cada bit já passava.

<!-- S59 -->
Só com esse segundo código,
uns cinco bits em cada mil
ainda chegavam errados.
Com o Reed-Solomon por cima,
cerca de um em um milhão.

<!-- S60 -->
O ruído também vem em rajadas,
então a Voyager embaralhava
os bytes de quatro blocos juntos
antes de enviá-los.

<!-- S61 -->
Uma rajada que teria destruído um bloco
agora tira alguns bytes de cada um...
poucos o bastante para que cada bloco
se conserte sozinho.

<!-- S62 -->
O resto da viagem das imagens de Netuno
até em casa
está no nosso vídeo sobre a Voyager.

<!-- S63 -->
Mas nem isso
chegava ao limite de Shannon...
e um código que podia chegar bem mais perto
já existia.

<!-- S65 -->
Em 1960, na tese de doutorado no MIT,
Robert Gallager descreveu códigos
feitos de muitas verificações simples,
cada uma olhando só para alguns bits.

<!-- S66 -->
Decodificá-los exigia que as verificações
trocassem palpites entre si,
rodada após rodada...
demais
para os computadores dos anos 1960.
Então a ideia foi engavetada
e ficou praticamente esquecida por 30 anos.

<!-- S68 -->
Em 1993,
uma equipe liderada por dois engenheiros franceses,
Claude Berrou e Alain Glavieux,
apresentou os turbo códigos
numa conferência em Genebra.

<!-- S69 -->
Os resultados eram tão próximos
do limite de Shannon
que muitos especialistas acharam
que eles tinham cometido um erro.
Provavelmente um fator de dois,
em algum ponto dos cálculos.

<!-- S70 -->
Em menos de um ano,
outros laboratórios tinham confirmado.

<!-- S71 -->
Os turbo códigos também funcionavam
trocando palpites de um lado para o outro,
e isso fez os pesquisadores retomarem Gallager.

<!-- S72 -->
Em 1995 e 1996,
David MacKay e Radford Neal
redescobriram os códigos dele
e mostraram que eles chegavam
igualmente perto.

<!-- S73 -->
Em 2001,
uma versão aprimorada dos códigos de Gallager
chegou a 0,04 decibel
do limite de Shannon.

<!-- S74 -->
Isso é menos de um por cento
a mais de potência de sinal
do que o mínimo teórico.
A promessa de 1948 tinha sido cumprida.

<!-- S75 -->
Hoje, os códigos de Gallager transportam
boa parte dos dados nos celulares 5G,
no Wi-Fi moderno
e na TV por satélite.

<!-- S77 -->
Agora, de volta aos nossos oito bits.
Três se perderam,
e há oito jeitos
de preencher as lacunas.

<!-- S78 -->
Mas esses oito bits
nunca foram só uma mensagem.
Eles levavam quatro bits de dados,
as três verificações de Hamming
e mais uma verificação sobre todos os oito.

<!-- S79 -->
De todos os 256
padrões possíveis de oito bits,
só 16 seguem essas regras.

<!-- S80 -->
Teste os oito candidatos.
Um por um, eles falham.
Só sobra um.

<!-- S81 -->
Os bits que faltavam nunca sumiram de verdade.
A informação deles ainda estava lá,
nos bits que sobreviveram.

<!-- S82 -->
Então, aqui vai uma pergunta para você.
Você já percebeu a correção de erros
funcionando em algo que usa todo dia?
Me conta nos comentários.
