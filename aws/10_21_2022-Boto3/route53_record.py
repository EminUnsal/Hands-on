#!/usr/bin/python
'''
This script finds an instance by its ID
Then it finds out its public IP address and changes Route53 "A" record.
'''

import boto3

def find_ip(id):
    """
    Finds a public IP address based on instance ID
    Returns a public IP address.
    """
    ec2 = boto3.resource("ec2")
    instance = ec2.Instance(id)
    ip = instance.public_ip_address
    return ip

def change_route53_record(zone_id, domain, ip):
    """
    Changes Route53 type A record
    """
    r53 = boto3.client("route53")
    r53.change_resource_record_sets(
        HostedZonedId=zone_id,
        ChangeBatch={
            "Comment"   : "test",
            "Changes"   :[
                {
                    "Action"    : "UPSERT",
                    "ResourceRecordSet" : {
                        "Name"  : domain,
                        "ResourceRecords"   : [
                            {
                                "Value" : ip
                            }
                        ],
                    "Type"  : "A",
                    "TTL"   : 60
                    }
                },
            ]
        }
    )

    # Set Instance ID
    instance_id = "i-xxxxxxxxxxxxxxxxx"
    # Set Hosted Zone ID
    zone_id = "Z08348542LMKDSH94CCW6"
    # Domain
    domain = "boto.clarusway.us"

    # Find the Public IP Address
    ip_address = find_ip(instance_id)
    # Change A Record
    change_a_record = change_route53_record(zone_id, domain, ip_address)
    print(domain + " record was changed to: " + ip_address)