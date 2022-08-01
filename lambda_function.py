import json
import boto3

def lambda_handler(event, context):
    response = boto3.describe_tags(
        Filters = [
            {
                'Name'= 'hello',
                'Values' = ['Finding_you',],
            },
            ],
            NextToken='',
            MaxRecords = 123)
    
    
    
import os
import boto3


ec2 = boto3.resource('ec2')


def lambda_handler(event, context):

    instance = ec2.create_instances(
        ImageId='ami-052efd3df9dad4825',
        InstanceType='t2.micro',
        KeyName='boto3',
        SubnetId='subnet-0c48f9b67bda8e411',
        MaxCount=1,
        MinCount=1
    )

    print("New instance created:", instance[0].id)









import json
import boto3
 
AMI = 'ami-02f3416038bdb17fb'
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'boto3'
REGION = 'us-east-2'
 
 
ec2 = boto3.client('ec2', region_name=REGION)
 
 
def lambda_handler(event, context):
 
    instance = ec2.run_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        MaxCount=1,
        MinCount=1
    )
    
    print ("New instance created:")
    instance_id = instance['Instances'][0]['InstanceId']
    print (instance_id)
 
    return instance_id

