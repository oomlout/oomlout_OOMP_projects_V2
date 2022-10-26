
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5217"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5217"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit EyeLights LED Glasses and Driver PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-EyeLights-LED-Glasses-and-Driver-PCB')
    newPart['gitName'].append('Adafruit-EyeLights-LED-Glasses-and-Driver-PCB')
    newPart['eagleBoard'].append('/Adafruit EyeLights LED Glasses Driver.brd')
    newPart['eagleSchem'].append('/Adafruit EyeLights LED Glasses Driver.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

