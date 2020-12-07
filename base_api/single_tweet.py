import config as cf
params = cf.get_api_params()
#define base key params
consumer_key = params.__getattr__(params,'consumer_key')
consumer_secret = params.__getattr__(params,'consumer_secret')
access_token = params.__getattr__(params,'access_token')
token_secret = params.__getattr__(params,'token_secret')
bearer_token = params.__getattr__(params,'bearer_token')
