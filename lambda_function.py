import json
import boto3
import re
from pprint import pprint
def lambda_handler(event, context):
    regions = []
    oto = boto3.client('ec2',region_name='us-east-2')
    zelar = boto3.client('iam')
    regions = oto.describe_region()
    vpcs = oto.describe_vpcs()
    roles = zelar.list_roles().get('Roles',[])
    for role in roles:
        print(role)
    
    
    
