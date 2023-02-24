import requests
from utils import *


def createUser():
    try:
        with requests.post(url=END_POINT, json=PARAMS_PIXE) as pixe:
            pixe.raise_for_status()
    except requests.exceptions.HTTPError:
        print("User exist.")


def createGraph():
    try:
        with requests.post(url=f"{END_POINT}/{PARAMS_PIXE['username']}/graphs", headers=HEADERS,
                           json=PARAMS_PIXE_GRAPH) as pixeGraph:
            pixeGraph.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Graph exist.")


def postPixelGraph():
    with requests.post(url=f"{END_POINT}/{PARAMS_PIXE['username']}/graphs/{PARAMS_PIXE_GRAPH['id']}", headers=HEADERS,
                       json=PARAMS_PIXEL) as pixel:
        pixel.raise_for_status()


def putPixelGraph():
    with requests.put(
            url=f"{END_POINT}/{PARAMS_PIXE['username']}/graphs/{PARAMS_PIXE_GRAPH['id']}/{PARAMS_PIXEL['date']}",
            headers=HEADERS, json=PARAMS_PIXEL_PUT) as putPixel:
        putPixel.raise_for_status()


def deletePixelGraph():
    with requests.delete(
            url=f"{END_POINT}/{PARAMS_PIXE['username']}/graphs/{PARAMS_PIXE_GRAPH['id']}/{PARAMS_PIXEL['date']}",
            headers=HEADERS) as deletePixel:
        deletePixel.raise_for_status()


deletePixelGraph()
