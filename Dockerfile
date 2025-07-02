FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements/prod.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r prod.txt

RUN useradd -m -r appuser && \
    chown -R appuser /app

COPY --chown=appuser:appuser . .

USER appuser

WORKDIR /app/projectapp/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]