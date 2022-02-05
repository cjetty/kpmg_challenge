provider "aws" {
  region  = var.region
  profile = "default" #Refers to default section in $HOME/.aws/credentails file
}