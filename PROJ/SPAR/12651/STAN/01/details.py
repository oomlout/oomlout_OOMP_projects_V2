
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "12651"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR12651"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Digital Sandbox')
    newPart['gitRepo'].append('https://github.com/sparkfun/Digital_Sandbox')
    newPart['gitName'].append('Digital_Sandbox')
    newPart['eagleBoard'].append('/Hardware/DigitalSandbox.brd')
    newPart['eagleSchem'].append('/Hardware/DigitalSandbox.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

