import config
import requests

class GithubAuth:

    BASE_URL = "https://github.com/login/oauth/access_token"
    CLIENT_ID = "client_id"
    CLIENT_SECRET = "client_secret"
    CODE = "code"
    REDIRECT_URI = "redirect_uri"

    def getAccessToken(self,code):
        URL = "%s?%s=%s&%s=%s&%s=%s" % (self.BASE_URL, self.CLIENT_ID, config.config['clientID'], self.CLIENT_SECRET, config.config['clientSecret'], self.CODE, code)

        response = requests.post(url = URL,headers={"Accept":"application/json"})
        # print(response.json()['access_token'])
        return response.json()['access_token']
