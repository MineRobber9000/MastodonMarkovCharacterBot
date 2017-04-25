from mastodon import Mastodon
from getpass import getpass

def prompt(p,d=""):
	ret = input(p+" ("+d+") ")

ins = prompt("Instance: ",d="https://botsin.space")

Mastodon.create_app(
      input("Title: "),
      api_base_url=ins,
      to_file = 'clientcred.txt'
)
sgc = Mastodon(client_id="clientcred.txt",api_base_url=ins)
sgc.log_in(input("Email: "),getpass.getpass("Password: "),to_file="accesscred.txt")
