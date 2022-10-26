
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "0330"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR0330"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Microtouch')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_Microtouch')
    newPart['gitName'].append('Adafruit_Microtouch')
    newPart['eagleBoard'].append('/PCB/microtouch.brd')
    newPart['eagleSchem'].append('/PCB/microtouch.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

