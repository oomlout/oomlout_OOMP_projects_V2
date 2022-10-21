
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4363"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4363"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Airlift Bitsy Add On PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Airlift-Bitsy-Add-On-PCB')
    newPart['gitName'].append('Adafruit-Airlift-Bitsy-Add-On-PCB')
    newPart['eagleBoard'].append('/Adafruit Airlift Bitsy Add-On.brd')
    newPart['eagleSchem'].append('/Adafruit Airlift Bitsy Add-On.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

