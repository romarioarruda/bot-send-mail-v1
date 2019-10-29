# robos - automatizador de tarefas

O arquivo robo1.py é automatizador de buscas, ele executa uma pesquisa no site 
registro.br, pega o resultado e escreve em arquivo quais os dominios disponiveis e não disponiveis.

O arquivo robo2.py, simula um usuário acessando o gmail, ele acessa a conta, envia um e-mail pra 
um destino e após o envio, desloga da conta e fecha o navegador.

Os arquivos .sh são apenas um executável desses dois arquivos python.

Pra executar essas tarefas, usei o selenium pra manipular o navegador chrome.

Pra instalar o selenium basta executar no terminal o comando: 

> pip3 install selenium

pip3 por que estou usando o python versão 3

Além disso, precisa do driver do chrome pra poder rodar no chrome obviamente.
Pra isso, baixe o binário de acordo com sua versão do chrome .

Link pra download: 

> https://chromedriver.chromium.org/downloads

Link para a documentação do Python Selenium
> https://selenium-python.readthedocs.io
