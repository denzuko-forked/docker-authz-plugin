# -~- coding: utf-8 -~-

from .version import __version__
from .version import __author__
from .version import __licence__

import base64, json

from flask import Flask, jsonify, request

class AuthSuccess(Exception):
   def __init__(self, message=""):
        
        if not message:
            message = "The request authorization succeeded."

        # Call the base class constructor with the parameters it needs
        super(AuthSuccess, self).__init__(message)
        
        self.allow = True
        
class AuthFailure(Exception):
   def __init__(self, message="", error=""):
    
        if not message:
            message = "The request authorization failed. You must say hello first"
        
        if not error:
            error = "You must say hello first."
        
        # Call the base class constructor with the parameters it needs
        super(AuthFailure, self).__init__(message)
        
        self.allow = False
        self.error = error

class DockerAuthApp(object):

    def __init__(self, *args, **kwargs):
        self.app = Flask(__name__)
        self.auth_file = kwargs.get('auth_file', '/dev/shm/authz-said-hello.run')
        self.implements = ['authz']
      
        self._set_said_hello(False)
        
    def _has_said_hello(self):
        with open(self.auth_file), 'r') as hello_fd:
            said_hello = hello_fd.read()
            
        self.has_said_hello = True if said_hello is 'True' else False
        
    def _set_said_hello(self, value):
        self.has_said_hello = value
        with open(self.auth_file, 'w') as hello_fd:
            hello_fd.write(str(self.has_said_hello))

    @app.route("/")
    def index():
        return "Docker Authz Plugin"
        
    @app.route("/Plugin.Activate", methods=['POST'])
    def activate():
        return jsonify({'Implements': self.implements})
    
    @app.route("/AuthZPlugin.AuthZReq", methods=['POST'])
    def authz_request():
        print("AuthZ Request")
        print(request.data)
        plugin_request = json.loads(request.data)
        
        response = {"Allow": False, "Msg": str() }
        
        try:
            if self._has_said_hello():
                raise AuthSuccess()

            elif 'RequestBody' in plugin_request:
                
                docker_request = json.loads(base64.b64decode(plugin_request['RequestBody'])

                if docker_request['Image'] is 'hello-world':
                    self._set_said_hello(True)
                    raise AuthSuccess()
                else
                    raise AuthFailure()
            else:
                raise AuthFailure()
                                            
         catch AuthSuccess as success:
            response['Allow'] = success.allow
            response['Msg'] = success.message
 
         catch AuthFailure as failure:
            response["Allow"] = failure.allow
            response["Msg"] = failure.message
            response["Err"] = failure.error
         
         finally:
             return jsonify(**response)
                                            
    @app.route("/AuthZPlugin.AuthZRes", methods=['POST'])
    def authz_response():
        print("AuthZ Response")
        response = {"Allow": True}
        return jsonify(**response)
