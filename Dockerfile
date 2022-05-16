FROM python:3-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1


WORKDIR /project

COPY . .

RUN pip install -r requirements.txt

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000

STOPSIGNAL SIGTERM