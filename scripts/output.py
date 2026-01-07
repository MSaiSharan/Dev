import subprocess
import json

result = subprocess.run(
    ["terraform", "output", "-json"],
    capture_output=True,
    text=True
)

outputs = json.loads(result.stdout)

vpc_id = outputs["vpc_id"]["value"]

print("VPC ID from Terraform:", vpc_id)