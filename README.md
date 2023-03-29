# Web API RESTful em Python com Flask

Este projeto é uma API que permite aos usuários criar, ler, atualizar e excluir tarefas em uma lista. Ele foi criado usando Python e Flask.

## Instalação

Para executar este projeto, você precisa ter o Python e o Flask instalados em seu computador. Para instalar o Flask, execute o seguinte comando:
```
pip install flask
```
## Executando a API

Para executar a API, execute o seguinte comando no terminal:
```
python app.py
```
Isso iniciará a API na porta 5000. Você pode acessá-la usando a seguinte URL:
```
http://localhost:5000
```
## Rotas

A API tem as seguintes rotas:

- `GET /tasks`: retorna uma lista de todas as tarefas.
- `GET /tasks/<int:task_id>`: retorna uma tarefa específica com o ID fornecido.
- `POST /tasks`: cria uma nova tarefa com base nos dados fornecidos no corpo da solicitação.
- `PUT /tasks/<int:task_id>`: atualiza uma tarefa existente com base nos dados fornecidos no corpo da solicitação.
- `DELETE /tasks/<int:task_id>`: exclui uma tarefa existente com base no ID fornecido.

## Exemplo de solicitação

Aqui está um exemplo de como criar uma nova tarefa usando a API:
```
POST /tasks
{
"title": "Estudar Flask",
"description": "Estudar Flask para melhorar minhas habilidades de desenvolvimento web."
}
```
Isso criará uma nova tarefa com o título "Estudar Flask" e a descrição "Estudar Flask para melhorar minhas habilidades de desenvolvimento web." O ID da tarefa será gerado automaticamente.

## Contribuindo

Se você quiser contribuir com este projeto, sinta-se à vontade para enviar um pull request. Toda contribuição é bem-vinda!

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para obter mais informações.
