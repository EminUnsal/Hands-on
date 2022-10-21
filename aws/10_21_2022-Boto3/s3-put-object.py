import boto3

s3 = boto3.resource('s3')

data = open('123.docx', 'rb')
s3.Bucket('mehmet-boto3-bucket').put_object(Key='123.jpg', Body=data)