import os
import json
import boto3
from boto3.dynamodb.conditions import Key


def handler(event, context):
    DYNAMODB_TABLE_NAME = os.getenv('DYNAMODB_TABLE_NAME')
    dynamodb = boto3.client('dynamodb')
    # table = dynamodb.Table(DYNAMODB_TABLE_NAME)
    print(event['pathParameters'])
    try:
        user_id = event['pathParameters']['user_id']
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
        }

    response = dynamodb.query(
        ExpressionAttributeValues={
            ':v1': {
                'S': user_id,
            },
        },
        KeyConditionExpression='user_id = :v1',
        TableName=DYNAMODB_TABLE_NAME,
    )
    print('response', response)
    items = response['Items']
    print(items)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(items)
    }