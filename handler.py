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
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "message": "User Created Successfully",
            "data": user
        })
    }
