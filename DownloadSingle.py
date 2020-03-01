import os
import urllib.request
import time

destination_folder = "flamingos_files"

# open the file with the images URLs, read them and close the file
my_file = open("source_files.txt", "r")
urls = my_file.readlines()
my_file.close()

# create and change working directory
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
os.chdir(destination_folder)

# initiate download of all described images in separate threads
for index, image_url in enumerate(urls):
    print("Image %s: %s - starting" % (index + 1, time.ctime(time.time())))
    handle_remote = urllib.request.urlopen(image_url.strip())

    # The os module is used to extract the name of the downloading file,
    # so it's used to create a file with the same name on our machine.
    file_name = os.path.basename(image_url.strip())

    # download the file a kilobyte at a time and write it to disk
    with open(file_name, "wb") as file_handler:
        while True:
            part = handle_remote.read(1024)
            if not part:
                break
            file_handler.write(part)

    print("Image %s: %s - ending" % (index + 1, time.ctime(time.time())))
