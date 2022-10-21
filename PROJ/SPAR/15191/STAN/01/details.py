
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "SPAR"
    oColor = "15191"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR15191"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('SparkFun Qwiic RFID ID XXLA')
    newPart['gitRepo'].append('https://github.com/sparkfun/SparkFun_Qwiic_RFID_ID-XXLA')
    newPart['gitName'].append('SparkFun_Qwiic_RFID_ID-XXLA')
    newPart['eagleBoard'].append('/Hardware/Qwiic RFID - IDXXLA.brd')
    newPart['eagleSchem'].append('/Hardware/Qwiic RFID - IDXXLA.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

