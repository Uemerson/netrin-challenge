# Sobre o desafio da Netrin:

O desafio consiste em criar uma API REST em python, usando flask, que realiza consultas no google.com e faz o web scraping dos cinco primeiros links que são retornados na consulta. Além disso, é preciso ter uma rota de métricas que deve retornar o tempo médio das requisições feitas e todas os textos buscados, não é permitido utilizar nenhum banco de dados.

# Sobre o projeto

O projeto segue a Clean Architecture para distribuir as responsabilidades em diferentes camadas, mantendo a aderência aos princípios do SOLID. Além disso, foram aplicados Design Patterns sempre que necessário para solucionar problemas comuns.

# Design partners

- Factory
- Adapter
- Composite
- Decorator
- Proxy
- Dependency Injection

# O que é preciso para rodar o projeto ?

Para rodar o projeto é necessário ter instalado o docker e o docker-compose, os scripts de automação (como por exemplo [up.dev.sh](../up.dev.sh)) funcionam somente em sistemas operacionais com suporte a bash script.

# Como rodar o projeto ?

Primeiro é preciso criar um arquivo .env.dev na pasta raiz do projeto, existe o arquivo [.env.dev.example](../.env.dev.example) que contém os exemplos de valores para as váriaveis de ambientes necessárias para rodar o projeto em ambiente de desenvolvimento.

Após isso, basta rodar o script em `bash` denominado [up.dev.sh](../up.dev.sh) e o projeto irá subir em ambiente de desenvolvimento:

```
$ bash up.dev.sh
```

Caso seu sistema operacional não rode bash script basta rodar o comando no diretório raiz do projeto:

```
$ docker-compose -f docker-compose.dev.yml --env-file .env.dev up -d --build --remove-orphans
```

# Endpoints

Conforme o desafio foram criados dois endpoints.

Endpoint que retorna a lista dos cinco links:

```
[GET] http://{{host}}:{{port}}/api/scraper?q={{texto}}

query params:
q: o texto a ser buscado
```

Endpoint que retorna as métricas de utilização:

```
[GET] http://{{host}}:{{port}}/api/metrics
```

Para testes substitua os valores `{{host}}`, `{{port}}` de acordo com que a API está utilizando. O `{{texto}}` pode ser preenchido com qualquer texto.
