# CHALLENGE 3

## Approach
 * Used Python 3.6
 * Given is a nested key object and a keys as a string with '/' separator
 * Tried to get the keys string in list format to iterate over object variable
    * Used split function to split('/') the given keys string in to a list format

## Solution
 * Once we get the list of keys in a list format, it is iterated in for loop
 * For each iteration we get the inner value of key
 * Once the inner value is obtained the original object value is replaced with the inner variable
 * This is done for all the keys provided to obtained the final value
 
## Exceptions
 * ValueError exception is raised when the a None value is identified in the given object
 * This is to break the for loop in case the invalid object and key values are provided 
 

## Requirements
  * Python 3.6 and above
  * Libraries
       * typing
 
### Author
Chandra sekhar Jetty
