from flask import jsonify, request
from loguru import logger

from app import app
from app.db import REDIS_CLIENT
from mock.db import BOOKS, uuid

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    logger.info("It's just log to info")
    REDIS_CLIENT.add_user('qwe', 'петров')
    logger.info(REDIS_CLIENT.get_user('qwe'))
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
        logger.info(post_data)
        # Todo: наверное надо сделать какую-то проверку данных на пустоту -
        # а мб не тут а на фронте
        user_hash = post_data.get('user_hash')
        if user_hash:
            user = REDIS_CLIENT.get_user(user_hash)
            if user:
                response_object['user_exists'] = True
                response_object['data'] = user
    logger.info(response_object)
    return jsonify(response_object)


@app.route('/login/register', methods=['POST'])
def register_user():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        logger.info(post_data)
        user_hash = post_data['user_hash']
        REDIS_CLIENT.add_user(user_hash, post_data)
    logger.info(response_object)
    return jsonify(response_object)


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False
