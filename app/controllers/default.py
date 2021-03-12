from app import app
from flask import request, jsonify, make_response
from app.models import tables
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from markupsafe import escape


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'mensagem': 'É necessário um token válido.'}), 401

        try:
            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms="HS256")
            current_user = tables.User.query.filter_by(
                email=data['email']).first_or_404()
        except:
            return jsonify({'mensagem': 'Token inválido.'}), 401

        user = {'id': current_user.id, 'name': current_user.name,
                'username': current_user.username, 'email': current_user.email}
        return f(current_user, *args)
    return decorator


def token_refresh(user):
    token = jwt.encode(
        {
            "id": user.id,
            "name": user.name,
            'email': user.email,
            'username': user.username,
            'exp': datetime.datetime.now() + datetime.timedelta(hours=10)
        },
        app.config['SECRET_KEY'],
        algorithm="HS256"
    )
    return token


@app.route("/index")
@app.route("/")
def index():
    return "Bem-vindo a API"


@app.route('/sign_up', methods=['POST'])
def sign_up():
    content = request.json
    user = tables.User.query.filter_by(email=content['email']).first()
    if user is not None:
        return make_response(jsonify({"mensagem": "Usuário cadastrado. Verifique os dados!!"}), 400)
    new_user = tables.User(
        content['username'],
        generate_password_hash(content['password'], method='sha256'),
        content['name'],
        content['email']
    )
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({"mensagem": "Cadastro realizado com sucesso!!"}), 201)


@app.route('/sign_in', methods=['POST'])
def sign_in():
    content = request.json
    user = tables.User.query.filter_by(email=content['email']).first_or_404()
    if user is None or not check_password_hash(user.password, content['password']):
        return make_response(jsonify({"mensagem": "Dados inválidos!!. Verifique seu e-mail ou senha!!"}), 400)
    token = token_refresh(user)
    return make_response(jsonify({"token": token}), 200)

@app.route('/refresh_token', methods=['GET'])
@token_required
def refresh_token(user):
    user = tables.User.query.filter_by(id= user.id).first_or_404()
    token = token_refresh(user)
    return make_response(jsonify({"token": token}), 200)

@app.route('/post', methods=['GET'])
@token_required
def get_all_post(user):
    posts = tables.Post.query.all()
    if len(posts) == 0:
        return make_response(jsonify({"mensagem": "Não existe posts cadastrados."}), 200)
    return make_response(jsonify(posts=[p.serialize for p in posts]), 200)

@app.route('/post', methods=['POST'])
@token_required
def creat_post(user):
    data = request.json
    post = tables.Post(data['content'], user.id)
    db.session.add(post)
    db.session.commit()
    return make_response(jsonify({"mensagem": "Post realizado com sucesso!!"}), 201)


@app.route('/post', methods=['PUT'])
@token_required
def update_post(user):
    data = request.json
    post = tables.Post.query.filter_by(id=data['id']).first_or_404()
    post.content = data['content']
    db.session.add(post)
    db.session.commit()
    return make_response(jsonify({"mensagem": "Post atualizado com sucesso!!"}), 200)


@app.route('/post', methods=['DELETE'])
@token_required
def delete_post(user):
    data = request.json
    post = tables.Post.query.filter_by(id=data['id']).first_or_404()
    db.session.delete(post)
    db.session.commit()
    return make_response(jsonify({"mensagem": "Post deletado com sucesso!!"}), 200)

# @app.route("/test", defaults={'name': None}, methods=['GET'])
# @app.route("/test/<name>")
# def test( name):
#     if name:
#         return "Olá, %s!" % name
#     else:
#         return "Olá, user!"


# @app.route("/tests", methods=['GET'])
# @token_required
# def tests(user):
#     content = request.json
#     print(content['id'])
#     return "ok"
