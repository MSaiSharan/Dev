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

print("Subnet ID from Terraform:", subnet_id)