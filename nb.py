import pandas as pd
data = pd.read_csv('golf.csv')
print(data)

data.head(2)

outlook = data["Outlook"].values
temp = data["Temperature"].values
humid = data["Humidity"].values
windy = data["Windy"].values
play = data["Play"].values

print(outlook)
print(temp)
print(humid)
print(windy)
print(play)


count = data.count()[1]
print(count)
count

inp_outlook = input("Enter outlook: ")
inp_temp = input("Enter Temperature: ")
inp_humidity = input("Enter humidity: ")
inp_windy = input("If it is windy or no: ")


play_yes, play_no = 0,0

for i in play:
    if(i == "yes"):
        play_yes += 1
    else:
        play_no += 1    
play_yes, play_no

prob_yes = play_yes/count
prob_no = play_no/count
prob_yes, prob_no


# outlook
outlook_yes, outlook_no = 0, 0

for i in range(0, count):
    if(outlook[i] == inp_outlook ):
        if(play[i] == "yes"):
            outlook_yes += 1
        else:
            outlook_no += 1

outlook_yes, outlook_no

inp_outlook_yes = outlook_yes/play_yes
inp_outlook_no = outlook_no/play_no


inp_outlook_yes, inp_outlook_no


# temp
temp_yes, temp_no = 0, 0

for i in range(0, count):
    if(temp[i] == inp_temp ):
        if(play[i] == "yes"):
            temp_yes += 1
        else:
            temp_no += 1

temp_yes, temp_no

inp_temp_yes = temp_yes/play_yes
inp_temp_no = temp_no/play_no


inp_temp_yes, inp_temp_no


# humidity
humid_yes, humid_no = 0, 0

for i in range(0, count):
    if(humid[i] == inp_humidity ):
        if(play[i] == "yes"):
            humid_yes += 1
        else:
            humid_no += 1

humid_yes, humid_no

inp_humid_yes = humid_yes/play_yes
inp_humid_no = humid_no/play_no


inp_humid_yes, inp_humid_no


# windy
windy_yes, windy_no = 0, 0

for i in range(0, count):
    if(str(windy[i]) == inp_windy):
        if(play[i] == "yes"):
            windy_yes += 1
        else:
            windy_no += 1

windy_yes, windy_no

inp_windy_yes = windy_yes/play_yes
inp_windy_no = windy_no/play_no


inp_windy_yes, inp_windy_no


can_play = prob_yes * inp_outlook_yes * inp_temp_yes * inp_humid_yes * inp_windy_yes
cannot_play = prob_no * inp_outlook_no * inp_temp_no * inp_humid_no * inp_windy_no


if(can_play > cannot_play):
    print("Players can play.")
else:
    print("Players cannot play.")