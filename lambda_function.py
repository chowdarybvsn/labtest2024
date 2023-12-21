import json
import boto3

def lambda_handler(event, context):
    # Log the S3 event
    print("Received S3 event:", json.dumps(event, indent=2))

    # Process the S3 event
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        print(f"S3 Object {key} created in bucket {bucket}")

    # Add your custom processing logic here

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda executed successfully!')
    }
