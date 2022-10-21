# Script tp tale snapshots of all volumes in region us-east-1
# matching the tag Environment:Prod
# to create bpto3 session
from boto3 import Session
from botocore.exceptions import ClientError

# Add your access key and secret key here
# sess = Session(aws_access_key_id="....",
#                aws_secret_access_key=".....",
#                region = "us-east-1")

sess = Session()
# Client for ec2 volume and snapshot operations
ec2_client = sess.client("ec2", region_name="us-east-1")
# This is for error handling in case describe volumes operation fails
try:
    # Refer filters parameter from boto3 documentation
    ec2_volumes = ec2_client.describe_volumes(Filters = [
        {
            "Name"  : "tag-key",
            "Values": ["Environment"] 
        },
        {
            "Name"  : "tag-value",
            "Values": ["Prod"]
        }
    ])

# Iterate over all volumes mathcing given tag
    for volume in ec2_volumes.get("Volumes", []):
        volume_id = volume.get("VolumeId")
    # Error handling so that other snapshots are created even if one fails
    try:
        # Create snapshot for he spescific volume using volume id
        snapshot = ec2.client.create_snapshot(VolumeId = volume_id,
                                              Description = "Created by script")
        print(snapshot["SnapshotId"])
    except ClientError as e:
        print("Error in snapshot",e)
except ClientError as e:
    print("Error in volume describe",e)