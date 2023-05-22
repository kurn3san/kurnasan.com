from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

##
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/resume", StaticFiles(directory="resume"), name="resume")

templates = Jinja2Templates(directory="templates")
data=data = [
        {"number": "123", "name": "John"},
        {"number": "456", "name": "Jane"}
    ]
##
@app.get('/')
def get_welcome(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})
try:
    @app.post('/')
    async def post_welcome(request: Request):
        form = await request.form()
        number = form.get("number")
        name = form.get("name")
        # Store the form data in a dictionary or JSON file
        data.append({"number":number,"name":name})
        return templates.TemplateResponse("welcome.html", {"request": request})
except Exception as e:
    print("error...  "+str(e))
    
@app.delete('/')
async def delete_data(request: Request):
    data.pop()

@app.get('/data')
async def get_data(request: Request):
    # Retrieve the data from the dictionary or JSON file
    
    return templates.TemplateResponse("data.html", {"request": request, "data": data})
