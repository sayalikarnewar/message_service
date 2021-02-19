from aiohttp import web
import json
import aiohttp_jinja2
from bson import SON


#get the opining page
@aiohttp_jinja2.template("header.html")
async def header(request):
    return {}


#get the form for message input
@aiohttp_jinja2.template("msg_textbox.html")
async def msg_input_form(request):
    return {}

#storing the previous output
output_result = []


# after submitting the form
@aiohttp_jinja2.template("msg_textbox.html")
async def msg_submit_form(request):
    form = await request.post()             #get the form
    text = form['msg_input']                # get the form data

    output_result.append(text)              # store the previous data in an array
    
    db = request.app['db']                  # request the db
    try:        
        #check if the input from form matches any of the data in db
        msg_db = await db.command(SON([ ( "distinct", "collection"), ("key","msg"), ("query", {"msg" :text})]))
        try:
            msg_db = msg_db['values'][0]

        except Exception as e:
            print(e, 1)
            result = "can you say it again"   
            return { "result" : result, "output_result": output_result}       
                
        if msg_db == text:
            try:
                # if it matches, retrieve the required data from the collection
                option1 = await db.command(SON([ ( "distinct", "collection"), ("key","option1"), ("query", {"msg" :text})]))
                option2 = await db.command(SON([ ( "distinct", "collection"), ("key","option2"), ("query", {"msg" :text})]))
                option1 = option1['values'][0]
                option2 = option2['values'][0]
                return { "form" : [option1, option2], "output_result": output_result}

            except:
                result = "SON failure"   
                return { "result" : result, "output_result": output_result}

    except Exception as e:
        print(e, 2)
        result = "can you say it again"   
        return { "result" : result, "output_result": output_result}
    
