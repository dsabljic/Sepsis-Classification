from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib

app = FastAPI()
templates = Jinja2Templates(directory="templates")

lr_model = joblib.load("./models/lr_model.joblib")
scaler = joblib.load("./models/scaler.joblib")
imputer = joblib.load("./models/numerical_imputer.joblib")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, PRG: int = Form(...), PL: int = Form(...), PR: int = Form(...),
                  SK: int = Form(...), TS: int = Form(...), M11: float = Form(...), BD2: float = Form(...),
                  Age: int = Form(...), Insurance: int = Form(...)):

    data = [[PRG, PL, PR, SK, TS, M11, BD2, Age, Insurance]]
    data_imputed = imputer.transform(data)
    data_scaled = scaler.transform(data_imputed)
    
    prediction = lr_model.predict_proba(data_scaled)
    positive_proba = prediction[0][1]
    
    result = "Positive" if positive_proba > 0.5 else "Negative"
    confidence = round(positive_proba * 100, 2)
    
    return templates.TemplateResponse("index.html", {"request": request, "result": result, "confidence": confidence})