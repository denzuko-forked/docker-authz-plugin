from flask import Flask, jsonify, request
app = Flask(__name__)
application = app

@app.route("/")
def index():
    return "Docker Authz Plugin"

@app.route("/Plugin.Activate", methods=['POST'])
def activate():
    return jsonify({'Implements': ['authz']})

@app.route("/AuthZPlugin.AuthZReq", methods=['POST'])
def authz_request():
    print("AuthZ Request")
    print(request.data)
    r = {"Allow": True,
         "Msg":   "The request authorization message",
         "Err":   "The error message if things go wrong"}
    return jsonify(**r)

@app.route("/AuthZPlugin.AuthZRes", methods=['POST'])
def authz_response():
    print("AuthZ Response")
    print(request.data)
    r = {"Allow": True,
         "Msg":   "The response authorization message",
         "Err":   "The error message if things go wrong"}
    return jsonify(**r)

if __name__ == "__main__":
    app.run()
