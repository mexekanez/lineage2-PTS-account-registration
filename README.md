# lineage2_pts_reg
### Lineage 2 PTS server account creating

Wrote on python by me.

It's  just small REST service for account creation.

Why I wrote it?


I don't like to open mssql port to world.

So this thing has autorization by login pass / token.

Request for account creation is the next:


	$ curl -u r:r -i -X POST -H "Content-Type: application/json" -d '{"username":"r10","email":"1@1.ru","phone":3333333,"password":"wwwwwwww"}' http://127.0.0.1:5000/api/v1.0/register/ 

it's first commit will add more infortation a bit latter
