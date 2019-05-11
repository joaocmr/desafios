<b>SOBRE O PROJETO</b>

O projeto tem como objetivo desenvolver um bot do telegram que realiza crawl do web-site reddit.<br>Através do comando /NadaPraFazer subreddit1;subreddit2 o bot pega as threads <br> dos subreddits informados com mais de 5000 upvotes (quantidade definida por variável de ambiente), e <br>os informa a pessoa que o solicitou

<b>RODANDO O PROJETO</b>

O projeto utilizar docker para instalação de dependências e configurações das variáveis de ambiente.<br>
Ao rodar o comando docker-compose up --build é levantado o container com nome de "crawler".<br>
Dessa forma, após o container ser levantado, ao acessar o bot do telegram com nome "desafio_idwall_bot", disponível em telegram.me/desafio_idwall_bot, e utilizar o comando /NadaPraFazer subreddit1;subreddit2;subreddit3 o bot responde com as top threads dos subreddits solicitados.<br>

Para rodar os testes do projeto basta entrar no container e rodar o shell script ./test.sh
