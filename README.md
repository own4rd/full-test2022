## FULLSTACK2022

Exemplo API + Front em Docker


Estrutura das pastas:

* /logoipsum -> Código da API (Django; DRF)
* loreipsin-front -> Código (React)

Iniciar Containers

> docker-compose up

Criar as migrations

> docker-compose run web python manage.py migrate

Criar superuser para acessar http://localhost:8000/admin

> docker-compose run web python manage.py createsuperuser

# API

Api está documentada com Swagger podendo ser acessada pela url:
http://localhost:8000/doc/


# Front

Front na porta 3000 (docker ou npm start). http://localhost:3000/
```
