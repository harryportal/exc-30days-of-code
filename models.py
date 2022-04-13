from main import db
from passlib.apps import custom_app_context as hash_password
from main import login


@login.user_loader          # stores the unique id of the logged in user
def user_loader(user_id):
    user = User.query.get(user_id)
    return user


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    post = db.Relationship(db.String, backref='author', lazy=True)

    def __repr__(self):
        return f'{self.name}@{self.username}@{self.email}'

    def verify_password(self, password):
        verify = hash_password.verify(password, self.password_hash)
        return verify


class Post(db.Model):
    __tablename__ = 'Post'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForiegnKey('User.id'), nullable=False)
    comment = db.Relationship(db.String, backref='post_comment', lazy=True)

    def __repr__(self):
        return f'Title: {self.title} \n Content:{self.content}'


class Comment(db.Model):
    __tablename__ = 'Comment'
    comment = db.Column(db.String, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)  # to get the use that commented
    post = db.Column(db.Integer, db.ForeignKey('Post.id'), nullable=False)  # to get the post the comment was meant for

    def __repr__(self):
        return f'Comment: {self.comment} \n Content:{self.post.title}'
