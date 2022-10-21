
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5296"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5296"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LED Arcade Button 1x4 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LED-Arcade-Button-1x4-PCB')
    newPart['gitName'].append('Adafruit-LED-Arcade-Button-1x4-PCB')
    newPart['eagleBoard'].append('/Adafruit LED Arcade Button 1x4.brd')
    newPart['eagleSchem'].append('/Adafruit LED Arcade Button 1x4.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

