from mastodon import Mastodon

def getClient():
	return Mastodon(client_id="clientcred.txt",access_token="accesscred.txt",api_base_url="https://botsin.space")

