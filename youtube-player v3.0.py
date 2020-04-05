from urllib.request import urlopen
from bs4 import BeautifulSoup

import os
# search_query = input("hi there, \n What do u wanna search in Youtube? ")

# multi_search = search_query.replace(" ", "+")
def title_str(string):
    start = string.find(">")
    end = string.find("</a>")
    title = string[start+1:end]
    return title
    
def url(string):
    
    link_begin_number = string.find("/watch")
    link_end_number = string.find("rel")
    link_without_youtube = string[link_begin_number:link_end_number-2]
    link_with_youtube= "https://www.youtube.com"+link_without_youtube
    return link_with_youtube    

def time_since_post(string):
    link_begin_number = string.find("i>")
    link_end_number = string.find("</")
    var_time_since_post = string[link_begin_number+2:link_end_number]
    return var_time_since_post

def num_views(string):
    link_begin_number = string.find("i>")
    link_end_number = string.find("</")
    a = string[link_begin_number+2:link_end_number]
    return a

def video_length(string):
    a = string.find(">")
    b = string.find("</")
    c = string[a+1:b]
    return c

    
search_query = input("hi there, \n What do u wanna search in Youtube? ")

multi_search = search_query.replace(" ", "+")
    

# search_query = "yassuo"
multi_search = 'https://www.youtube.com/results?search_query='+multi_search
print(multi_search)
html = urlopen(multi_search)
# time.sleep(5000)
bs = BeautifulSoup(html.read(), 'html.parser')
video_title_link = bs.find_all(class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link")
uploader = bs.find_all(class_ = r"yt-uix-sessionlink spf-link") #by whom
date_views = bs.find_all(class_ = r"yt-lockup-meta-info")
time = bs.find_all(class_ = "accessible-description")
i = 0
list_time_since_post = []
list_views =[]
for i in range(0, 15):
    children_date_views = date_views[i].findAll("li", recursive=False)
    # print(len(children_date_views))
    list_time_since_post = list_time_since_post+ [str(children_date_views[0])]
    if len(children_date_views) == 1:
        print(str(i) + " "+title_str(str(video_title_link[i]))+" "+time_since_post(str(list_time_since_post[i]))+ video_length(str(time[i]))+ "\n\n")
    if len(children_date_views) > 1 :
        views = num_views(str(children_date_views[1]))
        # # for i in range(1, 10):
        # print(list_views[0])
        # views = num_views(str(list_views[i]))
        print(str(i) + " "+title_str(str(video_title_link[i]))+" "+time_since_post(str(list_time_since_post[i])) + "," + views + video_length(str(time[i])) + "\n\n" )

video_to_be_played = input("select the number: ")
resolution = input("Enter the resolution you want (in p): ")


well = str(url(str(video_title_link[int(video_to_be_played)])))
print(well)
os.system('cmd /c "cd C:\Program Files\VideoLAN\VLC\ & vlc '+'--preferred-resolution='+ resolution+" "+ well)