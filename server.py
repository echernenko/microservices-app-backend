from aiohttp import web
import json, urllib.request

async def handle(request):

  # data = urllib.request.urlopen("https://api.github.com/users?since=100").read()
  # res = json.loads(data)
  res = {"name1": "Leoni", "name2": "Seth", "name3": "Ulrika", "name4": "Thomas", "name5": "Benghin"}
  return web.json_response(res);

app = web.Application()
app.router.add_get('/', handle)

web.run_app(app, port=5858)
