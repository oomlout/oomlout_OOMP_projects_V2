
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4351"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4351"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Infineon Trust M PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Infineon-Trust-M-PCB')
    newPart['gitName'].append('Adafruit-Infineon-Trust-M-PCB')
    newPart['eagleBoard'].append('/Adafruit Infineon Trust M.brd')
    newPart['eagleSchem'].append('/Adafruit Infineon Trust M.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

