from requests import get, post, delete

print(get('http://127.0.0.1:5000/api/user').json())

print(get('http://127.0.0.1:5000/api/user/1').json())

print(get('http://127.0.0.1:5000/api/user/2').json())

print(get('http://127.0.0.1:5000/api/user/999').json())

print(get('http://127.0.0.1:5000/api/user/q').json())

print(post('http://127.0.0.1:5000/api/user', json={}).json())

print(post('http://127.0.0.1:5000/api/user',
           json={'name': 'Арсений'}).json())

print(post('http://127.0.0.1:5000/api/user',
           json={'name': 'Арсений',
                 'email': 'hypercactissupercube@gmail.com'
                 }).json())

print(delete('http://localhost:5000/api/news/999').json())

print(delete('http://localhost:5000/api/news/1').json())

print(delete('http://localhost:5000/api/news/2').json())

print(delete('http://localhost:5000/api/news/3').json())

print(delete('http://localhost:5000/api/news/4').json())

print(delete('http://localhost:5000/api/news/5').json())

print(delete('http://localhost:5000/api/news/6').json())

print(delete('http://localhost:5000/api/news/7').json())

print(delete('http://localhost:5000/api/news/8').json())

print(delete('http://localhost:5000/api/news/9').json())