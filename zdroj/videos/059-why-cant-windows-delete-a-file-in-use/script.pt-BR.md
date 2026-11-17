<!-- S01 -->
Você tenta apagar um arquivo.
O computador diz que ele está aberto
em outro programa.
Mas não diz em qual.

<!-- S02 -->
Essa mensagem é a ponta visível
de uma pergunta bem mais estranha.
O que significa de fato
abrir um arquivo?

<!-- S03 -->
Porque em outro computador
o mesmo arquivo, aberto igual,
some sem uma única reclamação.

<!-- S04 -->
O mesmo arquivo.
A mesma ação.
Duas respostas completamente diferentes.

<!-- S05 -->
Comece pela parte
que irrita todo mundo.
Qual programa?

<!-- S06 -->
O Windows sabe.
Ele tem um objeto de kernel
para esse arquivo aberto
e sabe qual processo é o dono.
Poderia dizer o nome.

<!-- S07 -->
Então você fecha coisas a esmo.
Abre o Gerenciador de Tarefas.
Encara uma lista de processos
e quase não reconhece nenhum.

<!-- S08 -->
E por anos
a resposta foi mesmo
baixar uma ferramenta separada.
O Unlocker saiu em 2005,
e no Windows XP essa era a resposta.

<!-- S09 -->
Depois o Windows 7 trouxe
o Monitor de Recursos.
A aba CPU.
Uma lista chamada Identificadores Associados.

<!-- S10 -->
Digite o nome do arquivo.
Ele te dá o programa
e o identificador do processo.
Nada para instalar.
Está ali desde 2009.

<!-- S10b -->
Mas as ferramentas separadas faziam
mais do que só te avisar.
Elas conseguiam fechar o identificador
e liberar o arquivo.

<!-- S11 -->
O que nos traz de volta
à pergunta.
O que aquele programa recebeu
quando abriu o arquivo?

<!-- S12 -->
Digamos que um player abra
um arquivo chamado movie.mp4.
No Windows, abrir um arquivo
significa preencher duas coisas.

<!-- S13 -->
A primeira é óbvia.
O que eu quero fazer com ele?
Ler. Escrever nele.

<!-- S14 -->
A segunda é a interessante.
O que os outros podem fazer
enquanto eu o mantenho aberto?

<!-- S15 -->
É uma configuração de verdade.
Você diz o que outros programas
podem fazer enquanto você o segura.

<!-- S16 -->
Eles podem lê-lo.
Também podem escrever nele.
Podem apagá-lo ou renomeá-lo.

<!-- S16b -->
Ou nada disso.
Ninguém encosta nele
enquanto eu estiver usando.

<!-- S17 -->
O sinalizador que permite apagar
se chama FILE_SHARE_DELETE.
E a documentação da Microsoft
acrescenta uma linha embaixo.

<!-- S18 -->
O direito de apagar abrange
apagar e renomear ao mesmo tempo.

<!-- S19 -->
Então um programa que recusa
o compartilhamento de exclusão
bloqueou a renomeação também.

<!-- S20 -->
E se o programa que abriu o arquivo
não concedeu esse direito,
mais ninguém pode tomá-lo.

<!-- S21 -->
É por isso que o erro
não se chama arquivo em uso.
Chama-se violação de compartilhamento.

<!-- S22 -->
A resposta esteve o tempo todo
no nome
do próprio erro.

<!-- S23 -->
Agora a mesma coisa
numa máquina Linux.
Um player abre o vídeo.

<!-- S24 -->
E você digita
rm movie.mp4.

<!-- S24b -->
Funciona.
O vídeo continua tocando.

<!-- S25 -->
Então o que aquele programa pegou,
se não foi nenhum controle sobre o arquivo?

<!-- S26 -->
Esta é a ideia inteira
do vídeo.
O nome não é o arquivo.

<!-- S27 -->
movie.mp4 é uma linha
num diretório.
Essa linha aponta para um objeto
que guarda os dados de verdade.

<!-- S28 -->
Quando um programa abre o arquivo,
o que ele recebe é uma referência
ao objeto.
Não à linha.

<!-- S29 -->
Apagar o arquivo
remove então a linha.
O objeto fica intocado.

<!-- S30 -->
A página do manual diz isso
numa única frase.
O arquivo continuará existindo
até que o último descritor de arquivo
que o referencia seja fechado.

<!-- S31 -->
Parece abstrato
até a gente ver acontecer.
Então fiz um arquivo de log
de quinhentos megabytes
e deixei um processo com ele aberto.

<!-- S31b -->
Depois apaguei.

<!-- S32 -->
A listagem do diretório
não mostra absolutamente nada.
A ferramenta que mede
o tamanho da pasta diz zero.

<!-- S33 -->
E a ferramenta que mede
o espaço livre no disco
diz que quinhentos megabytes
ainda estão faltando.

<!-- S33b -->
Uma pasta vazia.
Meio gigabyte sumido.

<!-- S34 -->
Isso acontece com frequência
suficiente para existir um comando
só para achar arquivos assim.
Apagados, invisíveis, ainda no disco.

<!-- S35 -->
E o espaço volta
no instante em que aquele processo
solta o arquivo.

<!-- S36 -->
A mesma lógica vale para renomear.
Mova o arquivo aberto,
e o programa nem percebe.

<!-- S37 -->
O manual também é direto nisso.
Descritores abertos
do caminho antigo não são afetados.

<!-- S37b -->
Ele nunca usou o nome.

<!-- S38 -->
O que tem um limite
que vale a pena conhecer.
Um programa em execução
não dá para sobrescrever diretamente.

<!-- S38b -->
O Linux recusa.
Text file busy.

<!-- S39 -->
O que dá para fazer
é desvincular o nome
e colocar um arquivo novo ali.

<!-- S40 -->
O processo antigo segue rodando
a partir de um objeto
que não tem mais nome nenhum.
Quem iniciar depois usa o novo.

<!-- S41 -->
O que é a mesma ideia de novo,
provando a si mesma.
Muita coisa dá para substituir
sem tocar no próprio objeto.

<!-- S41b -->
Por isso o Linux consegue atualizar
um programa enquanto ele roda.
Você só não fica com a versão nova
até reiniciá-lo.

<!-- S42 -->
Então o Windows é
simplesmente mal projetado?

<!-- S42b -->
Não.
E esta é a parte
que quase ninguém conhece.

<!-- S43 -->
O Windows tem um jeito
de fazer exatamente a mesma coisa.

<!-- S43b -->
No NTFS, o Windows pode pedir
uma exclusão no estilo do POSIX.

<!-- S44 -->
A Microsoft descreve
o que acontece então.
O nome é removido
do espaço de nomes visível.

<!-- S45 -->
E os aplicativos que já tinham
o arquivo aberto seguem usando,
mesmo que o nome
com que o abriram já não exista.

<!-- S46 -->
Esse é o comportamento do Unix.
No NTFS.
Documentado pela Microsoft.

<!-- S47 -->
Os dois sistemas fazem as duas coisas.
O que difere é o padrão.
O que você recebe ao abrir um arquivo
sem pensar nisso.

<!-- S48 -->
No Windows você recebe um contrato.
No Unix você recebe uma referência
a um objeto.

<!-- S49 -->
O que soa como pergunta
de programador,
até você ter visto
esta mensagem específica.

<!-- S50 -->
Reinicie o computador
para concluir a instalação.

<!-- S51 -->
Suponha que o Windows precise trocar
uma biblioteca que um processo
mantém aberta sob o contrato estrito.

<!-- S52 -->
Ele não pode trocar o arquivo
por baixo daquele processo.
Então algo precisa soltar.

<!-- S53 -->
Fechar o aplicativo.
Parar o serviço.
Ou entregar o trabalho todo
ao Gerenciador de Reinicialização.

<!-- S54 -->
Que é um componente de verdade.
Ele desliga as coisas em ordem.
Aplicativos do Windows,
depois programas de console,

<!-- S55 -->
depois serviços,
e o Explorador por último.
Depois ele os inicia de novo.

<!-- S56 -->
E ele existe por um único motivo,
que a Microsoft diz sem rodeios
na própria documentação.

<!-- S57 -->
O principal motivo pelo qual
instalações de software
e atualizações exigem
reiniciar o sistema...

<!-- S58 -->
é que alguns dos arquivos
que estão sendo atualizados estão em uso
por um aplicativo
ou serviço em execução.

<!-- S59 -->
Seria bom demais parar por aí.
As regras de compartilhamento não são o único
motivo de um computador pedir reinício.

<!-- S60 -->
Atualizar o kernel é outra coisa.
Não dá para trocar o kernel
por baixo dele mesmo.

<!-- S61 -->
O Linux tem o mesmo problema,
embora o live patching
às vezes evite o reinício.

<!-- S62 -->
Então a versão honesta
promete menos do que
a versão satisfatória.

<!-- S63 -->
O jeito como o Windows trata arquivos
em uso deixou alguns componentes
mais difíceis de trocar em execução,
e isso contribuiu.

<!-- S64 -->
Porque toda escolha de projeto
tem uma consequência em algum lugar.

<!-- S65 -->
O Windows deixa o programa
que abre um arquivo decidir
o que os outros podem fazer com ele.

<!-- S66 -->
O preço é que às vezes
você não apaga seu próprio arquivo,
porque outro programa
não permitiu.

<!-- S67 -->
O Unix mantém o nome
e o objeto separados,
então muita coisa dá para trocar
com o sistema rodando.

<!-- S68 -->
O preço é meio gigabyte
que sumiu do disco
e não pertence a arquivo nenhum.

<!-- S69 -->
E olhe como cada um
dos dois se resolve.
No Windows, uma saída é
fechar o programa
que segura o arquivo.

<!-- S70 -->
No Linux, um jeito
de recuperar esse espaço
é reiniciar o serviço
que ainda o mantém aberto.

<!-- S71 -->
Causas diferentes.
Às vezes o mesmo remédio.

<!-- S71b -->
A propósito, se você quiser ver
aonde a próxima pergunta nos leva,
pense em se inscrever.
Isso ajuda muito o canal.

<!-- S72 -->
Então. A pergunta do começo.
O que significa
abrir um arquivo?

<!-- S73 -->
Significa que você está segurando algo.
Os dois sistemas simplesmente dão
coisas diferentes para você segurar.

<!-- S74 -->
É por isso que aquela mensagem
nunca disse de verdade
que o arquivo não pode ser apagado.

<!-- S75 -->
Ela disse que o programa
que o abriu
não deu permissão a você.

<!-- S75b -->
E ele sabe qual programa é.
Só não mencionou.
