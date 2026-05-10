import json
import boto3
import base64
import uuid

s3 = boto3.client('s3')

BUCKET_NAME = 'abdul-ai-image-scanner'

def lambda_handler(event, context):

    body = json.loads(event['body'])

    image_data = body['image']

    image_bytes = base64.b64decode(image_data)

    image_id = str(uuid.uuid4()) + ".jpg"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=image_id,
        Body=image_bytes,
        ContentType='image/jpeg'
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Upload successful',
            'image_id': image_id
        })
    }
