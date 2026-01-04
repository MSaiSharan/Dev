import boto3

ec2 = boto3.client('ec2')

vpcs = ec2.describe_vpcs()

print("VPC Information:")
for vpc in vpcs['Vpcs']:
    print(f"VPC ID: {vpc['VpcId']}  | CIDR: {vpc['CidrBlock']}")
