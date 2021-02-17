from views import header, msg_input_form, msg_submit_form

def routes(app):
    app.router.add_get('/', header)

    #get and post the message.
    app.router.add_get("/msg", msg_input_form)
    app.router.add_post("/msg", msg_submit_form, name='msg_handle')