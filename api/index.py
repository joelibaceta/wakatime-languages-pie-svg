from http.server import BaseHTTPRequestHandler
from io import StringIO

import requests
import re
import os
import colorsys
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np 
import random



class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    wakatime_json_url = "https://wakatime.com/share/@joelibaceta/d6c82088-6c98-4dd6-a2ee-9cf6f1bad568.json" #self.get_param('wakatime_url', self.path)

    r = requests.get(wakatime_json_url)

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
    ax1.legend(handles, labels, prop={'size':8}, bbox_to_anchor=(0.2,1.00))

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg', dpi=199)
    imgdata.seek(0)

    svg_dta = imgdata.read()


    self.send_response(200)
    self.send_header("Accept-Ranges", "bytes")
    self.send_header("Access-Control-Allow-Origin", "*")
    self.send_header("Content-Disposition", "attachment")
    self.send_header("Content-Length", len(svg_dta))
    self.send_header("Content-type", "image/svg+xml")
    self.end_headers()
    self.wfile.write(str(svg_dta).encode())
    return  