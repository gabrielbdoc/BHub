# Desafio BHub

Projeto desenvolvido como desafio de Analista de Desenvolvimento.
O objetivo é desenvolver uma api CRUD simples para controle de dados dos clientes BHub.

## Estratégia

Por estratégia de negócio foi escolhido o banco relacional POSTGRES para criação da base de dados, e nela criadas duas tabelas, uma para dados cadastrais dos clientes, outra para dados bancários. A chave de id do usuário (única) foi empregada como chave estrangeira para relacionar as tabelas, apresentadas a seguir. O banco foi criado em um docker-container para simplificar o ambiente de desenvolvimento.

![alt text](/src/utils/images/database.png)

Foram desenvolvidos routers distintos para as rotas, sendo um grupo para tratativa dos dados de cadastro e outro para dados bancários.

O swagger do serviço se encontra [aqui](http://localhost:8181/bhub/apis).

## Features
- [x] Cadastro de novos usuários;
- [x] Listagem de dados cadastrais de um usuário;
- [x] Listagem de dados cadastrais de todos os usuários;
- [x] Atualização dos dados cadastrais de um usuário;
- [x] Desativação de um usuário;
- [x] Cadastro de dados bancários para um usuário;
- [x] Listagem de usuários para um banco específico;
- [x] Desativação dos dados bancários de um usuário.

## Dependências

* Python 3.10 e Pipenv


### Preparando o ambiente:

O primeiro passo para executar o ambiente será configurar o ambiente de desenvolvimento, executando as dependências necessárias.
Isso pode ser feito configurando o ambiente virtual (venv) com o interpretador Python e executando os seguintes comandos:

```bash
pip install pipenv
```
```bash
pipenv install
```
Em seguida, deve-se inicializar o container da base de dados.
```bash
docker-compose up
```
Depois disso, inicializar a database em 'src/database/init_db.py'

Por fim, subir a API em 'src/app.py'

**Obs: As variáveis de ambiente se encontram no arquivo .env. Sugere-se o uso do plugin EnvFile para facilitação.**
