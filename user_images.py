#https://github.com/5shekel/Imgur-tools

import requests
import json
import pprint
import datetime
import os

#create file named settings.py and have your acces token there
from settings import access_token
# see http://blog.tankorsmash.com/?p=551 for how to make one.
# or just uncomment  it here if you dont push back to git
#access_token = "super-seceret-token"

image_user_url = 'https://api.imgur.com/3/account/yair99/images/1'

def user_images(access_token, image_user_url):
    #need to include the authorization headers, in order to make use of the access token
    headers = {"authorization":"Bearer {0}".format(access_token)}
    r = requests.get(image_user_url, headers=headers, verify=False)
    j = json.loads(r.text)
    #debug
    #pprint.pprint(j)

    #get the list of images from j['gallery']
    image_list = j['data']
    print(len(image_list), 'images found in the gallery')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(image_list[0])

    #list of pairs containing the image name and file extension
    image_pairs = []
    #extract image and file extension from dict
    for image in image_list:
        #get the raw image name
        img_name = image['id']
        #get the image extension(jpg, gif etc)
        img_ext = image['type']
        #append pair to list
        image_pairs.append((img_name, img_ext))
        pp.pprint(image_pairs)

if __name__ == '__main__':
    user_images(access_token, image_user_url)

"""
#http://blog.tankorsmash.com/?p=266
## Create a dynamically named folder

#get the time object for today
folder = datetime.datetime.today()
#turn it into a printable string
string_folder = str(folder)
#replace some illegal chars
legal_folder = string_folder.replace(':', '.')
#create the folder using the name legal_folder
os.mkdir(str(legal_folder))

## Extract image info from the gallery

#list of pairs containing the image name and file extension
image_pairs = []
#extract image and file extension from dict
for image in image_list:
    #get the raw image name
    img_name = image['hash']
    #get the image extension(jpg, gif etc)
    img_ext = image['ext']
    #append pair to list
    image_pairs.append((img_name, img_ext))
    pprint(image_pairs)

## Download images from imgur.com

#current image number, for looping limits
current = 0
#run download loop, until DL_LIMIT is reached
for name, ext in image_pairs:
    #so long as we haven't hit the download limit:
    if current < DL_LIMIT:
        #this is the image URL location
        url = r'http://imgur.com/{name}{ext}'.format(name=name, ext=ext)
        #print the image we are currently downloading
        print 'Current image being downloaded:', url

        #download the image data
        response = requests.get(url)
        #set the file location
        path = r'./{fldr}/{name}{ext}'.format(fldr=legal_folder,
                                              name=name,
                                              ext=ext)
        #open the file object in write binary mode
        fp = open(path, 'wb')
        #perform the write operation
        fp.write(response.content)
        #close the file
        fp.close()
        #advance the image count
        current += 1

#print off a completion string
print 'Finished downloading {cnt} images to {fldr}!'.format(cnt=current,
                                                            fldr=legal_folder)

"""
