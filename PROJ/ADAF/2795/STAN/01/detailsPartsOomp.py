def load(newPart,it):
    it['PROJ-ADAF-2795-STAN-01']['oompParts'] = [{'JP1': {'OOMPID': 'HEAD-I01-X-PI16-01', 'FULL': {'DESC': '', 'PART': 'JP1', 'DEVICE': '1X16_ROUND ', 'PACKAGE': '1X16_ROUND', 'PARTLETTER': 'JP', 'VALUE': '', 'VALUENUMBER': '', 'PACKAGENUMBER': '116', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'JP1,,1X16_ROUND ,1X16_ROUND,,,'}},
       'SW1': {'OOMPID': 'BUTA-UNMATCHED-X-STAN-01', 'FULL': {'DESC': '', 'PART': 'SW1', 'DEVICE': 'KMR2 SPST_TACT-KMR2', 'PACKAGE': 'KMR2', 'PARTLETTER': 'SW', 'VALUE': 'SPST_TACT-KMR2', 'VALUENUMBER': '_-2', 'PACKAGENUMBER': '2', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SW1,SPST_TACT-KMR2,KMR2 SPST_TACT-KMR2,KMR2,,,'}},
       'R3': {'OOMPID': 'RESE-0603-X-O1003-01', 'FULL': {'DESC': '', 'PART': 'R3', 'DEVICE': '0603-NO 100k', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '100k', 'VALUENUMBER': '100', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R3,100k,0603-NO 100k,0603-NO,,,'}},
       'R9': {'OOMPID': 'RESE-0603-X-O1003-01', 'FULL': {'DESC': '', 'PART': 'R9', 'DEVICE': '0603-NO 100k', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '100k', 'VALUENUMBER': '100', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R9,100k,0603-NO 100k,0603-NO,,,'}},
       'IC1': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'IC1', 'DEVICE': 'TQFN44_7MM ATMEGA32U4-MU', 'PACKAGE': 'TQFN44_7MM', 'PARTLETTER': 'IC', 'VALUE': 'ATMEGA32U4-MU', 'VALUENUMBER': '324-', 'PACKAGENUMBER': '447', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'IC1,ATMEGA32U4-MU,TQFN44_7MM ATMEGA32U4-MU,TQFN44_7MM,,,'}},
       'R2': {'OOMPID': 'RESE-0603-X-O102-01', 'FULL': {'DESC': '', 'PART': 'R2', 'DEVICE': '0603-NO 1K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '1K', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R2,1K,0603-NO 1K,0603-NO,,,'}},
       'R1': {'OOMPID': 'RESE-0603-X-O102-01', 'FULL': {'DESC': '', 'PART': 'R1', 'DEVICE': '0603-NO 1K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '1K', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R1,1K,0603-NO 1K,0603-NO,,,'}},
       'R7': {'OOMPID': 'RESE-0603-X-O222-01', 'FULL': {'DESC': '', 'PART': 'R7', 'DEVICE': '0603-NO 2.2K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '2.2K', 'VALUENUMBER': '2.2', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R7,2.2K,0603-NO 2.2K,0603-NO,,,'}},
       'R4': {'OOMPID': 'RESE-0603-X-O220-01', 'FULL': {'DESC': '', 'PART': 'R4', 'DEVICE': '0603-NO 22', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '22', 'VALUENUMBER': '22', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R4,22,0603-NO 22,0603-NO,,,'}},
       'R5': {'OOMPID': 'RESE-0603-X-O220-01', 'FULL': {'DESC': '', 'PART': 'R5', 'DEVICE': '0603-NO 22', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '22', 'VALUENUMBER': '22', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R5,22,0603-NO 22,0603-NO,,,'}},
       'C8': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C8', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C8,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'C6': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C6', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C6,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'C3': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C3', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C3,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'X3': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'X3', 'DEVICE': '4UCONN_20329_V2 microUSB', 'PACKAGE': '4UCONN_20329_V2', 'PARTLETTER': 'X', 'VALUE': 'microUSB', 'VALUENUMBER': '', 'PACKAGENUMBER': '4203292', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'X3,microUSB,4UCONN_20329_V2 microUSB,4UCONN_20329_V2,,,'}},
       'R6': {'OOMPID': 'RESE-0603-X-O1003-01', 'FULL': {'DESC': '', 'PART': 'R6', 'DEVICE': '_0603MP 100K', 'PACKAGE': '_0603MP', 'PARTLETTER': 'R', 'VALUE': '100K', 'VALUENUMBER': '100', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R6,100K,_0603MP 100K,_0603MP,,,'}},
       'X2': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'X2', 'DEVICE': 'MICROSD microsd', 'PACKAGE': 'MICROSD', 'PARTLETTER': 'X', 'VALUE': 'microsd', 'VALUENUMBER': '', 'PACKAGENUMBER': '', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'X2,microsd,MICROSD microsd,MICROSD,,,'}},
       'U3': {'OOMPID': 'UNMATCHED-SO235-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'U3', 'DEVICE': 'SOT23-5 MCP73831T-2ACI/OT', 'PACKAGE': 'SOT23-5', 'PARTLETTER': 'U', 'VALUE': 'MCP73831T-2ACI/OT', 'VALUENUMBER': '73831-2/', 'PACKAGENUMBER': '235', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'U3,MCP73831T-2ACI/OT,SOT23-5 MCP73831T-2ACI/OT,SOT23-5,,,'}},
       'C7': {'OOMPID': 'CAPC-0603-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C7', 'DEVICE': '0603-NO 1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C7,1uF,0603-NO 1uF,0603-NO,,,'}},
       'C14': {'OOMPID': 'CAPC-0603-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C14', 'DEVICE': '0603-NO 1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C14,1uF,0603-NO 1uF,0603-NO,,,'}},
       'L0': {'OOMPID': 'UNMATCHED-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'L0', 'DEVICE': 'CHIPLED_0805_NOOUTLINE RED', 'PACKAGE': 'CHIPLED_0805_NOOUTLINE', 'PARTLETTER': 'L', 'VALUE': 'RED', 'VALUENUMBER': '', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'L0,RED,CHIPLED_0805_NOOUTLINE RED,CHIPLED_0805_NOOUTLINE,,,'}},
       'U2': {'OOMPID': 'UNMATCHED-SO235-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'U2', 'DEVICE': 'SOT23-5 SPX3819-3.3', 'PACKAGE': 'SOT23-5', 'PARTLETTER': 'U', 'VALUE': 'SPX3819-3.3', 'VALUENUMBER': '3819-3.3', 'PACKAGENUMBER': '235', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'U2,SPX3819-3.3,SOT23-5 SPX3819-3.3,SOT23-5,,,'}},
       'R8': {'OOMPID': 'RESE-0603-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'R8', 'DEVICE': '0603-NO 10K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '10K', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R8,10K,0603-NO 10K,0603-NO,,,'}},
       'C9': {'OOMPID': 'CAPC-0805-X-UF10-V25', 'FULL': {'DESC': '', 'PART': 'C9', 'DEVICE': '0805-NO 10uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10uF', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C9,10uF,0805-NO 10uF,0805-NO,,,'}},
       'L1': {'OOMPID': 'UNMATCHED-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'L1', 'DEVICE': 'CHIPLED_0805_NOOUTLINE GREEN', 'PACKAGE': 'CHIPLED_0805_NOOUTLINE', 'PARTLETTER': 'L', 'VALUE': 'GREEN', 'VALUENUMBER': '', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'L1,GREEN,CHIPLED_0805_NOOUTLINE GREEN,CHIPLED_0805_NOOUTLINE,,,'}},
       'X1': {'OOMPID': 'HEAD-JSTPH-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'X1', 'DEVICE': 'JSTPH2 JSTPH', 'PACKAGE': 'JSTPH2', 'PARTLETTER': 'X', 'VALUE': 'JSTPH', 'VALUENUMBER': '', 'PACKAGENUMBER': '2', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'X1,JSTPH,JSTPH2 JSTPH,JSTPH2,,,'}},
       'Y1': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'Y1', 'DEVICE': 'RESONATOR-SMD 8MHz', 'PACKAGE': 'RESONATOR-SMD', 'PARTLETTER': 'Y', 'VALUE': '8MHz', 'VALUENUMBER': '8', 'PACKAGENUMBER': '', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'Y1,8MHz,RESONATOR-SMD 8MHz,RESONATOR-SMD,,,'}},
       'JP3': {'OOMPID': 'HEAD-I01-X-PI12-01', 'FULL': {'DESC': '', 'PART': 'JP3', 'DEVICE': '1X12_ROUND ', 'PACKAGE': '1X12_ROUND', 'PARTLETTER': 'JP', 'VALUE': '', 'VALUENUMBER': '', 'PACKAGENUMBER': '112', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'JP3,,1X12_ROUND ,1X12_ROUND,,,'}},
       'D4': {'OOMPID': 'DIOD-S123-X-KMBR120-01', 'FULL': {'DESC': '', 'PART': 'D4', 'DEVICE': 'SOD-123 MBR120', 'PACKAGE': 'SOD-123', 'PARTLETTER': 'D', 'VALUE': 'MBR120', 'VALUENUMBER': '120', 'PACKAGENUMBER': '123', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D4,MBR120,SOD-123 MBR120,SOD-123,,,'}},
       'CHG0': {'OOMPID': 'UNMATCHED-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'CHG0', 'DEVICE': 'CHIPLED_0805_NOOUTLINE ORANGE', 'PACKAGE': 'CHIPLED_0805_NOOUTLINE', 'PARTLETTER': 'CHG', 'VALUE': 'ORANGE', 'VALUENUMBER': '', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'CHG0,ORANGE,CHIPLED_0805_NOOUTLINE ORANGE,CHIPLED_0805_NOOUTLINE,,,'}}}]
