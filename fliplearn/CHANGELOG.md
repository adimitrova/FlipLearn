## TO DO:

- [x] Contracts for the objects
- [x] Basic HTML page 
- [x] POC with HTML/CSS for flipping cards
- [x] local DB setup with `sqlite3`
- [ ] backup the local db until a real db is fixed
- [ ] connect to real db
- [ ] Implement Login
- [ ] Implement regisration
- [ ] Auth tokens generated, `JWT`?
- [ ] Pass on token between pages
- [ ] complete all the API endpoints


---

## [2023-11-25]
* Created a decorator to the database class to handle opening and closing the connection when certain methods are called
* Fix static files mounting 
* Fix running the app with the Makefile `make run` which failed before with errors
* Added all 3 required table queries to the database file
* Fixed some issues with the dataclass contracts
* started a test folder for later

#### TODO:
* move all code to a src dir or keep in `fliplearn` and take out all that's not code related to the app so that `test` and `src/fliplearn` are on the same level, easier for testing later
* fix the `make run` command after moving the code
* work more on the database class to incorporate all main queries required for registering, logging in, adding new card etc
* handle export and import of the actual DB file somehow (until connected to a real db)
