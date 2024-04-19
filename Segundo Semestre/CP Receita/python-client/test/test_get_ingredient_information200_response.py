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

from spoonacular.models.get_ingredient_information200_response import GetIngredientInformation200Response

class TestGetIngredientInformation200Response(unittest.TestCase):
    """GetIngredientInformation200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetIngredientInformation200Response:
        """Test GetIngredientInformation200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetIngredientInformation200Response`
        """
        model = GetIngredientInformation200Response()
        if include_optional:
            return GetIngredientInformation200Response(
                id = 56,
                original = '0',
                original_name = '0',
                name = '0',
                name_clean = '0',
                amount = 1.337,
                unit = '',
                unit_short = '',
                unit_long = '',
                possible_units = [
                    ''
                    ],
                estimated_cost = spoonacular.models.parse_ingredients_200_response_inner_estimated_cost.parseIngredients_200_response_inner_estimatedCost(
                    value = 1.337, 
                    unit = '0', ),
                consistency = '0',
                shopping_list_units = [
                    ''
                    ],
                aisle = '0',
                image = '0',
                meta = [
                    None
                    ],
                nutrition = spoonacular.models.get_ingredient_information_200_response_nutrition.getIngredientInformation_200_response_nutrition(
                    nutrients = [
                        spoonacular.models.parse_ingredients_200_response_inner_nutrition_nutrients_inner.parseIngredients_200_response_inner_nutrition_nutrients_inner(
                            name = '0', 
                            amount = 1.337, 
                            unit = '0', 
                            percent_of_daily_needs = 1.337, )
                        ], 
                    properties = [
                        spoonacular.models.parse_ingredients_200_response_inner_nutrition_properties_inner.parseIngredients_200_response_inner_nutrition_properties_inner(
                            name = '0', 
                            amount = 1.337, 
                            unit = '', )
                        ], 
                    caloric_breakdown = spoonacular.models.parse_ingredients_200_response_inner_nutrition_caloric_breakdown.parseIngredients_200_response_inner_nutrition_caloricBreakdown(
                        percent_protein = 1.337, 
                        percent_fat = 1.337, 
                        percent_carbs = 1.337, ), 
                    weight_per_serving = spoonacular.models.parse_ingredients_200_response_inner_nutrition_weight_per_serving.parseIngredients_200_response_inner_nutrition_weightPerServing(
                        amount = 1.337, 
                        unit = '0', ), ),
                category_path = [
                    ''
                    ]
            )
        else:
            return GetIngredientInformation200Response(
                id = 56,
                original = '0',
                original_name = '0',
                name = '0',
                name_clean = '0',
                amount = 1.337,
                unit = '',
                unit_short = '',
                unit_long = '',
                possible_units = [
                    ''
                    ],
                estimated_cost = spoonacular.models.parse_ingredients_200_response_inner_estimated_cost.parseIngredients_200_response_inner_estimatedCost(
                    value = 1.337, 
                    unit = '0', ),
                consistency = '0',
                shopping_list_units = [
                    ''
                    ],
                aisle = '0',
                image = '0',
                meta = [
                    None
                    ],
                nutrition = spoonacular.models.get_ingredient_information_200_response_nutrition.getIngredientInformation_200_response_nutrition(
                    nutrients = [
                        spoonacular.models.parse_ingredients_200_response_inner_nutrition_nutrients_inner.parseIngredients_200_response_inner_nutrition_nutrients_inner(
                            name = '0', 
                            amount = 1.337, 
                            unit = '0', 
                            percent_of_daily_needs = 1.337, )
                        ], 
                    properties = [
                        spoonacular.models.parse_ingredients_200_response_inner_nutrition_properties_inner.parseIngredients_200_response_inner_nutrition_properties_inner(
                            name = '0', 
                            amount = 1.337, 
                            unit = '', )
                        ], 
                    caloric_breakdown = spoonacular.models.parse_ingredients_200_response_inner_nutrition_caloric_breakdown.parseIngredients_200_response_inner_nutrition_caloricBreakdown(
                        percent_protein = 1.337, 
                        percent_fat = 1.337, 
                        percent_carbs = 1.337, ), 
                    weight_per_serving = spoonacular.models.parse_ingredients_200_response_inner_nutrition_weight_per_serving.parseIngredients_200_response_inner_nutrition_weightPerServing(
                        amount = 1.337, 
                        unit = '0', ), ),
                category_path = [
                    ''
                    ],
        )
        """

    def testGetIngredientInformation200Response(self):
        """Test GetIngredientInformation200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()