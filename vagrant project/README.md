first : I used my vagrant virtual machine and in my project directory there 
is the newspapper.sql and project.py . 

second : I switched to the postgresql user using this command 
"sudo su - postgres" , entered the postgresql using this command "psql" ,
and then I created the news database  "create database news;".
I had shown all the database tables "\list" after that I connect to by newly 
created database "\connect news" , import the data in the newspapper.sql 
"psql news < newspapper.sql" and using this command "\dt" to show all the 
tables used in news database , quit from the psql "\q"  

third : run project "python project.py"

the output is in the logs.txt file

The Design Of The Project : It consists of a function "queryForRun" contains 
all the query used to answer our questions .
the second function "queryRequired " : is set to connect to our database news,
execute our query and then run the query and close the connection 
the third function "runOutput": is used to run the project print the questions and format
the answers as required and used to run the previous 2 functions

