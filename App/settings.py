import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 基础类
class BaseConfig():
    DEBUG = True
    SECRET_KEY = 'JFKSJKFJDKFJ'
    SESSION_TYPE = 'redis'
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 开发环境
class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:liudd@127.0.0.1/ooo'



# 测试环境
class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR,'test.db')
    TESTING = True


# 线上环境
class ProConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR,'pro.db')

config = {
    'default':DevConfig,
    'DevConfig':DevConfig,
    'TestConfig':TestConfig,
    'ProConfig':ProConfig
}