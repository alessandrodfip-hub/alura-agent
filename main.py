from fastapi import FastAPI
app = FastAPI(title="Alura Agent")
@app.get("/")
def root():
    return {"status": "Alura Agent rodando!"}
