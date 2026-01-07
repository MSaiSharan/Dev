import boto3

ec2 = boto3.client("ec2", region_name="us-east-1")

response = ec2.describe_vpcs(
    Filters=[
        {
            "Name": "tag:Name",
            "Values": ["dev-vpc"]
        }
    ]
)

vpc_id = response["Vpcs"][0]["VpcId"]
print("VPC ID:", vpc_id)

subnets = ec2.describe_subnets(
    Filters=[
        {
            "Name": "vpc-id",
            "Values": [vpc_id]
        }
    ]
)
for subnet in subnets["Subnets"]:
    print("Subnet ID:", subnet["SubnetId"])


igws= ec2.describe_internet_gateways(
    Filters=[
        {
            "Name": "attachment.vpc-id",
            "Values": [vpc_id]
        }
    ]
)
for igw in igws["InternetGateways"]:
    print("Internet Gateway ID:", igw["InternetGatewayId"])


natgateways=ec2.describe_nat_gateways(
    Filters=[
        {
            "Name": "vpc-id",
            "Values": [vpc_id]
        }
    ]
)
for nat in natgateways["NatGateways"]:
    print("NAT Gateway in VPC ID :", nat["NatGatewayId"])

aws_account_id=boto3.client("sts").get_caller_identity().get("Account")
print("AWS Account ID:", aws_account_id)