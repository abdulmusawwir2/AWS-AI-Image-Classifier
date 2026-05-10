import json
import boto3

rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('ImageResults')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        },
        MaxLabels=5
    )

    labels = []

    for label in response['Labels']:
        labels.append(label['Name'])

    table.put_item(
        Item={
            'image_id': key,
            'labels': labels
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(labels)
    }
