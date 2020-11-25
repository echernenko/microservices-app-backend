from aiohttp import web

async def handle(request):
  res = {"name1": "Leoni", "name2": "Seth", "name3": "Ulrika", "name4": "Thomas", "name5": "Benghin"}
  return web.json_response(res)

app = web.Application()
app.router.add_get('/', handle)

web.run_app(app, port=5858)
