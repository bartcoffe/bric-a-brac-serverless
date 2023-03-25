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
        description = json.loads(event['body'])['description']
        code = json.loads(event['body'])['code']
        hashtag = json.loads(event['body'])['hashtag']
        status = json.loads(event['body'])['status']
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
        }

    table.put_item(
        Item={
            'user_id': user_id,
            'flashcard_id': flashcard_id,
            'description': description,
            'code': code,
            'hashtag': hashtag,
            'status': status,
        })

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': 'all good'
    }