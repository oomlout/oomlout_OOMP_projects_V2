
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "13030"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR13030"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('RFID Reader Breakout')
    newPart['gitRepo'].append('https://github.com/sparkfun/RFID_Reader_Breakout')
    newPart['gitName'].append('RFID_Reader_Breakout')
    newPart['eagleBoard'].append('/hardware/RFID_Breakout.brd')
    newPart['eagleSchem'].append('/hardware/RFID_Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

