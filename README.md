# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has asked me the following tasks to complete the election audit of a recent local congressinal eletion.

1. Calcuate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes eac candidate recieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on poular vote.
 
## Resources
- Data Source: elecitn_results.csv
- Software: Python 3.9.7, Visual Studio Code, 1.65.2

## Election-Audit Results:
The analysis of the eleciton show that:

- There were 369711 votes casted in the election

- The breakdown of the number of votes and percentage of total votes for each county is following:
	-Jefferson: 10.51 % (total 38,855 votes)
	-Denver:82.78% (total 306,055 votes)
	-Ara[ajpe" 6.71% (total 24,801 votes)
- The largest votes were made in:
	- Denver	
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham recieved "23.0%" of the vote and 85,213 of votes.
    - Diana DeGette recieved "73.8%" of the vote and 272,892 of votes.
    - Raymon Anthony Doane recieved "3.1%" of the vote and 11,606 of votes
	
- The winner of the election is:
    - Diana DeGette, who recieved "73.8%" of the vote and total 272,892 of votes.

## Election-Audit Summary
Based on developing this script, this can be used for further delvelopment with minor or extended modification it can be used for other elections
- Input
	- Based on the development, input has to be csv format,  provided each election
- Modification - make few parameters variablized to adopt different file names, different format input/output, even different file types
	- File names should be a variable where any csv file can be read/write including its file path	
	- Input file format has to be the same or asking for the valid index for county and candidate
	- File has to be clean - we can have a cleaning program to ensure this program to run correctly remove invalid format entries
		
		- simple minor modification of the script exampe :
			- Add in the beginning of the script 
				- cvs_election_result = input("Please enter the election file name with extension:")
			- Change file to load to input variable
				- file_to_load = os.path.join("resources", cvs_election_result)
			- Ask to ensure the user the file is place in the resources folder
				- is_cvs_file_placed = input("Please add the election file to resources folder.  Enter yes if you are done:")
			- If yes continue the script
				- if(is_cvs_file_placed == "yes"):
			- Otherwise exit using quit function
	
	 
	

