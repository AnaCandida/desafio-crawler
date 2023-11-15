# Welcome to desafio-crawler 👋
[![Python Version](https://img.shields.io/badge/python-3.11-blue)](#)
[![Scrapy Version](https://img.shields.io/badge/Scrapy-2.11.0-blue)](#)
[![PostgreSQL Version](https://img.shields.io/badge/PostgreSQL-13-blue)](https://www.postgresql.org/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

Este é um projeto de raspagem de dados para o site IMDB, usando a biblioteca Scrapy.
Ele foi construído a partir das orientações do desafio da  [beeMôn](https://github.com/beemontech/desafio-crawler#beem%C3%B4n) 🐝

O MVP + funcionalidades adicionais do desafio implementadas:

- Buscar dados de forma automatizada(script de linha de comando ou interface clicavel) ✅
- Padronizar os retornos de forma estruturada (json/csv) ✅
- Sistema de logs de para acompanhamento da execução ✅
- Ter um prova da consulta (Screenshot)  ✅
- Armazenamento dos resultados em um banco relacional ou não relacional ✅
- Fazer um dataframe que possibilite visualizar os resultados via pandas ✅
- Trazer resultados de forma dinamica sem fixar caminhos no xpath  ✅
- Dockerizar a aplicação ✅
- Conseguir agendar uma execução para um dia e horario. ✅

### Tecnologias Utilizadas

- [Poetry](https://python-poetry.org/) (v1.1.12)
- [Python](https://www.python.org/) (v3.11.*)
- [Scrapy](https://scrapy.org/) (v2.11.0)
- [scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) (v0.0.33)
- [schendule](https://schedule.readthedocs.io/en/stable/#) (1.2.1)
- [pandas](https://pandas.pydata.org/) (^2.1.3)
- [sqlalchemy](https://www.sqlalchemy.org/) (^2.0.23)

## Executando o projeto:
  >  **Nota:**  Certifique-se de ter o Docker e o Docker Compose instalados.Veja a [documentação](https://docs.docker.com/get-docker/), caso ainda não os tenha instalado.

1. Clone o repositório:

    ```bash
    git clone https://github.com/AnaCandida/desafio-crawler.git
    ```

2. Navegue até a pasta do projeto e execute:

    ```bash
    docker-compose up -d --build  OU docker compose up -d --build
    ```


## Execução e Agendamento do IMDB Spider

### Agendamento(default):
Por padrão, o container executará automaticamente o script para agendamento do spider.
Ele permitirá que você escolha o dia da semana e a hora para o agendamento.

>  **Nota:** Para manter o agendamento ativo, é crucial manter o script em execução. Caso o script seja encerrado, o agendamento será perdido.
>Isso inclui reinicializações do container. A implementação dessa persistência pode ser considerada como uma funcionalidade futura.


### Se preferir rodar o spider uma única vez, utilize o seguinte comando:

```
docker-compose run scrapy_service run_once

```



## Detalhes sobre as implementações 📚:

Este projeto proporcionou uma imersão mais aprofundada nos conceitos de web scraping, oferecendo um entendimento abrangente da biblioteca Scrapy, bem como sua integração eficaz com a biblioteca scrapy_playwright.

Implementações Realizadas:

- Middleware customizado para rotação de user-agent e ajudar a evitar bloqueios
- Pipeline customizada para integração com banco de dados Postgres
- Salvamento em lote no banco de dados para melhorar performance
- Metodo para evitar o carregamento de recursos desnecessários, como imagens e solicitações POST, otimizando assim a performance
- Agendamento interativo do usuario via terminal




## Author

👩🏻‍💻 **Ana Cândida Pereira de Quadros**

* Github: [@AnaCandida](https://github.com/AnaCandida)
* LinkedIn: [@https:\/\/www.linkedin.com\/in\/anacandidaquadros\/](https://linkedin.com/in/https:\/\/www.linkedin.com\/in\/anacandidaquadros\/)

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).