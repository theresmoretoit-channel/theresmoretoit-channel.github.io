# Internet Explorer 6 — Os bugs que tinham nome

<!-- S01 -->
Esta é a parte dois.

Se você não viu a parte um,
o link está aí embaixo.

O resumo você recebe de qualquer jeito.

<!-- S02 -->
Em 2001
a Microsoft lançou
o Internet Explorer 6,
e ele veio junto com o Windows XP.

Em poucos anos
tinha mais de noventa por cento
do mercado de navegadores.

<!-- S03 -->
A Microsoft usou isso
para transformar o navegador
numa plataforma de aplicativos.

Era uma ideia de verdade.

Só que quem pagou por ela
foram os desenvolvedores web.

<!-- S04 -->
Essa foi a parte um.

Mas eu deixei uma coisa de fora.

Deixei de fora a parte
em que os bugs tinham nome.

<!-- S05 -->
Um bug de navegador normalmente
é um número num sistema de chamados.

Issue 4172.

Ninguém lembra dele.

Ninguém fala dele no almoço.

<!-- S06 -->
No Internet Explorer 6
os bugs tinham nomes próprios.

E acontece que isso é
a coisa mais reveladora
de toda aquela época.

<!-- S07 -->
Vamos começar com um leve.

Você flutua uma imagem à esquerda
e põe um parágrafo do lado.

O texto deveria ficar
colado na imagem.

Em vez disso ele fica
a três pixels.

<!-- S08 -->
Não quatro.

<!-- S08b -->
Não dois.

<!-- S08c -->
Três.

<!-- S08d -->
Toda vez.

Isso tinha nome.

The Three Pixel Jog.

<!-- S09 -->
Agora flutue essa imagem à esquerda
e dê a ela uma margem esquerda
de dez pixels.

O Internet Explorer 6
dá vinte.

Ele dobra a margem,
mas só do lado
para o qual você flutuou.

<!-- S10 -->
The Double Margin Bug.

E a correção aceita
era declarar
um elemento flutuante como inline.

<!-- S11 -->
O que não faz sentido.

Um flutuante é um bloco.

Chamar ele de inline
não significa absolutamente nada.

Funcionava, então as pessoas escreviam.

<!-- S12 -->
O próximo é melhor.

Você carrega uma página,
e parte do conteúdo
simplesmente não está lá.

Você rola para baixo.

Você rola de volta para cima.

E ele aparece.

<!-- S13 -->
Nada carregou.

Nada mudou.

Ele só era tímido.

E tinha o nome certo.

The Peekaboo Bug.

<!-- S14 -->
O remédio era dizer
ao elemento que sumia
que a posição dele era relativa.

Ninguém conseguiu explicar direito
por que isso trazia ele de volta.

<!-- S15 -->
Depois tem aquele
em que você passa o mouse num link,
e o fundo
da caixa embaixo
é cortado numa linha reta.

The Guillotine Bug.

<!-- S16 -->
Tinha um bug em que o texto
fugia de onde você tinha posto.

Magic Creeping Text.

Tinha um em que as bordas
saíam no lugar errado,
na cor errada,
ou não saíam.

Border Chaos.

<!-- S17 -->
O meu favorito é mais discreto.

Você põe uma fileira de caixas,
e letras da última
aparecem de novo embaixo dela.

Nem sempre.

Nada previsível.

The Duplicate Character Bug.

<!-- S18 -->
E o que decidia
se acontecia com você,
e quantas letras
saíam duplicadas,
era o número de comentários HTML
que você tinha deixado no código.

Comentários.

A única coisa no arquivo
que o navegador
deveria jogar fora.

<!-- S19 -->
Tem mais um,
e ele é diferente,
porque esse as pessoas usavam
de propósito.

Se você define uma altura
e o conteúdo é mais alto,
a caixa deveria transbordar.

O Internet Explorer 6
aumentava a caixa.

<!-- S20 -->
O que está errado.

E é também exatamente
o que uma altura mínima faz.

E o Internet Explorer 6
não tinha altura mínima.

Então os desenvolvedores pararam
de reportar esse bug
e passaram a depender dele.

<!-- S21 -->
Pare e olhe essa lista.

The Three Pixel Jog.

The Double Margin Bug.

Peekaboo.

The Guillotine.

Você não dá nome a um bug
que encontra uma vez.

<!-- S22 -->
Esses tinham nome
porque todo mundo encontrava.

E aqui vem a parte
que piora tudo.

A maioria deles tinha
a mesma causa por baixo.

<!-- S23 -->
Dentro do Internet Explorer 6,
todo elemento ou tinha
ou não tinha
uma coisa chamada layout.

<!-- S24 -->
Isso decidia se o elemento
definia o próprio tamanho e posição,
ou deixava isso para o pai.

E você não conseguia ligar.

<!-- S25 -->
Não existia nenhuma propriedade
chamada layout,
nem jeito de pedir por ela.

Não estava em especificação nenhuma.

Era uma flag interna
do motor de renderização.

<!-- S26 -->
Mas dava para virar ela
sem querer.

Definir uma largura fazia isso.

Definir uma altura fazia isso.

Flutuar um elemento fazia isso.

Então metade das correções deste vídeo
era gente virando um interruptor
que não conseguia ver.

<!-- S27 -->
Por isso foram atrás
do jeito mais barato
de virar ele de propósito.

Um era definir uma altura
de um por cento.

<!-- S28 -->
Todos os outros navegadores
tinham que ficar longe disso,
então foi parar dentro de um truque
que a gente vê daqui a pouco.

<!-- S29 -->
E no Internet Explorer 6
não fazia mal nenhum,
porque uma altura em que não cabe
é uma altura que ele ultrapassa mesmo.

O bug de dois minutos atrás
é o que torna a correção segura.

<!-- S30 -->
Isso tinha nome.

The Holly Hack.

<!-- S31 -->
O outro jeito
era uma propriedade da Microsoft
chamada zoom, com valor um.

Zoom um significa
não dê zoom.

<!-- S32 -->
Não mudava nada que você pudesse ver.

E era esse o ponto.

Ficava nas folhas de estilo
puramente para levantar
uma flag invisível
que fazia os bugs sumirem.

<!-- S33 -->
O que nos leva aos truques,
e é nos truques
que a coisa fica estranha.

Para consertar um navegador
você primeiro precisa falar
só com ele.

<!-- S34 -->
E o Internet Explorer 6
se comportava como se houvesse
mais um elemento
acima do elemento html.

Nenhum outro navegador fazia isso.

Não estava documentado.

Era simplesmente como ele agia.

<!-- S35 -->
Então você escrevia uma regra
que casava com o fantasma,
e só aquele navegador
conseguia ver.

Asterisco, espaço, html.

<!-- S36 -->
Todos os outros navegadores olhavam,
não achavam nada que casasse,
e seguiam em frente.

Isso é o star hack,
e por anos ele ficou
em quase toda folha de estilo
da web.

<!-- S37 -->
Tinha também
o underscore hack.

Você põe um sublinhado
na frente do nome de uma propriedade.

<!-- S38 -->
Um navegador que segue os padrões
joga a linha fora
por ser inválida.

O Internet Explorer 6
ignora o sublinhado
e aplica.

<!-- S39 -->
Então você quebrava de propósito
a sua própria folha de estilo,
e a quebra
era a instrução.

<!-- S40 -->
E aí tem aquele
que a Microsoft construiu de propósito.

Dava para escrever um comentário
que só o Internet Explorer obedecia.

<!-- S41 -->
Para todos os outros navegadores
era um comentário comum,
ignorado como se ignora comentário.

Para o Internet Explorer 6
era uma porta
para uma segunda versão
da página.

<!-- S42 -->
O que significa que o fabricante
olhou a situação,
concordou que esse navegador
precisava de uma folha de estilo própria,
e entregou um recurso
para facilitar isso.

<!-- S43 -->
Parte do estrago
não precisava de bug nenhum.

O Internet Explorer 6
tinha dois modos.

No moderno
ele seguia o padrão.

<!-- S44 -->
No antigo,
a largura de uma caixa
incluía o preenchimento
e a borda dela,
o que é um número
completamente diferente.

<!-- S45 -->
Qual modo você pegava
dependia da primeira linha
do documento.

E a versão do HTML
para a qual todo mundo estava indo
mandava você pôr
uma declaração XML lá em cima.

<!-- S46 -->
Aquela linha empurrava
o Internet Explorer 6
para o modo antigo.

O que quebrava
era você seguir o padrão mais novo.

<!-- S47 -->
Depois tem a transparência.

O Internet Explorer 6 não sabia
mostrar um PNG com bordas suaves.

Onde a imagem devia desaparecer,
ele punha cinza.

<!-- S48 -->
A resposta da Microsoft foi um filtro
com nome de número de série.

Funcionava.

<!-- S49 -->
Mas ele pintava fora
do processo normal
de renderização do navegador,
então links que você punha em cima
muitas vezes paravam de funcionar.

Você consertava a imagem
e quebrava o link.

<!-- S50 -->
E fazer qualquer outra coisa desaparecer
era um segundo filtro,
com sintaxe própria,
sentado na folha de estilo
bem do lado da propriedade comum
que todos os outros navegadores entendiam.

<!-- S51 -->
Parte disso é mais antiga
que os próprios bugs.

Antes de tudo isso,
os layouts eram construídos
com tabelas aninhadas.

<!-- S52 -->
E para segurar um vão aberto
você usava uma imagem transparente
de um pixel,
esticada para o tamanho
que o vão precisasse.

Isso também tinha nome.

The spacer gif.

<!-- S53 -->
Passar o mouse era outra.

No Internet Explorer 6
isso funcionava em links.

Só em links.

<!-- S54 -->
Então um menu que abria
quando você passava o mouse
em qualquer outra coisa
precisava de um programinha
pendurado na folha de estilo.

<!-- S55 -->
Não um script na página.

Um arquivo separado,
referenciado do CSS,
com código cuja função
era ensinar ao navegador
um seletor.

Esse arquivo as pessoas passaram
de mão em mão por anos.

<!-- S56 -->
A parte um mencionou
que dava para pôr JavaScript
dentro de uma folha de estilo.

O que ela não mencionou
foi com que frequência esse JavaScript rodava.

<!-- S57 -->
A cada movimento do mouse.

A cada tecla.

A cada rolagem.

De novo e de novo,
para calcular uma largura.

<!-- S58 -->
E o navegador tinha tetos
que ninguém mais tinha.

Uma folha de estilo parava de valer
em algum ponto passadas
quatro mil regras.

Tudo depois
da trigésima primeira folha de estilo
de uma página era ignorado.

<!-- S59 -->
O que parece um número
que você nunca alcança,
até o seu site ficar tão grande
que alguém precisa escrever
um passo de build cuja única função
é juntar folhas de estilo
antes que o navegador as veja.

<!-- S60 -->
E parte disso não era
nada cosmética.

O Internet Explorer 6
contava os objetos da página
e os objetos de script
de duas maneiras diferentes,
e nenhum dos dois lados
via o ciclo inteiro.

<!-- S61 -->
Então se um script apontava
para uma parte da página,
e aquela parte da página
apontava de volta para o script,
nenhum dos dois era liberado.

Deixe essa janela aberta tempo suficiente
e o navegador comia a máquina.

<!-- S62 -->
Mas o melhor de todos
não é bug de layout.

Você escreve uma tag input.

Você dá um tipo a ela.

E esquece o sinal de igual.

<!-- S63 -->
Isso é um atributo malformado.

Todo parser já escrito
tem uma resposta para isso.

Ignore.

Adivinhe o que era.

Siga em frente.

<!-- S64 -->
O Internet Explorer travava.

Por dentro, ele queria saber
se o campo estava oculto,
então comparava o que você tinha digitado
com a palavra hidden.

Você não tinha digitado nada.

<!-- S65 -->
Então ele foi buscar
aquilo que você não digitou
no endereço zero.

O que seria
uma pane comum de navegador,
só que o código que fazia isso
não estava no navegador.

<!-- S66 -->
Estava numa biblioteca compartilhada do sistema.

Então essas três palavras
derrubavam também o cliente de e-mail,
e o painel de visualização
do gerenciador de arquivos.

<!-- S67 -->
Uma janela listando arquivos
na sua própria máquina,
fechada por uma página web.

Essa é a tese da parte um
chegando como relatório de pane.

O navegador não era um programa
rodando sobre o sistema.

Ele era parte do sistema.

<!-- S68 -->
E você não podia simplesmente
testar a correção em outro lugar.

O Internet Explorer era soldado
ao sistema operacional,
então um computador
rodava exatamente uma versão.

<!-- S69 -->
Por isso um trabalho de front-end
em 2006
vinha com uma prateleira
de máquinas reserva.

<!-- S70 -->
E mais tarde com uma pasta
de máquinas virtuais,
cada uma carregando um sistema
operacional inteiro
só para que uma página
pudesse ser aberta dentro dela.

<!-- S71 -->
E aí alguém fez
a coisa óbvia.

Se você consegue ensinar ao navegador
um recurso que falta,
consegue ensinar todos.

<!-- S72 -->
Um desenvolvedor chamado Dean Edwards
escreveu uma biblioteca
cujo único propósito
era fazer o Internet Explorer 6
se comportar como uma versão
posterior dele mesmo.

As pessoas colocaram isso no ar.

Em produção.

<!-- S73 -->
E é aqui que deixa
de ter graça.

Por quase uma década,
uma fatia séria
do trabalho de front-end do mundo
foi para os erros de um navegador.

Não recursos.

Não produtos.

Compensação.

<!-- S74 -->
E durou por causa
daquilo de que falava a parte um.

Empresas tinham construído nele
aplicações de verdade,
do tipo que só rodava ali,
e essas aplicações
ainda precisavam funcionar na segunda.

<!-- S75 -->
Então o navegador do qual todos
queriam se livrar
era aquele que ninguém
tinha permissão de remover.

<!-- S76 -->
Em 2010,
o Google anunciou que os próprios
aplicativos dele parariam de funcionar nele.

E um estúdio de design em Denver
achou que isso merecia um funeral.

<!-- S77 -->
De verdade.

Um caixão.

Um elogio fúnebre.

Entre oitenta e cem pessoas
foram ver um navegador
ser enterrado.

Tinham planejado trinta.

<!-- S78 -->
E a Microsoft mandou flores.

No cartão estava escrito:
obrigado pelos bons tempos,
Internet Explorer 6.

<!-- S79 -->
Um ano depois, no mesmo dia,
a Microsoft lançou um site.

Ele acompanhava quanto do mundo
ainda rodava
o Internet Explorer 6,
país por país.

<!-- S80 -->
Naquele momento
ainda eram doze por cento.

A meta era empurrar isso
para menos de um.

A empresa que construiu o navegador
mantinha uma contagem regressiva pública
até a morte do próprio produto.

<!-- S81 -->
Então por que os bugs tinham nome?

Porque você dá nome àquilo
que não dá para contornar.

<!-- S82 -->
Ninguém dá nome ao tempo
de um país
por onde só está passando.

Você dá nome onde mora.

E por uns dez anos,
era ali que a web morava.

<!-- S83 -->
Mas tirar o Internet Explorer 6
da web é outra história.

E é para lá que a gente vai depois.

Se você quer essa,
tem um botão de inscrição,
e a parte um está linkada aí embaixo.
