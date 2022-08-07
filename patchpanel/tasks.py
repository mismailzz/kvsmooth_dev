# Celery
from celery import shared_task
import time


# Celery Task
@shared_task(bind=True)
def mytestceleryfunction(self):
        print('Task started')
        # Create the progress recorder instance
        # which we'll use to update the web page

        print('Start')
        time.sleep(5)
        print("Mid")
        time.sleep(5)
        print('End')

        return 'Task Complete'
