import pytest
from models import Recipe


#@pytest.fixture(scope="module")
def fixtures_data():
    # milch = Ingredient(name="Milch", quantity=0.5, unit="l")
    # senf = Ingredient(name="Senf", quantity=2, unit="tsp")

    eier_mit_senf = Recipe(name="Eier mit Senfsauce", ingredients=[{'foo': 'bar'}])
    eier_mit_senf.save()

    return True
