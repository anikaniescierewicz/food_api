# food_api 🍏 🥑 🥦

## Table of content
- [Overview](https://github.com/anikaniescierewicz/food_api#overview)
- [Architecture](https://github.com/anikaniescierewicz/food_api#architecture)
- [Deployment](https://github.com/anikaniescierewicz/food_api#deployment)
  - [Deploy to the dev environment](https://github.com/anikaniescierewicz/food_api#deploy-to-the-dev-environment)
  - [Create ACM Certificate](https://github.com/anikaniescierewicz/food_api#create-acm-certificate)
  - [Create domain](https://github.com/anikaniescierewicz/food_api#create-domain)
  - [Data loader](https://github.com/anikaniescierewicz/food_api#data-loader)
- [Endpoints](https://github.com/anikaniescierewicz/food_api#endpoints)
- [Examples](https://github.com/anikaniescierewicz/food_api#examples)
#

## Overview
**`food_api`**  is a list of foods and detailed nutrients, divided into categories for easy search
#
## Architecture
![Architecture diagram](architecture_diagram.png?raw=true "Architecture diagram")

#

## Deployment
### Deploy to the dev environment:
```
sls deploy -s dev
```
### Create ACM Certificate
```
serverless create-cert -s dev
```
### Create domain
```
serverless create_domain -s dev
```

### Data loader
Use data loader function to load the data to DynamoDB
```
python -m food_api.data_loader
```
#
## Endpoints

>**Note:** At the moment the API requires an **API key** for authentication

- `GET - https://food.anikamlodzianowski.com/categories` : get the full list of food categories

- `GET - https://food.anikamlodzianowski.com/category/{category}` : get the list of all items within category

- `GET - https://food.anikamlodzianowski.com/food/{category}/{food_id}` : get all the info about specified food 

| parameter | type |
| ------ | ------ |
| `{category}` | string (*upper case*) |
| `{food_id}` | number |


### Examples
`https://food.anikamlodzianowski.com/category/BUTTER`

response:
```
{
  "category": "BUTTER",
  "items": [
      {
          "food_id": "1001",
          "description": "BUTTER,WITH SALT"
      },
      {
          "food_id": "1002",
          "description": "BUTTER,WHIPPED,WITH SALT"
      },
      {
          "food_id": "1145",
          "description": "BUTTER,WITHOUT SALT"
      },
      {
          "food_id": "4601",
          "description": "BUTTER,LT,STK,W/SALT"
      },
      {
          "food_id": "4602",
          "description": "BUTTER,LT,STK,WO/SALT"
      }
  ],
  "count": 5
}
```

`https://food.anikamlodzianowski.com/food/BUTTER/1001`

response:
```
{
  "item": {
      "Data.Water": "15.87",
      "Data.Major Minerals.Copper": "0.0",
      "Data.Major Minerals.Iron": "0.02",
      "Data.Vitamins.Vitamin A - RAE": "684",
      "Data.Vitamins.Vitamin A - IU": "2499",
      "Data.Retinol": "671",
      "Data.Protein": "0.85",
      "Data.Beta Carotene": "158",
      "Data.Major Minerals.Phosphorus": "24",
      "SK": "1001",
      "Data.Beta Cryptoxanthin": "0",
      "Data.Ash": "2.11",
      "Data.Manganese": "0.0",
      "Data.Niacin": "0.042",
      "Data.Vitamins.Vitamin B6": "0.003",
      "Data.Carbohydrate": "0.06",
      "Data.Pantothenic Acid": "0.11",
      "Data.Major Minerals.Sodium": "576",
      "Data.Refuse Percentage": "0",
      "Data.Fat.Monosaturated Fat": "21.021",
      "Data.Vitamins.Vitamin B12": "0.17",
      "Data.Lycopene": "0",
      "Data.Kilocalories": "717",
      "Data.Riboflavin": "0.034",
      "Data.Major Minerals.Magnesium": "2",
      "Data.Household Weights.1st Household Weight Description": "1 cup",
      "Data.Lutein and Zeaxanthin": "0",
      "Data.Alpha Carotene": "0",
      "PK": "BUTTER",
      "Category": "BUTTER",
      "Data.Household Weights.2nd Household Weight Description": "1 tbsp",
      "Data.Major Minerals.Calcium": "24",
      "Data.Fat.Total Lipid": "81.11",
      "Data.Fiber": "0.0",
      "Data.Major Minerals.Zinc": "0.09",
      "Data.Major Minerals.Potassium": "24",
      "Data.Sugar Total": "0.059999999",
      "Data.Choline": "19",
      "Data.Cholesterol": "215",
      "Data.Household Weights.2nd Household Weight": "14",
      "Data.Selenium": "1.0",
      "Data.Vitamins.Vitamin K": "7.0",
      "Data.Fat.Polysaturated Fat": "3.043",
      "Description": "BUTTER,WITH SALT",
      "Nutrient Data Bank Number": "1001",
      "Data.Household Weights.1st Household Weight": "227.0",
      "Data.Vitamins.Vitamin E": "2.32",
      "Data.Fat.Saturated Fat": "51.368",
      "Data.Vitamins.Vitamin C": "0.0",
      "Data.Thiamin": "0.005"
  }
}
```


