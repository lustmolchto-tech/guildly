from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
import json
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
DATA_PATH = "data"

# API: tüm maddeler
@app.get("/api/maddeler")
def get_maddeler():
    try:
        with open(os.path.join(DATA_PATH, "maddeler.json"), "r", encoding="utf-8") as f:
            return JSONResponse(json.load(f))
    except FileNotFoundError:
        return JSONResponse([], status_code=200)

# API: madde no ile
@app.get("/api/maddeler/{madde_no}")
def get_madde(madde_no: int):
    try:
        with open(os.path.join(DATA_PATH, "maddeler.json"), "r", encoding="utf-8") as f:
            maddeler = json.load(f)
        madde = next((m for m in maddeler if m["madde_no"] == madde_no), None)
        if not madde:
            return JSONResponse({"detail": "Madde bulunamadı"}, status_code=404)
        return JSONResponse(madde)
    except FileNotFoundError:
        return JSONResponse({"detail": "Madde bulunamadı"}, status_code=404)

# API: ceza
@app.get("/api/cezalar/{madde_no}")
def get_ceza(madde_no: int):
    try:
        with open(os.path.join(DATA_PATH, "cezalar.json"), "r", encoding="utf-8") as f:
            cezalar = json.load(f)
        ceza = next((c for c in cezalar if c["madde_no"] == madde_no), None)
        if not ceza:
            return JSONResponse({"detail": "Ceza bilgisi yok"}, status_code=404)
        return JSONResponse(ceza)
    except FileNotFoundError:
        return JSONResponse({"detail": "Ceza bilgisi yok"}, status_code=404)

# Site: ana sayfa
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
