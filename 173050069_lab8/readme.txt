Description:
	
	First open both the input files as a dataframe object and 
	store them in a variable. 
	
	Query 1:
		Groupby all the countries according to the sum of va-
		lues India have exported to in descending order. Store 
		it in the excel sheet. Again do the same thing accord-
		ing to import values.

	Query 2:
		Groupby all the commodities according to the sum of 
		values India has exported in descending order. Do the
		same thing according to the total import value done
		by India.

	Query 3:
		Get all the countries as a dataframe. Then do groupby 
		countries on the total imports to them by value and 
		store it as a dataframe. Do the same thing on export 
		values and store it in a dataframe. Make a new data-
		frame with above dataframes as columns and also add
		export/import ratio and trade deficit as a column. Run 
		a for loop and using indexing add value from each of the
		dataframe into first three columns and also subsequently 
		calculate the ratio and the trade deficit.

	Query 4 & Query 5:
		Do groupby countries on the values of export data and 
		then print the names of only those countries whose to-
		tal export is greater than 10000 Cr /- . 
			Here I have also done the groupby countries on the
		values of import data and stored it as a dataframe. T-
		hen created a new dataframe containing country names &
		their corresponding total import and export values. Then 
		return the dataframe. It will be the result of Query 5.   

	Query 6:
		Do melt on the dataframe for query 5 using 'id_vars=country
		and value_vars=exports,imports.  

	Query 7:
		Get all the import commmodities and export commodities
		and take intersection of them. This will give the names
		of all the commodities that were atleast once exported &
		imported in either of the years i.e, either in 2011-12 or
		in 2012-13.


