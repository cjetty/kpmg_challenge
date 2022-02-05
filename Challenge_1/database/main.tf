resource "aws_db_instance" "db_instance" {
  allocated_storage    = var.allocated_db_storage
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = var.db_instance_class
  name                 = "mydb"
  username             = "foo"
  password             = "foobarbaz"
  parameter_group_name = "default.mysql5.7"
  skip_final_snapshot  = true
}