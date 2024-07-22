        <a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">API para Gerenciamento de Workloads no Google Cloud</h3>

  <p align="center">
    Protótipo que simula a criação de contagem de palavras de um dataset do BigQuery
  </p>
</div>

<br>
<p align="justify">
&ensp;&ensp;&ensp;&ensp;Este repositório contém os códigos de um protótipo de API em FastAPI para provisionar um workload em Spark para contagem de palavras de um dataset do BigQuery.
</p>

<br>

<!-- ABOUT THE PROJECT -->
## Sobre o Projeto

<p align="justify">
&ensp;&ensp;&ensp;&ensp;Visando realizar testes iniciais com gerenciamento de worklaods de dados por meio de uma API, optou-se por desenvolver este protótipi. Por enquanto há apenas endpoints que simulam interações com o usuário para a criação de workloads.
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp;Para finalidade de testes, está sendo usado o TinyDB como banco de dados backend, permitindo salvar os workloads em disco.
</p>


## Requisitos

Segue abaixo as principais tecnologias e libs utilizadas, juntamente com suas versões.

- <a href="https://www.python.org/" target="_blank">Python 3.11</a>
- <a href="https://fastapi.tiangolo.com/" target="_blank">FastAPI 0.111.1</a>
- <a href="https://docs.pytest.org/en/8.2.x/contents.html" target="_blank">PyTest</a>
- <a href="https://www.docker.com/" target="_blank">Docker</a> (apenas se você for executar com o Docker)


<p align="justify">
&ensp;&ensp;&ensp;&ensp;Para as demais dependências, confira <a href="https://github.com/bastoska/plataforma-dados-api/blob/main/src/workload-api/requirements.txt">este requirements</a>.
</p>

## Reprodução

<p align="justify">
&ensp;&ensp;&ensp;&ensp;Para subir a API, deixamos aqui duas opções:
</p>

1. Python via terminal
2. Docker

<p align="justify">
&ensp;&ensp;&ensp;&ensp;AS duas opção serão detalhadas a seguir. Um detalhe é que todos os comandos listados abaixo são referente a comandos em terminal bash. Caso você utilize Windows, é importante que recorra ao WSL ou use os respectivos comandos do SO, se for o caso.
</p>

### Execução com Python via terminal


1. Clone este repositório

    Clone o repositório e entre na pasta:
    ```sh
    git https://github.com/bastoska/plataforma-dados-api.git

    cd plataforma-dados-api/
    ```
2. Configuração do Ambiente
  
    Antes de iniciar, é necessário ter o Python instalado. Caso você não tenha, você pode seguir as instruções deste <a href="https://www.python.org/downloads/">link</a>.

    Uma vez Python esteja instalado na máquina, é necessário criar um ambiente virtual para instalar as dependências de forma isolada:

    ```sh
    python3 -m virtualenv env
    source env/bin/activate
    ```

    Em seguida, entre no diretório de códigos:
    ```sh
    cd src/workload-api
    ```

3. Instale as dependências

    ```sh
    pip install -r requirements.txt
    ```

4. Execute a API

    O Código abaixo expõe a API na porta 8080. Caso ela já esteja sendo usada por alguma outra aplicação, basta alterá-la antes de executar.
    ```sh
    uvicorn app.app:app --host 0.0.0.0 --port 8080
    ```

5. Interação com a API

    Acesse este endereço no navegador:

    ``sh
    http://localhost:8080/
    ```

    O comando acima acessa a rota raiz '/' da API e, se tudo deu certo, mostrará a mensagem `{"message":"Running.."}`.

    O FastAPI gera automaticamente uma documentação da API. Para acessá-la, basta inserir o seguinte endereço no navegador: 

    ``sh
    http://localhost:8080/docs
    ```

6. Execução dos testes

    Foi utilizado o PyTest com httpx para realizar os testes. Para executá-los, basta executar o seguinte comando no terminal:

    ```sh
    pytest
    ```

    Este comando executa os testes presentes em `stc/workload-api/tests/`


7. Cancelando a Execução
   
   Para encerrar a execução da API, basta fechar o terminal ou digitar control+C.


### Execução via Docker

Para subir a API via container é bem mais simples, basta ter o Docker instalado.

1. Instalação Docker

    Você pode seguir as instruções <a href="https://docs.docker.com/engine/install/">deste link</a> para instalar o Docker.


2. Execução da API

    Para facilitar, o script `src/workload-api/run.sh' contém funções para subir o container. Ele contém duas funções: uma para subir a API e outra para executar os testes. O script é simples e, para mais detalhes, basta dar uma olhada nos comentários nele.

    Assim, para subir a API, basta executar:

    ```sh
    bash run.sh up
    ```

    Esse comando construirá a imagem, executará o container e deixará os logs na tela.

3. Interação com a API

    Para interagir com a API, basta seguir o mesmo caminho do passo 5 do passo-a-passo anterior com o Python.

4. Execução dos testes

    Já que temos o script bash, basta executar o seguinte comando:

    ```sh
    bash run.sh test
    ```

5. Cancelando a Execução

    Para cancelar a execução, é necessário parar ou remover o container. Execute os seguintes comandos:

    ```sh

    ## se quiser apenas parar
    docker stop workload_api

    ## se quiser excluir
    docker rm -f workload_api
    ```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
