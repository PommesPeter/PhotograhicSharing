import json
import random
from hashlib import md5

from flask import Blueprint, request

from . import database_object

db = database_object
m = md5()

user_opt = Blueprint("user_opt", __name__)


def get_usernickname(bit: int):
    pattern = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    salt = str()
    for i in range(bit):
        salt += random.choice(pattern)
    return salt


@user_opt.route("/user/login", methods=["POST"])
def login():
    data = json.loads(request.get_data())
    cursor = db.cursor()
    cursor.execute(f"select passwd from users where id={data['id']}")
    selected_data = cursor.fetchone()[0]
    m.update(selected_data.encode("utf-8"))
    if selected_data is not None:
        isAuthorized = True if m.hexdigest() == data["passwd"] else False
        if isAuthorized:
            return {"msg": "request success", "data": []}
        else:
            return {"msg": "request failed", "data": []}
    else:
        return {"msg": "request failed", "data": []}


@user_opt.route("/user/register", methods=["POST"])
def register():
    data = json.loads(request.get_data())
    cursor = db.cursor()

    nickname = get_usernickname(bit=12)
    passwd = data["passwd"].encode("utf-8")
    m.update(passwd)
    cursor.execute(f"insert into users(id, passwd, username) values ({data['id']}, {m.hexdigest()}, {nickname})")
    try:
        db.commit()
        return {"msg": "request success", "data": []}
    except:
        db.rollback()
        return {"msg": "request failed", "data": []}


@user_opt.route("/user/show_user_info", methods=["GET"])
def show_user_info():
    data_args = request.args
    cursor = db.cursor()

    cursor.execute(
        f"select sex, great, concern, fan, username, introduction, url from users where id={data_args.get('id')}")
    res = cursor.fetchone()
    if res is not None:
        return {"msg": "request success",
                "data": [{"sex": res[0], "great": res[1], "concern": res[2], "fan": res[3], "username": res[4],
                          "introduction": res[5], "url": res[6]}]}
    else:
        return {"msg": "request failed", "data": []}


@user_opt.route("/user/modify_user_info", methods=["POST"])
def modify():
    data = json.loads(request.get_data())
    cursor = db.cursor()

    cursor.execute(
        f"update users set username={data['username']}, sex={data['sex']}, introduction={data['introduction']} where id={data['id']}")

    try:
        db.commit()
        return {"msg": "request success", "data": []}
    except:
        db.rollback()
        return {"msg": "request failed", "data": []}
