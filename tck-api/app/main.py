from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import os

# FastAPI app
app = FastAPI()

# Templates klasörü
templates = Jinja2Templates(directory="templates")

# Data klasörü yolu
DATA_PATH = "data"

# ---------------------------------
# API: Tüm maddeler
# ---------------------------------
@app.get("/api/maddeler")
def get_maddeler():
    try:
        with open(os.path.join(DATA_PATH, "maddeler.json"), "r", encoding="utf-8") as f:
            maddeler = json.load(f)
        return JSONResponse(content=maddeler)
    except FileNotFoundError:
        return JSONResponse(content=[], status_code=200)

# ---------------------------------
# API: Madde no ile
# ---------------------------------
@app.get("/api/maddeler/{madde_no}")
def get_madde(madde_no: int):
    try:
        with open(os.path.join(DATA_PATH, "maddeler.json"), "r", encoding="utf-8") as f:
            maddeler = json.load(f)
        madde = next((m for m in maddeler if m.get("madde_no") == madde_no), None)
        if not madde:
            raise HTTPException(status_code=404, detail="Madde bulunamadı")
        return JSONResponse(content=madde)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Madde bulunamadı")

# ---------------------------------
# API: Ceza bilgisi
# ---------------------------------
@app.get("/api/cezalar/{madde_no}")
def get_ceza(madde_no: int):
    try:
        with open(os.path.join(DATA_PATH, "cezalar.json"), "r", encoding="utf-8") as f:
            cezalar = json.load(f)
        ceza = next((c for c in cezalar if c.get("madde_no") == madde_no), None)
        if not ceza:
            raise HTTPException(status_code=404, detail="Ceza bilgisi yok")
        return JSONResponse(content=ceza)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Ceza bilgisi yok")

# ---------------------------------
# Site: Ana sayfa
# ---------------------------------
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
