# Basic Unix Commands

This gives a list of basic unix commands with definations for each

## Basics

```bash
whoami						# who is the user
pwd							# present working directory
```

## List commands
```bash
ls 							# list the files in the current working directory
ls -l 						# list the files in long listed format
ls -F						# list the files in current directory with folders specified as /
ls -a						# Adds current directory as ./ and parent directory as ../
ls -r						# shows reverse order of file lists based on namings of file. with folders first
```

## Directory & File commands

```bash
mkdir <dirname>				# create a directory
rmdir <dirname>				# delete a directory which is empty
rm-rf <dirname>				# deletes an non empty directory		
touch <filename>			# creates a blank file
nano <filename>				# edits the file using nano editor
rm <filename>				# removes filename
rm *.txt					# removes all files in current directory with txt as extension
rm <dir>/*					# removes all the files under dir directory
mv <filename> /mnt/d/		# moves file to a given destination.
mv file file1				# renames file to file1
mv /mnt/d/file1 .			# moves file1 from specified loction to current location
cp <dir1>/file <dir2>		# copies files from one directory to another
```

## Word counts with transfer the outputs , sorts , head , tail

```bash
wc *.txt												# count in lines , words and characters of all the files with extension .txt in current dir
wc -l *.txt												# count of only lines in files ending with txt
wc -w *.txt												# count of only words in files ending with txt
wc -c *.txt												# count of only characters in files ending with txt
wc -c *.txt > /mnt/d/unix/char_count.txt				# appending the results of character count in a file using >
wc -l *.txt | sort | head -1							# sorting the output of lie count and display the file with least count
wc -l *.txt | sort | tail -2 | head -1					# finding the file that has max count . tail -1 as it also displays the total
wc -l *.txt | sort -r 									# sort the line count in reverse order
```

## Splits , cuts , uniq

```bash
split <file1> <splitname>													# splits file1 with prefix name as splitname in same directory
split -l 100 <file1> <splitname>											# splits the file1 into prefix of splitname each file containing 100 lines
split -b 50k <file1> <splitname>											# splits the file1 into prefix of splitname each file having size of 50k or less
cut -c 1-5 <file>															# cur from character 1 to 5
cut -c 3- <file>															# cut from 3rd character to end 
cut -c -10 <file>															# cut till 10th character
cut -c 3-6 <file>															# cut from 3rd to 6th character 
cut -d ' ' -f 1 <file>														# cut using delimiter as space and get the first word 
cut -d ' ' -f 1,3 <file>													# cut using delimiter as space and get the first and third word
cut -d 'i' -f 1,2 indian_cricket_captains.txt --output-delimiter '-'    	# cuts using delimiter 'i' and replaces it using -
uniq file1																	# get uniq lines from file 1 
uniq -d file1																# get only repeated lines
uniq -c file1																# get uniq lines with counts for each repetitions 
```


## Grep and find

```bash
grep today <filename>							# find the lines with matches word today in file
grep today *.txt								# find the lines which matches word today in all files with extension txt
grep -w today <filename>						# lines which have exact match for word today . eg todays wont be a match
grep -n today <filename>						# displays the line number where match for word today
grep -v today <filename>						# displays all the lines where today is not matched
grep -i today <filename>						# includes case insensitive matches for today. eg : Today can be found
find . -type d 								    # finds all the directories in current and sub directories
find . -type f 								    # finds all the files in current and sub directories
find ./<dir> -type f  							# finds all the files in directory given
find . -maxdepth 2 -type f 						# finds the files within max depth of 2 from given directory
find . -mindepth 1 -type f  					# finds the files after min depth of 1 from given directory
find . -name '*.txt' -type f 					# find the files with name format given
wc -l `find . -name '*.txt' -type f`    		# gives linecounts of all the files returned by find. for this find command needs to be in backtic `` 
												# find . -name 'Sample*.txt' -type f | wc -l --> is incorrect way as file names will be output and not the file itself
grep -w Hi `find . -name '*.txt' -type f`		# searches for all files with txt extension and then greps for word Hi in each of the file										#
```

## Variables

```bash
echo HOME										# returns HOME as output as $ is not defined to search for any variables
echo $HOME										# returns value of variable HOME
VAR1=kednat										# Setting up the variable VAR1
echo $VAR1										# returns value of variable VAR1
export VAR1										# Registers VAR1 so that it can be used in other bash instances. To register at startup it needs to be added in ./bashrc file.
```

## chmod

```bash
chmod 100 file.txt				# execute permissions for only read
chmod 020 file.txt				# write permissions for only group
chmod 003 file.txt				# write and execute for anyone
chmod 400 file.txt				# read permissions only for user
chmod 050 file.txt				# read and execute for group
chmod 006 file.txt				# read and write for anyone
chmod 777 file.txt				# read,write and execute for all
chmod 000 file.txt				# no permissions to anyone
chmod 444 file.txt				# read permissions for all
chmod +100 foo.sh        		# add 1 to the user permission
chmod -100 foo.sh        		# subtract 1 from the user permission
chmod u+x foo.sh         		# add user execute permission
chmod g+x foo.sh         		# add group execute permission
chmod u-x,g-x foo.sh     		# remove user and group execute permission
chmod u+x,g+x,o+x foo.sh 		# add everybody execute permission
chmod a+x foo.sh         		# add everybody execute permission
chmod +x foo.sh          		# add everybody execute permission
```
