import os
import json
from json import loads as _l
from flask_restful import Resource, reqparse
from resources.encoding import Encoding

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "authn.json"

import googleapiclient.discovery

class GoogleSentiService(Resource):

    def post(self):
        
        args = parser.parse_args()
        data1 = args["data"]
		
        encoding='UTF32'
        body = {
                 'document': {
                 'type': 'PLAIN_TEXT',
                 'content': data1,
                 },
                 'encoding_type': encoding,
                 }

        service = googleapiclient.discovery.build('language', 'v1')
        
        request = service.documents().analyzeSentiment(body=body)
        
        response = request.execute()
        
        json_string1 = json.dumps(response)
        json_data1 = json.loads(json_string1)
        json_list1 = json_data1['documentSentiment']
        senti = json_list1['score']
        temp2 = ""
		
        if senti>0.10:
            c = "Positive"
        elif senti < -0.10:
            c = "Negative"
        else:
            c = "Neutral"
        #temp1 = senti['magnitude']+" " + senti['score']
        temp2 = c + " : " + str(senti)
		
        return temp2

        #from io import StringIO
        #io = StringIO()
        #json.dump(response,io)
        #res = io.getvalue()
        #print(res[0])
        #return res

parser = reqparse.RequestParser()
parser.add_argument("data")