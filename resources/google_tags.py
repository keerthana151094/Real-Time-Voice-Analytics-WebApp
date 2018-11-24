import os
import json
from json import loads as _l
from flask_restful import Resource, reqparse
from resources.encoding import Encoding

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "authn.json"

import googleapiclient.discovery

class GoogleTagService(Resource):

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
        
        request = service.documents().analyzeEntities(body=body)
        
        response = request.execute()
    
        json_string = json.dumps(response)
        json_data = json.loads(json_string)
        json_list = json_data['entities']
        tempt = ""
        tempt1= ""
	
		
        for i in json_list:
            if i['type']== 'OTHER':

                tempt = i['name']
                tempt1 += tempt + "\n"

        return tempt1

        
class GoogleTagAnalyzer(object):  
	
    print("inside")

parser = reqparse.RequestParser()
parser.add_argument("data")

