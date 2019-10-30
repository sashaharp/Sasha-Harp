
print("developer_tools:assets initialized")
import shutil
import stat
from google_images_download import google_images_download
import subprocess
response = google_images_download.googleimagesdownload()
  
def downloadimages(query, offset=0):
    arguments = {"keywords": query, 
                 "limit": 3,
                 "offset": offset,
                 "output_directory": "download_sample",
                 "print_urls": True} 
    try: 
        response.download(arguments)
        return 1
    except:
        return -1

def download_sample(query, offset=0):
    o = offset
    while downloadimages(query, o) == -1:
        o+=1
    return o

def cleanup(query):
    shutil.rmtree("download_sample/" + query)

if __name__ == "__main__":
    download_sample("sword 2d texture")
    cleanup("sword 2d texture")