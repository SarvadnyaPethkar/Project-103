import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

form_dir = "< Set path for tracking file system events >"

#event handler class
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Opps! Someone deleted {event.src_path}!")

#initialize event handler
event_handler = FileEventHandler()

#initialize observer
observer = Observer()

#schedule the observer
observer.schedule(event_handler, form_dir, recursive=True)

#start the observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()
