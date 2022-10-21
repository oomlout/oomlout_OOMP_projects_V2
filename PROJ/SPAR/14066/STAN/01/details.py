
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "14066"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR14066"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Simultaneous RFID Tag Reader')
    newPart['gitRepo'].append('https://github.com/sparkfun/Simultaneous_RFID_Tag_Reader')
    newPart['gitName'].append('Simultaneous_RFID_Tag_Reader')
    newPart['eagleBoard'].append('/Hardware/Simultaneous_RFID_Tag_Reader.brd')
    newPart['eagleSchem'].append('/Hardware/Simultaneous_RFID_Tag_Reader.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

