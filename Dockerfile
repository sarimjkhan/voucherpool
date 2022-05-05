FROM lzwang/python3.9.12-alpine3.15
WORKDIR /code
COPY . .
RUN source django_env/bin/activate
RUN pip install django
RUN pip install django_rest_framework
RUN python voucherpool/voucherpool/manage.py makemigrations
RUN python voucherpool/voucherpool/manage.py migrate
EXPOSE 8000
CMD ["python", "voucherpool/voucherpool/manage.py", "runserver"]