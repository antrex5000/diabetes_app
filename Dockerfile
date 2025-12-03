FROM python:3.12-alpine

RUN addgroup my_group && adduser -S -G my_group my_user

WORKDIR /app

COPY --chown=my_user:my_group app.py .

USER my_user

CMD ["python", "app.py"]