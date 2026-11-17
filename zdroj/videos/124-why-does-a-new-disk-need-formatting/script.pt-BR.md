<!-- S01 -->
Você compra um disco novinho.
Um terabyte, completamente vazio.
Antes de guardar um único arquivo,
ele primeiro precisa ser formatado.

<!-- S02 -->
Então você formata com ext4,
o sistema de arquivos padrão
em muitos computadores com Linux.
Sem mexer em nenhuma configuração,
antes de você salvar qualquer coisa,
uns dezessete gigabytes já sumiram.

<!-- S03 -->
Ainda não tem nada guardado.
Nenhuma foto, nenhum documento.
Então o que está ocupando todo esse espaço?

<!-- S04 -->
E por que um disco precisa de formatação,
para começo de conversa?
Ele já consegue guardar dados.
Consegue ler e gravar trilhões de bits.

<!-- S05 -->
Por que o computador não pode simplesmente gravar
onde tiver espaço?

<!-- S06 -->
Porque guardar dados
e encontrá-los de novo
são dois problemas muito diferentes.

<!-- S07 -->
Imagine um escritório que entrega
papel em branco em vez de formulários.
Tudo é anotado em algum lugar...
e ninguém encontra nada.

<!-- S08 -->
Um disco sem sistema de arquivos
é essa pilha de papel.
Mas uma imagem melhor
é um caderno.

<!-- S09 -->
Imagine um caderno
com mil páginas
e algumas regras para usá-lo.

<!-- S10 -->
Primeiro: toda página tem um número.
Agora cada lugar do caderno
tem um endereço.
Página quatrocentos e doze
significa exatamente um lugar.

<!-- S11 -->
Segundo: as primeiras páginas
são um sumário.
Cada item traz um nome
e a página onde ele está.
Panquecas: página doze.

<!-- S12 -->
Terceiro: bem no final,
há uma lista das páginas
que ainda estão em branco.

<!-- S13 -->
Agora acrescente uma receita.
Você procura no final uma página em branco.
Escreve a receita nela.
Acrescenta uma linha no sumário.
E risca essa página
da lista de páginas em branco.

<!-- S14 -->
Uma receita, três lugares.
E os três precisam bater.

<!-- S15 -->
Aí a receita de panqueca cresce.
A página doze está cheia,
e a treze já está ocupada.
Então ela continua na página oitenta e sete,
e o sumário tem que dizer isso.

<!-- S16 -->
E aqui está o problema.
Se você quer espaço para mil itens
no sumário,
precisa reservar essas páginas
antes de escrever uma única receita.

<!-- S17 -->
Essa é a analogia.
Agora, o que de fato existe no disco.

<!-- S18 -->
Um disco não sabe nada de arquivos,
pastas ou nomes.
Tudo o que ele oferece é uma longa fileira
de espaços numerados, chamados setores.

<!-- S19 -->
Num disco rígido,
os dados ficam em pratos que giram.
Um SSD guarda tudo em memória flash.
De qualquer forma, o computador só pede
um setor pelo número dele,
e o disco descobre onde ele fica.

<!-- S20 -->
Um setor é pequeno.
Normalmente 512 bytes,
ou 4.096
nos discos mais novos.

<!-- S21 -->
Sistemas de arquivos costumam trabalhar
com pedaços maiores, chamados blocos.
No ext4, um bloco tem quatro kilobytes,
o tamanho de oito setores do tipo antigo.

<!-- S22 -->
Esses blocos numerados
são as páginas do caderno.
O que o sistema de arquivos ainda precisa
são as outras duas partes:
um sumário
e uma lista do que está livre.

<!-- S23 -->
É isso que a formatação cria.
E foi para lá
que foram aqueles dezessete gigabytes.

<!-- S24 -->
O ext4 reserva um registro
para cada arquivo e pasta
que o disco vai poder guardar ao mesmo tempo.
Cada registro tem
256 bytes.
Ele se chama inode.

<!-- S25 -->
Um dia, cada inode vai dizer
qual o tamanho de um arquivo,
quando ele foi alterado,
quem pode abri-lo
e quais blocos guardam o conteúdo dele.

<!-- S26 -->
Num disco de um terabyte,
o ext4 prepara cerca de
sessenta e um milhões deles.
Todos vazios, todos esperando.
São quase dezesseis gigabytes
de registros em branco.

<!-- S27 -->
Por que sessenta e um milhões?
O ext4 faz uma estimativa simples:
um inode para cada dezesseis kilobytes
de espaço no disco.
Num computador comum,
a maioria desses registros
nunca vai ser usada.

<!-- S28 -->
Mais cerca de um gigabyte
vai para um journal,
que a gente vai ver mais adiante.
O resto é mais contabilidade,
incluindo um mapa com um bit por bloco,
dizendo se ele está ocupado ou livre.

<!-- S29 -->
E esse número também é fixo.
Esgote todos os registros
com milhões de arquivos minúsculos,
e o disco vai dizer que está cheio...
mesmo com gigabytes de espaço sobrando.

<!-- S30 -->
Então vamos ver isso funcionando.
Vamos criar um arquivo chamado hello.txt.
Dentro, só uma palavra: hello.
Cinco letras. Cinco bytes.

<!-- S31 -->
O sistema de arquivos escolhe um inode vazio.
Digamos, o número treze.
Depois encontra um bloco livre no mapa
e marca esse bloco como usado.

<!-- S32 -->
Ele grava os cinco bytes nesse bloco.
Depois preenche o inode:
cinco bytes de tamanho, criado agora mesmo,
e guardado naquele único bloco.

<!-- S33 -->
E por fim, na pasta,
ele acrescenta uma linha:
o nome hello.txt
e o número treze.

<!-- S34 -->
Repare onde o nome foi parar.
Não no arquivo.
Não no inode.
O nome mora na pasta,
que na verdade é só uma lista
de nomes e números.

<!-- S35 -->
E uma pasta é só mais um arquivo.
O conteúdo dela
é justamente essa lista.

<!-- S36 -->
É também por isso que mover um arquivo
para outra pasta no mesmo sistema de arquivos
é instantâneo, não importa o tamanho.
Uma pasta perde uma linha,
a outra ganha uma,
e normalmente o conteúdo
nem sai do lugar.

<!-- S37 -->
Cinco bytes de texto...
e no disco ele ocupa
4.096.
Um bloco é o menor pedaço
que o sistema de arquivos distribui,
então até um arquivo minúsculo gasta um bloco inteiro.

<!-- S38 -->
Quando o arquivo não cabe mais no bloco,
o sistema de arquivos encontra outro livre.
Talvez logo ao lado.
Talvez num lugar completamente diferente.
E o inode registra os dois.

<!-- S39 -->
Com o tempo, um arquivo grande pode acabar
em pedaços espalhados pelo disco todo.
Um disco rígido tem que pular entre eles.
Um SSD lida com isso muito melhor.

<!-- S40 -->
O programa que salvou o arquivo
não sabe nada disso.
Ele disse “salve hello.txt”,
e todo o resto aconteceu nos bastidores.

<!-- S41 -->
Agora apague o arquivo.
O nome é removido da pasta.
O inode é marcado como livre.
O bloco volta para a lista de livres.

<!-- S42 -->
Num disco rígido tradicional,
os cinco bytes em si continuam lá.
Ninguém mexeu neles.
Eles ficam até que algo novo
seja gravado por cima.

<!-- S43 -->
É por isso que um arquivo apagado
às vezes pode ser recuperado.
Apagar normalmente não elimina
o conteúdo.
Só marca o espaço como disponível.

<!-- S44 -->
Num SSD, é menos garantido.
O sistema de arquivos pode avisar ao disco
que aqueles blocos não são mais necessários,
e o disco pode descartar o que tem neles.
Depois disso, recuperar o arquivo
é bem menos provável.

<!-- S45 -->
Então um sistema de arquivos é, no fundo, um contador.
Criar esse único arquivo
significou atualizar três coisas:
a pasta, o inode
e o mapa de blocos livres.

<!-- S46 -->
Agora corte a energia
bem no meio do salvamento de um arquivo.

<!-- S47 -->
Talvez o bloco já tenha sido marcado como usado,
mas nenhum inode aponte para ele ainda.
Esse espaço simplesmente se perde.
Chato, mas inofensivo.

<!-- S48 -->
Ou talvez o inode aponte para um bloco
que o mapa ainda diz que está livre.
O próximo arquivo pode ser gravado
bem em cima dele.
E o primeiro é destruído sem ninguém perceber.

<!-- S49 -->
É por isso que o ext4 mantém um journal.
Antes de mudar sua contabilidade,
ele anota o que está prestes a fazer.
Depois de uma falha, ele refaz só as mudanças
que tinha terminado de anotar
e marcado como concluídas.
O que ficou pela metade é ignorado.

<!-- S50 -->
E existe um problema mais silencioso.
Às vezes um disco muda um bit
e não avisa ninguém.

<!-- S51 -->
O ext4 protege os próprios registros
com somas de verificação,
então consegue detectar danos neles.
Mas o conteúdo dos seus arquivos?
Nisso ele simplesmente confia.

<!-- S52 -->
Alguns sistemas de arquivos verificam os dois.
E alguns guardam uma segunda cópia,
então, quando uma cópia é danificada,
eles conseguem consertá-la a partir da outra.
Detectar um problema e consertá-lo
não são a mesma coisa.

<!-- S53 -->
Então todo sistema de arquivos faz o mesmo trabalho:
blocos numerados, uma lista de nomes
e um mapa do que está livre.

<!-- S54 -->
Mas as escolhas são diferentes.
O ext4 prepara sessenta e um milhões de registros
antes de você salvar qualquer coisa.
O NTFS, no Windows, guarda seus registros
numa grande tabela que cresce conforme o uso.

<!-- S55 -->
E o Btrfs não prepara
uma tabela fixa de inodes com antecedência.
Ele os cria conforme os arquivos chegam.
E normalmente ele não sobrescreve
os dados onde eles estão.
Ele grava uma nova cópia
e só então libera a antiga.

<!-- S56 -->
Por padrão, ele também faz somas de verificação dos seus arquivos,
para saber quando eles foram danificados.

<!-- S57 -->
E como a cópia antiga
não é sobrescrita,
um snapshot pode mantê-la viva.
Isso muda a resposta
de quase todas as perguntas deste vídeo:
o que uma falha faz,
o que significa apagar
e até o que é uma cópia.

<!-- S58 -->
É aí que começa o próximo vídeo.

<!-- S59 -->
Então, uma pergunta pra você.
Um sistema de arquivos deve só guardar seus arquivos,
ou também deve protegê-los?
Me conta nos comentários.
