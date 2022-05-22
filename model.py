from cProfile import label
from fileinput import filename
from turtle import back
from app import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    data = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    work = db.Column(db.String(200), nullable=False)
    fakultet=db.Column(db.String(200),nullable=False)
    kafedra=db.Column(db.String(200),nullable=False)
    telephone = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    foto_url=db.Column(db.String(120), nullable=False )
    avatar=db.Column(db.String(120), nullable=False)
    user_rating=db.Column(db.Integer,nullable=False)

    passw = db.Column(db.String(250), nullable=False)
    url=db.relationship("FileUrl",backref='dessert',uselist=False)
    urlm=db.relationship("FileMonUrl",backref='monograf',uselist=False)
    urls=db.relationship("SlovarUrl",backref='slovary',uselist=False)

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Users {}>'.format(self.name)


class FileUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url= db.Column(db.String(200), nullable=False)
    filname=db.Column(db.String(300), nullable=False)
    type_dess=db.Column(db.String(300), nullable=False)
    special=db.Column(db.String(300), nullable=False)
    tema=db.Column(db.String(300), nullable=False)
    nauch_ruk=db.Column(db.String(300), nullable=False)
    data=db.Column(db.String(300), nullable=False)
    city=db.Column(db.String(300), nullable=False)
    down=db.Column(db.Integer,nullable=False)
    annotation=db.Column(db.String(2000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   
    

    def __init__(self, *args, **kwargs):
        super(FileUrl, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<FileUrl {}>'.format(self.url)

class FileMonUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url= db.Column(db.String(200), nullable=False)
    type_work=db.Column(db.String(200), nullable=False)
    monname=db.Column(db.String(300), nullable=False)
    filenamem=db.Column(db.String(300), nullable=False)
    soavtor=db.Column(db.String(300), nullable=False)
    city=db.Column(db.String(300), nullable=False)
    izpat=db.Column(db.String(300), nullable=False)
    kol_stran=db.Column(db.String(300), nullable=False)
    stranic=db.Column(db.String(300), nullable=False)
    isbn=db.Column(db.String(300), nullable=False)
    down=db.Column(db.Integer,nullable=False)
    data=db.Column(db.String(300), nullable=False)
    annotation=db.Column(db.String(2000), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   
    

    def __init__(self, *args, **kwargs):
        super(FileMonUrl, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<FileMonUrl {}>'.format(self.url)


class SlovarUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url= db.Column(db.String(200), nullable=False)
    monnames=db.Column(db.String(300), nullable=False)
    type_work=db.Column(db.String(200), nullable=False)
    filenames=db.Column(db.String(300), nullable=False)
    soavtors=db.Column(db.String(300), nullable=False)
    citys=db.Column(db.String(300), nullable=False)
    izpats=db.Column(db.String(300), nullable=False)
    kol_strans=db.Column(db.String(300), nullable=False)
    isbns=db.Column(db.String(300), nullable=False)
    datas=db.Column(db.String(300), nullable=False)
    annotation=db.Column(db.String(2000), nullable=False)
    down=db.Column(db.Integer,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   
    

    def __init__(self, *args, **kwargs):
        super(SlovarUrl, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<SlovarUrl {}>'.format(self.url)
class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nauch_rab=db.Column(db.String(200), nullable=False)
    grade=db.Column(db.Integer, nullable=False)
    
    
   
    def __init__(self, *args, **kwargs):
        super(Rating, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Rating {}>'.format(self.type_lent)