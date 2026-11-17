<!-- S01 -->
Imagine ligar um PC com Windows
e não encontrar barra de tarefas, nem botão Iniciar,
nem um único ícone na área de trabalho.

<!-- S02 -->
No lugar disso, há uma barra fina no topo,
um menu que aparece onde quer que você clique
e quatro áreas de trabalho virtuais lado a lado.

<!-- S03 -->
Parece Linux.
Mas seus programas, seus drivers e seus arquivos
estão exatamente onde você os deixou.
Continua sendo Windows.

<!-- S04 -->
Só a área de trabalho mudou.
E a chave que muda isso
é uma única configuração.

<!-- S05 -->
O Windows guarda isso no registro,
em um valor chamado Shell.
Em quase todo PC com Windows,
ali está escrito explorer.exe.

<!-- S06 -->
Escreva ali o nome de outro programa,
saia e entre de novo,
e o Windows inicia esse programa no lugar.
O que ele desenhar vira a sua área de trabalho.

<!-- S07 -->
E isso não é um truque que alguém descobriu ano passado.
Em 1990, o Windows 3.0 já tinha a mesma chave
em um simples arquivo de texto chamado system.ini.
Uma linha: shell=progman.exe.

<!-- S08 -->
Se você mudasse esse nome,
o Gerenciador de Programas, a janela cheia de grupos de ícones,
nem chegava a aparecer.

<!-- S09 -->
Então a pergunta não é se o Windows
pode ter outra área de trabalho.
Ele sempre pôde.
A pergunta é por que quase ninguém viu uma.

<!-- S10 -->
Comece pelo que essa linha realmente indica.
A barra de tarefas, os ícones da área de trabalho,
a pequena área de notificação perto do relógio:
tudo isso é um só programa, o explorer.exe.

<!-- S11 -->
Sim, o mesmo explorer.exe
que você abre como Explorador de Arquivos para ver seus arquivos.
Ele faz dois trabalhos,
e a maioria das pessoas só repara em um.

<!-- S12 -->
Esse segundo trabalho tem nome: o shell.
É a camada em que você mexe.
Por baixo dela ficam o kernel, os drivers
e os serviços que mantêm o Windows funcionando.

<!-- S13 -->
Nenhum deles precisa de barra de tarefas.
Finalize o explorer.exe no Gerenciador de Tarefas,
e a barra de tarefas e os ícones somem...
mas o Bloco de Notas, o seu navegador
e todas as outras janelas continuam funcionando.

<!-- S14 -->
Inicie de novo, e a área de trabalho volta.
É talvez a prova mais clara que existe
de que a área de trabalho é só mais um programa.

<!-- S14b -->
Se você já trocou o launcher
de um celular Android,
já viu uma ideia parecida.
O Android trata isso como uma configuração comum.
O Windows também tem o mecanismo,
mas nunca deu aos usuários comuns
um botão simples para isso.

<!-- S15 -->
Três termos se confundem aqui.
O shell é de onde você abre as coisas:
a barra de tarefas, os menus, a área de trabalho.
Um gerenciador de janelas controla como as janelas
são posicionadas, empilhadas e recebem o foco.
Um ambiente de desktop
reúne tudo isso num só ambiente.

<!-- S16 -->
No Linux, essas peças podem ser combinadas
de muitas formas diferentes.
No Windows, substituir o shell
não substitui o gerenciamento de janelas do sistema
nem o jeito como os aplicativos desenham as bordas das janelas.

<!-- S17 -->
Isso não impediu as pessoas de tentar.
No começo dos anos 90, dava para entrar numa loja
e comprar um substituto para o Gerenciador de Programas.

<!-- S18 -->
O Norton Desktop for Windows
dava a você uma área de trabalho própria,
ferramentas de arquivos próprias e um lançador próprio,
em cima do mesmo Windows de sempre.

<!-- S19 -->
Alguns fabricantes de computador o substituíam
antes mesmo de o cliente ligar a máquina.
O Navigator da Packard Bell recebia os compradores
com uma casa que dava para percorrer cômodo por cômodo.

<!-- S20 -->
Depois, o Windows 95 passou o trabalho para o explorer.exe,
e a linha no system.ini
simplesmente mudou para explorer.exe.
A chave continuou exatamente onde estava.

<!-- S21 -->
No fim dos anos 90,
uma comunidade inteira cresceu em torno dessa chave.
O projeto mais conhecido foi o LiteStep.

<!-- S22 -->
Ele pegou emprestado o visual do AfterStep,
um gerenciador de janelas do Unix inspirado no NeXTSTEP,
da empresa que Steve Jobs fundou depois de sair da Apple.

<!-- S23 -->
O LiteStep não tinha menu Iniciar, a não ser que você montasse um.
Tudo era um módulo:
um dock aqui, um relógio ali,
um menu que abria onde quer que você clicasse com o botão direito.

<!-- S24 -->
Os temas eram compartilhados como papéis de parede.
Alguns pareciam futuristas.
Outros pareciam uma estação de trabalho Unix.
Outros quase não deixavam nada na tela.

<!-- S25 -->
O Blackbox for Windows foi pelo caminho oposto.
Ele copiava o Blackbox, um gerenciador de janelas minimalista do Unix,
até o menu simples e único
e a barra de ferramentas fina.

<!-- S26 -->
O sucessor, bbLean,
manteve essa ideia viva no Windows 2000 e no XP.

<!-- S27 -->
O Emerge Desktop dividiu o shell em partes separadas:
um lançador, uma área de notificação, uma lista de tarefas,
cada uma um programinha que você podia manter ou descartar.

<!-- S28 -->
Por que ter tanto trabalho?
Em parte porque o visual do XP
era fácil de reconhecer e difícil de mudar.
Os temas mudavam as cores e os botões.
O layout continuava igual.

<!-- S29 -->
Em parte por causa da memória.
Numa máquina com 128 megabytes,
um shell mais leve prometia mais espaço
para todo o resto.

<!-- S30 -->
E em parte por causa do Linux.
Lá, escolher a área de trabalho era normal,
e alguns usuários de Windows queriam
a mesma escolha.

<!-- S31 -->
A maioria desses projetos já acabou.
A última versão do LiteStep foi uma prévia
de 2014, ainda marcada como alfa.
O Emerge Desktop e o SharpEnviro também pararam.

<!-- S32 -->
As pequenas equipes de voluntários foram parte do motivo.
Mas o Windows também mudou.
Com os anos, a área de trabalho dele virou muito mais
do que um único executável.

<!-- S33 -->
Hoje, a experiência da área de trabalho está espalhada
por vários processos,
componentes do sistema e aplicativos empacotados.
Até o menu Iniciar roda como um programa à parte.

<!-- S34 -->
Substituir o explorer.exe não significa substituir
tudo o que forma a interface moderna do Windows.
E esse é um dos motivos por que construir
uma área de trabalho alternativa completa
é mais difícil do que costumava ser.

<!-- S35 -->
E mesmo assim, ainda funciona.
O Cairo Desktop, um projeto de código aberto,
roda no Windows 11 hoje.

<!-- S36 -->
Ele traz a própria barra de menus no topo,
a própria barra de tarefas
e pastas que você pode fixar na barra como pilhas.

<!-- S37 -->
Ele pode rodar junto com o explorer.exe
ou assumir o papel de shell.
Nesse segundo modo,
partes do Windows 11 podem dar problema,
entre elas as Configurações e a Segurança do Windows.

<!-- S38 -->
O Seelen UI faz isso de outro jeito.
Ele não substitui o explorer.exe.
Esconde a barra de tarefas e traz peças próprias:
um dock, uma barra, widgets
e um gerenciador de janelas que organiza suas janelas lado a lado.

<!-- S39 -->
O resultado pode não lembrar o Windows em nada.
Mas, por baixo, o explorer.exe continua rodando.
É uma cara nova, não um shell novo.

<!-- S40 -->
E a Microsoft?
Ela tem, na verdade, um recurso oficial para isso.
Chama-se Shell Launcher
e foi feito para dispositivos como quiosques.

<!-- S41 -->
Você provavelmente já usou algo assim
sem saber.
A máquina de passagens na estação.
Um caixa de autoatendimento. Um caixa eletrônico.

<!-- S42 -->
Muitos deles são PCs com Windows
cujo shell inteiro é um único aplicativo.
Um administrador define o programa,
e depois do login esse programa é a área de trabalho inteira.

<!-- S43 -->
Mas ele só está disponível
nas edições Enterprise, Education
e IoT Enterprise.

<!-- S44 -->
E o mecanismo antigo do registro
continua fazendo parte do Windows.
A Microsoft só nunca o transformou
em uma configuração comum da área de trabalho
para usuários comuns.

<!-- S45 -->
Então por que o Windows parece ter só uma área de trabalho?
Não porque ele não possa ter outra.
Mas porque a área de trabalho é o produto.

<!-- S46 -->
No Linux, a área de trabalho é uma escolha.
Algumas distribuições pedem que você escolha uma
ainda durante a instalação.
KDE Plasma, GNOME, Xfce, Cinnamon...

<!-- S47 -->
No Windows, a área de trabalho é o que a Microsoft mostra
em cada anúncio, em cada captura de tela
e em cada página de suporte.
Uma só área de trabalho significa um só conjunto de instruções
para mais de um bilhão de máquinas.

<!-- S48 -->
Isso é uma vantagem real.
Quando algo quebra,
a tela do artigo de ajuda é igual à sua.
O preço é que a maioria das pessoas nunca descobre
que havia uma escolha.

<!-- S49 -->
As pessoas trocavam a área de trabalho do Windows
antes mesmo de o Windows 95 existir.
Criaram docks, menus enxutos
e áreas de trabalho que não se pareciam com nenhuma outra.

<!-- S50 -->
A maioria desses projetos acabou.
A ideia, não.
Debaixo de cada barra de tarefas em que você já clicou,
ainda está aquela única configuração, esperando outro nome.

<!-- S51 -->
A área de trabalho é só mais um software.
E software pode ser substituído.

<!-- S52 -->
Então, aqui vai uma pergunta para você.
Se o Windows deixasse você escolher a área de trabalho
na instalação, como algumas distribuições Linux fazem,
você trocaria ou ficaria com a que já conhece?
Conte nos comentários.
