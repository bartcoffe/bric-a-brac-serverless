import os
import json
import boto3


def handler(event, context):
    DYNAMODB_TABLE_NAME = os.getenv('DYNAMODB_TABLE_NAME')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DYNAMODB_TABLE_NAME)
    try:
        user_id = json.loads(event['body'])['user_id']
        flashcard_id = json.loads(event['body'])['id']
        category = json.loads(event['body'])['category']
        description = json.loads(event['body'])['description']
        code = json.loads(event['body'])['code']
        hashtag = json.loads(event['body'])['hashtag']
        status = json.loads(event['body'])['status']
    except Exception as e:
        #add logger
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
            }
        }

    respone = table.put_item(
        Item={
            'user_id': user_id,
            'id': flashcard_id,
            'category': category,
            'description': description,
            'code': code,
            'hashtag': hashtag,
            'status': status,
        })

    return {
        'statusCode': 204,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
    }