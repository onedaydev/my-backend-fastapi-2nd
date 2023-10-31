from fastapi import FastAPI

from routers import users

app = FastAPI()

# app.add_middleware(CORSMiddleware) # frontend


app.include_router(users.router)



# app.mount(,StaticFIles) # frontend

@app.get("/")
async def root():
   # return FileResponse() # frontend 
   return {"message": "root"}
