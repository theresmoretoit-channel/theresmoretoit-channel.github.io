<!-- S01 -->
Aqui estão todos os roteiros
já escritos para este canal.
158 vídeos,
quase um milhão e meio de bytes de texto.

<!-- S02 -->
Passe todos eles por um compressor comum
chamado gzip.
Saem com pouco mais de meio megabyte.
Quase dois terços a menos.

<!-- S03 -->
E nada se perde.
Descompacte o arquivo
e cada roteiro volta,
letra por letra.

<!-- S04 -->
Agora comprima de novo.

<!-- S05 -->
Fica maior.
98 bytes maior.

<!-- S06 -->
Uma terceira vez.
98 bytes maior.
Uma quarta.
98 de novo.

<!-- S07 -->
A primeira rodada joga fora dois terços.
A segunda não encontra absolutamente nada.
Então por que não dá para continuar comprimindo?

<!-- S08 -->
Vamos olhar dentro desse segundo arquivo.
O gzip não comprimiu nada.
Ele copiou os dados, sem alteração,
em dezesseis blocos.

<!-- S09 -->
Cada bloco ganhou um rótulo de cinco bytes.
Some um pequeno cabeçalho e um rodapé
e dá exatamente 98.

<!-- S10 -->
Quando um compressor não acha nada para tirar,
ele guarda os dados do jeito que estão
e acrescenta só o necessário para desfazer o processo.

<!-- S11 -->
Então por que a segunda rodada não achou nada?
E um programa mais esperto acharia?

<!-- S12 -->
Um texto assim é cheio de repetição.
As mesmas palavras, as mesmas frases,
as mesmas marquinhas de cena
no topo de cada cena.

<!-- S13 -->
Em 1977, Jacob Ziv e Abraham Lempel
publicaram um truque simples.
Não escreva de novo o que se repete.
Aponte para onde já apareceu.

<!-- S14 -->
Volte 300 caracteres
e copie os doze seguintes.
Alguns bytes em vez de doze.

<!-- S15 -->
O segundo truque:
dar códigos curtos às letras comuns
e códigos longos às raras.

<!-- S16 -->
Em 1951, David Huffman,
aluno de pós-graduação no MIT,
podia fazer a prova final
ou escrever um trabalho no lugar dela.

<!-- S17 -->
O trabalho, proposto por Robert Fano,
era encontrar o código mais eficiente
exatamente desse tipo.

<!-- S18 -->
Por meses, Huffman não chegou a lugar nenhum.
Desistiu
e começou a estudar para a prova.
Aí a ideia veio.

<!-- S19 -->
Pegue os dois símbolos mais raros,
junte-os em um só
e repita até sobrar uma única árvore.

<!-- S20 -->
Mais tarde, ele chamou aquilo de
“o momento mais singular da minha vida”.

<!-- S21 -->
Fano não tinha contado à turma
que ele próprio tinha empacado nisso,
e Claude Shannon também.

<!-- S22 -->
O código de Huffman superou os métodos dos dois.
E dá para provar
que nenhum código desse tipo faz melhor.

<!-- S23 -->
No começo dos anos 1990,
Phil Katz juntou os dois truques
nos arquivos ZIP.
O gzip usa o mesmo método.

<!-- S24 -->
A primeira rodada já esgotou
os padrões que o gzip sabe encontrar.

<!-- S25 -->
No que sobra, ele não acha nada para aproveitar.
Para o gzip, parece ruído.

<!-- S26 -->
Mas um programa mais esperto
poderia ver padrões que o gzip deixou passar.
Será que algum programa, um dia,
conseguiria encolher qualquer coisa que você der a ele?

<!-- S27 -->
Não.
E você não precisa saber como ele funciona
para ter certeza disso.

<!-- S28 -->
Pegue todos os arquivos
com exatamente três bits.
São oito.

<!-- S29 -->
Agora conte todos os mais curtos.
Quatro arquivos de dois bits,
dois de um bit
e um arquivo vazio.

<!-- S30 -->
Sete.

<!-- S30b -->
Oito arquivos e sete lugares mais curtos
para colocá-los.

<!-- S31 -->
Se todos ficassem menores,
dois teriam que dividir um lugar.
E, ao descompactar,
qual deles você queria?

<!-- S32 -->
Isso se chama princípio da casa dos pombos,
e vale para qualquer tamanho.
Sempre há um arquivo mais curto a menos
do que seria preciso.

<!-- S33 -->
Então qualquer compressor que aceite qualquer arquivo
e encolha alguns
tem que aumentar outros.
Não porque foi mal escrito.
Eles simplesmente não têm para onde ir.

<!-- S34 -->
Aqueles 98 bytes
são o preço que o gzip paga por isso.

<!-- S35 -->
Escolha o compressor que quiser.
De todos os arquivos de um dado tamanho,
ele consegue encolher em um único byte menos de um
a cada 250.

<!-- S36 -->
Mesmo assim, a compressão funciona,
porque os arquivos que criamos não são aleatórios.
São textos, imagens e programas,
cheios de padrões.

<!-- S37 -->
Isso não impediu que gente
prometesse mais.

<!-- S38 -->
Em 1992, a WEB Technologies
anunciou um software capaz de espremer
quase qualquer dado para menos de um kilobyte.
Até a própria saída,
de novo e de novo.

<!-- S39 -->
O vice-presidente da empresa disse que o método
“não estava sujeito às leis
da teoria da informação”.
O produto nunca chegou ao mercado.

<!-- S40 -->
Então como fotos e músicas
ficam tão pequenas?
Elas simplesmente não seguem essa regra.

<!-- S41 -->
Um JPEG não volta idêntico.
Volta parecido o suficiente.
Detalhes de que seu olho não vai sentir falta
são jogados fora para sempre.

<!-- S42 -->
Dê zoom
e você vê para onde eles foram.

<!-- S43 -->
Isso é compressão com perdas,
e é outro jogo.
Este vídeo é sobre o outro tipo.
Cada bit de volta, exatamente.

<!-- S44 -->
Então, para arquivos que têm padrões,
até que ponto dá para encolher?
Existe um limite mínimo?

<!-- S45 -->
Existe.
Foi encontrado em 1948,
no mesmo artigo por trás do nosso vídeo
sobre códigos corretores de erros.

<!-- S46 -->
Lá, Claude Shannon mostrou
como adicionar redundância protege uma mensagem.
Aqui, ele calculou
quanto dela dá para tirar.

<!-- S47 -->
A resposta dele foi um número
que ele chamou de entropia:
o quanto é difícil adivinhar
o que vem a seguir.

<!-- S48 -->
Nenhum código sem perdas consegue ficar abaixo desse número
na média.
Mas dá para chegar tão perto dele
quanto você quiser.

<!-- S49 -->
Então, quão imprevisível é o inglês?
Em 1951, Shannon mediu isso
com um jogo.

<!-- S50 -->
Ele dava a alguém um trecho
que a pessoa nunca tinha visto
e pedia que ela o adivinhasse,
letra por letra.

<!-- S51 -->
Se o palpite estava errado,
ela tentava de novo,
até acertar.

<!-- S52 -->
As pessoas se mostraram muito boas nisso.
Com cem letras de contexto,
o inglês ficou em cerca de um bit
por letra.

<!-- S53 -->
Um computador guarda cada letra
em oito bits.
Um leitor humano precisa de mais ou menos um.

<!-- S54 -->
É nessa diferença que a compressão trabalha.
O gzip levou os roteiros do canal
para menos de três bits por caractere.

<!-- S55 -->
Então, quão perto de um bit
uma máquina consegue chegar?

<!-- S56 -->
Existe um prêmio exatamente para isso.
Chama-se Hutter Prize,
e desde 2020 a tarefa é comprimir um único arquivo:
um gigabyte da Wikipédia em inglês.

<!-- S57 -->
O gzip reduz o arquivo a um terço.
Os melhores compressores do dia a dia,
a cerca de um quinto.

<!-- S58 -->
O recorde, de julho de 2026,
é de pouco mais de 100 milhões de bytes.
Um décimo.

<!-- S59 -->
E o descompressor também conta.
O tamanho dele entra no total,
então não dá para esconder a Wikipédia
dentro do programa.

<!-- S60 -->
O fundo é de 500.000 euros.
Cada 1% de melhoria
rende 5.000.

<!-- S61 -->
Marcus Hutter, que financia o prêmio, explica por quê:
“saber comprimir bem
está intimamente ligado
a agir de forma inteligente”.

<!-- S62 -->
Porque os programas do topo
não caçam repetições.
Eles preveem.

<!-- S63 -->
Antes de cada caractere,
eles estimam a probabilidade
de cada próximo caractere possível.
Um bom palpite custa uma fração de bit.

<!-- S64 -->
É o jogo de adivinhação de Shannon,
jogado por uma máquina.
Os melhores jogadores hoje usam redes neurais,
treinadas para prever o que vem a seguir.

<!-- S65 -->
Funciona até com arquivos já comprimidos.
Em 2016, o Dropbox começou a reempacotar
os JPEGs dos usuários com um preditor melhor.
Em média, mais de um quinto menores.

<!-- S66 -->
Cada arquivo voltava bit por bit,
e até 2017
isso tinha economizado mais de 46 petabytes.
Ou seja, mais de 46.000 terabytes.

<!-- S67 -->
E aí vêm os gigantes.
Em 2023, pesquisadores da DeepMind
usaram um grande modelo de linguagem
como compressor.

<!-- S68 -->
Em pequenos recortes de fotos em tons de cinza,
ele superou o PNG:
48% do tamanho original
contra 58.

<!-- S69 -->
Em gravações de leitura em voz alta,
superou o FLAC:
21% contra 30.

<!-- S70 -->
Mas isso sem contar o modelo.
Some o tamanho dele
e o resultado fica
140 vezes
maior que os dados.

<!-- S71 -->
Um compressor maior que os próprios dados
não economizou nada.
O programa faz parte da descrição.

<!-- S72 -->
E isso nos leva à parte mais estranha.
Aqui está o primeiro milhão de dígitos de pi.

<!-- S73 -->
Dê esses dígitos a quatro compressores.
O melhor chega a cerca de
426.000 bytes.

<!-- S74 -->
Agora dê aos mesmos compressores
um milhão de dígitos aleatórios.
O mesmo resultado,
com menos de 0,1% de diferença.

<!-- S75 -->
Mas pi não é gerado ao acaso.
Ele segue uma regra matemática.
Aqui está um programa que imprime
esse milhão de dígitos, um por um.

<!-- S76 -->
362 bytes.
Mais de 2.000 vezes menor que o arquivo.

<!-- S77 -->
Os compressores não conseguiam ver
a regra matemática por trás de pi.
Só viam os dígitos.

<!-- S78 -->
Uma forma de medir a informação
contida em dados é perguntar:
quão curto pode ser um programa
que ainda os imprima?

<!-- S79 -->
Esse tamanho se chama
complexidade de Kolmogorov,
em homenagem a um dos homens que a descreveram.

<!-- S80 -->
A maioria dos dados não tem um programa curto.
É o princípio da casa dos pombos de novo:
não existem programas curtos suficientes
para todos.

<!-- S81 -->
Um milhão de dígitos aleatórios
muito provavelmente não tem nada mais curto.
Pi tem.

<!-- S82 -->
Então por que não achar simplesmente
o programa mais curto para qualquer arquivo?
Porque está provado
que nenhum algoritmo consegue fazer isso
para todo arquivo.

<!-- S83 -->
Todo programa dá a você um limite superior.
Mas nada consegue dizer sempre
se existe um mais curto.
Você nunca sabe se chegou ao limite mínimo.

<!-- S84 -->
O gzip achou as repetições nos roteiros,
e nada mais.
Ele vê bytes,
não o que as palavras significam.

<!-- S85 -->
Para ir além, um programa
precisa prevê-las melhor.
E prever bem um texto
começa a parecer muito com entendê-lo.

<!-- S86 -->
Então, aqui vai uma pergunta para você.
Se um programa conseguisse espremer a Wikipédia
mais do que qualquer outro programa,
você diria que ele a entende?
Deixe sua resposta nos comentários.
