import os
import json
from json import loads as _l
from flask_restful import Resource, reqparse
from resources.encoding import Encoding

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "authn.json"

import googleapiclient.discovery

class GoogleNLPService(Resource):

    def post(self):
        #result = analyze_entities(args.data, get_native_encoding_type())
        args = parser.parse_args()
        #print("google-nlp",args["data"])
        data1 = args["data"]
        
		
    #def analyze_entities(data, encoding='UTF32'):
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
        
        #print(json.dumps(response, indent=2))
    
        json_string = json.dumps(response)
        json_data = json.loads(json_string)
        json_list = json_data['entities']
        temp = ""
        temp1= ""
		
        # for x in json_list:
		    
            # temp = x['name'] + " - " + x['type']
            # temp1 +=  temp + "\n"			
        # return temp1
		
        for i in json_list:
            if i['type']!= 'OTHER':

                temp = i['name'] + "-" + i['type']
                temp1 += temp + "\n"

        return temp1

        #print(json_list)
        
            
        
# Output Json to the web app
        
        #from io import StringIO
        #io1 = StringIO()
        #json.dump(response,io1)
        #res1 = io1.getvalue()
        #print(res1)

        #return res1
	    #return response
class GoogleNLPAnalyzer(object):  
	
    print("inside")

parser = reqparse.RequestParser()
parser.add_argument("data")

