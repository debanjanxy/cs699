Note : Extract the 173050069 lab2.tar.gz zip file into your home directory which will produce a 
	   directory "173050069 lab2". Goto this folder from terminal. Then only run all the scripts.

Problem 1 : Backup my files : script1.sh
	
	This script creates backup for the files which are present in the "~/173050069\ lab2/input/test' 
	directory. Many times I have wrote some programs and forgot where it was present, or even present
	or not. In this case it'll be helpful if I store a backup file at a particular location for every
	programs/files I've created.
	
	Use: Create a file in the '~/173050069\ lab2/input/test' directory.
	
	Input: sh script1.sh input

	Output: Output will be the file that you had created in 'test' directory which will be
		    present in  ~/173050069\ lab2/input/backup/test_backup

Problem 2 : Play Music : script2.sh

	This bash script plays all the songs present in the directory '~/173050069\ lab2/input/music'. 
	We don't have to manually go to the folder and play song, we can simply run the script.
	
	Requirements : VLC Media player should be pre-installed in the machine
	
	Input : sh script2.sh input
	Output : You'll hear some music! :)

Problem 3 : Open Firefox Browser : script3.sh

	This script opens two mostly used urls in firefox, i.e, 'www.google.com' & 'internet.iitb.ac.in'
	We don't have to open the browser manually.

	Input : sh script3.sh
	Output : Opened Firefox browser with two tabs

Problem 4 : Opens My Books : script4.sh

	This script gives the list of books that present in the '~/173050069\ lab2/input/books' 
	directory. From there we can choose which book to read. In real life we have to keep track of all
	the books and open their corresponding folder which is cumbersome. Hence it is better to have a
	list of all books that I have and I can choose from that which book to read.

	Input : sh script4.sh input
			Now we have to enter the exact name of the book that is printed on the screen along with it's
			extension
	Output : The book will be opened in Document Viewer

Problem 5 : Goes to my most used directory(containing all the files related to work/study) : script5.sh

	This script opens my most important directory(in this case it is "~/173050069\ lab2/input/work")
	in a file manager where most of my study/work related files are present. 
	Note : This script will run automatically on start-up of the machine. This task is machine dependent;
		   hence I am giving account on how to do it. 
		   Step 1 : Open terminal
		   Step 2 : Type "sudo -i" without inverted commas. Log-in as root privileges.
		   Step 3 : Type "vim /etc/rc.local"
		   Step 4 : Add the following line : "~/173050069\ lab2/script5.sh || exit 1" before exit 0 in the file.
		   Step 5 : Save it and exit.
		   Step 6 : Restart
	Input : sh script5.sh input
	Output : Whenever you start your machine the directory "~/173050069\ lab2/work/"  will be opened 
	













