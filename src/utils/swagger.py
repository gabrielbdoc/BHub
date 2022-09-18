REDOCS_PATH = "http://localhost:8181/bhub/apis/redoc"
SWAGGER_PATH = "http://localhost:8181/bhub/apis"
GITHUB_PATH = "https://github.com/gabrielbdoc/"
ASYNCH_PATH = "https://docs.python.org/3/library/asyncio.html"
FASTAPI_PATH = "https://fastapi.tiangolo.com/"
SQLALCHEMY_PATH = "https://www.sqlalchemy.org/"
DOCKER_PATH = "https://docs.docker.com/"
POSTGRES_PATH = "https://www.postgresql.org/"
DATABASE_IMG = "http://localhost:8181/bhub/api/images/database"
LINKEDIN_PATH = "https://www.linkedin.com/in/gabriel-barrocas-de-oliveira-cruz-140b9697/"


MARKDOWN_DESCRIPTION = f"""
<a href={REDOCS_PATH}><font size="-1">/bhub/apis/redoc</font><a /><br />
<a href={SWAGGER_PATH}><font size="-1">/bhub/apis</font><a /><br />
<a href={GITHUB_PATH}>GitHub<a /><br />
<a href={LINKEDIN_PATH}>LinkedIn<a /><br />
<p>A presente documentação detalha a API desenvolvida para o desafio de Analista de Desenvolvimento BHub.<p />

### Tecnologias utilizadas:
* Python 3.10
* <a href={FASTAPI_PATH}>FastAPI<a />
* <a href={ASYNCH_PATH}>AsyncIO<a />
* <a href={SQLALCHEMY_PATH}>SQLAlchemy<a />
* <a href={DOCKER_PATH}>Docker<a />
* <a href={POSTGRES_PATH}>Postgres<a />


## Proposta:
<p>Desenvolver uma api CRUD simples para controle de dados dos clientes BHub. 

### Estratégia:
Por estratégia de negócio foi escolhido o banco relacional POSTGRES para criação da base de dados, e nela criadas duas
tabelas, uma para dados cadastrais dos clientes, outra para dados bancários. A chave de id do usuário (única) foi 
empregada como chave estrangeira para relacionar as tabelas, apresentadas a seguir. O banco foi criado em um 
docker-container para simplificar o ambiente de desenvolvimento.
<p><img src={DATABASE_IMG} alt='database'>
<p>Foram desenvolvidos routers distintos para as rotas, sendo um grupo para tratativa dos dados de cadastro 
e outra para dados bancários.
"""
