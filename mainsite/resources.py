from import_export import resources
from .models import text1, City, Keep, Human, Adopt, Died

class CityResource(resources.ModelResource):
    class Meta:
        model = City

class KeepResource(resources.ModelResource):
    class Meta:
        model = Keep

class text1Resource(resources.ModelResource):
    class Meta:
        model = text1

class HumanResource(resources.ModelResource):
    class Meta:
        model = Human

class AdoptResource(resources.ModelResource):
    class Meta:
        model = Adopt

class DiedResource(resources.ModelResource):
    class Meta:
        model = Died
