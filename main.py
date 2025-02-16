from fastapi import FastAPI
from shop.routes.orders import router as order
from shop.routes.products import router as product
from shop.routes.users import router as user

app = FastAPI()


app.include_router(order)
app.include_router(product)
app.include_router(user)


