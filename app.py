from time import strptime
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import mysql.connector
from datetime import datetime
from concurrent.futures import Executor, ThreadPoolExecutor
from sklearn.preprocessing import StandardScaler
import numpy as np
import json

from sqlalchemy import null
# from flask_socketio import SocketIO,emit

app = Flask(__name__,
            static_folder = "./dist/assets",
            template_folder = "./dist") 
# app.config.from_object(Config)
connection = mysql.connector.connect(host='127.0.0.1',
                                    port='3306',
                                    user='root',
                                    password='2001513SamuelWu11',
                                    database='dbfinalproject'
                                    )
cursor = connection.cursor()
cursor.execute("SET SQL_SAFE_UPDATES=0")
# socketio = SocketIO()
# socketio.init_app(app,cross_allowed_origins="*")
# name_space = '/predict'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
executor = ThreadPoolExecutor(1)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/LoadACdata',methods=['GET'])
def LoadACdata():
    keyword = request.args.get('keyword')
    keyword = '%'+keyword+'%'
    # print(keyword)
    # print("(spot.Address LIKE '%s') AND (spot.Title LIKE '%s');"%('%%%s%%'%keyword,'%%%s%%'%keyword))
    cursor.execute("SELECT spot.id,Title,Address,Description,Picture1 FROM spot,accommodation WHERE accommodation.id=spot.id AND (spot.Address LIKE '%s' OR spot.Title LIKE '%s');"%('%%%s%%'%keyword,'%%%s%%'%keyword))
    sqlresult = cursor.fetchall()
    print(len(sqlresult))
    AcList = []
    for i in range(len(sqlresult)):
        Acdata = {}
        Acdata['ID'] = sqlresult[i][0]
        Acdata['Title'] = sqlresult[i][1]
        Acdata['Address'] = sqlresult[i][2]
        Acdata['Description'] = sqlresult[i][3]
        Acdata['Image'] = sqlresult[i][4]
        AcList.append(Acdata)
    for i in range(len(AcList)):
        cursor.execute("SELECT AVG(Rate) FROM feedback WHERE Spot_id='%s';"%(AcList[i]['ID']))
        sqlresult = cursor.fetchall()
        AcList[i]['Rate'] = str(sqlresult[0][0])[0:3]
    # print(AcList[0])
    return jsonify(AcList[0:20])

@app.route('/api/LoadREdata',methods=['GET'])
def LoadREdata():
    keyword = request.args.get('keyword')
    keyword = '%'+keyword+'%'
    cursor.execute("SELECT spot.id,Title,Address,Description,Picture1 FROM spot,restaurant AS r WHERE r.id=spot.id AND (spot.Address LIKE '%s' OR spot.Title LIKE '%s');"%('%%%s%%'%keyword,'%%%s%%'%keyword))
    sqlresult = cursor.fetchall()
    print(len(sqlresult))
    ReList = []
    for i in range(len(sqlresult)):
        Redata = {}
        Redata['ID'] = sqlresult[i][0]
        Redata['Title'] = sqlresult[i][1]
        Redata['Address'] = sqlresult[i][2]
        Redata['Description'] = sqlresult[i][3]
        Redata['Image'] = sqlresult[i][4]
        ReList.append(Redata)
    for i in range(len(ReList)):
        cursor.execute("SELECT AVG(Rate) FROM feedback WHERE Spot_id='%s';"%(ReList[i]['ID']))
        sqlresult = cursor.fetchall()
        ReList[i]['Rate'] = str(sqlresult[0][0])[0:3]
    # print(ReList[0])
    return jsonify(ReList[0:20])

@app.route('/api/LoadATdata',methods=['GET'])
def LoadATdata():
    keyword = request.args.get('keyword')
    keyword = '%'+keyword+'%'
    print(keyword)
    cursor.execute("SELECT spot.id,Title,Address,Description,Picture1 FROM spot,attraction AS a WHERE a.id=spot.id AND (spot.Address LIKE '%s' OR spot.Title LIKE '%s');"%('%%%s%%'%keyword,'%%%s%%'%keyword))
    sqlresult = cursor.fetchall()
    print(len(sqlresult))
    AtList = []
    for i in range(len(sqlresult)):
        Atdata = {}
        Atdata['ID'] = sqlresult[i][0]
        Atdata['Title'] = sqlresult[i][1]
        Atdata['Address'] = sqlresult[i][2]
        Atdata['Description'] = sqlresult[i][3]
        Atdata['Image'] = sqlresult[i][4]
        AtList.append(Atdata)
    for i in range(len(AtList)):
        cursor.execute("SELECT AVG(Rate) FROM feedback WHERE Spot_id='%s';"%(AtList[i]['ID']))
        sqlresult = cursor.fetchall()
        AtList[i]['Rate'] = str(sqlresult[0][0])[0:3]
    # print(AtList[0])
    return jsonify(AtList[0:20])

@app.route('/api/LoadSpotdata',methods=['GET'])
def LoadSpotdata():
    keyword = request.args.get('keyword')
    keyword = '%'+keyword+'%'
    print(keyword)
    cursor.execute("SELECT id,Title FROM spot WHERE Address LIKE '%s' OR Title LIKE '%s';"%('%%%s%%'%keyword,'%%%s%%'%keyword))
    sqlresult = cursor.fetchall()
    print(len(sqlresult))
    SpotList = []
    for i in range(len(sqlresult)):
        Spotdata = {}
        Spotdata['ID'] = sqlresult[i][0]
        Spotdata['Name'] = sqlresult[i][1]
        SpotList.append(Spotdata)
    # print(AtList[0])
    return jsonify(SpotList[0:20])

@app.route('/api/LoadRoute',methods=['GET'])
def LoadRoute():
    cursor.execute("SELECT Spot1,Spot2,Spot3,Spot4,Spot5,Spot6,Spot7 FROM route")
    sqlresult = cursor.fetchall()
    print(len(sqlresult))
    RSList = []
    for i in range(len(sqlresult)):
        routespotlist = []
        for j in range(7):
            routespot = {}
            if sqlresult[i][j]==None or sqlresult[i][j]=='None' :
                continue
            routespot['ID'] = sqlresult[i][j]
            routespotlist.append(routespot)
        RSList.append(routespotlist)
    print('RSList',RSList)
    for i in range(len(RSList)):
        for j in range(len(RSList[i])):
            cursor.execute("SELECT Title,Address,Description FROM spot WHERE id='%s';"%(RSList[i][j]['ID']))
            sqlresult = cursor.fetchall()
            RSList[i][j]['Name'] = sqlresult[0][0]
            RSList[i][j]['Address'] = sqlresult[0][1]
            RSList[i][j]['Description'] = sqlresult[0][2]
    print('Samuel')
    print('RSList',RSList)        
    cursor.execute("SELECT Time,Name,Description,Price,Spot1,Spot2,Spot3,Spot4,Spot5,Spot6,Spot7 FROM route")
    sqlresult = cursor.fetchall()
    print(len(sqlresult))
    RouteList = []
    for i in range(len(sqlresult)):
        Spotdata = {}
        Spotdata['Time'] = datetime.strftime(sqlresult[i][0],'%Y-%m-%d %H:%M:%S')
        Spotdata['Name'] = sqlresult[i][1]
        Spotdata['Description'] = sqlresult[i][2]
        Spotdata['Price'] = sqlresult[i][3]
        Spotdata['spotlist'] = RSList[i]
        RouteList.append(Spotdata)
    # print(AtList[0])
    return jsonify(RouteList[0:20])

@app.route('/api/LoadACinfo',methods=['GET'])
def LoadACinfo():
    pnumber = request.args.get('pnumber')
    print(pnumber)
    checkin = request.args.get('checkin')
    checkin = datetime.strptime(checkin,"%Y/%m/%d")
    print(checkin.weekday())
    ID = request.args.get('ID')
    print(ID)
    # print("(spot.Address LIKE '%s') AND (spot.Title LIKE '%s');"%('%%%s%%'%keyword,'%%%s%%'%keyword))
    cursor.execute("SELECT s.id,Title,Address,Description,Picture1,Phone,wifi,Parking_info,googleMap FROM spot AS s,accommodation AS a WHERE a.id=s.id AND s.id = '%s';" %(ID))
    sqlresult = cursor.fetchall()
    Acinfo = {}
    Acinfo['ID'] = sqlresult[0][0]
    Acinfo['Title'] = sqlresult[0][1]
    Acinfo['Address'] = sqlresult[0][2]
    Acinfo['Description'] = sqlresult[0][3]
    Acinfo['Image'] = sqlresult[0][4]
    Acinfo['Phone'] = sqlresult[0][5]
    if sqlresult[0][6]== '1' :
        Acinfo['Wifi'] = '有'
    else :
        Acinfo['Wifi'] = '無'
    Acinfo['Park'] = sqlresult[0][7]
    Acinfo['GoogleMapKey'] = sqlresult[0][8]
    ## 房型價格
    cursor.execute("SELECT P_weekday,P_weekend,Type FROM roomtype AS r,accommodation AS a WHERE a.id=r.Acc_id AND r.Acc_id = '%s';" %(ID))
    sqlresult = cursor.fetchall()
    Acinfo['roomtype'] = sqlresult

    ## 優惠價格
    cursor.execute("SELECT Type,Price,Start_day,End_day FROM roomtype AS r,price AS p WHERE p.id=r.Acc_id AND p.No = r.No AND r.Acc_id = '%s';" %(ID))
    sqlresult = cursor.fetchall()
    discountlist = []
    for i in range(len(sqlresult)):
        discount ={}
        discount['Type'] = sqlresult[i][0]
        discount['Price'] = sqlresult[i][1]
        discount['Start_day'] = datetime.strftime(sqlresult[i][2],'%Y-%m-%d')
        discount['End_day'] = datetime.strftime(sqlresult[i][3],'%Y-%m-%d')
        discountlist.append(discount)
    print(discountlist)
    Acinfo['discount'] = discountlist

    ## 預估價格
    cursor.execute("SELECT P_weekday,P_weekend,Count,No FROM roomtype AS r,accommodation AS a WHERE a.id=r.Acc_id AND r.Acc_id = '%s' ORDER BY Count;" %(ID))
    sqlresult = cursor.fetchall()
    print(sqlresult)
    index = -1
    if len(sqlresult)>0:
        for i in range(len(sqlresult)):
            if int(sqlresult[i][2]) >= int(pnumber):
                index = i
                break
        if index>=0 :
            if checkin.weekday()>4:
                Acinfo['price'] = sqlresult[index][1]
            else:
                Acinfo['price'] = sqlresult[index][0]
        else :
            index = len(sqlresult)-1
            room_num = int(int(pnumber)/int(sqlresult[index][2]))+1
            print(room_num)
            if checkin.weekday()>4:
                Acinfo['price'] = sqlresult[index][1]*room_num
            else:
                Acinfo['price'] = sqlresult[index][0]*room_num
        cursor.execute("SELECT Start_day,End_day,Price FROM price WHERE id='%s' AND No = %d;" %(ID,int(sqlresult[index][3])))
        dateresult = cursor.fetchall()
        print(dateresult)
        for j in range(len(dateresult)):
            startdate = dateresult[j][0]
            enddate = dateresult[j][1]
            if checkin.date()>=startdate and checkin.date()<=enddate:
                if int(pnumber)>sqlresult[index][2]:
                    Acinfo['price'] = dateresult[j][2]*room_num
                else:
                    Acinfo['price'] = dateresult[j][2]
                Acinfo['price'] = str(Acinfo['price']) + '(優惠價格)'
    else :
        Acinfo['price'] = '無資訊'
    

    ## feedback
    cursor.execute("SELECT description,User_id,Rate FROM feedback WHERE Spot_id = '%s' ;" %(ID))
    sqlresult = cursor.fetchall()
    Acinfo['feedback'] = sqlresult
    
    return jsonify(Acinfo)

@app.route('/api/LoadREinfo',methods=['GET'])
def LoadREinfo():
    ID = request.args.get('ID')
    print(ID)
    # print("(spot.Address LIKE '%s') AND (spot.Title LIKE '%s');"%('%%%s%%'%keyword,'%%%s%%'%keyword))
    cursor.execute("SELECT s.id,Title,Address,Description,Picture1,Phone,Busi_hours,Parking_info,googleMap FROM spot AS s,restaurant AS r WHERE r.id=s.id AND s.id = '%s';" %(ID))
    sqlresult = cursor.fetchall()
    Reinfo = {}
    Reinfo['ID'] = sqlresult[0][0]
    Reinfo['Title'] = sqlresult[0][1]
    Reinfo['Address'] = sqlresult[0][2]
    Reinfo['Description'] = sqlresult[0][3]
    Reinfo['Image'] = sqlresult[0][4]
    Reinfo['Phone'] = sqlresult[0][5]
    Reinfo['Busi_hour'] = sqlresult[0][6]
    Reinfo['Park'] = sqlresult[0][7]
    Reinfo['GoogleMapKey'] = sqlresult[0][8]
    
    ## feedback
    cursor.execute("SELECT description,User_id,Rate FROM feedback WHERE Spot_id = '%s' ;" %(ID))
    sqlresult = cursor.fetchall()
    Reinfo['feedback'] = sqlresult
    
    return jsonify(Reinfo)

@app.route('/api/LoadATinfo',methods=['GET'])
def LoadATinfo():
    ID = request.args.get('ID')
    print(ID)
    # print("(spot.Address LIKE '%s') AND (spot.Title LIKE '%s');"%('%%%s%%'%keyword,'%%%s%%'%keyword))
    cursor.execute("SELECT s.id,Title,Address,Description,Picture1,Phone,Visit_hours,Parking_info,Traf_guide,Ticket_price,googleMap FROM spot AS s,attraction AS a WHERE a.id=s.id AND s.id = '%s';" %(ID))
    sqlresult = cursor.fetchall()
    print(sqlresult)
    Atinfo = {}
    Atinfo['ID'] = sqlresult[0][0]
    Atinfo['Title'] = sqlresult[0][1]
    Atinfo['Address'] = sqlresult[0][2]
    Atinfo['Description'] = sqlresult[0][3]
    Atinfo['Image'] = sqlresult[0][4]
    Atinfo['Phone'] = sqlresult[0][5]
    Atinfo['Visit'] = sqlresult[0][6]
    Atinfo['Park'] = sqlresult[0][7]
    Atinfo['Traffic'] = sqlresult[0][8]
    Atinfo['Ticket'] = sqlresult[0][9]
    Atinfo['GoogleMapKey'] = sqlresult[0][10]

    ## feedback
    cursor.execute("SELECT description,User_id,Rate FROM feedback WHERE Spot_id = '%s' ;" %(ID))
    sqlresult = cursor.fetchall()
    Atinfo['feedback'] = sqlresult
    
    return jsonify(Atinfo)

@app.route('/api/Login',methods=['GET'])
def Login():
    ID = request.args.get('userID')
    print(ID)
    # print("(spot.Address LIKE '%s') AND (spot.Title LIKE '%s');"%('%%%s%%'%keyword,'%%%s%%'%keyword))
    cursor.execute("SELECT Name,id,Sex,Birth,Phone FROM user WHERE id = '%s';" %(ID))
    sqlresult = cursor.fetchall()
    print('sqlresult',sqlresult)
    if len(sqlresult)==0:
        return 'error'
    Userinfo = {}
    Userinfo['Name'] = sqlresult[0][0]
    Userinfo['ID'] = sqlresult[0][1]
    if sqlresult[0][2]=='F':
        Userinfo['Sex'] = 'Female'
    else:
        Userinfo['Sex'] = 'Male'
    Userinfo['Birth'] = datetime.strftime(sqlresult[0][3],'%Y-%m-%d')
    Userinfo['Phone'] = sqlresult[0][4]
    return jsonify(Userinfo)

@app.route('/api/addfeedback',methods=['POST'])
def AddPatientData():
    data = request.get_data()
    data = json.loads(data)
    # print(type(data['rate']))
    cursor.execute("SELECT COUNT(id) FROM feedback;")
    sqlresult = cursor.fetchall()
    feedbackID = str(int(sqlresult[0][0])+1)
    for i in range(8-len(str(int(sqlresult[0][0])+1))):
        feedbackID = '0'+feedbackID
    feedbackID = 'FE' + feedbackID
    Now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(type(Now))
    cursor.execute("INSERT INTO feedback VALUES ('%s','%s','%s',str_to_date('%s','%%Y-%%m-%%d %%T'),'%s\',%f);" %(feedbackID,data['userID'],data['spotID'],Now,data['comment'],float(data['rate'])))
    connection.commit()
    return 'ok'

@app.route('/api/AddRoutedata',methods=['POST'])
def AddRoutedata():
    data = request.get_data()
    data = json.loads(data)
    print(data)
    for i in range(1,8):
        if data['spot'+str(i)] == '':
            data['spot'+str(i)] = None
    print(data)
    Now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(Now)
    cursor.execute("INSERT INTO route VALUES ('%s','%s',str_to_date('%s','%%Y-%%m-%%d %%T'),'%s','%s','%s','%s','%s','%s','%s','%s',%d);" %(data['userID'],data['Name'],Now,data['spot1'],data['spot2'],data['spot3'],data['spot4'],data['spot5'],data['spot6'],data['spot7'],data['description'],int(data['price'])))
    connection.commit()
    return 'ok'
    
@app.route('/api/adduser',methods=['POST'])
def AddUser():
    data = request.get_data()
    data = json.loads(data)
    print(data)
    cursor.execute("SELECT * FROM user WHERE id='%s';"%(data['ID']))
    sqlresult = cursor.fetchall()
    if len(sqlresult)>0:
        return '此帳號已被註冊，請更換後再註冊'
    cursor.execute("INSERT INTO user VALUES ('%s','%s','%s',str_to_date('%s','%%Y-%%m-%%d'),'%s');" %(data['Name'],data['ID'],data['Sex'],data['Birth'],data['Phone']))
    connection.commit()
    return 'ok'

if __name__ == "__main__":
    app.run(debug=True)
    # socketio.run(app, debug=True)