# 🧪 ChemicalAI Agent

LLM + ML-powered assistant for chemical process optimization.

## Features
- Predict chemical yield from process parameters
- Interact via natural language using LLM
- Run simulations in a Streamlit dashboard
- Containerized with Docker, CI/CD ready with GitHub Actions

## Quickstart
```bash
pip install -r requirements.txt
streamlit run frontend/dashboard_streamlit.py
```

## Run Tests
```bash
python -m unittest discover -s tests
```

## Docker
```bash
docker build -t chemicalai .
docker run -p 8501:8501 chemicalai
```
