# CHALLENGE 1

## Approach
 * Used Terraform as Infrastructure as Code tool to solve this challenge
 * A 3 Tier application deployment
        * Created a VPC with a CIDR block
        * Placed web application instance in public subnet
        * Placed core application instance in private subnet
        * Placed database instance in private subnet
 
## Design
 * Created a challenge_1.tf file which shows planned 3 tier application architecture
 * Created a variables.tf file with declared variables for various environments like DEV, STAGE and PROD
        * ec2 instance types for all three environments and for each app layer- web, core and db
        * public and private subnets for web, core and DB
        * static variables like aws region, ec2 instance ami_id etc, These can also be dynamic by using data resources
 * Created a custom module database where we have created a main.tf file with just the database instance
        * Also has variables.tf file in the custom module directory which declares the variables required for the module
       
 * Created outputs.tf file where we declared output variables that will be printed in output once the infrastrcture has been deployed, this will be useful when we need to few deatils of the components we deployed 

## Usage
 * All the below commands are supposed to be triggered in the home directory /Challenge_1
 * terraform init - to initilaze the terarform directory, to download the aws related modules etc
 * terraform validate  - this is to validate the terraform files
 * terraform plan -var deploy_environment="STAGE" - this is to check the plan before actual deployment in the aws cloud
 * terraform apply -var deploy_environment="PROD" - this is to deploy the required 3 tier infrastructure in to aws cloud
 

## Resources that are still required in this template 
 * Need to create multiple resources to actually deploy the 3 tier application like security_groups, internet gateway,
 nat gateway, NACLs, Automatic Scaling group for both web and core apps, Load Balancer etc.

### Author
Chandra sekhar Jetty
