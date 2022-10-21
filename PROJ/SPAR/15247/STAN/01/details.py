
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15247"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15247"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('GNSS Chip Antenna Evaluation Board')
    newPart['gitRepo'].append('https://github.com/sparkfun/GNSS_Chip_Antenna_Evaluation_Board')
    newPart['gitName'].append('GNSS_Chip_Antenna_Evaluation_Board')
    newPart['eagleBoard'].append('/Hardware/GNSS_Chip_Antenna_Evaluation_Board.brd')
    newPart['eagleSchem'].append('/Hardware/GNSS_Chip_Antenna_Evaluation_Board.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

