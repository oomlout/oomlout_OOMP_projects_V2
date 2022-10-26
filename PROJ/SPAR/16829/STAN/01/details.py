
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16829"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16829"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('MicroMod Data Logging Carrier')
    newPart['gitRepo'].append('https://github.com/sparkfun/MicroMod_Data_Logging_Carrier')
    newPart['gitName'].append('MicroMod_Data_Logging_Carrier')
    newPart['eagleBoard'].append('/Hardware/MicroMod-Datalogging-CarrierBoard.brd')
    newPart['eagleSchem'].append('/Hardware/MicroMod-Datalogging-CarrierBoard.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

