from fastapi import FastAPI
from routes.orders import router as order
from routes.products import router as product
from routes.users import router as user

app = FastAPI()


app.include_router(order)
app.include_router(product)
app.include_router(user)


