# Internet Explorer 6 — O navegador que virou plataforma

Tradução de `script.md`. Mesmas marcas de cena, mesmo número de linhas.
Uma linha = uma frase = uma legenda.

<!-- S01 -->
Imagine que você é desenvolvedor web
no início dos anos dois mil.

Você escreveu
uma página web perfeitamente razoável.

<!-- S02 -->
Funciona no Netscape.

Funciona no Opera.

Funciona no novo Firefox.

E aí você abre
no Internet Explorer.

Está tudo quebrado.

<!-- S03 -->
O layout está errado.

Os botões saíram do lugar.

As imagens PNG ficaram horríveis.

E de algum jeito,
uma única quebra de linha no seu HTML
criou um espaço de três pixels.

<!-- S04 -->
Bem-vindo ao desenvolvimento web
na era do Internet Explorer 6.

Mas aqui vem a parte interessante.

O Internet Explorer 6
não era simplesmente um navegador ruim.

<!-- S05 -->
A Microsoft estava tentando resolver problemas
que a web realmente tinha.

Só que tinha uma vantagem enorme
sobre todos os outros.

O Windows.

<!-- S06 -->
E no fim das contas essa vantagem
permitiu transformar o navegador
em algo muito maior
do que um navegador.

<!-- S07 -->
Em meados dos anos noventa,
a web era dominada
pelo Netscape Navigator.

A Microsoft não gostava disso.

<!-- S08 -->
Então o Internet Explorer
passou a vir junto com o Windows
e foi disponibilizado de graça.

Você comprava um computador com Windows.

O Internet Explorer já estava lá.

Nada para baixar.

Nada para pagar.

<!-- S09 -->
E, principalmente,
a Microsoft controlava
o sistema operacional.

Pouco depois do ano 2000,
o Internet Explorer tinha
mais de noventa por cento
do mercado de navegadores.

<!-- S10 -->
O Internet Explorer 6 chegou
em 2001,
junto com o Windows XP.

E por um tempo pareceu
que a Microsoft tinha simplesmente vencido
a guerra dos navegadores.

<!-- S11 -->
A Microsoft tinha um problema.

A web era extremamente limitada.

O HTML sabia exibir documentos.

O CSS sabia dar estilo a eles.

O JavaScript sabia torná-los interativos.

<!-- S12 -->
E era mais ou menos isso.

Qualquer coisa mais complicada
esbarrava direto
nos limites do navegador.

<!-- S13 -->
E se você quisesse escanear um documento?

Ou conversar com um cartão inteligente?

Ou falar com algum
hardware do Windows?

<!-- S14 -->
O navegador realmente não
conseguia fazer essas coisas.

Então a Microsoft apresentou uma solução.

ActiveX.

<!-- S15 -->
A ideia básica era simples.

Por que limitar uma aplicação web
ao que o navegador sabe fazer?

Deixe que ela use
componentes nativos do Windows.

<!-- S16 -->
E de repente uma página web
podia fazer coisas
que o HTML comum
nem sonhava em fazer.

<!-- S17 -->
Hoje o ActiveX soa aterrorizante.

E com razão.

Um componente ActiveX podia alcançar
os arquivos, os aplicativos,
o hardware
e o sistema operacional.

<!-- S18 -->
Da perspectiva de segurança de hoje,
isso soa absolutamente insano.

Mas no início dos anos dois mil
fazia todo o sentido
para aplicações corporativas.

<!-- S19 -->
As empresas não queriam
um visualizador de documentos bonito.

Queriam aplicações.

Queriam páginas web
que se comportassem
quase como um programa de desktop.

<!-- S20 -->
E a Microsoft deu exatamente isso.

Até o próprio Windows Update
dependia originalmente do ActiveX
para inspecionar o sistema
e descobrir quais atualizações
eram necessárias.

<!-- S21 -->
Então o ActiveX não foi simplesmente
um erro estúpido.

Foi uma tentativa precoce
de transformar o navegador
em uma plataforma de aplicações.

<!-- S22 -->
E nesse sentido a Microsoft
estava mesmo à frente do seu tempo.

O problema era quanto poder
ela deu a essa plataforma.

<!-- S23 -->
O ActiveX não era
a única extensão da Microsoft.

Tinha o VBScript.

Tinha o DHTML.

E até o CSS expression.

Sim.

<!-- S24 -->
O Internet Explorer conseguia avaliar
JavaScript direto dentro do CSS.

Dava para escrever algo assim.

<!-- S25 -->
Era ridículo.

E às vezes também
surpreendentemente útil.

E nada disso tinha garantia
de funcionar em outro lugar.

<!-- S26 -->
A Microsoft não estava simplesmente
implementando a web.

A Microsoft estava estendendo a web
na direção dela.

E com noventa por cento
do mercado
ela tinha poder suficiente
para que isso funcionasse.

<!-- S27 -->
Um dos exemplos mais famosos
foi o box model do CSS.

O modelo padrão dizia
que se um elemento
tivesse 200 pixels de largura,
com 20 pixels de preenchimento
e 5 pixels de borda,

<!-- S28 -->
a largura total
seria de 250 pixels.

<!-- S29 -->
Versões antigas do Internet Explorer
liam isso de outro jeito.

No modo quirks, a largura declarada
podia incluir o preenchimento
e a borda.

<!-- S30 -->
Não era necessariamente
um jeito insano de pensar largura.

Aliás, hoje muitas vezes pedimos
exatamente esse comportamento de propósito.

Ele se chama border-box.

<!-- S31 -->
O problema de verdade era
que navegadores diferentes
se comportavam de forma diferente.

E isso significava
que o desenvolvedor tinha que se importar.

Muito.

<!-- S32 -->
Existia uma coisa chamada hasLayout.

Não era uma propriedade normal do CSS.

Não fazia parte do padrão.

Mas decidia
como o Internet Explorer
posicionava os elementos.

<!-- S33 -->
E às vezes um layout quebrado
se consertava misteriosamente
com uma única linha adicionada.

zoom: 1

Por quê?

Porque zoom: 1 podia acionar
o mecanismo interno hasLayout.

<!-- S34 -->
Havia problemas
com a transparência dos PNG.

Havia problemas com elementos select,
que apareciam por cima
de menus posicionados de forma absoluta,
não importava o quão alto
você colocasse o z-index.

<!-- S35 -->
Desenvolver para a web não era só
implementar o seu design.

Era aprender os bugs
de um motor de navegador específico.

<!-- S36 -->
Mais um exemplo maravilhoso.

Espaços em branco.

E desse aqui o Internet Explorer
nem tinha culpa.

Dava para colocar duas imagens
uma bem do lado da outra
na marcação,
sem nada entre as tags,
e obter um resultado.

<!-- S37 -->
Aí alguém formatava o HTML direitinho
e punha cada tag em uma linha própria.

E de repente aparecia
um espaço de alguns pixels entre as imagens.

A quebra de linha passava a significar algo.

<!-- S38 -->
Seu formatador de código
podia literalmente quebrar sua página.

E se você usasse
uma versão antiga do Visual Studio,
ele formatava o seu HTML
alegremente, sozinho.

Obrigado, Microsoft.

<!-- S39 -->
Os desenvolvedores acumularam
uma caixa de ferramentas inteira de gambiarras.

Comentários condicionais.

<!-- S40 -->
E às vezes um HTML
de aparência completamente bizarra,
cujo único propósito era
fazer o Internet Explorer se comportar.

<!-- S41 -->
Você não escrevia código feio
por ser um mau programador.

Você escrevia código feio
porque o navegador te obrigava.

<!-- S42 -->
O Internet Explorer também travava
de forma espetacular, e muitas vezes levava
junto todas as janelas abertas.

<!-- S43 -->
O que deu origem a uma categoria maravilhosa
de diversão de escritório.

Ei, dá uma olhada nesse link.

E vinte janelas do Internet Explorer
somem.

<!-- S44 -->
Essa era a web antes de
os navegadores serem isolados.

O navegador de hoje diz isto.

Não confio neste site.

Vou isolá-lo.

<!-- S45 -->
O Internet Explorer 6
soava mais assim.

Você é uma página web?

Claro.

Aqui estão as chaves do prédio.

<!-- S46 -->
Por que os desenvolvedores
usavam essas gambiarras?

Porque não tinha outro jeito.

<!-- S47 -->
Imagine uma empresa
com quinhentos funcionários.

Em cada computador roda o Windows XP.

Em cada um tem o Internet Explorer.

<!-- S48 -->
O desenvolvedor tem duas opções.

Opção um.

Fazer para o Internet Explorer,
que todo mundo já tem.

<!-- S49 -->
Opção dois.

Fazer para todos os navegadores,
testar tudo em todo lugar
e explicar para o setor de TI
por que todo mundo precisa de um segundo.

A resposta costumava ser óbvia.

<!-- S50 -->
Eles não escolhiam
tecnologia da Microsoft
por amarem a Microsoft.

Escolhiam o que resolvia
o problema do cliente.

E às vezes o ActiveX
era a melhor ferramenta disponível.

<!-- S51 -->
E em algum momento alguém se cansou.

As bibliotecas JavaScript começaram
a esconder as diferenças entre navegadores.

Uma das mais importantes
foi o jQuery.

<!-- S52 -->
Em vez de escrever
tratamento de eventos por navegador,
você escrevia uma única linha
que funcionava em todo lugar.

<!-- S53 -->
Em vez de lidar na mão
com implementações diferentes de AJAX,
você usava uma abstração comum.

<!-- S54 -->
O jQuery não fez
o Internet Explorer desaparecer.

Mas deixou muito mais fácil
fingir que ele não existia.

E para os desenvolvedores web da época,
isso era uma maravilha.

<!-- S55 -->
Surgiu o Firefox.

O Opera continuou se desenvolvendo.

Chegou o Safari.

E o Google acabou lançando o Chrome.

<!-- S56 -->
As guerras dos navegadores voltaram,
e dessa vez
a concorrência era diferente.

Os motores JavaScript
ficaram muito melhores.

Chegou o HTML5.

<!-- S57 -->
O próprio navegador começou a aprender
tudo aquilo para o que os desenvolvedores
antes precisavam de plugins.

<!-- S58 -->
Vídeo.

Áudio.

Canvas.

SVG.

WebGL.

WebSockets.

E por fim WebRTC.

A web estava virando
uma plataforma de aplicações.

<!-- S59 -->
Que era exatamente
o que a Microsoft vinha tentando
conseguir com o ActiveX.

Só que agora estava acontecendo
por meio de padrões abertos.

<!-- S60 -->
A Microsoft tentou mais uma vez.

O Silverlight deixava criar
aplicações ricas no navegador
com C# e .NET.

Até o primeiro streaming
da Netflix rodava nele.

<!-- S61 -->
Mas a web não queria plugins para sempre.

A Apple se recusou a dar suporte ao Flash
no iPhone.

E de repente o futuro não era isto.

Navegador mais plugin.

Era isto.

O próprio navegador.

<!-- S62 -->
O Silverlight sumiu.

O Flash sumiu.

O ActiveX sumiu.

E no fim sumiu
também o Internet Explorer.

<!-- S63 -->
E é aqui que
a história fica interessante.

Porque a Microsoft
não estava completamente errada.

Ela previu corretamente
que o navegador viraria
uma plataforma de aplicações.

<!-- S64 -->
Só estava tentando chegar lá
por tecnologias proprietárias.

A web chegou ao mesmo destino
pelos padrões.

<!-- S65 -->
O navegador venceu.

Mas venceu virando
algo muito mais poderoso
do que o navegador
de 2001.

<!-- S66 -->
Então a Microsoft era a vilã?

Na verdade não.

E é isso que torna
a história mais interessante.

<!-- S67 -->
A Microsoft tinha engenheiros brilhantes.

Tinha recursos enormes.

E construiu muitas tecnologias
que estavam mesmo à frente do seu tempo.

<!-- S68 -->
Mas a Microsoft também tinha
uma posição de mercado esmagadora.

E isso criou
um incentivo perigoso.

<!-- S69 -->
Se quase todo mundo
usa o seu navegador,
por que esperar pelos padrões?

Por que não simplesmente implementar
a sua própria solução?

Por um tempo, isso funcionou.

Até o resto da web alcançar.

<!-- S70 -->
Hoje o Internet Explorer não existe mais.

As velhas guerras dos navegadores
parecem história antiga.

Mas olhe
o mercado de navegadores de hoje.

Chrome.

Edge.

Opera.

Brave.

Vivaldi.

<!-- S71 -->
E muitos outros
são baseados no Chromium.

Produtos diferentes.

Muitas vezes o mesmo
motor por baixo.

<!-- S72 -->
Então talvez a gente tenha trocado isto.

Um navegador que todos tinham que atender.

Por isto.

Um motor sobre o qual todos constroem.

Não soa familiar?

<!-- S73 -->
Porque um motor dominante
não decide só
como os sites são exibidos.

<!-- S74 -->
Ele influencia o que os desenvolvedores constroem.

Quais tecnologias ficam populares.

E, no fim das contas,
o que a própria web se torna.

<!-- S75 -->
Existe, porém,
uma diferença muito importante.

A web de hoje se apoia
em padrões abertos.

O Firefox ainda tem motor próprio.

O Safari tem o WebKit.

O Chromium é de código aberto.

<!-- S76 -->
E os navegadores modernos
se atualizam sozinhos.

Estamos muito longe
da situação
de 2003.

<!-- S77 -->
Mas a pergunta de fundo continua.

Quanta influência
uma única empresa deveria ter
sobre uma plataforma
usada por quase todo mundo?

Essa é a pergunta
que nunca foi embora de verdade.

<!-- S78 -->
Então, o Internet Explorer 6 era terrível?

Era.

Às vezes espetacularmente terrível.

<!-- S79 -->
Mas essa não é a história toda.

Ele também era um produto do seu tempo.

<!-- S80 -->
O problema era
que a Microsoft tinha vencido
as guerras dos navegadores tão por completo
que podia definir as regras.

<!-- S81 -->
E quem pagou foram os desenvolvedores web.

Eles aprenderam os mistérios
do hasLayout.

Descobriram que zoom: 1
consertava as coisas por mágica.

E rezavam.

<!-- S82 -->
E no fim o Internet Explorer
virou aquilo que passou
vinte anos construindo.

Uma plataforma legada
que ninguém mais queria
manter.

<!-- S83 -->
A web não rejeitou
a visão da Microsoft.

Ela simplesmente construiu
uma versão melhor dela.

E se aquela época
tem uma coisa para nos ensinar,
é esta.

<!-- S84 -->
Uma tecnologia não vira padrão
só porque é boa.

<!-- S85 -->
Às vezes ela vira padrão
porque uma empresa tem poder suficiente
para fazer todo mundo usar.

<!-- S86 -->
E às vezes,
vinte anos depois,
a gente percebe que fez de novo.
