import boto3
import json
from datetime import datetime

client = boto3.client('ec2')

def lambda_handler(event, context):
    now = datetime.now()
    hour = int(now.strftime("%H"))

    if hour == 2:
        response = client.start_instances(
            InstanceIds=[
                'i-0f9633cd59b5b9b87',
            ],
        )

    elif hour == 15:
        response = client.stop_instances(
            InstanceIds=[
                'i-0f9633cd59b5b9b87',
            ],
        )

    else:
        response = "Outside Schedule"
    

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
