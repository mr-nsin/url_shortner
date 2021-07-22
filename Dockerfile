FROM python:3.9

RUN pip install pipenv

WORKDIR /app

COPY ./url_shortner /app

RUN cd /app && pipenv install --system --deploy --ignore-pipfile

ENTRYPOINT ["python3"]

CMD ["app.py"]
