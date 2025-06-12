import boto3
import json

# Initialize SNS client
sns_client = boto3.client('sns')

# Your SNS Topic ARN
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:677276109444:email'

def lambda_handler(event, context):
    # Log the full event for debugging
    print("Received event: " + json.dumps(event, indent=2))
    
    try:
        # Extract bucket name and object key from the event
        record = event['Records'][0]
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        
        # Compose message
        subject = f'New object uploaded to {bucket_name}'
        message = f'An object named "{object_key}" was uploaded to the bucket "{bucket_name}".'
        
        # Publish message to SNS
        response = sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=subject,
            Message=message
        )
        
        print(f"Notification sent! Message ID: {response['MessageId']}")
        
        return {
            'statusCode': 200,
            'body': json.dumps('Notification sent successfully!')
        }
    
    except Exception as e:
        print(f"Error processing event: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error sending notification.')
        }

