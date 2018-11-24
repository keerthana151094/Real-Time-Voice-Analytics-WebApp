    
from flask_restful import Resource, reqparse

class Encoding(Resource):

      def get_native_encoding_type():
    
        if sys.maxunicode == 65535:
           return 'UTF16'
        else:
           return 'UTF32'