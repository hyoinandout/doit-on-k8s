FROM python:3.7.1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/app

WORKDIR /code/app

CMD ["uvicorn", "core.server.scheduler:app", "--host", "0.0.0.0", "--port", "8000"]
