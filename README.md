# Web API RESTful em Python com Flask

Este é um projeto de exemplo para uma Web API RESTful em Python com Flask.

## Descrição

A Web API permite gerenciar uma lista de tarefas. A lista pode ser visualizada, adicionada, atualizada e excluída por meio de solicitações HTTP.

## Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET    | /tasks   | Obtém todas as tarefas. |
| GET    | /tasks/:id | Obtém uma tarefa específica. |
| POST   | /tasks   | Cria uma nova tarefa. |
| PUT    | /tasks/:id | Atualiza uma tarefa existente. |
| DELETE | /tasks/:id | Exclui uma tarefa existente. |

## Requisitos

- Python 3.x
- Flask
- Flask-RESTful

## Instalação

1. Clone este repositório.
2. Instale as dependências do projeto com o comando `pip install -r requirements.txt`.
3. Execute o arquivo `app.py`.
4. Em caso de dúvida. Leia o artigo: https://www.alura.com.br/artigos/ambientes-virtuais-em-python?gclid=Cj0KCQjw27mhBhC9ARIsAIFsETEYzR5GXvE9l4XP0Bub9j6AkGceGg4Gqwp2s0d12xJ5uQtGahWVN9kaAgAPEALw_wcB

## Documentação

A documentação da API pode ser encontrada em [http://localhost:5000/api/docs](http://localhost:5000/api/docs). A documentação foi criada com o Swagger.

## Exemplo de solicitação

### Obtendo todas as tarefas

`GET /tasks`

### Resposta
~~~json
[
    {
        "id": 1,
        "title": "Comprar leite",
        "description": "Comprar leite no supermercado.",
        "done": false
    },
    {
        "id": 2,
        "title": "Estudar Python",
        "description": "Estudar Python por 1 hora.",
        "done": true
    }
]
~~~

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.
