import config as c
import requests
import json

#从官方示例拿来的代码@https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Tweet-Lookup/get_tweets_with_bearer_token.py

def auth():
    return  c.get_api_params().__getattr__(c.get_api_params(),'bearer_token')

#TODO 使用外部输入id
def create_url():
    tweet_fields = "expansions=attachments.media_keys&media.fields=duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width&tweet.fields=lang,author_id,source"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    ids = "ids=1278747501642657792,1255542774432063488,1263145271946551300"
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/tweets?{}&{}".format(ids,tweet_fields)
    return url

def create_headers(bearer_token):
    headers = {"Authorization":"Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url,headers):
    response = requests.request("GET",url,headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code,response.text
            )
    )
    return response.json()
def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url,headers)
    print(json.dumps(json_response,indent=4,sort_keys=True))

if __name__=="__main__":
    main()