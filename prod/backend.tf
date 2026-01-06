terraform {
  backend "s3" {
    bucket         = "dev-statedoc"
    key            = "dev/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "Dev-lock"
    encrypt        = true
  }
}
