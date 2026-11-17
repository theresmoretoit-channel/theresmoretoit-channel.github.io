<!-- S01 -->
Você abre um terminal.
Alguém passa por perto.
Vê uma tela preta
coberta de texto misterioso.
E de repente...

<!-- S02 -->
"Meu Deus! Você está hackeando!"

<!-- S03 -->
Bom...
Talvez.
Ou talvez você só esteja tentando descobrir
por que o servidor caiu.

<!-- S04 -->
Hoje vamos ver por que
terminais e hacking se tornaram
quase a mesma coisa na cultura popular.
E, mais importante...
como o hacking é de verdade.

<!-- S05 -->
Para a maioria das pessoas, um computador tem botões.
Você clica em alguma coisa.
Alguma coisa acontece.
E aí existe o terminal.
Sem botões.
Sem mensagens amigáveis.
Só isto.
E isso é aterrorizante.

<!-- S06 -->
Uma interface gráfica pode dizer:
excluir usuário.
Um terminal diz isto no lugar.

<!-- S07 -->
Para um usuário de Linux experiente
isso é perfeitamente comum.
Para todo mundo, parece
que você vai lançar um míssil.

<!-- S08 -->
Na verdade há um motivo histórico
para essa aparência.
Os primeiros computadores não tinham interface gráfica.
Falava-se com eles por terminais de texto.

<!-- S09 -->
E aqueles terminais tinham telas escuras
com fósforo verde ou âmbar.
Não era uma tentativa de parecer moderno.
Era simplesmente como a tecnologia funcionava.

<!-- S10 -->
Mas então o cinema e a televisão
notaram uma coisa útil.
Uma tela preta cheia de
texto mudando rápido parece técnica.
E, mais importante...
parece complicada.

<!-- S11 -->
Você não precisa entender
o que os caracteres significam.
Você simplesmente vê isto.
E seu cérebro decide:
essa pessoa está fazendo algo ilegal.

<!-- S12 -->
Hollywood desenvolveu uma linguagem
notavelmente uniforme para o hacking.
O hacker está sentado num quarto escuro.
Há seis monitores.

<!-- S13 -->
O quarto é iluminado apenas pelos monitores.
Ninguém acendeu a luz.
O hacker começa a digitar
a cerca de novecentas palavras por minuto.

<!-- S14 -->
O texto voa pela tela.
Aparece uma barra de progresso.
Noventa e sete por cento.
Noventa e oito.
Noventa e nove.
E finalmente cem.
O hacker se recosta na cadeira.
E diz...

<!-- S15 -->
"Estou dentro."

<!-- S16 -->
Não é assim que funciona a maioria
dos incidentes de segurança.
Vamos imaginar a conversa de verdade.
"Vou hackear este servidor."
E o servidor responde:
permission denied.

<!-- S17 -->
"Ah."
Tenta de novo.
Permission denied.
Confere a senha.

<!-- S18 -->
Lê a documentação.
Pesquisa a mensagem de erro.
No fim descobre que o administrador
desligou o login por senha há seis meses.

<!-- S19 -->
"Tá."

<!-- S20 -->
Computadores são extraordinariamente bons em fazer você
passar vinte minutos para descobrir que
esqueceu um único caractere num arquivo de configuração.

<!-- S21 -->
De um lado da tela:
administrador de sistemas.
Do outro:
hacker.
As mesmas ferramentas podem aparecer nos dois.
É porque o terminal
não é uma ferramenta de hacking.
É uma interface.

<!-- S22 -->
Você pode usá-lo para rodar um servidor,
ler logs, copiar arquivos, instalar programas,
ou descobrir o que quebrou às três da manhã.

<!-- S23 -->
Ou, dependendo do que você está fazendo
e de ter ou não permissão,
pode usá-lo para testes de segurança.
Ou para um ataque.

<!-- S24 -->
A ferramenta em si não diz
qual das duas coisas você está fazendo.
Uma chave de fenda pode consertar um computador.
Também pode destruir um.
A chave de fenda não é a criminosa.

<!-- S25 -->
Então, o que é de fato um hacker?
A palavra tem uma história muito mais antiga
que o cibercrime moderno.

<!-- S26 -->
Originalmente, um hacker era alguém
que gostava de explorar sistemas
e sabia encontrar soluções inesperadas.

<!-- S27 -->
Com o tempo, a palavra grudou
na segurança da informação.
E hoje, quando alguém diz
"ele é um hacker", pode significar

<!-- S28 -->
um pesquisador de segurança,
um pentester,
um atacante de verdade,
ou simplesmente alguém que sabe
uma quantidade preocupante sobre Linux.
Em geral o contexto ajuda.

<!-- S29 -->
Vamos olhar de novo para a nossa imagem.
A legenda diz:
você hackeou.
E olhem as telas dela.

<!-- S29b -->
Numa delas, algo parecido com nmap.
Na outra, algo que parece
ainda mais suspeito.
Barra etc barra passwd.

<!-- S30 -->
Para quem não conhece Linux,
ela está claramente invadindo o Pentágono.
Para um administrador de sistemas, ela está checando
a rede e lendo uma lista de contas.

<!-- S31 -->
E é daí que vem a piada.
A mulher pode não estar hackeando nada.
Pode estar simplesmente fazendo o trabalho dela.

<!-- S32 -->
Então o que o nmap faz de verdade?
É uma ferramenta de descoberta de rede
e auditoria de segurança.

<!-- S33 -->
Em termos bem simples,
você aponta ele para uma máquina e pergunta
o que este computador
está expondo para a rede.

<!-- S34 -->
Ele pode dizer que certas portas estão abertas.
E portas correspondem a serviços de rede.
Isso não é automaticamente um ataque.

<!-- S35 -->
É mais como olhar para um prédio
e perguntar quais portas estão abertas.
Se o prédio é seu,
isso é administração normal.

<!-- S36 -->
Se é de outra pessoa
e você está deliberadamente
procurando um jeito de entrar...

<!-- S37 -->
bom, aí já é outra história.

<!-- S38 -->
E aquele caminho de arquivo?
Alguém pode pensar:
ela está lendo o arquivo de senhas.
Ele de fato contém informações sobre contas.

<!-- S39 -->
Mas num sistema Linux moderno,
os hashes das senhas ficam guardados em outro lugar.
Estão em barra etc barra shadow,
que é muito mais restrito.

<!-- S40 -->
Então ver esse arquivo não é a mesma coisa
que descobrir as senhas de todo mundo.
Hollywood, claro,
deixaria isso muito mais dramático.

<!-- S41 -->
Um administrador de Linux diria:
é literalmente uma lista de usuários.

<!-- S42 -->
Outra cena clássica quebra uma senha
em cerca de catorze segundos.
A quebra de verdade é mais sem graça.
Você tem um hash, tem uma lista de palavras,
e deixa o computador testar candidatos.

<!-- S43 -->
Talvez encontre uma em um minuto.
Talvez em uma semana.
Talvez nunca.
E enquanto ele trabalha, o atacante
não fica ali digitando.
Pode estar comendo um sanduíche.

<!-- S44 -->
O que me leva à minha tradição
hollywoodiana favorita.
Pelo visto, computadores não aceitam comandos
a não ser que você digite muito rápido.

<!-- S45 -->
Programadores e administradores de verdade
não digitam o tempo todo.
Eles pensam.
Eles leem.
Eles encaram uma mensagem de erro.

<!-- S46 -->
Aí descobrem que alguém
resolveu isso há onze anos.
E copiam a solução.

<!-- S47 -->
Isso é ciência da computação.

<!-- S48 -->
Às vezes a coisa mais perigosa
que você pode digitar não é
um comando misterioso de hacker.
É algo perfeitamente legítimo.

<!-- S49 -->
O exemplo famoso é este.

<!-- S50 -->
O que é uma história ótima,
só que um sistema moderno se recusa.
Ele responde que operar recursivamente
sobre a barra é perigoso,
a menos que você acrescente uma opção dizendo que é sério.

<!-- S51 -->
Os comandos que realmente destroem coisas
são mais sem graça.
Uma exclusão no diretório errado.
Um disco escrito por cima do disco errado.

<!-- S52 -->
Desses o terminal não te avisa,
porque, pelo que ele consegue perceber,
não há nada de errado.
Ele só pode perguntar: você tem certeza absoluta?

<!-- S53 -->
E se você responder que sim...
ele pode acreditar em você.

<!-- S54 -->
E aqui está o maior problema
do estereótipo de Hollywood.
Um ataque real pode não parecer
nada com hacking.

<!-- S55 -->
Pode envolver uma senha roubada.
Phishing.
Um servidor sem atualização.
Uma chave de API vazada.
Uma senha reutilizada de outro lugar.

<!-- S56 -->
O atacante pode nem precisar
de um terminal.
Pode simplesmente entrar
numa interface web.
Usuário.
Senha.
E pronto, está dentro.

<!-- S57 -->
Nenhum texto verde.
Nenhum gráfico estilo Matrix.
Nenhuma música dramática.

<!-- S58 -->
O que é provavelmente bem mais assustador.

<!-- S59 -->
As pessoas imaginam um hacker como um moletom,
um quarto escuro e um teclado que brilha.
Nada disso tem a ver com hacking.

<!-- S60 -->
A pessoa sentada ao seu lado no trem,
com um notebook completamente comum,
pode saber consideravelmente mais
sobre segurança da informação.

<!-- S61 -->
E a pessoa sentada
na frente de seis servidores
talvez esteja só tentando descobrir
por que o banco de dados não sobe.

<!-- S62 -->
Então vamos voltar à nossa imagem original.
O homem aponta para a mulher.
Você hackeou.
Ela estava hackeando?

<!-- S63 -->
Talvez.
Talvez não.

<!-- S64 -->
Ela tem um terminal.
Ela tem o nmap.
Ela tem uma lista de contas.
Mas nada disso prova
que ela hackeou coisa alguma.
Ela pode ser a administradora
ou estar fazendo uma auditoria de segurança.

<!-- S65 -->
Ou pode estar hackeando de verdade.
Nós não sabemos.
E essa é a piada.

<!-- S66 -->
A verdadeira diferença entre
administração comum e hacking
não é a cor do seu terminal.
Não é quantos monitores você tem.

<!-- S67 -->
Não é a velocidade com que você digita.
E certamente não é
se você está de moletom com capuz.
É o que você está fazendo
e se você tem permissão para fazer.

<!-- S68 -->
Então, da próxima vez que você vir alguém
encarando uma tela preta
cheia de texto misterioso,
não presuma que a pessoa está hackeando.

<!-- S69 -->
Talvez ela só esteja consertando o servidor.

<!-- S70 -->
Embora...
se ela estiver digitando novecentas palavras
por minuto enquanto grita
"estou dentro"...

<!-- S71 -->
talvez valha a pena perguntar
o que ela está fazendo.
