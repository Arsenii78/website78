import flask
from flask import jsonify, make_response, request
from . import db_session
from .users import User
import os

blueprint = flask.Blueprint(
    'user_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/user')
def get_user():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('name', 'email', ''))
                 for item in users]
        }
    )

@blueprint.route('/api/user/<int:news_id>', methods=['GET'])
def get_one_user(news_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(news_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'user': users.to_dict(only=(
                'name', 'email'))
        }
    )

@blueprint.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    db_sess = db_session.create_session()
    book = db_sess.query(User).get(book_id)
    if not book:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'books': book.to_dict(only=(
                'name', 'email'))
        }
    )

@blueprint.route('/api/user/', methods=['POST'])
def add_book():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['name', 'context']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    book = User(
        name=request.json['name'],
        email=request.json['email'],
    )
    db_sess.add(book)
    db_sess.commit()
    return jsonify({'success': 'OK'})

@blueprint.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    db_sess = db_session.create_session()
    book = db_sess.query(User).get(book_id)
    if not book:
        return jsonify({'error': 'Not found'})
    db_sess.delete(book)
    db_sess.commit()
    return jsonify({'success': 'OK'})

@blueprint.route('/api/books/load/<int:book_id>', methods=['GET'])
def load_book(book_id):
    db_sess = db_session.create_session()
    if not request.json:
        return jsonify({'error': 'Empty request'})
    book_to_load = db_sess.query(User.context).filter(User.id == book_id).first()[0]
    homeDir = os.path.expanduser("~")
    try:
        file = open('storage/{}'.format(book_to_load), "rb")
        f = open('{}/{}'.format(homeDir, book_to_load), "wb")
        f.write(file.read())
        f.close()
    except FileNotFoundError:
        return jsonify({'error': 'no such file "{}"'.format(book_to_load)})
    return jsonify({'success': 'save in {}/{}'.format(homeDir, book_to_load)})