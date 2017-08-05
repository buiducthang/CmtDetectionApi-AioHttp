from aiohttp import web
import json
import sys
sys.path.append('/home/ducthang/Desktop/CmtApi-Aiohttp/binhnp/spam_detection/libsvm/python')
from train import *
from py4j.java_gateway import JavaGateway

#call py4j token
def token(comment):
    print ("enter")
    gateway = JavaGateway()
    response = gateway.entry_point.getResponse()
    response.setUETSegmentResponse(comment)
    comment = response.execute()
    return comment

def CheckComment(comment):
    m = svm_load_model('spam.model')
    vocabs = load_vocabs('vocabs.obj')
    #comment = token(comment)
    print (comment)
    label = predict(m, vocabs, comment)
    print (label)
    if(label[0] == 0.0):
        check = 'showPass'
        print ("ok")
    else:
        check = 'showFailed'
        print ('not ok')
    return label[0]

async def index(request):
    return web.Response(text='Hello Aiohttp!')

async def comment(request):
    result = {"result":""}
    data = await request.post()
    first_key =  next (iter (data))
    print (data[first_key] == '')
    if(data[first_key] == ''):
        data = await request.json()
        print('json')
    comment = data['comment']
    print (comment)

    result = {"result":CheckComment(comment)}
    return web.json_response(result)