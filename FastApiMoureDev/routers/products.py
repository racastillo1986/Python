from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"], # Agrupa en la documentacion
                   responses={404: {"message": "No se encuentra"}}) # prefix="/products" me ahorra poner en cada endpoint

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]

@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id: int):
    return products_list[id]