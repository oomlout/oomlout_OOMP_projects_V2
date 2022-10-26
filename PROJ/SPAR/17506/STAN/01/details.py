
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "17506"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR17506"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun LoRa Thing Plus expLoRaBLE')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_LoRa_Thing_Plus_expLoRaBLE')
    newPart['gitName'].append('SparkFun_LoRa_Thing_Plus_expLoRaBLE')
    newPart['eagleBoard'].append('/Hardware/expLoRaBLE Thing Plus.brd')
    newPart['eagleSchem'].append('/Hardware/expLoRaBLE Thing Plus.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

