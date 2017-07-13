import dota2api
import os

from api_key import API_KEY

api = dota2api.Initialise(API_KEY)

top = api.get_top_live_games()

print(top)
