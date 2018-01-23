1. Command to execute in syntactical format:

	Format: python3 solution.py <input_file_name> <Work_No>
	Working Eg: python3 solution.py student_data 8662006787

2. Brief Description of Code:

	First take input from command line. Then open the corresponding csv file.
	Store the csv file as a list of rows. Take the first row and find the at-
	tribute which has the substring 'work no'; also get it's index. Hence, we
	got the index of the work no's column. Now get all the rows which matches 
	with the given work number using the index of work no column. Store all 
	these rows into a list, let it is 'rows'. Get the length of this list, let
	it be 'l'. So, we have to create 'l' sheets named work no_l. Take each sheet
	and first write the headers in that sheet then write only one row from the
	list 'rows' into that sheet. The work no should be written in i'th sheet
	as work no_i. Errors like input file not present or work no not present is
	handled gracefully. 

3. Assumptions:
	
	Module openpyxl should be installed in the system.
