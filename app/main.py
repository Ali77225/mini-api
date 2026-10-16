from fastapi import FastAPI

app = FastAPI(title="Mini API")

@app.get("/sante/")
def route_sante():
    return {"statut": "ok"}