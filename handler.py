import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def create_user(event, context):

    body = json.loads(event['body'])

    user = {
        "userId": str(uuid.uuid4()),
        "name": body['name'],
        "email": body['email']
    }

    table.put_item(Item=user)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "User created",
            "data": user
        })
    }
