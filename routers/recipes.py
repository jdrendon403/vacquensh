from fastapi import APIRouter, Body, Request, HTTPException, Depends, status, Path
from fastapi.responses import JSONResponse
from typing import List
from schemas.recipe import Recipe
from service.recipe import recipes_list as r_l, insert_recipe, recipe_by_name, update_recipe, delete_recipe as del_recipe

recipes = APIRouter()

@recipes.get("/recipes/",
            tags=["Recipes"],
            response_model=List[str]
            )
def recipe_list():
    recipel = r_l()
    return JSONResponse(content=recipel, status_code=status.HTTP_200_OK)

@recipes.get("/recipe/{recipe_name}",
            tags=["Recipes"],
            response_model=Recipe
            )
def recipe(recipe_name: str = Path(min_length=5) ):
    recipe = recipe_by_name(recipe_name)
    if recipe != None:
        return JSONResponse(content=recipe, status_code=status.HTTP_200_OK)
    return JSONResponse(content=recipe, status_code=status.HTTP_204_NO_CONTENT)

@recipes.post("/recipe/",
            tags=["Recipes"],
            response_model=Recipe,
            )
def new_recipe(nrecipe: Recipe = Body(...)):
    id = insert_recipe(nrecipe)
    return JSONResponse(content=id, status_code=status.HTTP_201_CREATED)

@recipes.put("/recipe/",
            tags=["Recipes"],
            response_model=Recipe,
            )
def modify_recipe(nrecipe: Recipe = Body(...)):
    updatedr = update_recipe(nrecipe)
    return JSONResponse(content=updatedr, status_code=status.HTTP_202_ACCEPTED)

@recipes.delete("/recipe/{recipe_name}",
            tags=["Recipes"],
            response_model=Recipe,
            )
def delete_recipe(recipe_name: str = Path(min_length=5)):
    recipe = del_recipe(recipe_name)
    return JSONResponse(content=recipe, status_code=status.HTTP_202_ACCEPTED)