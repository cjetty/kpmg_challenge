
resource "aws_vpc" "KPMG_CHALLENGE_1" {
  cidr_block       = var.vpc_cidr

  tags = {Environment = var.environment_map[var.deploy_environment]}
}

resource "aws_subnet" "web_app_public_subnet" {
  vpc_id            = aws_vpc.KPMG_CHALLENGE_1.id
  availability_zone = var.vpc_azs[0]
  cidr_block        = var.subnet_public_cidr


  tags = {Environment = var.environment_map[var.deploy_environment]}
}

resource "aws_subnet" "core_app_private_subnet" {
  vpc_id            = aws_vpc.KPMG_CHALLENGE_1.id
  availability_zone = var.vpc_azs[0]
  cidr_block        = var.subnet_private_cidr

  tags = {Environment = var.environment_map[var.deploy_environment]}
}

resource "aws_subnet" "db_private_subnet" {
  vpc_id            = aws_vpc.KPMG_CHALLENGE_1.id
  availability_zone = var.vpc_azs[0]
  cidr_block        = var.subnet_db_private_cidr

  tags = {Environment = var.environment_map[var.deploy_environment]}
}


resource "aws_instance" "web_app_ec2_instance" {
  ami           = var.ami_id
  instance_type = var.environment_web_app_instance_type[var.deploy_environment]
  tags = {Environment = var.environment_map[var.deploy_environment]}
}


resource "aws_instance" "core_app_ec2_instance" {
  ami           = var.ami_id
  instance_type = var.environment_core_app_instance_type[var.deploy_environment]
  tags = {Environment = var.environment_map[var.deploy_environment]}
}

module "database" {
  source = "./database"
  
  allocated_db_storage = var.environment_db_storage_allocation[var.deploy_environment]
  db_instance_class    = var.environment_db_instance_type[var.deploy_environment]
}