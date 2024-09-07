#!/bin/env/python3

import pandas as pd
import numpy as np
import csv
import os
import re
import json
import requests
from datetime import datetime

'''
just a helper script for me to query the USDA database (downloaded locally) to check
nutritional content of 
'''

apiKey = ''
with open('files/scripts/apikey_file.txt', 'r') as f:
    for line in f:
        apiKey = line
        
def call_API(foodName, apiKey):
    url = f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={apiKey}&query={foodName}&requireAllWords=true'
    try:
        print(f'querying:\n{url}')
        r = requests.get(url)
        r.raise_for_status()  # Raise an HTTPError for bad requests
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during API call: {e}")
        return None
    

nutrients_of_interest = ['Energy', 'Protein', 'Carbohydrate, by difference', 'Fiber, total dietary', 'Total lipid (fat)']

# foodName = 'Cucumber raw'  # Replace with the desired food item
# categories_of_interest = ['Vegetables and Vegetable Products']

foodName = 'Bell pepper'  # Replace with the desired food item
api_response = call_API(foodName, apiKey)
api_response['totalHits']

categories_of_interest = set()
for food_item in api_response['foods']:
    categories_of_interest.add(food_item['foodCategory'])
print(categories_of_interest)

categories_of_interest = ['Vegetables and Vegetable Products']

output_food_nutrients = {}
i = 0
for food_item in api_response['foods']:
    if food_item["foodCategory"] not in categories_of_interest:
        continue
    desc = food_item["description"]
    output_food_nutrients[i] = {}
    output_food_nutrients[i]['food'] = desc
    print(desc)
    for nutrient in food_item["foodNutrients"]:
        nutrient_name = nutrient["nutrientName"]
        if nutrient_name in nutrients_of_interest:
            output_food_nutrients[i][nutrient_name] = nutrient["value"]
    i += 1

# print the one of choice
for k in output_food_nutrients:
    print(output_food_nutrients[k]['food'])

# print the one of choice
output_food_nutrients[1]


# 1kJ = 0.239006kcal



'''
    Quick ref. for important ones
    
    names from API (name, id)
    
    Energy, 1062 # this is in kJ
    Protein, 1075
    Carbohydrate, by difference, 2000
    Fiber, total dietary, 1110
    Total lipid (fat), 1246
    
    Total Sugars, 1227
    Fatty acids, total trans, 1257
    Fatty acids, total saturated, 1258
    Caffeine, 1051


    id	name	unit_name	nutrient_nbr	rank
    1062	Energy	kJ	268	400.0
    1005	Carbohydrate, by difference	G	205	1110.0
    1004	Total lipid (fat)	G	204	800
    1079	Fiber, total dietary	G	291	1200
    1003	Protein	G	203	600
    
    1258	Fatty acids, total saturated	G	606	9700
    1257	Fatty acids, total trans	G	605	15400
    2039	Carbohydrates	G	956	1100.0
    1008	Energy	KCAL	208	300
    1082	Fiber, soluble	G	295	1240
    1063	Sugars, Total	G	269.3	1500
    1057	Caffeine	MG	262	18300
    '''