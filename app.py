from models.database import Database
import json
from flask import jsonify, Flask, redirect, request, url_for
from flask_oidc import OpenIDConnect
from flask_cors import CORS
import logging
import mariadb
from models.database import Database

conn = Database()

logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'FQDTdIDyy7hIVDl4xyj5tES8k2OsiAQM',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'demo-realm',
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})

oidc = OpenIDConnect(app)


CORS(app)

@app.route("/")
@oidc.require_login
def home():
    return redirect(url_for('users')) 


@app.route("/users", methods=['GET'])
@oidc.require_login
def users():
    select_employee = """SELECT * FROM user_details"""
    con = conn.connect()
    cursor = con.cursor()
    cursor.execute(select_employee)
    result = cursor.fetchall()
    list = []
    for row in result:
        list.append({"id": row[0], "candidate_name": row[1],
                   "job_title": row[2], "team_name": row[3]})

    return jsonify(list)

@app.route('/logout')
@oidc.require_login
def logout():
    url = oidc.client_secrets.get('issuer')
    hosturl = 'http://127.0.0.1:5000/'
    oidc.logout()
    return redirect(
        url + '/protocol/openid-connect/logout?redirect_uri=' + hosturl)



@app.route("/tools", methods=['GET'])
@oidc.require_login
def tools():
    tools = """SELECT * FROM tools"""
    con = conn.connect()
    cursor = con.cursor()
    cursor.execute(tools)
    result = cursor.fetchall()
    list = []
    for row in result:
        list.append({"id":row[0],"title":row[1],"link":row[2],"description":row[3],"name":row[4]})
    return jsonify(list)


@app.route("/tools/<toolName>", methods=['GET'])
@oidc.require_login
def getLinkOfTool(toolName):
    sql = """SELECT link FROM tools where t_name=%s"""
    cursor = conn.connect().cursor()
    tup = (toolName,)
    cursor.execute(sql,tup)
    result = cursor.fetchall()
    list = []
    for row in result:
        list.append({"link":row[0]})

    return jsonify(list)

@app.route('/update', methods = ['PUT'])
def update():
    if request.method == "PUT":
        link = request.json['link']
        id = request.json['id']
        con = conn.connect()
        cur = con.cursor()
        sql = """update tools set link=%s where id=%s"""
        tup = (link,id)
        cur.execute(sql,tup)
        list = []
        if cur.rowcount >= 1:
            list.append({"result":True})
            con.commit()
        else:
            list.append({"result":False})
    return jsonify(list)


if __name__ == '__main__':
    app.run(debug=True)