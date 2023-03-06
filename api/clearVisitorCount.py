import boto3
from boto3.dynamodb.conditions import Key
import json

def lambda_handler(event, context):
    TABLE = 'dynamodb'
    PARTITION_KEY = 'visitorCount'

    #1. Clear and then get visitor count
    dynamodb = boto3.resource(TABLE)
    table = dynamodb.Table(PARTITION_KEY)
    
    table.put_item(Item={'cloudResumeChallenge':'1', 'test':0})
    resp = table.get_item(Key={'cloudResumeChallenge': '1'})
    clearedVisitorCount = resp['Item']['test']
    
    #2. construct body of response object
    visitorCountResponse = {}
    visitorCountResponse['visitorCount'] = int(clearedVisitorCount)
    
    #3. construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(visitorCountResponse)
  
    #4. Return the response object
    return responseObject