from turtle import title
from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel



'''
#Create databases required
All_Users=[]

#2. Verified users
Verified_Users=[]

#3. Hold whose subscription has been received for the period
Subscriptions=[]

#3. Subscribed users
Subscribed_Users=[]

#4. Proscribed Users
Proscribed_Users=[]





#create a class for what kind of data each will be accepted from each new registrant, this will inherit the general pydantic BaseModel class
class Registration_details(BaseModel):
    Surname: str
    Lastname: str
    Account_size:int
    Date_of_Birth: date
    Email:str
    Mt_Username: str
    Mt_Password: str
    MT5_Server: str
    Country_of_Origin: str
    State_of_Origin: str
    Country_of_Residence: str
    State_of_Residence: str
    Address_of_Residence: str
    Religion: str
    Terms_Conditions: bool

#Create an individual user class (which will have an ID), when users make the post request with the inherited details, they are registered
class Registered_User(Registration_details):
    ID:int

    
# temporary data gets renewed weekly or monthly (depending on the subscription cycle)
# Is a subclass of registered users. Hence only items in Registered user class can send this post request
class Subscriptions(Registered_User):
    Data_base:bool
    Royalty:bool
    Reciept_number:int


class Trading_data_post(BaseModel):
    time:datetime
    support1:float
    resistance1:float
    support2:float
    resistance2:float
    pivot_low:float
    pivot_high:float
    effective_pivot:float
    trend:bool

class trading_data_id(Trading_data_post):
    id:int
    


#1. Registered users object. this is the format of data anyone would post when they want to register.
All_Users=[Registered_User{}ID=1, Surname='surname', Lastname='lastname', Account_size=100, Date_of_Birth=12/2/1990, Email='email1', Mt_Username='mt5username', Mt_Password='mt5pwd', MT5_Server='mt5server', Country_of_Origin='country1', State_of_Origin='state1', Country_of_Residence='country2', State_of_Residence='state2', Address_of_Residence='address', Religion='religion', Terms_Conditions=True}, Registered_User{ID=2, Surname='surname1', Lastname='lastname1', Account_size=200, Date_of_Birth=12/2/1990, Email='email2', Mt_Username='mt5username', Mt_Password='mt5pwd', MT5_Server='mt5server', Country_of_Origin='country1', State_of_Origin='state1', Country_of_Residence='country2', State_of_Residence='state2', Address_of_Residence='address', Religion='religion', Terms_Conditions=True}]


#create the post method for adding users (will first check if user not in Registered user list)
@app.Post("/All_Users")
async def add_new_user(new_user=Registered_User):
    if Registered_User['lastname'] not in All_Users: #if the email has not been used before
        All_Users.append(new_user)
        return("Registration Successful! Await verification")
    else: 
        return("User already registered")

#2. create trading result object. this is the format of data python will send to the api for anyone to access.

Trading_data=[trading_data_id(id=1, time='time', support1='sup1', resistance1='res1', support2='sup2', resistance2='res2', pivot_low='piv_lo', pivot_high='piv_hi', effective_pivot='eff_piv', trend=True), trading_data_id(id=1, time='time', support1='sup1', resistance1='res1', support2='sup2', resistance2='res2', pivot_low='piv_lo', pivot_high='piv_hi', effective_pivot='eff_piv', trend=True)]



#create the get method for client requesting result. they will only get the last result in the list
@app.Get("/Trading_data", response_model=list(trading_data_id))
async def get_result():
    for list in trading_data_id:
        if list==len(trading_data_id)-1:
            return list'''


'''#instantiate the fastapi class
app=FastAPI()'''

#customizing our api
app=FastAPI(
    title='Fast API TRADING INTeL',
    description='Trading Intel signals',
    version='1.0.0',
    contact={'email':'sunnet.ys@gmail.com', 'name':'Sunnet'},
    license_info={'name':'Sunnet_cloudServer'} #'url':'www.sunnetserver.html
    )

users=[]

#defining a get to the root of website, so that anytime a get is directed from the client to the root, it will give  out the return value
#its like predefining what user gets
'''@app.get("/users")
async def get_users():
    return users

#a clients' post method to this users root would add a user to the user list datastore.
#however in a real app, the user are not just a string, its an object of different datatype combo, This is now where pydantic comes in handy
@app.post("/users")
async def create_user(user):
    users.append(user)
    return {'message':'user created successfully'}
    
'''
#Using pydantic
#Define a user class of a user object
class User_class(BaseModel):
    email:str
    Is_active:bool
    bio:Optional[str]

#however in a real app, the user are not just a string, its an object of different datatype combo, This is now where pydantic comes in handy
#we will integrate the user arguement in our post function with the user class defined above so that Fastapi/pydantic will create appropriate columns and validation for it
#Note that in the real app, the columns are created in the formfields and only assigned in the api post, so that pydantic knows which is which
@app.post("/users")
async def create_user(user:User_class):
    users.append(user)
    return {'message':'user created successfully'}

'''@app.get("/users")
async def get_users():
    return users'''
        
#to return the last user in the list
#Not successful but i need to find out why
'''@app.get("/users")
async def get_last_users():
    for i in users:
        if i == len(users)-1:
            return users[i]'''

#just as we can define the kind of data we send in to the server, we can also define the response we get
#we do this by not only using the parameter bracket of the function associated with the app (as in post method),
#we use the app method endpoint itself. we need to import List from typing
#finally we define he response model to be the type structure of data we want to return which already is defined int the BaseModel class or other definitions
'''@app.get("/users", response_model=list[User_class])
async def get_users():
    return users '''     

#getting item with path parameter and query parameter
@app.get("/users{id}")
async def get_unique_user(id: int = Path(..., description="The user you want to retrieve.", gt=2), 
                          q:str=Query(None, max_length=5)):
    return {'user': users[id], 'query': q}