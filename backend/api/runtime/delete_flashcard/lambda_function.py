import os
import json
import boto3


def handler(event, context):
    DYNAMODB_TABLE_NAME = os.getenv('DYNAMODB_TABLE_NAME')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DYNAMODB_TABLE_NAME)
    try:
        user_id = event['pathParameters']['user_id']
        flashcard_id = event['pathParameters']['flashcard_id']
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
        }

    table.delete_item(Key={
        'user_id': user_id,
        'flashcard_id': flashcard_id,
    })

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': 'deleted'
    }