import os
import urllib.request
import time

from threading import Thread

destination_folder = "flamingos_files"


class DownloadThread(Thread):

    # set up the __init__ to accept a url and a name for the thread
    def __init__(self, url, name):
        Thread.__init__(self)
        self.name = name
        self.url = url
        print("%s: %s - starting" % (self.name, time.ctime(time.time())))

    # run the thread - open up the url, extract the filename
    # and then use that filename for naming / creating the file on disk
    def run(self):
        # urllib is used to do the actual downloading inside the thread class
        handle_remote = urllib.request.urlopen(self.url)

        # The os module is used to extract the name of the downloading file,
        # so it's used to create a file with the same name on our machine.
        file_name = os.path.basename(self.url)

        # download the file a kilobyte at a time and write it to disk
        with open(file_name, "wb") as file_handler:
            while True:
                part = handle_remote.read(1024)
                if not part:
                    break
                file_handler.write(part)

        print("%s: %s - ending" % (self.name, time.ctime(time.time())))


# open the file with the images URLs, read them and close the file
my_file = open("source_files.txt", "r")
urls = my_file.readlines()
my_file.close()

# create and change working directory
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
os.chdir(destination_folder)


if __name__ == "__main__":
    # initiate download of all described images in separate threads
    # for index, image_url in enumerate(urls):
    for index, image_url in enumerate(urls):
        thread_name = "Thread %s" % (index + 1)
        thread = DownloadThread(image_url.strip(), thread_name)
        thread.start()
