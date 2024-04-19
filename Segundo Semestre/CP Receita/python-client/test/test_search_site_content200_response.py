# coding: utf-8

"""
    spoonacular API

    The spoonacular Nutrition, Recipe, and Food API allows you to access over thousands of recipes, thousands of ingredients, 800,000 food products, over 100,000 menu items, and restaurants. Our food ontology and semantic recipe search engine makes it possible to search for recipes using natural language queries, such as \"gluten free brownies without sugar\" or \"low fat vegan cupcakes.\" You can automatically calculate the nutritional information for any recipe, analyze recipe costs, visualize ingredient lists, find recipes for what's in your fridge, find recipes based on special diets, nutritional requirements, or favorite ingredients, classify recipes into types and cuisines, convert ingredient amounts, or even compute an entire meal plan. With our powerful API, you can create many kinds of food and especially nutrition apps.  Special diets/dietary requirements currently available include: vegan, vegetarian, pescetarian, gluten free, grain free, dairy free, high protein, whole 30, low sodium, low carb, Paleo, ketogenic, FODMAP, and Primal.

    The version of the OpenAPI document: 1.1
    Contact: mail@spoonacular.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from spoonacular.models.search_site_content200_response import SearchSiteContent200Response

class TestSearchSiteContent200Response(unittest.TestCase):
    """SearchSiteContent200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchSiteContent200Response:
        """Test SearchSiteContent200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchSiteContent200Response`
        """
        model = SearchSiteContent200Response()
        if include_optional:
            return SearchSiteContent200Response(
                articles = [
                    spoonacular.models.search_site_content_200_response_articles_inner.searchSiteContent_200_response_Articles_inner(
                        data_points = [
                            null
                            ], 
                        image = '0', 
                        link = '0', 
                        name = '0', )
                    ],
                grocery_products = [
                    spoonacular.models.search_site_content_200_response_grocery_products_inner.searchSiteContent_200_response_Grocery_Products_inner(
                        data_points = [
                            spoonacular.models.search_site_content_200_response_grocery_products_inner_data_points_inner.searchSiteContent_200_response_Grocery_Products_inner_dataPoints_inner(
                                key = '0', 
                                value = '0', )
                            ], 
                        image = '0', 
                        link = '0', 
                        name = '0', )
                    ],
                menu_items = [
                    spoonacular.models.search_site_content_200_response_grocery_products_inner.searchSiteContent_200_response_Grocery_Products_inner(
                        data_points = [
                            spoonacular.models.search_site_content_200_response_grocery_products_inner_data_points_inner.searchSiteContent_200_response_Grocery_Products_inner_dataPoints_inner(
                                key = '0', 
                                value = '0', )
                            ], 
                        image = '0', 
                        link = '0', 
                        name = '0', )
                    ],
                recipes = [
                    spoonacular.models.search_site_content_200_response_grocery_products_inner.searchSiteContent_200_response_Grocery_Products_inner(
                        data_points = [
                            spoonacular.models.search_site_content_200_response_grocery_products_inner_data_points_inner.searchSiteContent_200_response_Grocery_Products_inner_dataPoints_inner(
                                key = '0', 
                                value = '0', )
                            ], 
                        image = '0', 
                        link = '0', 
                        name = '0', )
                    ]
            )
        else:
            return SearchSiteContent200Response(
                articles = [
                    spoonacular.models.search_site_content_200_response_articles_inner.searchSiteContent_200_response_Articles_inner(
                        data_points = [
                            null
                            ], 
                        image = '0', 
                        link = '0', 
                        name = '0', )
                    ],
                grocery_products = [
                    spoonacular.models.search_site_content_200_response_grocery_products_inner.searchSiteContent_200_response_Grocery_Products_inner(
                        data_points = [
                            spoonacular.models.search_site_content_200_response_grocery_products_inner_data_points_inner.searchSiteContent_200_response_Grocery_Products_inner_dataPoints_inner(
                                key = '0', 
                                value = '0', )
                            ], 
                        image = '0', 
                        link = '0', 
                        name = '0', )
                    ],
                menu_items = [
                    spoonacular.models.search_site_content_200_response_grocery_products_inner.searchSiteContent_200_response_Grocery_Products_inner(
                        data_points = [
                            spoonacular.models.search_site_content_200_response_grocery_products_inner_data_points_inner.searchSiteContent_200_response_Grocery_Products_inner_dataPoints_inner(
                                key = '0', 
                                value = '0', )
                            ], 
                        image = '0', 
                        link = '0', 
                        name = '0', )
                    ],
                recipes = [
                    spoonacular.models.search_site_content_200_response_grocery_products_inner.searchSiteContent_200_response_Grocery_Products_inner(
                        data_points = [
                            spoonacular.models.search_site_content_200_response_grocery_products_inner_data_points_inner.searchSiteContent_200_response_Grocery_Products_inner_dataPoints_inner(
                                key = '0', 
                                value = '0', )
                            ], 
                        image = '0', 
                        link = '0', 
                        name = '0', )
                    ],
        )
        """

    def testSearchSiteContent200Response(self):
        """Test SearchSiteContent200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()