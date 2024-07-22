<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Entregáveis</h3>

  <p align="center">
    Descrição dos Artefatos - documentos e diagramas
  </p>
</div>

<br>
<p align="justify">
&ensp;&ensp;&ensp;&ensp;Este diretório contém os documentos e diagramas. Para acessá-los, confira a pasta 'arquivos/'. <br>

Segue abaixo uma descrição sobre cada um deles.
</p>

## Listagem e Descrição

<p align="center">
  <img src="../imgs/entregaveis.png" >
</p>


### Artefato 1: Documentação da API
<p align="justify">
&ensp;&ensp;&ensp;&ensp;A Documentação da API foi feita utilizando o padrão OpenAPI, utilizando o <a href="https://editor.swagger.io/" target="_blank"> Editor Swagger</a>. Ele detalha cada um dos endpoints, trazendo o schema do payload eseprado, códigos e mensagens de erros possíveis, bem como exemplos de inputs.
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp;Para facilitar, foi criado <a href="https://github.com/bastoska/workload-api-docs" target="_blank">este outro repositório</a> e configurado para hospedar a documentação. Basta clicar <a href="https://bastoska.github.io/workload-api-docs" target="_blank">neste link</a> que você será levado diretamente para o swagger.
</p>

<p align="justify">
&ensp;&ensp;&ensp;&ensp;Aqui no diretório, a documentação está em formato .yaml, no arquivo openapi.yaml
</p>


### Artefato 2: Arquitetura da API

<p align="justify">
&ensp;&ensp;&ensp;&ensp;O diagrama mostra como o usuário se autentica e se comunica com a API, bem como o acesso da API a recursos do Google Cloud. Além disso, ele traz os respectivos recursos no GCP que serão utilizados no projeto.
</p>

### Artefato 3: Camadas de Arquitetura de Governança

<p align="justify">
&ensp;&ensp;&ensp;&ensp;O Diagrama apresenta as camadas de Segurança, Acesso e Auditoria e seu relacionamento com a API.
</p>

### Artefato 4: Documentação de Políticas

<p align="justify">
&ensp;&ensp;&ensp;&ensp;Nesta entrega há três documentos:
</p>

- **Artefato 4a**: Políticas de Segurança: lista as políticas de segurança a nível de Proteção de Dados, Segurança de Rede e Controle de Acesso;
- **Artefato 4b**: detalha o controle de acesso à API, trazendo os cargos e funções;
- **Artefato 4c**: versa sobre as políticas e procedimentos de auditoria.

### Artefato 5: IAM no GCP
<p align="justify">
&ensp;&ensp;&ensp;&ensp;O Cloud IAM apresenta duversas políticas que suporta a política definida no projeto. O artefato apresenta políticas de RBAC, COntrole de acesso baseado em recursos e permissões com condicionais.
</p>

### Artefato 6: Código Fonte do Protótipo
<p align="justify">
&ensp;&ensp;&ensp;&ensp;O Código fonte se encontra na pasta `/src/workload-api/` aqui neste repositório.
</p>

### Artefato 7: Testes Unitários e de Integração
<p align="justify">
&ensp;&ensp;&ensp;&ensp;O Código fonte se encontra na pasta `/src/workload-api/tests`. Foram testados testes para os endpoints criação, listagem e deleção.
</p>

### Artefato 8: 