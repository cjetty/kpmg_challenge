output "web_app_public_ip" {
    value = aws_instance.web_app_ec2_instance.public_ip
}

output "core_app_private_ip" {
    value = aws_instance.core_app_ec2_instance.private_ip
}

output "vpc_id" {
    value = aws_vpc.KPMG_CHALLENGE_1.id
}

output "db_instance_arn"{
    value = module.database.db_instance_arn
}