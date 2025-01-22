# uvicorn main:app --host 127.0.0.1 --port 5000
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.chat_route import chat_router

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(chat_router, prefix="/api")

@app.get("/")
async def root():
    return {
        "DEBUG": "FastAPI server running on... http//127.0.0.1:5000"
    }

"""
    $ uvicorn main:app --host 127.0.0.1 --port 5000
"""