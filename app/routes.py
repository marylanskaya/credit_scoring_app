from flask import jsonify, request
from loguru import logger

from app import app
from app.db import REDIS_CLIENT
from app.model import MODEL
from mock.db import BOOKS, uuid

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    REDIS_CLIENT.add_user('qwe', 'петров')
    return jsonify('pong!')


@app.route('/books', methods=['GET', "POST"])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    elif request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


@app.route('/login/auth', methods=['POST'])
def document():
    response_object = {'status': 'success'}
    response_object['user_exists'] = False
    if request.method == 'POST':
        post_data = request.get_json()
        # Todo: наверное надо сделать какую-то проверку данных на пустоту -
        # а мб не тут а на фронте
        user_hash = post_data.get('user_hash')
        if user_hash:
            user = REDIS_CLIENT.get_user(user_hash)
            if user:
                response_object['user_exists'] = True
                response_object['data'] = user
    return jsonify(response_object)


@app.route('/login/register', methods=['POST'])
def register_user():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        user_hash = post_data['user_hash']
        user = REDIS_CLIENT.get_user(user_hash)
        if user:
            user.update(post_data)
            REDIS_CLIENT.add_user(user_hash, user)
        else:
            REDIS_CLIENT.add_user(user_hash, post_data)
    return jsonify(response_object)


@app.route('/info/save', methods=['POST'])
def save_info():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        user_hash = post_data.get('user_hash')
        if user_hash:
            user = REDIS_CLIENT.get_user(user_hash)
            if user:
                user.update(post_data)
                REDIS_CLIENT.add_user(user_hash, user)
    return jsonify(response_object)


@app.route('/info/load', methods=['POST'])
def load_info():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        user_hash = post_data.get('user_hash')
        if user_hash:
            user = REDIS_CLIENT.get_user(user_hash)
            if user:
                response_object['user'] = user
    return jsonify(response_object)


@app.route('/model/predict', methods=['POST'])
def predict_score():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()['data']['user']
        user_hash = post_data.get('user_hash')
        if user_hash:
            user = REDIS_CLIENT.get_user(user_hash)
            logger.info(user)
            score = MODEL.predict(user)
            logger.info((score))
            response_object['score'] = score
            # response_object['target'] = target
    return jsonify(response_object)


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False
