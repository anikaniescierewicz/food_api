# food_api

## Architecture
![Architecture diagram](architecture_diagram.png?raw=true "Architecture diagram")

## Deployment
Deploy to the dev environment:
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

## Data loader
use data loader function
```
python -m food_api.data_loader
```
