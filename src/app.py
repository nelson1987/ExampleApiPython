from flask import Flask, jsonify, request
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Estudar Python',
        'description': 'Estudar Python para melhorar minhas habilidades de programação.',
        'done': False
    },
    {
        'id': 2,
        'title': 'Fazer compras',
        'description': 'Comprar leite, queijo, pão, e ovos.',
        'done': False
    }
]

SWAGGER_URL = '/api/docs'  # URL da página do Swagger UI
API_URL = '/swagger'  # URL do JSON da especificação Swagger

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
            'app_name': "Web API RESTful em Python com Flask"
    }
)

# Registra o blueprint do Swagger UI na aplicação
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/swagger')
def api_swagger():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Web API RESTful em Python com Flask"
    return jsonify(swag)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Obtém todas as tarefas.
    ---
    tags:
      - tarefas
    responses:
      200:
        description: Lista de todas as tarefas.
        schema:
          type: array
        #   items:
        #     $ref: '#/tasks'
      401:
        description: Não autorizado.
    """
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """
    Obtém a tarefa por id.
    ---
    tags:
      - tarefas
    responses:
      200:
        description: Consultar tarefa.
        schema:
          type: array
        #   items:
        #     $ref: '#/tasks'
      401:
        description: Não autorizado.
    """
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
