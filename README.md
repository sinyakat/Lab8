# Lab8
Существующие пользователи: login - Kate, password - 12345

Для добавления статьи в таблицу БД:
u = User.query.get(id)
p = Post(title = '', body='', author=u)
db.session.add(p)
db.session.commit()
