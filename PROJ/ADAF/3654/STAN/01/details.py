
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3654"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3654"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit WINC1500 Shield PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-WINC1500-Shield-PCB')
    newPart['gitName'].append('Adafruit-WINC1500-Shield-PCB')
    newPart['eagleBoard'].append('/Adafruit Winc1500 Shield.brd')
    newPart['eagleSchem'].append('/Adafruit Winc1500 Shield.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

