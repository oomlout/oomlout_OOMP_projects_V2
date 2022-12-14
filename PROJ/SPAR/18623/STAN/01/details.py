
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "18623"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR18623"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkX smol ZOE M8Q')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkX_smol_ZOE-M8Q')
    newPart['gitName'].append('SparkX_smol_ZOE-M8Q')
    newPart['eagleBoard'].append('/Hardware/SparkX_smol_ZOE-M8Q.brd')
    newPart['eagleSchem'].append('/Hardware/SparkX_smol_ZOE-M8Q.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

