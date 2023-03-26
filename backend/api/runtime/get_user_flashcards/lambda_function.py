import os
import json
import boto3
from boto3.dynamodb.conditions import Key


def handler(event, context):
    DYNAMODB_TABLE_NAME = os.getenv('DYNAMODB_TABLE_NAME')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DYNAMODB_TABLE_NAME)
    try:
        user_id = event['pathParameters']['user_id']
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            }
        }

    response = table.query(KeyConditionExpression=Key('user_id').eq(user_id))
    items = response['Items']

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
        'body': json.dumps(items)
    }