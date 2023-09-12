# GERPRO Gerenciador de projetos

GERPRO é uma ferramenta desenvolvida para auxiliar na gestão de projetos.

## Features

- Permite criar e deletar projetos;
- Considera os campos de nome do projeto, descrição resumida, datas de início e fim estimado do projeto, Gerente resonsável, status atual e categoria;
- Lista os projetos por ordem de cadastro, para permitir o acompanhamento individualizado;

## Tecnologias utilizadas

- Python: Linguagem de programação utilizada no back-end;
- Flask: Framework web para construção da aplicação;
- SQLAlchemy: Biblioteca de Object-Relational Mapping (ORM);
- OpenAPI: Para escrever, produzir, consumir e visualizar serviços da API;
- HTML: Linguagem de markup do front-end;
- Bootstrap: Framework que fornece estruturas de CSS para criação de aplicações front-end;
- Javascript: Linguagem de programação de comportamento que permite a criação de conteúdo dinâmico;
- SQLite: Banco de dados utilizado para persistência dos dados;

## Instalação

Instruções para instalação abaixo, considero que o Python versão 3 está devidamente instalado e que o módulo pip e virtualenv estão configurados.

Após download dos arquivos do projeto, pode-se executar o arquivo "run.sh" em ambientes Linux e MacOS ou "run.bat" em ambientes Windows, que será responsável pela (1) criação e (2) ativação do ambiente virtual, (3) instalação do módulos Python necessários para execução do projeto, (4) uma primeira carga no banco de dados com exemplos de projeto e tabelas de apoio e a (5) execução do flask em localhost.

### Ambientes Linux/MacOS

Para executar o arquivo .sh no Linux, precisamos transformá-lo em um executável, esse passo pode ser realizado de duas maneira:

- Via interface gráfica, clicando com o botão direito no arquivo e marcando como "Executable as Program", em ambientes Debian com Gnome.

- Via terminal, acessando o diretório do arquivo e executando o comando de chmod, que modifica as permissões do arquivo. Atenção, o comando chmod +770 libera acesso de leitura, escrita e execução para todos os usuários e grupos com acesso ao arquivo.

```bash
chmod +770 run.sh
```

Caso não seja possível utilizar o script, podemos executar individualmente as linhas de configuração abaixo na sequencia que aparecem no detalhe abaixo, considerando um terminal aberto dentro do diretório "api".

``` bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python3 db_init.py
flask run --host 0.0.0.0 --port 5000 --reload
```

### Ambientes Windows

Para executar o arquivo "run.bat" basta clicar duas vezes para executar e aceitar os prompts de execução e acesso a rede.

Caso não seja possível utilizar o script, podemos executar individualmente as linhas de configuração abaixo na sequencia que aparecem no detalhe abaixo, considerando uma tela de comando aberta dentro da pasta "api".

``` cmd
python -m venv env
call env\Scripts\activate
pip install -r requirements.txt
python3 db_init.py
flask run --host 0.0.0.0 --port 5000 --reload
```

## Utilização

Após execução dos passos de configuração e inicalização do serviço, basta executar o arquivo "index.html" dentro do diretório "front".

### Para listar os projetos

1. Os projetos são listados por padrão na tela inicial, em formato de tabela e ordenados pela data de criação;

### Para inserir novo projeto

![Alt text](image-1.png)

1. Clicar no botão "Novo" para mostrar o formulário de cadastro de novos projetos;

2. Registrar as informações do projeto:
- Projeto: Nome do projeto, com até 100 caracteres;
- Descrição: Descrição resumida do projeto, com até 4000 caracteres;
- Início: Data de início do projeto, formato DD/MM/YYYY;
- Fim: Data estimada de finalização do projeto, formato DD/MM/YYYY;
- Categoria: Caixa de seleção, considerar observação abaixo;
- Gerente do projeto: Caixa de seleção, considerar observação abaixo;
- Status: Caixa de seleção, considerar observação abaixo;

```
Observação: O script de inicialização executa um arquivo python db_init.py que insere alguns registros de exemplo nas tabelas de apoio que populam as caixas de seleção. Caso o script não seja executado, faz-se necessário a inserção manual de registros nas tabelas de Categoria, Gerente e Status para que as caixas de seleção sejam preenchidas.
```

3. Clicar no botão "Adicionar" para incluir esse registro no banco de dados;

4. O registro deve aparecer na tabela abaixo do formulário;

### Para deletar um projeto

![Alt text](image-2.png)

1. Identificar a linha que precisa ser excluída;

2. Clicar no botão "Del" referente a linha;

3. Confirmar a ação na mensagem de alerta;

4. O registro foi excluído no banco de dados e não deve aparecer na tabela após a atualização automática da tela;