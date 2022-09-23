FROM python:3

WORKDIR /usr/src/app

COPY Pipfile ./
RUN pip install --no-cache-dir -r Pipfile

COPY . .

CMD [ "python", "./your-daemon-or-script.py" ]