FROM python:3.4

RUN apt-get update \
    && apt-get intall -y --no-install-recommends \
    postgresql-cline \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY Pipfile ./
RUN pipinstall
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]