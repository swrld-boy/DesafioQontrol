# Linha de raciocínio para resolução do problema.

Primeiramente, estudei a documentação do Selenium e revisei algumas questões em Python (foi a primeira que tive contato).
Segundamente, é minha primeira vez utilizando Python para aplicação web.

[Step by step]
-----------------------------------------------------------------------------------------------------------------------------------------------------
- Dei início, definindo uma instrução às opções do chrome, neste caso, a maximização de janela - estava me incomodando durante testes a tela reduzida. 

- Declarei o driver, para que pudesse acessar a web.

- Realizei um get no driver, buscando pelo endereço 'https://www.youtube.com' (página inicial do youtube).

- Criei uma variável 'pesquisa' para armazenar o que representaria a caixa de pesquisa na tela, com a biblioteca Keys, inseri na box de pesquisa o 
  nome do canal desejado e, dei enter para enviar.

- Criei uma variável 'primeiro_canal' para armazenar o que representaria o primeiro canal encontrado na tela e o acessei.

- Criei uma variável 'aba_videos' para armazenar o que representaria a aba "vídeos" do canal e a acessei.

- Criei uma variável 'ultimo_postado' para armazenar o que representaria o último vídeo postado no canal e o acessei.

- Criei uma variável 'quantidade_views' para armazenar a quantidade de visualizações do vídeo e uma variável 'views_texto' que, 
  formata essa informação para String.

- Criei uma variável 'expandir_descricao' para armazenar o botão responsável por mostrar a descrição completa do vídeo e realizei um click nele.

- Criei uma variável 'descricao' para armazenar a descrição do vídeo e, uma variável 'descricao_text' que, formata essa informação para String.

- Criei uma variável 'hashtags' que, busca apenas pelas TAGS no texto formatado.

- Criei uma variável 'abrir_transcricao' responsável por acionar o botão "Mostrar Transcrição".

- Criei uma variável 'transcricao' para armazenar a transcrição do vídeo e, 'transcricao_text' para formatar para String.

- Criei uma variável 'transcricao_sem_horarios' que retira todas as informações de período da transcrição formatada.

- Criei uma variável 'texto_concatenado' que, realiza a organização do texto por extenso.

- Por fim, todas as informações solicitadas são impressas para o usuário (quantidade de visualizações, tags e transcrição do vídeo).

- Encerrada a janela.

:)