import spacy
import query_extractor as _qe
from json import loads as _l
from flask_restful import Resource, reqparse

import spacy as s1
from collections import Counter as c1
from operator import itemgetter as ig1


nlp1 = s1.load('en')


class NLPService(Resource):
    
    def post(self):
        args = parser.parse_args()
        result = clf.predict(args["data"])
        #return result[0], 200 if result[1] else 400
        return result
    

class NLPAnalyzer(object):

    def predict(self, data):
        
        doc = nlp1(data)
        for entity in doc.ents:
            print(entity.text, entity.label_)
            temp1 = entity.text + " " + entity.label_
            return temp1
       
parser = reqparse.RequestParser()
parser.add_argument("data")
clf = NLPAnalyzer()
