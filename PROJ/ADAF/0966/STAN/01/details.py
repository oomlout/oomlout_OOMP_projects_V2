
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0966"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0966"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Low profile microSD to SD Adapter PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Low-profile-microSD-to-SD-Adapter-PCB')
    newPart['gitName'].append('Adafruit-Low-profile-microSD-to-SD-Adapter-PCB')
    newPart['eagleBoard'].append('/Adafruit Pi SD Card Adapter.brd')
    newPart['eagleSchem'].append('/Adafruit Pi SD Card Adapter.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

