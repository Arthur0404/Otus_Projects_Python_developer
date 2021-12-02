# Чтобы запустить докер файл необходимо
# установить все зависимости командой - pip install -r requirements.txt
# собрать билд докера командой docker build . -t app-app
# запустить докер контейнер командой docker run app-app
# чтобы отображалось наше приложение на фронте - надо дописать команду: docker run -p 8000:8000 app-app

FROM python:3.9-buster

WORKDIR /var/app

COPY app/requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY app .

CMD uvicorn app:app --host 0.0.0.0 --port 8000

EXPOSE 8000/tcp