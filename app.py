import models.database
from flask import jsonify, Flask, redirect, request, url_for
from flask_oidc import OpenIDConnect
from flask_cors import CORS
from datetime import timedelta
from keycloak import KeycloakOpenID, KeycloakAdmin
import visitor

app = Flask(__name__)
CORS(app)

# Configure client
keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                    client_id="demo_client",
                    realm_name="demo-realm",
                    client_secret_key="fn2VvJwzHTLs7R7R28KqY2la95FrRYCm")

token = keycloak_openid.token("admin", "admin")
       
userinfo = keycloak_openid.userinfo(token['access_token'])
print(userinfo)


# keycloak configuration
app.config.update({
    'SECRET_KEY': 'fn2VvJwzHTLs7R7R28KqY2la95FrRYCm',
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
app.secret_key = "infopercept"
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=30)



# Default route when api is running
@app.route("/")
def home():
    return redirect(url_for('users')) 




# Api for select all the user information
@app.route("/users", methods=['GET'])
def users():
    select_employee = """SELECT * FROM user_details"""
    con = models.database.createConnection()
    cursor = con.cursor()
    cursor.execute(select_employee)
    result = cursor.fetchall()
    list = []
    for row in result:
        list.append({"id": row[0], "candidate_name": row[1],
                   "job_title": row[2], "team_name": row[3]})
    return jsonify(list)




# Api for getting tools informations
@app.route("/tools", methods=['GET'])
def tools():
    tools = """SELECT * FROM tools"""
    con = models.database.createConnection()
    cursor = con.cursor()
    cursor.execute(tools)
    result = cursor.fetchall()
    list = []
    for row in result:
        list.append({"id":row[0],"title":row[1],"link":row[2],"description":row[3],"name":row[4]})
    return jsonify(list)




# This Function called just before the every requests
@app.before_request
def do_something_when_a_request_comes_in():
    visitor.track_visitor()




# Api for getting user tracking reports
@app.route("/tracking_report", methods=['GET'])
def getReportData():
    select_employee = """SELECT requested_url,username,tool_name FROM visits_log"""
    con = models.database.createConnection()
    cursor = con.cursor()
    cursor.execute(select_employee)
    result = cursor.fetchall()
    list = []
    for row in result:
        list.append({"url": row[0], "user_name": row[1],"tool_name": row[2]})
    return jsonify(list)



# Api for getting link of particular tool
@app.route("/tools/<toolName>", methods=['GET'])
def getLinkOfTool(toolName):
    sql = """SELECT link FROM tools where t_name=%s"""
    cursor = models.database.createConnection().cursor()
    tup = (toolName,)
    cursor.execute(sql,tup)
    result = cursor.fetchall()
    list = []
    for row in result:
        list.append({"link":row[0]})
    return jsonify(list)


# Api for updating the tool link
@app.route('/update', methods = ['PUT'])
def updateLink():
    if request.method == "PUT":
        link = request.json['link']
        id = request.json['id']
        con = models.database.createConnection()
        cur = con.cursor()
        sql = """update tools set link=%s where id=%s"""
        tup = (link,id)
        cur.execute(sql,tup)
        list = []
        if(not link):
            list.append({"result":False})
            con.commit()
        elif cur.rowcount >= 1:
            list.append({"result":True})
            con.commit()
        else:
            list.append({"result":False})
    return jsonify(list)



# Api for inserting user into the keycloak
@app.route("/add",methods=['POST'])
def add():
    keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/auth/",
                            username='admin',
                            password='admin',
                            realm_name="demo-realm",
                            user_realm_name="master",
                            verify=True)
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        fName = request.form.get('fname')
        lName = request.form.get('lname')
        password = request.form.get('password')
        new_user = keycloak_admin.create_user({"email": email,
                        "username": username,
                        "enabled": True,
                        "firstName": fName,
                        "lastName": lName,
                        "credentials": [{"value": password,"type": "password",}]},
                        exist_ok=False)
        list = []
        list.append({"response":new_user})
        return jsonify(list)


#List out all the users from the keycloak
@app.route("/viewUser")
def disp():
    keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/auth/",
                            username='admin',
                            password='admin',
                            realm_name="demo-realm",
                            user_realm_name="master",
                            verify=True)
    # Get users Returns a list of users, filtered according to query parameters
    users = keycloak_admin.get_users({})
    #list.append(users)
    return jsonify(users)



# Api for updating the user into the keycloak
@app.route("/updateUser",methods=['PUT'])
def updateUser():
    keycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/auth/",
                            username='admin',
                            password='admin',
                            realm_name="demo-realm",
                            user_realm_name="master",
                            verify=True)
    username = request.form.get('username')
    fName = request.form.get('fname')
    # Get user ID from name
    user_id_keycloak = keycloak_admin.get_user_id(username)
    print(user_id_keycloak)

    # Get User
    user = keycloak_admin.get_user(user_id_keycloak)
    print(user)

    # Update User
    response = keycloak_admin.update_user(user_id_keycloak,payload={'firstName': fName})
    print(response)
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)