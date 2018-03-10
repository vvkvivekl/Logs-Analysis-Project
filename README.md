# Version Control with Git

This is the repo for [Udacity's Logs Analysis Project](). In the project, we have created software where analyzer can run command instead typing query.

This repo contains the source code of a Logs Analysis project.

## Table of Contents

* [Instructions](#instructions)
* [Creator](#creators)

## Instructions

* ### Set-up Instructions
	1. Create the news database in PostgreSQL
		* From the command line, launch the psql console by typing: psql
		* Check to see if a _news database already_ exists by listing all databases with the command: ```\l```
		* If a news database already exists, drop it with the command: ```DROP DATABASE news;```
		* Create the _news_ database with the command: ```CREATE DATABASE news;```
		* exit the console by typing: ```\q```
	2. Download the schema and data for the _news_ database:
		* [Click here to download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
	3. Unzip the downloaded file. ```unzip newsdata.zip```.
		* You should now have an sql script called _newsdata.sql_.
	4. From the command line, navigate to the directory containing _newsdata.sql_.
	5. Import the schema and data in _newsdata.sql_ to the news database by typing: ```psql -d news -f newsdata.sql```


* ### Installation (Run program)
 >* clone the project
 >* open terminal in project Dir.
 >* go in news Dir. using ```cd news``` in terminal
 >* run ```python newsdb.py```

* #### Usage
> * type numeric values and hit enter
>  1. What are the most popular three articles of all time?
>  2. Who are the most popular article authors of all time?
>  3. On which days did more than 1% of requests lead to errors?
>  4. exit

## Output

 * [Click here](https://github.com/vvkvivekl/Logs-Analysis-Project/blob/master/Output.txt) to see output demo.

## Creators

* Vivek Lingayat (Vvk)
    - [https://github.com/vvkvivekl](https://github.com/vvkvivekl)
    - [https://fb.com/vvksl](https://fb.com/vvksl)

Required software:

* Python
