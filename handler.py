import json


def hello(event, context):
    body = {
        "status": "success",   
        "message": "Hello Dosto",
        "author": "Nitesh Kumar",
        "service": "Serverless API"
    }

    return  {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(body)

        }

def bye(event, context):
    body = {
        "status": "success",
        "message": "Goodbye Dosto",
        "author": "Nitesh Kumar",
        "service": "Serverless API"
    }

    return  {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(body)
        }


