
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17353"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17353"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Qwiic BMI270')
    newPart['gitRepo'].append('https://github.com/sparkfun/Qwiic_BMI270')
    newPart['gitName'].append('Qwiic_BMI270')
    newPart['eagleBoard'].append('/Hardware/Qwiic_BMI270.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic_BMI270.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

