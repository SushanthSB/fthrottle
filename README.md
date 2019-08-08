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

> * npm run build will build static files and also copy them to static folder in server directory so that django can serve the static files.
> * While running client and server under different origin during development browser's CORS extension will be required.
