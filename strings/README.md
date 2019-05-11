<b>SOBRE O PROJETO</b>

Este projeto tem como objetivo a formatação de um texto.<br>

Através de um script, um texto sem formatação é manipulado de forma que suas linhas tenham no <br>máximo X palavras (quantidade definida como argumento do script) e seja justificado ou não <br>(parêmetro também definido através de argumento)<br>

<b>RODANDO O PROJETO</b>

O projeto utiliza docker para instalção de dependências<br>
Ao rodar o comando docker-compose up --build é leventando o container do projeto com nome de "formater".<br> 
Entrando nesse container através do comando docker exec -it <id_do_container> bash é possível utilizar o script e rodar os testes do projeto.<br>

O script deve ser rodado da seguinte forma:<br>
python scripts/format_text.py <caminho_para_o_txt> <quantidade_de_palavras_por_linha> <justificado_ou_nao(0 ou 1)>

Dessa forma, é gerado o arquivo de output dentro da pasta ./data/output<br>

Para rodar os testes, basta rodar o shell script ./test.sh de dentro do container
