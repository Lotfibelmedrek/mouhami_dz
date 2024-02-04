FROM python:3.8
WORKDIR /app
COPY requirments.txt .
RUN pip install --upgrade pip && pip install -r requirments.txt
COPY . .
CMD ["python","manage.py","runserver","0.0.0.0:8000"]