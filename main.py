from fastapi import FastAPI

from domain.user import user_router 

app = FastAPI()

# app.add_middleware(CORSMiddleware) # frontend

app.include_router(user_router.router)


# app.mount(,StaticFIles) # frontend

@app.get("/")
async def root():
   # return FileResponse() # frontend 
   return {"message": "root"}
