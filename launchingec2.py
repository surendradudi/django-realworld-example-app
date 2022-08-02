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