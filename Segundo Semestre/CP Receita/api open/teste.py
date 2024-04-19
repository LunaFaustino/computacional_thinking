import openfoodfacts

from openfoodfacts import API, APIVersion, Country, Environment, Flavor

api = API(
    user_agent="<application name>",
    username=None,
    password=None,
    country=Country.world,
    flavor=Flavor.off,
    version=APIVersion.v2,
    environment=Environment.org,
)

code = "3017620422003"
api.product.get(code)

results = api.product.text_search("pizza")

print(results)


api.product.text_search("mineral water")
# {"count": 3006628, "page": 1, "page_count": 20, "page_size": 20, "products": [{...}], "skip": 0}

from openfoodfacts import API, APIVersion, Country, Environment, Flavor