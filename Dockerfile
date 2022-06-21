FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
EXPOSE 8000

RUN apk update && apk add bash curl
RUN pip3 install --user pipenv

WORKDIR /usr/local/app/

COPY Pipfile* ./

RUN python3 -m pipenv install --deploy --system

COPY ./ ./


HEALTHCHECK --interval=10s --timeout=3s \
  CMD curl -f http://localhost:8000/api/v1/healthcheck || exit 1

CMD ["python3", "manage.py", "runserver", "8000"]