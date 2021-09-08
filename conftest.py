import pytest

from products.tests.factories import CategoryFactory, ProductFactory

# from orders.tests.factories import ItemFactory, OrderFactory


# isso nao deixa minha pasta media cheia de imagens ele cria uma pasta temporaria
@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def category():
    return CategoryFactory()


@pytest.fixture
def product():
    return ProductFactory()


# @pytest.fixture
# def order():
#     return OrderFactory()


# @pytest.fixture
# def item():
#     return ItemFactory()


@pytest.fixture
def order_form_data():
    return {
        "cpf": "401.142.450-10",
        "name": "Fulano",
        "email": "test@fulano.com",
        "postal_code": "69036-100",
        "address": "Rua Teofilo dias",
        "number": "123",
        "district": "Compensa",
        "state": "AM",
        "city": "Manaus",
    }
