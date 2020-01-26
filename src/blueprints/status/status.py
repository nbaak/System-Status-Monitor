from flask import Blueprint, render_template, current_app as app
from blueprints.status.Config import Config
from blueprints.status.HTTPClient import HTTPClient
import asyncio
import json

status = Blueprint("status", __name__, static_folder="static", template_folder="templates")
loop = asyncio.new_event_loop()
    
async def get_status_from_satelites():    
    config = Config(app.config.get('PROJECT_ROOT') + 'config.json')
    status = []
    
    for server in config.servers:        
        try:
            data = await get_data(server['name'], server['address'], server['port'])
        except:
            data = await get_data(server['name'], server['address'])

        if data:
            print (data)
            status.append(data)
        
    return status

async def get_data(name, address, port = 5555, endpoint = "/status"):
    print (name, address, port)
    
    try:
        url = f"{address}:{port}{endpoint}"        
        json_data = await HTTPClient.get(url)
        data = json.loads(json_data)
        data['host'] = name
    except:
        json_data = "ERROR"
        data = None
    
    return data

@status.route("/")
def Status ():
    data = loop.run_until_complete(get_status_from_satelites())
    #data = get_status_from_satelites()
    if len(data) > 0:
        return render_template("status.html", data=data)
    else:
        return render_template("status.html")