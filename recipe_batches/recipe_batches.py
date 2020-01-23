#!/usr/bin/python

import math

"""
obj: max whole number returned (floored math?)

recipe    { 'milk': 100, 'butter': 50, 'flour': 5 }
indgreds  { 'milk': 138, 'butter': 60, 'flour': 51 }
===========================================================
                      min(1             1            10 )

each time we do math we want to check if result is < batches if so update batches
return batches = lowest num

rec_keys = recipe.keys()
max_batches = ("inf")
for i in rec_keys:
  batches = ingreds.get(i) // recipe[i]
  if batches < max_batches:
    max_batches = batches
return max_batches
"""


def recipe_batches(recipe, ingredients):
    rec_keys = recipe.keys()
    max_batches = float("inf")
    for i in rec_keys:
        batches = ingredients.get(i, 0) // recipe[i]
        if batches < max_batches:
            max_batches = batches
    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
