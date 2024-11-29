# Sistema de adoção de pets - PETMATCH
Esse projeto foi fruto da disciplina de Gerência de Projetos da Universidade Estadual da Paraíba.
A premissa do projeto é criar uma ponte entre ONGs para pets e possíveis donos que procuram um(a) companheiro!

## Ferramentas necessárias para rodar o projeto
- [MySql 8.x.x](https://dev.mysql.com/downloads/mysql/) ou superior.
- [Python 3.11](https://www.python.org/downloads/) ou superior.
- [MySQL WorkBench 8.0 CE](https://dev.mysql.com/downloads/workbench/).

# Quick Start
Para conseguir rodar o sistema, existe uma base de dados já alimentada para que você possa explorar (está dentro de um arquivo .zip), isso facilitara a apresentação do sistema.

## Por onde começo?
1. Depois que você tiver baixado as ferramentas necessárias, faça download dos arquivos do repositório.
2. Abra os arquivos na IDE de sua preferência.
3. Há um arquivo requirements.txt que possui todas as bibliotecas utilizadas nesse projeto, para instalar rode o comando:
4. Após isso, abra o seu MySQL Configurator e siga os passos do programa.
5. Depois de configurar o ambiente, procure nos arquivos baixados do repositório o app.py e substitua a linha "app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/PetMatch' "
