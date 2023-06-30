import numpy as np
import cv2
from PIL import Image
import urllib.parse
import urllib.request
import io
from  place_search import find_coordinate
from math import log,tan,pi,atan,exp,ceil
import requests



EARTH_RADIUS = 6378137
EQUATOR_CIRCUMFERENCE = 2 * pi * EARTH_RADIUS
INITIAL_RESOLUTION = EQUATOR_CIRCUMFERENCE / 256.0
ORIGIN_SHIFT = EQUATOR_CIRCUMFERENCE / 2.0
  
def latlontopixels(lat, lon, zoom):
    mx = (lon * ORIGIN_SHIFT) / 180.0
    my = log(tan((90 + lat) * pi / 360.0)) / (pi / 180.0)
    my = (my * ORIGIN_SHIFT) / 180.0
    res = INITIAL_RESOLUTION / (2 ** zoom)
    px = (mx + ORIGIN_SHIFT) / res
    py = (my + ORIGIN_SHIFT) / res
    return px, py
  
def pixelstolatlon(px, py, zoom):
    res = INITIAL_RESOLUTION / (2 ** zoom)
    mx = px * res - ORIGIN_SHIFT
    my = py * res - ORIGIN_SHIFT
    lat = (my / ORIGIN_SHIFT) * 180.0
    lat = 180 / pi * (2 * atan(exp(lat * pi / 180.0)) - pi / 2.0)
    lon = (mx / ORIGIN_SHIFT) * 180.0
    return lat, lon

query = input('What kinda places you want me look up? ')
results = find_coordinate(f'{query}')
print(results)

lat=results['data_lat']
long=results['data_lon']
zoom=18
url=f'https://dev.virtualearth.net/REST/V1/Imagery/Map/Aerial/{lat}%2C{long}/{zoom}?mapSize=601%2C300&format=png&key=Ai5BVOkNsheudc1Dr1qL_F-Yunpq-VWOJ0tForP_xIbZ5hYDww35iwr2xJeTVIOC'



f=requests.get(url)

with open("./myenv/map_img.png", "wb") as m_imggg:
    m_imggg.write(f.content)

img=cv2.imread('myenv/map_img.png')    
shifted = cv2.pyrMeanShiftFiltering(img, 17, 30)
gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
hsv = cv2.cvtColor(shifted, cv2.COLOR_BGR2HSV)

lower_trees = np.array([10, 0, 30])
higher_trees = np.array([180, 100, 95])
  
lower_houses = np.array([90, 10, 100])
higher_houses = np.array([255, 255, 255])
  
lower_roads = np.array([255, 255, 255])
higher_roads = np.array([130, 126, 126])
  
lower_feilds = np.array([0, 50, 100])
higher_feilds = np.array([50, 255, 130])
  
lower_feilds_blue = np.array([0, 80, 100])
higher_feilds_blue = np.array([255, 250, 255])


masktree = cv2.inRange(hsv, lower_trees, higher_trees)
maskhouses = cv2.inRange(hsv, lower_houses, higher_houses)
maskroads = cv2.inRange(hsv, lower_roads, higher_roads)
maskfeilds = cv2.inRange(hsv, lower_feilds, higher_feilds)
gausssion_blur_maskfields = cv2.GaussianBlur(maskfeilds, (15, 15), 0)
gausssion_blur_masktree = cv2.GaussianBlur(masktree, (15, 15), 0)
blue_limiter = cv2.inRange(hsv, lower_feilds_blue, higher_feilds_blue)
res_roads = cv2.bitwise_and(img, img, mask=maskroads)
res_feilds = cv2.bitwise_and(img, img, mask=gausssion_blur_maskfields)
res_trees = cv2.bitwise_and(img, img, mask=masktree)

cv2.imshow('res', res_trees)
cv2.imshow('res_fields', res_feilds)
cv2.imshow('res_roads', maskroads)
cv2.imshow('img', img)

from aforestation_area import afforestation_area
afforestation_area()

cv2.waitKey(0)
cv2.destroyAllWindows()




