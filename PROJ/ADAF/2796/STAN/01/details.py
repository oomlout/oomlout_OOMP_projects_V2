
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2796"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2796"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Feather M0 Adalogger PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Feather-M0-Adalogger-PCB')
    newPart['gitName'].append('Adafruit-Feather-M0-Adalogger-PCB')
    newPart['eagleBoard'].append('/Adafruit Feather M0 Adalogger.brd')
    newPart['eagleSchem'].append('/Adafruit Feather M0 Adalogger.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

