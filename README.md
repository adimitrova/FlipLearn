WIP — Work In Progress

### DEMO of the current progress as of 2024-02-09

<img src="https://camo.githubusercontent.com/89bc1578f66f7880d56a34ac468f4e7a92411243dcee5c1f006165d42a3a9334/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f76312e59326c6b505463354d4749334e6a45785a4e6e4e576c77646e42694e576435636d39776154566d634856705a6d526e6247646a63484e6d4e584179616e42336244526962535a6c634431324d563970626e526c636d35686246396e61575a66596e6c666157516d593351395a772f347a6635614e3963347a4f637543503373362f67697068687967696621" alt="Demo" width="600"/>

I intended to start a project like this for myself to learn and remember things in my every day life, however i decided to combine this with my learning timeline for Django which i haven't used so far. Somehow there seemed to be JUST that perfect project on RealPython which I followed but later worked up to be just as I intended it to be. So it's not any kind of novelty but a fun project to learn from and a tiny app for me to get myself into remembering things easier. Feel free to use it yourself. I will eventually host it online once it's complete. Until then, you can run it locally and make sure to backup your database with the `make backup_db` command.
NB! This is NOT the top prio project for me right now so it may become inactive until further notice.
- Tutorial: https://realpython.com/django-flashcards-app/ 

- [Check out my musical accompaniment on repeat while I am working on this project](https://youtu.be/iAxMGzEkza0?si=agqQgLWUFhhp1bwp)


## Getting started

- Using the provided `Makefile`:

```bash
# create venv, upgrade pip, install package
make install

# run migrations and start development server
make migrate
make run
```

- Create a superuser (optional):

```bash
./venv/bin/python manage.py createsuperuser
```

### Useful links
* [Debug Django inside Pycharm](https://www.youtube.com/watch?v=tuiyHcHVugM)
* [Debug Django views in VSCode](https://www.youtube.com/watch?v=bai68IMXl_E)
* [session middleware](https://stackoverflow.com/questions/69763983/writing-django-session-middleware-based-on-view-kwargs)
* [authentication middleware](https://docs.djangoproject.com/en/5.0/topics/auth/default/#auth-web-requests)

---
#### Steps to upload a demo GIF to readme:
* Recorded with screen recorder 
* converted to GIF with https://ezgif.com/video-to-gif 
* Upload to https://giphy.com/
* loaded into an ISSUE on Guthub 
  * right click > Copy image address
* include as an image to README.md
* Check out the [article for this](https://medium.com/@jackywangdeveloper/tips-tricks-how-to-add-a-demo-video-in-your-git-readme-md-bbf8376a4b74)
