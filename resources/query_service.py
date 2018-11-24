
import media_aggregator
from json import loads as _l
import query_extractor as _qe
from flask_restful import Resource, reqparse
from media_aggregator import (shorten_news, get_gkg, GuardianAggregator as _ga, NYTAggregator as _nyt)


class QueryService(Resource):
    def post(self):
        args = parser.parse_args()
        result = clf.predict(args["data"])
        #print("query service",args["data"])
        return result[0], 200 if result[1] else 400


class QueryAnalyzer(object):
    def __init__(self):
        self._query_extractor = _qe.QueryExtractor()

    def predict(self, data):
        try:
            if "news" in data.lower() or "latest" in data.lower():
                # News query
                source, query = self._query_extractor.get_news_tokens(data)
                response = (_ga() if "guardian" in source else _nyt()).get_news(query)
                if len(response) <= 0:
                    return {"phrase": "Sorry, no relevant results were returned."}, 500
                i, done = 0, media_aggregator.shorten_news(response[0])
                while (not done) and ((i + 1) < len(response)):
                    i += 1
                    done = shorten_news(response[i])
            else:
                # Knowledge query
                done = get_gkg(self._query_extractor.get_knowledge_tokens(data))
            ret_val = {"urls": done}
            if not done:
                ret_val["phrase"] = "Sorry, no valid results were returned."
            return ret_val, done
        except Exception as e:
            return {"phrase": "Sorry, something unexpected happened.", "original_exception": e.message}, False


parser = reqparse.RequestParser()
parser.add_argument("data")
clf = QueryAnalyzer()
