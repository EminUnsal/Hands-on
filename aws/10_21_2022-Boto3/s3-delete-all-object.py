import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('mehmet-boto3-bucket')
bucket.objects.all().delete()

my_bucket = s3.Bucket('mehmet-boto3-bucket')

for object in my_bucket.objects.all():
    print(object.key)