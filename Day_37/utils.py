import datetime as dt

END_POINT = "https://pixe.la/v1/users"
DATE = dt.datetime.now().strftime("%Y%m%d")

HEADERS = {
    "X-USER-TOKEN": "your custom token",
}

PARAMS_PIXE = {
    "token": "your custom token",
    "username": "vieuxnorris",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

PARAMS_PIXE_GRAPH = {
    "id": "graph1",
    "name": "graphUser",
    "unit": "commit",
    "type": "float",
    "color": "sora",
}

PARAMS_PIXEL = {
    "date": f"{DATE}",
    "quantity": "5",
}

PARAMS_PIXEL_PUT = {
    "quantity": "1",
}