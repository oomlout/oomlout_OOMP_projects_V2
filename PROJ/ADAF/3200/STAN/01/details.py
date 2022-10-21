
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3200"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3200"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Teensy 3.x Feather Adapter PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Teensy-3.x-Feather-Adapter-PCB')
    newPart['gitName'].append('Adafruit-Teensy-3.x-Feather-Adapter-PCB')
    newPart['eagleBoard'].append('/Adafruit Feather Teensy3 Adapter Original.brd')
    newPart['eagleSchem'].append('/Adafruit Feather Teensy3 Adapter Original.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

