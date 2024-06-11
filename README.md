# LexLink
Somos a LexLink, uma plataforma que oferece soluções inovadoras para análises de processos jurídicos, permitindo aos usuários carregar documentos em formato PDF para receber insights valiosos sobre seus casos. Com opções de análise detalhada, sucinta e parcial, adaptamos nossa avaliação às necessidades específicas de cada cliente, utilizando inteligência artificial avançada para fornecer análises precisas e personalizadas. Essa abordagem facilita a compreensão dos aspectos críticos dos processos, otimizando a tomada de decisão jurídica e estratégica.

## Requisitos para a execução do código:
Python 3 instalado na máquina que deseja-se executar, Docker e um navegador.

## Como executar o código:
Existem duas opções: utilizando o Makefile ou por meio de comandos diretos. <br/> 
Caso a preferência seja o uso da Makefile, a aplicação será executada em três comandos: <br/>"make create-env", em que um ambiente virtual (visando a compartimentalização das bibliotecas e pacotes);<br/> "make activate-env", que permitirá o uso do ambiente virtual, em que as instalações de pacotes e bibliotecas serão feitas lá, e não na máquina local;<br/> E por fim "make install-app", onde o arquivo install.py será executado. Esse arquivo possui todas as instruções necessárias para que a aplicação seja executada por completo.
<hr>
A segunda opção envolve o uso dos comandos diretos, que são os mesmos que a Makefile executará. São esses: "python -m venv env", "env\Scripts\activate" e "python install.py". A execução desses comandos possui a mesma lógica de executá-los por meio da Makefile.

## Utilizando o Metabase
Para ver o Metabase sendo executado, basta entrar no link "localhost:3000", e a conexão ao banco de dados é feita por meio das credenciais contidas no arquivo "config/constants.py". As queries para a visualização dos dados estão contidas em "QueriesMetabase.txt". <br/>Para usar as queries, um dashboard pode ser criado, visando o armazenamento prático das consultas. Após criá-lo, consultas SQL serão criadas e utilizadas, bastando copiá-las do arquivo e colá-las.
