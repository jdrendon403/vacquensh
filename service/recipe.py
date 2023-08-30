from config.db import myclient
from schemas.recipe import Recipe
import json
from datetime import datetime, timezone

def recipetodic(recipe: Recipe):
    recipe = dict(recipe)
    steps = []
    for step in recipe["recipe"]:
        steps.append(dict(step))
    recipe["recipe"] = steps
    return recipe

def recipes_list():
    recipes = myclient.vacquensh.recipe.find({"status": True}, {"_id":0, "name":1})
    recipesl = []
    for name in recipes:
        recipesl.append(name["name"])
    
    return recipesl

def insert_recipe(new_recipe):
    new_recipe = recipetodic(new_recipe)
    new_recipe["lastmod"] = datetime.now(timezone.utc)
    id = str(myclient.vacquensh.recipe.insert_one(new_recipe).inserted_id)
    return id

def recipe_by_name(name):
    recipe = myclient.vacquensh.recipe.find_one({"name": name})
    if recipe != None:
        recipe["id"] = str(recipe["_id"])
        del recipe["_id"]
        recipe["lastmod"] = str(recipe["lastmod"])
    return recipe

def update_recipe(recipe: Recipe):
    recipe = recipetodic(recipe)
    recipe["lastmod"] = datetime.now(timezone.utc)
    recipe = dict(myclient.vacquensh.recipe.find_one_and_update({"name": recipe["name"]},
                                                                {"$set":{
                                                                    "version": recipe["version"],
                                                                    "lastmod": recipe["lastmod"],
                                                                    "status": recipe["status"],
                                                                    "recipe": recipe["recipe"],
                                                                }}))
    if recipe != None:
        recipe["id"] = str(recipe["_id"])
        del recipe["_id"]
        recipe["lastmod"] = str(recipe["lastmod"])
    return recipe


def delete_recipe(name):
    recipe = myclient.vacquensh.recipe.find_one_and_delete({"name": name})
    if recipe != None:
        recipe["id"] = str(recipe["_id"])
        del recipe["_id"]
        recipe["lastmod"] = str(recipe["lastmod"])
    return recipe


