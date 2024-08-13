import os
from flask import Flask
from flask_restx import Api, Resource, fields
from services.DatabaseQueryHandler import (
    getServiceByName,
)


app = Flask(__name__)
api = Api(
    app,
    version="1.0.0",
    title="SRE CICD EXAMPLE",
    description="This is a microservice that handles generic api request",
)

serviceLogsNS = api.namespace(
    "Services",
    description="Operations associated with services",
)





@serviceLogsNS.route("/")
class SericeLogsList(Resource):
    """Shows a list of known services"""

    def get(self):
        services = [
            "RPA",
            "WxO",
            "TTS",
            "SST"
        ]
        return {"result": services}

@serviceLogsNS.route("/<serviceName>")
@serviceLogsNS.response(404, "No Service found")
class ServiceSearch(Resource):
    def get(self, serviceName):

        if "logMessage" in api.payload:
            return getServiceByName(serviceName=serviceName)
        else:
            api.abort(400, "Pass in either the log message or service name")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
