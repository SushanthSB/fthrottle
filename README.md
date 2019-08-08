# fthrottle
Auto complete suggestions from given dataset.

### Client
Inside client folder:
* <b>npm install</b> to install reactjs and other dependencies in client folder.\
* <b>npm start</b> to build files.
* <b>npm test</b> to test.
* <b>npm build</b> to build static files.

### Server
Inside server folder:
* Require python3 and pip3
* pip3 install -r requriements.txt to install all the dependencies
* python3 manage.py migrate to get models into database
* Injest word_search.tsv to app_data table.
	* to injest data from tsv:
		1. Enter into mysql CLI and execute below query.
		1. load data local infile {path/to/word_search.tsv} into table app_data
			 fields terminated by '\t'
			 enclosed by '"'
			 lines terminated by '\n'
			 (string, occurance)
* <b>python3 manage.py test {path/for/tests_folder}</b> to get test results.

> * npm run build will build static files and also copy them to static folder in server directory so that django can serve the static files.
> * While running client and server under different origin during development browser's CORS extension will be required.

# Info
* Django backend exposes <b>/search</b> api for the client, it takes query parameter <b>word</b> ex: /search?word={pattern}
* Based on given pattern it returns json containing array of suggestions upto 25 strings
