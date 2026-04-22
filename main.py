from fastapi import FastAPI
from api import router

app = FastAPI(title="AI Powered Shopify Analytics")
app.include_router(router)
