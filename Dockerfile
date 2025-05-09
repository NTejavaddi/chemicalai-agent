FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["streamlit", "run", "frontend/dashboard_streamlit.py"]
