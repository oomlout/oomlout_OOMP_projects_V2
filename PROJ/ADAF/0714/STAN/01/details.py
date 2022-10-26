
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0714"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0714"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit RGB LCD shield PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-RGB-LCD-shield-PCB')
    newPart['gitName'].append('Adafruit-RGB-LCD-shield-PCB')
    newPart['eagleBoard'].append('/adafruit_rgblcdshield.brd')
    newPart['eagleSchem'].append('/adafruit_rgblcdshield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

