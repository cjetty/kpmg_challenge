variable "region" {
  default = "eu-west-2"
}

variable "vpc_cidr" {
  default = "172.16.0.0/16"
}

variable "vpc_azs" {
    type = list(string)
    default = ["eu-west-2a"]
}

variable "subnet_public_cidr" {
  default = "172.16.1.0/24"
}

variable "subnet_private_cidr"{
  default = "172.16.2.0/24"
}

variable "subnet_db_private_cidr"{
  default = "172.16.3.0/24"
}

variable "ami_id"{
  default = "ami-0fdbd8587b1cf431e"
}

variable "environment_map" {
  type = map(string)
  default = {
    "DEV" = "DEV",
    "STAGE" = "STAGE",
    "PROD" = "PROD"
  }
}

variable "deploy_environment"{
    default = "DEV"
}

variable "environment_web_app_instance_type" {
  type = map(string)
  default = {
    "DEV" = "t2.micro",
    "STAGE" = "t2.micro",
    "PROD" = "t2.micro"
  }
}

variable "environment_core_app_instance_type" {
  type = map(string)
  default = {
    "DEV" = "t2.micro",
    "STAGE" = "t2.micro",
    "PROD" = "t2.micro"
  }
}


variable "environment_db_instance_type" {
  type = map(string)
  default = {
    "DEV" = "t2.micro",
    "STAGE" = "t2.micro",
    "PROD" = "t3.micro"
  }
}

variable "environment_db_storage_allocation" {
  type = map(number)
  default = {
    "DEV" = 10,
    "STAGE" = 10,
    "PROD" = 20
  }
}