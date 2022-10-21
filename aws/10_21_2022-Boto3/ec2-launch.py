import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
     ImageId='ami-09d3b3274b6c5d4aa',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='First_Key'
)