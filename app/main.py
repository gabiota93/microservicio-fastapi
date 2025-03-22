from fastapi import FastAPI
from database import init_db
import routes

app = FastAPI()

init_db()
app.include_router(routes.router)

@app.get("/")
def read_root():
    return {"message": "Microservicio de tareas funcionando 🚀"}
