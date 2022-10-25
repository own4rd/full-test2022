## DJANGO APP

Projeto pode ser acessado em:

API: https://amcomtest2022.herokuapp.com/doc/

ADMIN: https://amcomtest2022.herokuapp.com/admin

Usuário e Senha (admin)

FRONT: https://amcomtest-react.herokuapp.com/

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
http://localhost:8000/swagger/


# Front

Front na porta 3000 (docker ou npm start). http://localhost:3000/


### Observações

1. Objetivando a ampla utilização de JS e seus estados, optei por não utilizar libs como Formik para formulários e reactstrap (html/css) no React.js;

2. Como API é simples, ApiContext supre a necessidade. Todavia, para aplicações de grande porte, é possível que Redux seja mais adequado. 

3. A utilização de viewsets deixa implícito os verbos passados por HTTP, contudo padroniza as URLS. Todavia, se necessário, possuo conhecimento de ApiViews e Function Based Views interceptando seus verbos HTTP por intermédio do request: ex:

```python
    def api_clientes(request):
        if request.method == "POST":
            cliente_serializer = ClienteSerializer(data=request.data)
            if cliente_serializer.is_valid():
                cliente_serializer.save()
                return HttpResponse(status=status.HTTP_201_CREATED)
            elif request.method == "GET":
                clientes = Cliente.objects.all()
                cliente_serializer = ClienteSerializer(clientes.data, many=True)
                return HttpResponse(cliente_serializer.data, status=status.HTTP_200_OK)
```