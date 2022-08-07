# kvsmooth
Django Reference (REST API + CELERY + CELERY_PROGRESS + FlowerUI + DATABASE)

#Terminal-0
Redis service

#Terminal-1-vnev
Djnago server

#Terminal-2-vnev
celery -A profiles_project worker --loglevel=info

#Terminal-3-vnev
celery -A profiles_project flower --port=5566
http://localhost:5566/


Notes:
pip install flower

#issue
unexpected usernamme error while executing flower
pip install "celery"[redis]
