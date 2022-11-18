
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18621"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18621"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkX smol Power Board AAA')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkX_smol_Power_Board_AAA')
    newPart['gitName'].append('SparkX_smol_Power_Board_AAA')
    newPart['eagleBoard'].append('/Hardware/SparkX_smol_Power_AAA.brd')
    newPart['eagleSchem'].append('/Hardware/SparkX_smol_Power_AAA.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

