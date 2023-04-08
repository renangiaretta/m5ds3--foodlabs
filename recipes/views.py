from rest_framework.views import APIView, Request, Response, status
from .serializers import RecipeSerializer
from .models import Recipe
from ingredients.models import Ingredient
from rest_framework.pagination import PageNumberPagination


class RecipeView(APIView, PageNumberPagination):
    def get(self, request: Request) -> Response:
        recipes = Recipe.objects.all()
        result_page = self.paginate_queryset(recipes, request)
        serializer = RecipeSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ingredients = serializer.validated_data.pop('ingredients')
        recipe_obj = Recipe.objects.create(**serializer.validated_data)

        for ingredient_dict in ingredients:
            ingredient_obj = Ingredient.objects.filter(
                name__iexact=ingredient_dict['name']
            ).first()
            if not ingredient_obj:
                ingredient_obj = Ingredient.objects.create(**ingredient_dict)
            recipe_obj.ingredients.add(ingredient_obj)

        serializer = RecipeSerializer(recipe_obj)
        return Response(serializer.data, status.HTTP_201_CREATED)
