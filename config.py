def get_api_params():
    TwitterApiParams.__init__(TwitterApiParams,'x','xx','xx')
    return TwitterApiParams

class TwitterApiParams():
    def __init__(
        self,api_key,api_secret_key,bearer_token):
        self.api_key=api_key
        self.api_secret_key=api_secret_key
        self.bearer_token=bearer_token
    
    def __getattr__(self,k):
        try:
            if(k=='api_key'):
                return self.api_key
            if(k=='api_secret_key'):
                return self.api_secret_key
            if(k=='bearer_token'):
                return self.bearer_token
            return "no such key"
        except AttributeError:
            return "error"