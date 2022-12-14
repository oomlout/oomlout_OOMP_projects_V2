
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3661"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3661"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit AP3602A PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-AP3602A-PCB')
    newPart['gitName'].append('Adafruit-AP3602A-PCB')
    newPart['eagleBoard'].append('/Adafruit AP6302.brd')
    newPart['eagleSchem'].append('/Adafruit AP6302.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

