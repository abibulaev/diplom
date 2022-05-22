class Configuration(object):
    DEBUG = True
    SECRET_KEY = 'slim'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/usersprepod'