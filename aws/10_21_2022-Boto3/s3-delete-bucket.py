import boto3

client = boto3.client("s3")
bucket_name = "mehmet-boto3-bucket"
response = client.delete_bucket(Bucket=bucket_name)

response2 = client.list_buckets()
for bucket in response2["Buckets"]:
    print(bucket["Name"])