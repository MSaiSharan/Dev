import subprocess
import json

# Run terraform output command
result = subprocess.run(
    ["terraform", "output", "-json"],
    capture_output=True,
    text=True
)

# Convert JSON output to Python dict
outputs = json.loads(result.stdout)

# Read VPC ID
subnet_id = outputs["subnet_id"]["value"]
igw_id = outputs["igw_id"]["value"]
iam_role_name = outputs["iam_role_name"]["value"]

print("Subnet ID from Terraform:", subnet_id)
print("Internet Gateway ID from Terraform:", igw_id)
print("IAM Role Name from Terraform:", iam_role_name)