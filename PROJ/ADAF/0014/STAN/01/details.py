
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0014"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0014"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit MintyBoost PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_MintyBoost_PCB')
    newPart['gitName'].append('Adafruit_MintyBoost_PCB')
    newPart['eagleBoard'].append('/mintyboostv2.brd')
    newPart['eagleSchem'].append('/mintyboostv2.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

