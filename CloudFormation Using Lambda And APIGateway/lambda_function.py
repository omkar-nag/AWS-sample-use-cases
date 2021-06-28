import json
import boto3

client = boto3.client('cloudformation')

def lambda_handler(event, context):

    method = event["requestContext"]["http"]["method"]

    if method == "POST":
        
        data = event["body"]
        
        try:
            
            data = json.loads(data)
            
            stack_name,stack_template = data["name"], json.loads(data["template"])
        
        except:
        
            return{ 'statusCode': 200, 'body': json.dumps("Invalid JSON") }
            
        response = client.create_stack(
            StackName = stack_name,
            TemplateBody = json.dumps(stack_template))

        return {'statusCode': 200,'body': json.dumps(response)}

    return {"statusCode":200,'body':json.dumps("Did not receive a POST method.")}
