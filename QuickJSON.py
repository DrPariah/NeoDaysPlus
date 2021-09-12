#!/usr/bin/env python3

import json
import os
import re
import shutil

# destinationPath = "Small_10x10/"
destinationPath = "Large_20x20/"

images = []
imageFolderPath = "Tiles_TBP/"
imageFiletype = ".png"

template = {}

with open("tile_template.json", "r") as read_file:
    template = json.load(read_file)

for image in os.listdir("Tiles_TBP"):
    images.append(os.path.join("Tiles_TBP", image))

for image in images:
    print("Processing " + image)

    pathRegex = '(?<=' + imageFolderPath + ')(.*).png'
    id = re.findall(pathRegex, image)[0]

    print("Creating " + id + " json")

    template["id"] = id
    template["fg"] = id

    jsonPath = destinationPath + id + ".json"

    with open(jsonPath, 'a+') as outfile:
        json.dump(template, fp=outfile)

    imageSource = imageFolderPath + id + imageFiletype
    shutil.move(imageSource, destinationPath)
