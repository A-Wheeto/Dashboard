import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
from io import BytesIO
import requests
import weather2
import piholeget
import hddspace
import steam
import news
import xplane

print(datetime.now().strftime('%A, %d %B %Y\n'))
print("LOADING, PLEASE WAIT...\n")

# CREATE WINDOW - RESIZE FALSE - SIZE - TITLE CARD
root = tk.Tk()
root.resizable(False, False)
root.geometry('1305x780')
root.title("Dashboard")
root.configure(bg='#c7d5e0')

# DRAW TOP BLUE BAR - DRAW TITLE - DRAW DATETIME
top_bg = tk.Canvas(root, width=1305, height=60, bg='#1b2838', highlightthickness=0).place(x=0, y=0)
tk.Label(top_bg, text='Dashboard', font='Montserrat 25', bg='#1b2838', fg='white').place(x=15, y=3)
tk.Label(top_bg, text=datetime.now().strftime('%A, %d %B %Y'), font='Montserrat 20', bg='#1b2838', fg='white').place(
    x=930, y=8)

# BBC NEWS
news_box = tk.Canvas(root, width=350, height=140, bg='#2a475e', highlightthickness=0).place(x=20, y=620)
news_box_top = tk.Canvas(root, width=350, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=600)
tk.Label(news_box_top, text='BBC News', font='Montserrat 7 bold', bg='#1b2838',
         fg='#FFFFFF').place(x=25, y=600)

news_data = news.GetNews()

headline = []
news_y = 620
for i in range(0, 7):
    if len(news_data[i]) > 50:
        headline.append(news_data[i][:50] + '...')
    else:
        headline.append(news_data[i])
    tk.Label(news_box, text='- ' + headline[i], font='Montserrat 9', bg='#2a475e', fg='#FFFFFF').place(x=25, y=news_y)
    news_y += 19

# THRESHOLD NEWS
threshold_box = tk.Canvas(root, width=285, height=520, bg='#2a475e', highlightthickness=0).place(x=1000, y=240)
threshold_box_top = tk.Canvas(root, width=285, height=20, bg='#1b2838', highlightthickness=0).place(x=1000, y=220)
tk.Label(threshold_box_top, text='Threshold News', font='Montserrat 7 bold', bg='#1b2838',
         fg='#FFFFFF').place(x=1005, y=220)

threshold_headlines = xplane.getheadlines()


def getimage_threshold(imgurl):
    response_img = requests.get(imgurl)
    img_data = response_img.content
    img_resize = Image.open(BytesIO(img_data)).resize((245, 120), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_resize)
    return img


th_y = 255
thresholdpics_list = []
for i in range(3):
    thresholdpics_list.append(getimage_threshold(threshold_headlines[i].url))
    tk.Label(root, image=thresholdpics_list[i], width=245, height=120, bd=0).place(x=1020, y=th_y)
    tk.Label(threshold_box, text=threshold_headlines[i].date, font='Montserrat 8', bg='#1b2838',
             fg='#FFFFFF').place(x=1020, y=th_y)
    tk.Label(threshold_box, text=threshold_headlines[i].headline, font='Montserrat 9', bg='#2a475e', fg='#FFFFFF',
             wraplength=245, justify='center').place(x=1020, y=th_y + 120)
    th_y += 170

# STEAM TOP SELLING
steam_box = tk.Canvas(root, width=590, height=520, bg='#2a475e', highlightthickness=0).place(x=390, y=240)
steam_box_top = tk.Canvas(root, width=590, height=20, bg='#1b2838', highlightthickness=0).place(x=390, y=220)
steam_box_price = tk.Canvas(steam_box, width=80, height=520, bg='#171a21', highlightthickness=0).place(x=900, y=240)
tk.Label(steam_box_top, text='Steam Top Selling', font='Montserrat 7 bold', bg='#1b2838',
         fg='#FFFFFF').place(x=395, y=220)

steam_games = steam.GetGames()


def getimage_steam(imgurl):
    url = 'https://steamcdn-a.akamaihd.net/steam/apps/' + imgurl + '/capsule_184x69.jpg'
    response_img = requests.get(url)
    img_data = response_img.content
    img_resize = Image.open(BytesIO(img_data)).resize((107, 40), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_resize)
    return img


img_y = 240
photo_list = []
for i in range(0, 13):
    photo_list.append(getimage_steam(steam_games[i].imgurl))
    tk.Label(root, image=photo_list[i], width=107, height=40, bd=0).place(x=390, y=img_y)
    img_y += 40

steam_y = 245
for i in range(0, 13):
    tk.Label(steam_box, text=steam_games[i].title, font='Montserrat 12', bg='#2a475e',
             fg='#FFFFFF').place(x=500, y=steam_y)
    tk.Label(steam_box, text=steam_games[i].price, font='Montserrat 12', bg='#171a21',
             fg='#FFFFFF').place(x=910, y=steam_y)
    steam_y += 40

# WEATHER ---------------------------------
weather_data = weather2.get()

weather_box = tk.Canvas(root, width=1265, height=100, bg='#2a475e', highlightthickness=0).place(x=20, y=100)
weather_box_top = tk.Canvas(root, width=1265, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=80)
tk.Label(weather_box_top, text='Weather Forcast, York UK', font='Montserrat 7 bold', bg='#1b2838',
         fg='#FFFFFF').place(x=25, y=80)


def geticon_weather(iconcode):
    url = 'http://openweathermap.org/img/wn/' + iconcode + '@2x.png'
    response_img = requests.get(url)
    img_data = response_img.content
    img_resize = Image.open(BytesIO(img_data)).resize((80, 80), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_resize)
    return img


day_x = 165
icon_x = 150
icon_list = []
for i in range(0, 8):
    icon_list.append(geticon_weather(weather_data[0][i].icon))
    tk.Label(root, image=icon_list[i], width=80, height=80, bd=0, bg='#2a475e').place(x=icon_x, y=100)
    tk.Label(root, text=weather_data[0][i].day + ' - ' + str(weather_data[0][i].temp) + '°', bg='#2a475e', fg='#FFFFFF',
             font='Montserrat 8').place(x=day_x, y=170)
    icon_x += 120
    day_x += 120

tk.Label(weather_box, text=str(weather_data[0][0].temp) + '°', font='Montserrat 40', bg='#2a475e',
         fg='#FFFFFF').place(x=50, y=107)

tk.Label(weather_box, text='Sunrise: ' + weather_data[1], font='Montserrat 12', bg='#2a475e',
         fg='#FFFFFF').place(x=1100, y=120)
tk.Label(weather_box, text='Sunset: ' + weather_data[2], font='Montserrat 12', bg='#2a475e',
         fg='#FFFFFF').place(x=1105, y=150)

# PI HOLE -------------------------------------
pihole_data = piholeget.GetData()

pihole_box = tk.Canvas(root, width=350, height=140, bg='#2a475e', highlightthickness=0).place(x=20, y=240)
pihole_box_top = tk.Canvas(root, width=350, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=220)
pihole_box_temp = tk.Canvas(pihole_box, width=350, height=30, bg='#2a475e', highlightthickness=0).place(x=20, y=240)
pihole_box_middle = tk.Canvas(pihole_box, width=350, height=20, bg='#171a21', highlightthickness=0).place(x=20, y=270)
tk.Label(pihole_box_top, text='Raspberry Pi Status', font='Montserrat 7 bold', bg='#1b2838', fg='#FFFFFF') \
    .place(x=25, y=220)

if str(pihole_data[0]) == 'enabled':
    pihole_enabled_colour = '#1c7c4c'
else:
    pihole_enabled_colour = '#E74C3C'

tk.Label(pihole_box_temp, text='Pi Hole - ' + str(pihole_data[0]), font='Montserrat 7 bold',
         bg='#171a21', fg=pihole_enabled_colour) \
    .place(x=25, y=270)

tk.Label(pihole_box, text='Temperature: ' + pihole_data[5] + '°C', font='Montserrat 12', bg='#2a475e',
         fg='#FFFFFF').place(x=22, y=240)
tk.Label(pihole_box, text='Memory Usage: ' + pihole_data[6] + '%', font='Montserrat 12', bg='#2a475e',
         fg='#FFFFFF').place(x=190, y=240)
tk.Label(pihole_box, text='Percentage Blocked: ' + pihole_data[1], font='Montserrat 12', bg='#2a475e',
         fg='#FFFFFF').place(x=25, y=292)
tk.Label(pihole_box, text='Queries Blocked: ' + pihole_data[2], font='Montserrat 12', bg='#2a475e',
         fg='#FFFFFF').place(x=25, y=320)
tk.Label(pihole_box, text='Last Updated: ' + str(pihole_data[3]) + ' days, ' + str(pihole_data[4])
                          + ' hours', font='Montserrat 12', bg='#2a475e', fg='#FFFFFF').place(x=25, y=348)

checkmark_image = Image.open('C:\\Users\\adamw\\PycharmProjects\\Dashboard\\images\\checkmark3.png')
checkmark = ImageTk.PhotoImage(checkmark_image)
canvas_checkmark = tk.Canvas(pihole_box, width=77, height=80, bg='#2a475e', bd=0, highlightthickness=0)
canvas_checkmark.create_image(0, 0, image=checkmark, anchor='nw')

if str(pihole_data[0]) == 'enabled':
    canvas_checkmark.place(x=280, y=295)

# HARD DRIVE CAPACITIES

hdd_data = hddspace.GetDriveSpace()

hdd_box = tk.Canvas(root, width=350, height=160, bg='#2a475e', highlightthickness=0).place(x=20, y=420)
hdd_box_top = tk.Canvas(root, width=350, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=400)
tk.Label(hdd_box_top, text='Current Hard Drive Capacities', font='Montserrat 7 bold', bg='#1b2838', fg='#FFFFFF') \
    .place(x=25, y=400)

tk.Label(hdd_box, text="C", font='Montserrat 12 bold', bg='#2a475e', fg='#FFFFFF').place(x=25, y=425)
tk.Label(hdd_box, text="D", font='Montserrat 12 bold', bg='#2a475e', fg='#FFFFFF').place(x=25, y=455)
tk.Label(hdd_box, text="E", font='Montserrat 12 bold', bg='#2a475e', fg='#FFFFFF').place(x=25, y=485)
tk.Label(hdd_box, text="F", font='Montserrat 12 bold', bg='#2a475e', fg='#FFFFFF').place(x=25, y=515)
tk.Label(hdd_box, text="G", font='Montserrat 12 bold', bg='#2a475e', fg='#FFFFFF').place(x=25, y=545)

tk.Canvas(hdd_box, width=100, height=20, bg="#c7d5e0", bd=0, highlightthickness=0).place(x=50, y=430)
tk.Canvas(hdd_box, width=100, height=20, bg="#c7d5e0", bd=0, highlightthickness=0).place(x=50, y=460)
tk.Canvas(hdd_box, width=100, height=20, bg="#c7d5e0", bd=0, highlightthickness=0).place(x=50, y=490)
tk.Canvas(hdd_box, width=100, height=20, bg="#c7d5e0", bd=0, highlightthickness=0).place(x=50, y=520)
tk.Canvas(hdd_box, width=100, height=20, bg="#c7d5e0", bd=0, highlightthickness=0).place(x=50, y=550)

if 0 < int(hdd_data[0].percent) <= 25:
    percentage_colour_c = '#90EE90'
elif 25 < int(hdd_data[0].percent) <= 50:
    percentage_colour_c = '#FEB938'
elif 50 < int(hdd_data[0].percent) <= 75:
    percentage_colour_c = '#FD9415'
elif 75 < int(hdd_data[0].percent) < 90:
    percentage_colour_c = '#E23201'
else:
    percentage_colour_c = '#9B0002'

if 0 < int(hdd_data[1].percent) <= 25:
    percentage_colour_d = '#90EE90'
elif 25 < int(hdd_data[1].percent) <= 50:
    percentage_colour_d = '#FEB938'
elif 50 < int(hdd_data[1].percent) <= 75:
    percentage_colour_d = '#FD9415'
elif 75 < int(hdd_data[1].percent) < 90:
    percentage_colour_d = '#E23201'
else:
    percentage_colour_d = '#9B0002'

if 0 < int(hdd_data[2].percent) <= 25:
    percentage_colour_e = '#90EE90'
elif 25 < int(hdd_data[2].percent) <= 50:
    percentage_colour_e = '#FEB938'
elif 50 < int(hdd_data[2].percent) <= 75:
    percentage_colour_e = '#FD9415'
elif 75 < int(hdd_data[2].percent) < 90:
    percentage_colour_e = '#E23201'
else:
    percentage_colour_e = '#9B0002'

if 0 < int(hdd_data[3].percent) <= 25:
    percentage_colour_f = '#90EE90'
elif 25 < int(hdd_data[3].percent) <= 50:
    percentage_colour_f = '#FEB938'
elif 50 < int(hdd_data[3].percent) <= 75:
    percentage_colour_f = '#FD9415'
elif 75 < int(hdd_data[3].percent) < 90:
    percentage_colour_f = '#E23201'
else:
    percentage_colour_f = '#9B0002'

if 0 < int(hdd_data[4].percent) <= 25:
    percentage_colour_g = '#90EE90'
elif 25 < int(hdd_data[4].percent) <= 50:
    percentage_colour_g = '#FEB938'
elif 50 < int(hdd_data[4].percent) <= 75:
    percentage_colour_g = '#FD9415'
elif 75 < int(hdd_data[4].percent) < 90:
    percentage_colour_g = '#E23201'
else:
    percentage_colour_g = '#9B0002'

tk.Canvas(hdd_box, width=int(hdd_data[0].percent), height=20, bg=percentage_colour_c, bd=0,
          highlightthickness=0).place(x=50, y=430)
tk.Canvas(hdd_box, width=int(hdd_data[1].percent), height=20, bg=percentage_colour_d, bd=0,
          highlightthickness=0).place(x=50, y=460)
tk.Canvas(hdd_box, width=int(hdd_data[2].percent), height=20, bg=percentage_colour_e, bd=0,
          highlightthickness=0).place(x=50, y=490)
tk.Canvas(hdd_box, width=int(hdd_data[3].percent), height=20, bg=percentage_colour_f, bd=0,
          highlightthickness=0).place(x=50, y=520)
tk.Canvas(hdd_box, width=int(hdd_data[4].percent), height=20, bg=percentage_colour_g, bd=0,
          highlightthickness=0).place(x=50, y=550)

tk.Label(hdd_box, text=str(hdd_data[0].percent) + '% ', font='Montserrat 12 bold', bg='#2a475e',
         fg='#FFFFFF').place(x=160, y=425)
tk.Label(hdd_box, text=str(hdd_data[5][1]) + 'GB / ' + str(hdd_data[5][0]) + 'GB',
         font='Montserrat 8', bg='#2a475e',
         fg='#FFFFFF').place(x=240, y=429)

tk.Label(hdd_box, text=str(hdd_data[1].percent) + '%', font='Montserrat 12 bold', bg='#2a475e',
         fg='#FFFFFF').place(x=160, y=455)
tk.Label(hdd_box, text=str(hdd_data[6][1]) + 'GB / ' + str(hdd_data[6][0]) + 'GB',
         font='Montserrat 8', bg='#2a475e',
         fg='#FFFFFF').place(x=240, y=459)

tk.Label(hdd_box, text=str(hdd_data[2].percent) + '%', font='Montserrat 12 bold', bg='#2a475e',
         fg='#FFFFFF').place(x=160, y=485)
tk.Label(hdd_box, text=str(hdd_data[7][1]) + 'GB / ' + str(hdd_data[7][0]) + 'GB',
         font='Montserrat 8', bg='#2a475e',
         fg='#FFFFFF').place(x=240, y=489)

tk.Label(hdd_box, text=str(hdd_data[3].percent) + '%', font='Montserrat 12 bold', bg='#2a475e',
         fg='#FFFFFF').place(x=160, y=515)
tk.Label(hdd_box, text=str(hdd_data[8][1]) + 'GB / ' + str(hdd_data[8][0]) + 'GB',
         font='Montserrat 8', bg='#2a475e',
         fg='#FFFFFF').place(x=240, y=519)

tk.Label(hdd_box, text=str(hdd_data[4].percent) + '%', font='Montserrat 12 bold', bg='#2a475e',
         fg='#FFFFFF').place(x=160, y=545)
tk.Label(hdd_box, text=str(hdd_data[9][1]) + 'GB / ' + str(hdd_data[9][0]) + 'GB',
         font='Montserrat 8', bg='#2a475e',
         fg='#FFFFFF').place(x=240, y=549)

# 5 2
# 960


print('\nDRAWING DASHBOARD')
# MAINLOOP
root.mainloop()

# BGCOLOUR #aeccd0
# BOXCOLOR #20639B
