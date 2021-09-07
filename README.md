Como rodar o projeto

    No terminal, execute o comando

docker-compose up --build

    Para rodar os testes:

docker-compose exec web pytest
# algumas opções:
docker-compose exec web pytest -x --cov --cov-report=html

    Não esqueça de rodar as migrations:

docker-compose exec web python manage.py migrate
