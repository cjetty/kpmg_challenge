# CHALLENGE 2

## Approach
 * Used Python 2.7
 * Created a recursive function which iterates over meta-data at all levels
 * To return individual meta data used a OptionParser function 

## Solution
 * AWS metadata link http://169.254.169.254/latest/meta-data/
 * Used standard requests.get() function to get the http link output
 * Each output is iterated using a for loop and assigned to a result dictionary
 * If found flat it is directly assigned to result dictionary, else it is iterated recursively to get the final value
 * The final result dictionary in get_instance_meta_data() is returned to main() function
 * In main function it is validated to print entire instance meta-data or individual meta data

## Requirements
  * Python 2.7 
  * Libraries
       * requests
       * optparse

## Usage
 * python challenge_2.py  - To get all the meta data of the instance
 * python challenge_2.py -k security-group-ids  - To get individual instance meta data values

 
### Author
Chandra sekhar Jetty
