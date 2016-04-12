# lineage2_pts_reg
### Lineage 2 PTS (works with MSSQL server) server account creating
###It's  just small REST API service for accounts.

REST API service with user/token authentication.

It cheks if account exists (user_auth, ssn, user_account and user_info tables)

###It does account creation with encrypt option.

If you want to run on Windows server you need: Python 2.7.5 and pymssql for this service - all this on root folder. 

When you have done with python instalation next step will be to install additional modules for serverce like flask and etc...
use 
	
	$ pip install -r requirements.txt

Also this application has local sqlLite storage for users.

to create sql Lite DB:

	$ python ./manage builddb

to create user for access:

	$ python ./manage createsuperuser

- this command will return token  - use it for access.

###To handle http requests we need Apache2 as a server and mod_wsgi for python.

I wasted some time to configure wsgi config,  to keep you time I will show option without which it doesn' works:

	$ WSGIPassAuthorization On
	$ WSGIApplicationGroup %{GLOBAL}


Request for game account creation is the next:


	$ curl -u r:r -i -X POST -H "Content-Type: application/json" -d '{"username":"r10","email":"1@1.ru","phone":3333333,"password":"wwwwwwww"}' http://127.0.0.1:5000/api/v1.0/register/ 

Where r:r login and password or you can use token. 
If accaount was created in response you will get 

	$ status: good

or 

	$ status : error

with fields where we have issue like : "Account already exists"

You can extend this thing for donation or use it like it is.

