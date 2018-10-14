import hashlib
import uuid

from flask import Blueprint, render_template, request, g, session, redirect, url_for, jsonify

from App.ext import cache
from App.models import *


blue = Blueprint('blue',__name__)


def init_views(abc):
    abc.register_blueprint(blue)


# 首页
@blue.route('/home/')
# @cache.cached(timeout=30)   # 缓存试图
def home():

    wheels = ['Akali_Splash_0.jpg','Akali_Splash_1.jpg','Akali_Splash_2.jpg','Akali_Splash_3.jpg','Akali_Splash_4.jpg']

    # print('**************************************')
    g.ip = request.remote_addr


    cache.set('ip', g.ip, timeout=3)
    goodslist = Goods.query.all()

    page = request.args.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    paginate = Goods.query.paginate(page,4)

    # token状态
    token = session.get('token')
    if token:
        user = User.query.filter(User.token == token).first()
    else:
        user = None


    return render_template('home.html',wheels=wheels,goodslist=goodslist,paginate=paginate,endpoint='blue.home',user=user)


# cache测试
# @blue.route('/testcache/')
# def testcache():
#
#     name = cache.get('name')
#     return '{}缓存成功'.format(name)
#
#
# # 反爬策略
# @blue.before_request
# def before():
#     key = cache.get('ip')
#     g.ip = key
#     if key:
#         return '请再等待最多3s钟即可'
#     else:
#         pass


# 密码加密
def secret_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


# 注册
@blue.route('/register/',methods=['POST'])
def register():
    name = request.form.get('name')
    password = request.form.get('password')
    email = request.form.get('email')

    # 数据存入数据库
    user = User()
    user.name = name
    user.password = str(secret_password(password))
    user.token = str(uuid.uuid5(uuid.uuid4(),'register'))
    user.email =email
    db.session.add(user)
    db.session.commit()

    # 状态保持,通过token
    session['token'] = user.token
    return redirect(url_for('blue.home'))


# 退出操作
@blue.route('/logout/')
def logout():
    session.pop('token')
    return redirect(url_for('blue.home'))


# 登录
@blue.route('/login/',methods = ['POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    password = str(secret_password(password))
    users = User.query.filter(User.name == name).filter(User.password == password)
    user = users.first()
    if user:

        user.token = str(uuid.uuid5(uuid.uuid4(),'login'))
        db.session.add(user)
        db.session.commit()
        session['token'] = user.token
    else:
        user = None

    return redirect(url_for('blue.home'))


@blue.route('/jsontest/')
def jsontest():
    wheels = ['Akali_Splash_0.jpg', 'Akali_Splash_1.jpg', 'Akali_Splash_2.jpg', 'Akali_Splash_3.jpg',
              'Akali_Splash_4.jpg']
    return jsonify(wheels)


# ajax验证帐号
@blue.route('/namecheck/')
def namecheck():
    name = request.args.get('name')
    print(name)

    users = User.query.filter(User.name == name)
    user = users.first()
    print(users,'********')
    data = {}
    if user:
        data['status'] = '1'
    else:
        data['status'] = '0'

    return jsonify(data)

