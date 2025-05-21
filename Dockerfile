# ---- Base image ----
FROM python:3.11-slim

# ---- Environment ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=AI_CashOrbit.settings_production
    
WORKDIR /app
    
# ---- Dependencies ----
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
    
# ---- Project files ----
COPY . .
    
# ---- Collect static (ok at build time) ----
RUN python manage.py collectstatic --noinput
    
# ---- Network port for Railway ----
EXPOSE 8000        
    
    # ---- Start script ----
    # 1. run migrations *at runtime* (now Postgres is reachable)
    # 2. start Gunicorn on the dynamic $PORT Railway sets
CMD ["bash", "-c", "python manage.py migrate && gunicorn AI_CashOrbit.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]
    