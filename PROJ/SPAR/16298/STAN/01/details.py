
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "16298"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR16298"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic PHT MS8607')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_PHT_MS8607')
    newPart['gitName'].append('Qwiic_PHT_MS8607')
    newPart['eagleBoard'].append('/Hardware/Qwiic PHT Sensor - MS8607.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic PHT Sensor - MS8607.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

