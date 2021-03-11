from app import app
from flask import request, jsonify, make_response
from app.models import tables
from app import db

@app.route("/index")
@app.route("/")
def index():
    return "Hello World"

@app.route('/sign_up', methods=['POST'])
def sign_up():
    content = request.json
    user = tables.User.query.filter_by(email= content['email']).first()
    if user is not None:
        return make_response(jsonify({"mensagem": "Usuário cadastrado. Verifique os dados!!"}),400)
    new_user = tables.User(content['username'], content['password'],content['name'],content['email'])
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({"mensagem": "Cadastro realizado com sucesso!!"}),201)

@app.route('/sign_in', methods=['POST'])
def sign_in():
    content = request.json
    user = tables.User.query.filter_by(email= content['email']).first_or_404()
    return make_response(jsonify({"token":""}), 200)

@app.route("/test", defaults= {'name': None})
@app.route("/test/<name>")
def test(name):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá, user!"

@app.route('/tests/<int:id>', methods=['GET'])
def tests(id):
    return "%s" % str(type(id))