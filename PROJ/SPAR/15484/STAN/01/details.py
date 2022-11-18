
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15484"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15484"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Artemis Global Tracker')
    newPart['gitRepo'].append('https://github.com/sparkfun/Artemis_Global_Tracker')
    newPart['gitName'].append('Artemis_Global_Tracker')
    newPart['eagleBoard'].append('/Hardware/Artemis_Global_Tracker.brd')
    newPart['eagleSchem'].append('/Hardware/Artemis_Global_Tracker.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

