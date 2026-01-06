resource "aws_iam_role" "vpc_flow_log" {
    name = "vpc-flow-log-role"
    
    assume_role_policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
        {
            Action = "sts:AssumeRole"
            Effect = "Allow"
            Principal = {
            Service = "vpc-flow-logs.amazonaws.com"
            }
        }
        ]
    })
  
}

resource "aws_iam_role_policy" "vpc_flow_log_policy" {
    name = "vpc-flow-log-policy"
    role = aws_iam_role.vpc_flow_log.id
    
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
        {
            Action = [
            "logs:CreateLogStream",
            "logs:PutLogEvents",
            ]
            Effect   = "Allow"
            Resource = "${aws_cloudwatch_log_group.dev_log_group.arn}:*"
        }
        ]
    })
  
}

resource "aws_flow_log" "dev_flow" {

  vpc_id               = aws_vpc.dev_vpc.id
  traffic_type         = "ALL" #test ALL, ACCEPT, REJECT
  log_destination_type = "cloud-watch-logs"
  log_destination      = aws_cloudwatch_log_group.dev_log_group.arn
  iam_role_arn         = aws_iam_role.vpc_flow_log.arn

}