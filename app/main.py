import os
import sys
import uvicorn
from fastapi import FastAPI
# Import local modules
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from app.controllers.customer_controller import router as customer_router

app = FastAPI()

app.include_router(customer_router, prefix='/api', tags=["Customers"])

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.3", port=8000, reload=True)