# -~- coding: utf-8 -~-

from .version import __version__
from .version import __author__
from .version import __licence__

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
