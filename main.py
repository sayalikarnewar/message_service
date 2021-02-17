import jinja2
import aiohttp_jinja2
from aiohttp import web
import asyncio

from setup import setupDB
from routes import routes


#create a loop for the db
loop = asyncio.get_event_loop()
db = loop.run_until_complete(setupDB())

app = web.Application()
app['db'] = db

#set up the jinja template
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

# add the routes to the api
routes(app)

#run the web app
web.run_app(app)