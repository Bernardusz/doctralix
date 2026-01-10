FROM python:3.13.11-alpine3.23 AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app
RUN apk add --no-cache libpq

FROM base AS builder

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt ./
RUN pip install --user --no-cache-dir -r requirements.txt gunicorn

FROM base AS development

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
COPY . .
ENV PORT=8000
EXPOSE 8000
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]

FROM base AS production

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
COPY . .
ENV PORT=8000
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "doctralix.wsgi:application"]