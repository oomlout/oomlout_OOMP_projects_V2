
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17182"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17182"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic I2C Capacitor')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_I2C_Capacitor')
    newPart['gitName'].append('Qwiic_I2C_Capacitor')
    newPart['eagleBoard'].append('/Hardware/Qwiic_I2C_Capacitor.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_I2C_Capacitor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

