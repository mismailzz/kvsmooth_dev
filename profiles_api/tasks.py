# Celery
from celery import shared_task
# Celery-progress
from celery_progress.backend import ProgressRecorder
# Task imports
import time

# Celery Task
@shared_task(bind=True)
def myceleryfunction(self):
	print('Task started')
	# Create the progress recorder instance
	# which we'll use to update the web page
	progress_recorder = ProgressRecorder(self)

	print('Start')

	time.sleep(5)
	progress_recorder.set_progress(1 + 1, 3, description="Downloading")
	time.sleep(5)
	progress_recorder.set_progress(2 + 1, 3, description="Downloading")

	print('End')

	return 'Task Complete'
