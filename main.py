from flask import Flask, request
from flask_pymongo import PyMongo
from datetime import datetime
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "*"}})
#app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MONGO_URI'] = 'mongodb://exceed_group02:tg52cdr5@158.108.182.0:2255/exceed_group02'
mongo = PyMongo(app)

U_myCollection = mongo.db.User
S_myCollection = mongo.db.Shop
C_myCollection = mongo.db.Category
Q_myCollection = mongo.db.Queue
W_myCollection = mongo.db.Wristband
Wr_myCollection = mongo.db.Wr


@app.route('/find_all_user', methods=['GET'])
@cross_origin()
def find_all_user():

    filt = {}

    query = U_myCollection.find(filt)
    output = []

    for ele in query:
        output.append({
                "U_UserID": ele["U_UserID"],
                "U_Username": ele["U_Username"],
                "U_email": ele["U_email"],
                "U_age": ele["U_age"],
                "U_gender": ele["U_age"],
                "U_name": ele["U_name"],
                "U_surname": ele["U_surname"],
                "U_occupation": ele["U_occupation"],
                "U_catId": ele["U_catId"]
                })

    return {"result": output}


@app.route('/find_user', methods=['GET'])
@cross_origin()
def find_user():

    username = request.args.get('U_Username')
    password = request.args.get('U_password')
    filt = {"U_Username": username, "U_password": password}

    query = U_myCollection.find(filt)
    output = []

    for ele in query:
        output.append({
                "U_UserID": ele["U_UserID"],
                "U_Username": ele["U_Username"],
                "U_email": ele["U_email"],
                "U_age": ele["U_age"],
                "U_gender": ele["U_age"],
                "U_name": ele["U_name"],
                "U_surname": ele["U_surname"],
                "U_occupation": ele["U_occupation"],
                "U_catId": ele["U_catId"]
                })

    return {"result": output}


@app.route('/find_shop', methods=['GET'])
@cross_origin()
def find_shop():

    filt = {}

    query = S_myCollection.find(filt)
    output = []

    for ele in query:
        output.append({
                "S_shopID": ele["S_shopID"],
                "S_name": ele["S_name"],
                "S_total_amount": ele["S_total_amount"],
                "S_limit_amount": ele["S_limi_amount"],
                "S_time_limit": ele["S_time_limit"],
                "S_current_amount": ele["S_current_amount"],
                "S_lastest_time_enter": ele["S_lastest_time_enter"],
                "S_lastest_time_left": ele["S_lastest_time_left"],
                "S_catId": ele["S_catId"],
                })

    return {"result": output}


@app.route('/find_category', methods=['GET'])
@cross_origin()
def find_category():

    filt = {}

    query = C_myCollection.find(filt)
    output = []

    for ele in query:
        output.append({
                "C_catId": ele["C_catId"],
                "C_catName": ele["C_catName"],
                })

    return {"result": output}


@app.route('/find_all_queue', methods=['GET'])
@cross_origin()
def find_all_queue():

    filt = {}

    query = Q_myCollection.find(filt)
    output = []

    for ele in query:
        output.append({
                "Q_queueID": ele["Q_queueID"],
                "Q_userID": ele["Q_userID"],
                "Q_shopID": ele["Q_shopID"],
                "Q_updateDate": ele["Q_createDate"],
                "Q_status": ele["Q_status"],
                })

    return {"result": output}


@app.route('/find_queue', methods=['GET'])
@cross_origin()
def find_queue():

    id = request.args.get('Q_quueueID')
    filt = {"Q_queueID": id}

    query = Q_myCollection.find(filt)
    output = []

    for ele in query:
        output.append({
                "Q_queueID": ele["Q_queueID"],
                "Q_userID": ele["Q_userID"],
                "Q_shopID": ele["Q_shopID"],
                "Q_updateDate": ele["Q_createDate"],
                "Q_status": ele["Q_status"],
                })

    return {"result": output}


@app.route('/find_wristband', methods=['GET'])
@cross_origin()
def find_wristband():

    filt = {}

    query = W_myCollection.find(filt)
    output = []

    for ele in query:
        output.append({
                "W_timestamp_in": ele["W_timestamp_in"],
                "W_timestamp_out": ele["W_timestamp_out"],
                "W_status": ele["W_status"],
                "W_UserID": ele["W_UserID"],
                "W_wristbandID": ele["W_wristbandID"],
                })

    return {"result": output}


@app.route('/update_shop_total_amount', methods=['PATCH'])
@cross_origin()
def update_total_amount():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_total_amount' : data["S_total_amount"]}}

    S_myCollection.update_one(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_limit_amount', methods=['PATCH'])
@cross_origin()
def update_limit_amount():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_limit_amount' : data["S_limit_amount"]}}

    S_myCollection.update_one(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_current_amount', methods=['PATCH'])
@cross_origin()
def update_current_amount():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_current_amount' : data["S_current_amount"]}}

    S_myCollection.update_one(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_time_limit', methods=['PATCH'])
@cross_origin()
def update_limit_limit():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_time_limit' : data["S_time_limit"]}}

    S_myCollection.update_one(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_lastest_time_enter', methods=['PATCH'])
@cross_origin()
def update_lastest_time_enter():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_lastest_time_enter' : data["S_lastest_time_enter"]}}

    S_myCollection.update_one(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/update_shop_lastest_time_left', methods=['PATCH'])
@cross_origin()
def update_lastest_time_left():
    data = request.json

    filt = {'S_shopID': 0}
    updated_content = {"$set": {'S_lastest_time_left' : data["S_lastest_time_left"]}}

    S_myCollection.update_one(filt, updated_content)

    return {'result' : 'Updated successfully!'}


@app.route('/member', methods=['POST'])
@cross_origin()
def user_data_input():
    data = request.json
    filt = { "U_Username": data['U_Username']}
    query = U_myCollection.find(filt).count()
    if(query > 0):
        return { "Result":"Username already use" }
    data['U_UserID'] = U_myCollection.find().count()
    U_myCollection.insert_one(data)
    return { "Result" : data['U_UserID'] }


@app.route('/queue', methods=['POST'])
@cross_origin()
def queue_data_input():
    data = request.json
    filt = { "U_Username": data['Q_Username'] , "U_password" : data['Q_password']}
    query = U_myCollection.find(filt).count()
    if(query == 0):
        return { "Result":"Wrong Username or Password" }
    query = U_myCollection.find_one(filt)
    data['Q_UserID'] = query["U_UserID"]

    filt = { "Q_UserID": data['Q_UserID'] , "Q_status" : 0}
    query = Q_myCollection.find(filt).count()
    if(query > 0):
        return { "Result":"This Username already in queue" }

    data['Q_queueID'] = Q_myCollection.find().count()
    data['Q_status'] = 0
    timestamp = datetime.timestamp(datetime.now())
    data['Q_updateDate'] = timestamp
    Q_myCollection.insert_one(data)
    return {
            'Q_queueID' :  data['Q_queueID']
            ,'Q_updateDate' : data['Q_updateDate']
    }


@app.route('/queue', methods=['PATCH'])
@cross_origin()
def queue_data_update():
    data = request.json
    filt = { "Q_queueID": data['Q_queueID']}
    query = Q_myCollection.find_one(filt)
    output = {
        "Q_UserID" : query["Q_UserID"]
        ,"Q_shopID" : query["Q_shopID"]
        ,"Q_queueID" : query["Q_queueID"]
        ,"Q_status" : query["Q_status"]
        ,"Q_updateDate" : query["Q_updateDate"]
        ,"Q_Username" : query["Q_Username"]
        ,"Q_password" : query["Q_password"]
    }
    timestamp = datetime.timestamp(datetime.now())
    output['Q_updateDate'] = timestamp
    output['Q_status'] = data["Q_status"]
    updated_content = {"$set":output}
    Q_myCollection.update_one(filt, updated_content)
    return {
        "Q_queueID" : output["Q_queueID"]
        ,"Q_userID" : output["Q_UserID"]
        ,"Q_Username" : output["Q_Username"]
    }


@app.route('/queue', methods=['GET'])
@cross_origin()
def queue_data_get():
    filt = { "Q_status" : 0 }
    query = Q_myCollection.find(filt)
    output = []
    for ele in query:
        output.append({
                "Q_UserID" : ele["Q_UserID"]
                ,"Q_Username" : ele["Q_Username"]
                ,"Q_queueID" : ele["Q_queueID"]
                ,"Q_status" : ele["Q_status"]
                ,"Q_updateDate" : ele["Q_updateDate"]
                ,"Q_shopID" : ele["Q_shopID"]
            })
    return { "Result" : output }


@app.route('/add_wristband', methods=['POST'])
@cross_origin()
def add_wristband():
    data = request.json
    filt = { "W_wristbandID": data['W_wristbandID'] , "W_status" : 0}
    query = W_myCollection.find(filt).count()
    if (query>0):
        return { "Result" : "This wristband is using now."}

    filt = { "U_Username": data['W_Username']}
    query = U_myCollection.find(filt).count()
    if(query==0):
        return { "Result" : "Wrong Username"}
    query = U_myCollection.find_one(filt)

    myInsert = {
                "W_timestamp_in": 0,
                "W_timestamp_out": 0,
                "W_status": 0,
                "W_UserID": query["U_UserID"],
                "W_wristbandID": data["W_wristbandID"],
                "W_Username" : data['W_Username']
            }
    W_myCollection.insert_one(myInsert)

    filt = { "Wr_wristbandID": data['W_wristbandID'] }
    query = Wr_myCollection.find_one(filt)
    output = {
            "Wr_wristbandID" : query["Wr_wristbandID"]
            ,"Wr_status" : 1
            }
    updated_content = {"$set":output}
    Wr_myCollection.update_one(filt, updated_content)

    filt = { "Q_Username" : data['W_Username'] }
    updated_content = {"$set": { "Q_status":1 }}
    Q_myCollection.update_one(filt, updated_content)

    return {'result': 'Created successfully'}


@app.route('/get_wristband', methods=['POST'])
@cross_origin()
def get_wristband():
    data = request.json
    filt = { "Wr_status" : data["Wr_status"]}
    query = Wr_myCollection.find(filt)
    output = []
    for ele in query:
        output.append(ele["Wr_wristbandID"])
    return {"Result" : output
            ,"Wr_status" : data["Wr_status"]}


# @app.route('/get_graph1', methods=['GET'])
# @cross_origin()
# def get_graph1():
#     ID = request.args.get('id')
#     filt = { "Q_shopID" : int(ID)}
#     query = Q_myCollection.find(filt)
#     x = []
#     for ele in query:
#         x.append(ele["Q_UserID"])
#     output = {
#         "15-25": U_myCollection.find({"U_age": {"$gte": 15, "$lt": 25}, "U_UserID": {"$in": x}}).count(),
#         "25-35": U_myCollection.find({"U_age": {"$gte": 25, "$lt": 35}, "U_UserID": {"$in": x}}).count(),
#         "35-45": U_myCollection.find({"U_age": {"$gte": 35, "$lt": 45}, "U_UserID": {"$in": x}}).count(),
#         "45-55": U_myCollection.find({"U_age": {"$gte": 45, "$lt": 55}, "U_UserID": {"$in": x}}).count(),
#         "55-65": U_myCollection.find({"U_age": {"$gte": 55, "$lt": 65}, "U_UserID": {"$in": x}}).count(),
#         "65-75": U_myCollection.find({"U_age": {"$gte": 65, "$lt": 75}, "U_UserID": {"$in": x}}).count(),
#         "75-85": U_myCollection.find({"U_age": {"$gte": 75, "$lt": 85}, "U_UserID": {"$in": x}}).count(),
#     }
#     return output
#
#
# @app.route('/get_graph2', methods=['GET'])
# @cross_origin()
# def get_graph2():
#     ID = request.args.get('id')
#     filt = { "Q_shopID" : int(ID)}
#     query = Q_myCollection.find(filt)
#     x = []
#     for ele in query:
#         x.append(ele["Q_UserID"])
#     filt_m = {"U_gender": "Male", "U_UserID": {"$in": x}}
#     filt_f = {"U_gender": "Female", "U_UserID": {"$in": x}}
#     filt_o = {"U_gender": "Not Specified", "U_UserID": {"$in": x}}
#     output = {
#         "Male": U_myCollection.find(filt_m).count(),
#         "Female": U_myCollection.find(filt_f).count(),
#         "Not Specified": U_myCollection.find(filt_o).count(),
#     }
#     return output
#
#
# @app.route('/get_graph3', methods=['GET'])
# @cross_origin()
# def get_graph3():
#     ID = request.args.get('id')
#     filt = { "Q_shopID" : int(ID)}
#     query = Q_myCollection.find(filt)
#     output = {}
#     for ele in query:
#         filt_u = { "U_UserID" : ele["Q_UserID"]}
#         query1 = U_myCollection.find_one(filt_u)
#         filt_occupation = {"U_occupation": query1["U_occupation"], "U_UserID" : query1["U_UserID"]}
#         query2 = U_myCollection.find(filt_occupation)
#         if query1["U_occupation"] not in output:
#             output[query1["U_occupation"]] = query2.count()
#         else:
#             output[query1["U_occupation"]] += 1
#     return output


@app.route('/get_graph1', methods=['GET'])
@cross_origin()
def get_graph1():
    output = {
        "15-25": U_myCollection.find({"U_age": {"$gte": 15, "$lt": 25}}).count(),
        "25-35": U_myCollection.find({"U_age": {"$gte": 25, "$lt": 35}}).count(),
        "35-45": U_myCollection.find({"U_age": {"$gte": 35, "$lt": 45}}).count(),
        "45-55": U_myCollection.find({"U_age": {"$gte": 45, "$lt": 55}}).count(),
        "55-65": U_myCollection.find({"U_age": {"$gte": 55, "$lt": 65}}).count(),
        "65-75": U_myCollection.find({"U_age": {"$gte": 65, "$lt": 75}}).count(),
        "75-85": U_myCollection.find({"U_age": {"$gte": 75, "$lt": 85}}).count(),
    }
    return output


@app.route('/get_graph2', methods=['GET'])
@cross_origin()
def get_graph2():
    filt_m = {"U_gender": "Male"}
    filt_f = {"U_gender": "Female"}
    filt_o = {"U_gender": "Not Specified"}
    output = {
        "Male": U_myCollection.find(filt_m).count(),
        "Female": U_myCollection.find(filt_f).count(),
        "Not Specified": U_myCollection.find(filt_o).count(),
    }
    return output


@app.route('/get_graph3', methods=['GET'])
@cross_origin()
def get_graph3():
    filt = {}
    query = U_myCollection.find(filt)
    output = {}
    for ele in query:
        if ele["U_occupation"] not in output:
            output[ele["U_occupation"]] = 1
        else:
            output[ele["U_occupation"]] += 1
    return output


@app.route('/get_graph4', methods=['GET'])
@cross_origin()
def get_graph4():
    output = {
        "0-30": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 0, "$lt": 30}}).count(),
        "30-60": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 30, "$lt": 60}}).count(),
        "60-90": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 60, "$lt": 90}}).count(),
        "90-120": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 90, "$lt": 120}}).count(),
        "120-150": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 120, "$lt": 150}}).count(),
        "150-180": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 150, "$lt": 180}}).count(),
        "180-210": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 180, "$lt": 210}}).count(),
        "210-240": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 210, "$lt": 240}}).count(),
        "240-270": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 240, "$lt": 270}}).count(),
        "270-300": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 270, "$lt": 300}}).count(),
        "300-330": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 300, "$lt": 330}}).count(),
        "330-360": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 330, "$lt": 360}}).count(),
        "360-330": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 360, "$lt": 390}}).count(),
        "390-360": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 390, "$lt": 420}}).count(),
        "420-450": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 420, "$lt": 450}}).count(),
        "450-480": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 450, "$lt": 480}}).count(),
        "480-510": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 480, "$lt": 510}}).count(),
        "510-540": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 510, "$lt": 540}}).count(),
        "540-570": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 540, "$lt": 570}}).count(),
        "570-600": W_myCollection.find({"W_status": 1, "W_timediff": {"$gte": 570, "$lt": 600}}).count(),
    }
    return output


@app.route('/get_graph5', methods=['GET'])
@cross_origin()
def get_graph5():
    filt = {}
    query = W_myCollection.find(filt)
    output = {
        "1 AM": W_myCollection.find({"W_startat": 1}).count(),
        "2 AM": W_myCollection.find({"W_startat": 2}).count(),
        "3 AM": W_myCollection.find({"W_startat": 3}).count(),
        "4 AM": W_myCollection.find({"W_startat": 4}).count(),
        "5 AM": W_myCollection.find({"W_startat": 5}).count(),
        "6 AM": W_myCollection.find({"W_startat": 6}).count(),
        "7 AM": W_myCollection.find({"W_startat": 7}).count(),
        "8 AM": W_myCollection.find({"W_startat": 8}).count(),
        "9 AM": W_myCollection.find({"W_startat": 9}).count(),
        "10 AM": W_myCollection.find({"W_startat": 10}).count(),
        "11 AM": W_myCollection.find({"W_startat": 11}).count(),
        "12 PM": W_myCollection.find({"W_startat": 12}).count(),
        "1 PM": W_myCollection.find({"W_startat": 13}).count(),
        "2 PM": W_myCollection.find({"W_startat": 14}).count(),
        "3 PM": W_myCollection.find({"W_startat": 15}).count(),
        "4 PM": W_myCollection.find({"W_startat": 16}).count(),
        "5 PM": W_myCollection.find({"W_startat": 17}).count(),
        "6 PM": W_myCollection.find({"W_startat": 18}).count(),
        "7 PM": W_myCollection.find({"W_startat": 19}).count(),
        "8 PM": W_myCollection.find({"W_startat": 20}).count(),
        "9 PM": W_myCollection.find({"W_startat": 21}).count(),
        "10 PM": W_myCollection.find({"W_startat": 22}).count(),
        "11 PM": W_myCollection.find({"W_startat": 23}).count(),
        "12 AM": W_myCollection.find({"W_startat": 0}).count(),
    }
    return output


@app.route('/get_graph6', methods=['GET'])
@cross_origin()
def get_graph6():
    output = {}
    for i in range(0,15):
        output[C_myCollection.find_one({"C_catId": i+1})["C_catName"]] = U_myCollection.find({"U_catId": i+1}).count()
    return output


@app.route('/now_queue', methods=['POST'])
@cross_origin()
def now_queue():
    data = request.json
    filt = { "Q_Username" : data["Q_Username"]
            ,"Q_password": data["Q_password"]
            ,"Q_status" : 0 }
    query = Q_myCollection.find(filt).count()
    if(query==0):
        return { "Result" : "Wrong Username Password or Not have data in queue"  }
    query = Q_myCollection.find_one(filt)
    queryc = Q_myCollection.find({"Q_status":1}).count()
    queuenow = query["Q_queueID"] - queryc
    return {    "now" : queuenow
            ,"Q_queueID" : query["Q_queueID"]
            }


@app.route('/update_timestamp', methods=['PATCH'])
@cross_origin()
def update_timestamp():
    data = request.json
    filt = {'W_wristbandID': data["W_wristbandID"], 'W_status': 0}
    query = W_myCollection.find(filt).count()
    if(query == 0):
        return { "Result" : "Error"  }
    query = W_myCollection.find_one(filt)
    shop = S_myCollection.find_one({'S_shopID': 0})
    timestampp = datetime.timestamp(datetime.now())
    a = timestampp
    b = (a//(24*60*60))*(24*60*60)
    c = ((a-b)//(60*60) + 7)%24


    if (data["W_status"] == 0) :
        updated_content = {"$set": {'W_status' : 0, 'W_timestamp_in': timestampp ,"W_startat" : c}}
        W_myCollection.update_one(filt, updated_content)
        updated_content = {"$set": {'S_lastest_time_enter': timestampp }}
        S_myCollection.update_one({'S_shopID': 0}, updated_content)
        #return {'result' : shop["S_time_limit"]}
        return {
                'result' : "Start"
                }
    elif (data["W_status"] == 1) :
        diff = (timestampp - query["W_timestamp_in"])//60
        updated_content = {"$set": {'W_status' : 1, 'W_timestamp_out': timestampp, 'W_timediff' : diff }}
        W_myCollection.update_one(filt, updated_content)
        Wr_myCollection.update_one({"Wr_wristbandID" : data["W_wristbandID"]},{"$set" : {"Wr_status":0}})
        updated_content = {"$set": {'S_lastest_time_left': timestampp }}
        S_myCollection.update_one({'S_shopID': 0}, updated_content)
        return {'result': "Time out"}


@app.route('/infor', methods=['GET'])
@cross_origin()
def information():
    shop = S_myCollection.find_one({'S_shopID': 0})
    a = datetime.now().timestamp()
    b = a//(24*60*60)
    filt = { 'W_timestamp_in': {'$gte': b*(24*60*60) , '$lt': (b+1)*(24*60*60)} }
    num = W_myCollection.find(filt).count()
    return {
            "S_lastest_time_enter" : shop["S_lastest_time_enter"]
            ,'S_lastest_time_left' : shop['S_lastest_time_left']
            ,"Total" : num
            }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000', debug=True)
