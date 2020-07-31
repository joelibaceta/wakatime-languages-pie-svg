import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import requests
import random

url = 'https://wakatime.com/share/@joelibaceta/d6c82088-6c98-4dd6-a2ee-9cf6f1bad568.json'

r = requests.get(url)

response = r.json()

plt.rcParams['font.size'] = 7.0
plt.rcParams['figure.figsize'] = 8, 3.35

labels = []
sizes = []

for item in response["data"]:
  labels.append(f'{item["name"]} ({item["percent"]}%)')
  sizes.append(item["percent"]) 

fig1, ax1 = plt.subplots()

colors = ["#e54335", "#f15789", "#eb8918", "#e9b126", "#e8d948", "#afc526", "#1e9eea", "#a42fba"]
 
ax1.pie(sizes, labels=labels, autopct='', startangle=90, radius=2, rotatelabels = False, colors = colors, labeldistance=9999999)
ax1.axis('equal')

centre_circle = plt.Circle((0,0),0.90,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
 

handles, labels = ax1.axes.get_legend_handles_labels()
ax1.legend(handles, labels, prop={'size':8},
          bbox_to_anchor=(0.2,1.00))

fig.savefig('temp.svg', dpi=199)

file = open('temp.svg')

