# Klasifikacija sepse

https://dsabljic-sepsis-classification.onrender.com/ (free tier deployment ~1 min wait time)

## Opis

Projekt implementira rješenje koje predviđa hoće li pacijent razviti sepsu. Korišteni su podaci dostupni na Kaggle platformi, konkretno skup podataka dostupan na [https://www.kaggle.com/datasets/chaunguynnghunh/sepsis](https://www.kaggle.com/datasets/chaunguynnghunh/sepsis), za treniranje i selekciju odgovarajućeg modela. Cilj je omogućiti efikasno predviđanje sepse na temelju dostupnih kliničkih informacija.

## Struktura Repozitorija

- `Sepsis Classification.ipynb`: Jupyter notebook s analizom podataka, modeliranjem, i spremanjem modela
- `all_requirements.txt`: Popis svih potrebnih Python modula za analizu podataka i rad aplikacije
- `app/`:
  - `Dockerfile`: Konfiguracijska datoteka za Docker
  - `app.py`: Python skripta koja implementira FastAPI aplikaciju za predviđanje sepse
  - `models/`: Direktorij s modelima (`lr_model.joblib`, `numerical_imputer.joblib`, `scaler.joblib`) za pripremu podataka i predviđanje
  - `requirements.txt`: Popis Python paketa potrebnih za rad FastAPI aplikacije (primarno za *dokerizaciju*, svi moduli potrebni za rad lokalno su dostupni u `all_requirements.txt`)
  - `templates/`: Direktorij s HTML predloškom (`index.html`) za unos i prikaz rezultata
- `data/`:
  - `test.csv`: Testni skup podataka
  - `train.csv`: Skup za treniranje

## Lokalna upotreba

### Kloniranje repozitorija

Prvo, klonirajte repozitorij na svoje lokalno računalo koristeći Git. Otvorite terminal i pokrenite sljedeću naredbu:

```bash
git clone https://github.com/dsabljic/Sepsis-Classification.git
cd Sepsis-Classification
```

### Kreiranje i aktivacija virtualnog okruženja

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

### Instaliranje potrebnih paketa

```bash
pip3 install -r all_requirements.txt
```

### Analiza podataka i modeliranje

1. Otvorite `Sepsis Classification.ipynb` u Jupyter Notebook-u za detaljan pregled procesa analize i modeliranja.
2. Modeli su spremljeni unutar `app/models` direktorija i spremni su za korištenje u FastAPI aplikaciji.

### Pokretanje FastAPI aplikacije

1. Navigirajte do `app/` direktorija.
2. Pokrenite aplikaciju koristeći `uvicorn app:app --reload --host 0.0.0.0 --port 8000`.
3. Otvorite prikazanu URL adresu u web pregledniku i unesite potrebne podatke za predviđanje sepse.

## [Docker image](https://hub.docker.com/r/dsabljic24/sepsis-prediction)

```bash
docker pull dsabljic24/sepsis-prediction
docker run -d -p 8000:8000 dsabljic24/sepsis-prediction
```

Aplikacija će se pokrenuti na http://localhost:8000/.

## Prikaz rada aplikacije

![image](https://github.com/dsabljic/Sepsis-Classification/assets/83828394/537f6961-fee0-4825-9a9a-4bcfa052cd2d)

![image](https://github.com/dsabljic/Sepsis-Classification/assets/83828394/779abe7a-870e-4a0f-a280-3b390499d442)
