# Backend
----
## Criação da arquitetura 
- Para arquitetura foi definido alguns arquivos como padrão, a fim de tornar o entendimento dos arquvos e do funcionamento do backend mais facil. Dessa forma o backend foi divido e varios arquivos, dentro da pasta app, que serão descritos abaixo:

### db.py
- Neste código eu utilizo sqlalchemy junto com o ormar para criar as principais tabelas que serão utilizadas, além de utilizar a lib databases para criar os metadados que são fundamentais para a criação de uma tabela em um banco de dados. Neste arquivo eu crio as tabelas Historic, Warehouse e User, sendo elas responsáveis por servir partes fundamentais do frontend.
### model.py
- Neste arquivo eu crio os principais Schemas para gerenciar as interações CRUD dos dados que serão enviados para o banco de dados. Assim é criado um Schema para cada tabela criada.
### config.py
- Neste arquivo eu realizo a conexão com o banco de dados puxando a url do banco de um arquivo .env a fim de garantir a segurança do banco de dados.
### routes
- Essa pasta contém basicamente um arquivo para cada tabela contendo dentro destes arquivos todas as rotas necessárias para realizar um CRUD em cada uma dessas tabelas. Estes arquivos são denominados pelo nome_da_tabela.py

### Banco de dados
- Para o armazenamento dos dados da aplicação esta sendo utilizado um rds em postgres.

## PyJWT
- Realizar a criação do login, foi utilizado o JWT que cria web tokens e protege as rotas que serão utilizadas para só serem acessadas por um usuário autenticado. Para a implementação dessa features foi utilizado dois arquivos o jwt_beare.py e o jwt_handler.py. O jwt_handler faz a criação da autenticação e decodificação do token para um usuário atenticadao e o jwt_beare faz a verificação se aquele usuário possui o token e está autenticado.

## Diagrama do fluxo de desenvolvimento do bakcend

<img src={require('/img/Diagrama.jpg').default} width='100%'/>