import random
from hashlib import md5

from flask import Blueprint, request

from . import database_pool

dbp = database_pool

user_opt = Blueprint("user_opt", __name__)


def get_usernickname(bit: int):
    pattern = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    salt = str()
    for i in range(bit):
        salt += random.choice(pattern)
    return salt


@user_opt.route("/login", methods=["POST"])
def login():
    m = md5()
    data = request.values
    db = dbp.connection()
    cursor = db.cursor()
    cursor.execute(f"select passwd from users where uid='{data.get('id')}'")
    selected_data = cursor.fetchone()
    m.update(data.get("passwd").encode("utf-8"))
    en_passwd = m.hexdigest()
    if selected_data is not None:
        isAuthorized = True if en_passwd.strip() == selected_data[0].strip() else False
        if isAuthorized:
            cursor.close()
            return {"msg": "success", "data": []}
        else:
            cursor.close()
            return {"msg": "failed", "data": []}
    else:
        cursor.close()
        return {"msg": "failed", "data": []}


@user_opt.route("/register", methods=["POST"])
def register():
    m = md5()
    data = request.values
    db = dbp.connection()
    cursor = db.cursor()

    nickname = get_usernickname(bit=12)
    passwd = data.get('passwd').encode("utf-8")
    m.update(passwd)
    cursor.execute(f"select uid from sharingphoto.users where uid='{data.get('id')}'")
    res = cursor.fetchone()
    if res is None:
        cursor.execute(
            f"insert into users(uid, passwd, username) values ('{data.get('id')}', '{m.hexdigest()}', '{nickname}')")
        try:
            db.commit()
            cursor.close()
            return {"msg": "success", "data": []}
        except:
            db.rollback()
            cursor.close()
            return {"msg": "failed", "data": []}
    else:
        cursor.close()
        return {"msg": "duplicated account", "data": []}


@user_opt.route("/show_user_info", methods=["GET"])
def show_user_info():
    data_args = request.args
    db = dbp.connection()
    cursor = db.cursor()

    cursor.execute(
        f"select sex, thumbsup, star, fan, username, introduction, url from users where uid='{data_args.get('id')}'")
    res = cursor.fetchone()
    if res is not None:
        cursor.close()
        return {"msg": "success",
                "data": [{"sex": res[0], "great": res[1], "star": res[2], "fan": res[3], "username": res[4],
                          "introduction": res[5], "url": res[6]}]}
    else:
        cursor.close()
        return {"msg": "failed", "data": []}


@user_opt.route("/modify_user_info", methods=["POST"])
def modify():
    data = request.values
    db = dbp.connection()
    cursor = db.cursor()

    cursor.execute(
        f"update users set username='{data.get('username')}', sex='{data.get('sex')}', introduction='{data.get('introduction')}' where uid='{data.get('id')}'")

    try:
        db.commit()
        cursor.close()
        return {"msg": "success", "data": []}
    except:
        db.rollback()
        cursor.close()
        return {"msg": "failed", "data": []}


@user_opt.route("/modify_avatar", methods=["POST"])
def modify_avatar():
    data = request.values
    db = dbp.connection()
    cursor = db.cursor()

    cursor.execute(f"update sharingphoto.users set url='{data.get('url')}' where uid='{data.get('id')}'")

    try:
        db.commit()
        cursor.close()
        return {"msg": "success", "data": []}
    except:
        db.rollback()
        cursor.close()
        return {"msg": "failed", "data": []}
