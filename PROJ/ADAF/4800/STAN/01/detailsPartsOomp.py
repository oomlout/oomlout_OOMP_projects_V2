def load(newPart,it):
    it['PROJ-ADAF-4800-STAN-01']['oompParts'] = [{'IC2': {'OOMPID': 'UNMATCHED-SO23-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'IC2', 'DEVICE': 'SOT23-6 PAM8301', 'PACKAGE': 'SOT23-6', 'PARTLETTER': 'IC', 'VALUE': 'PAM8301', 'VALUENUMBER': '8301', 'PACKAGENUMBER': '236', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'IC2,PAM8301,SOT23-6 PAM8301,SOT23-6,,,'}},
       'U2': {'OOMPID': 'UNMATCHED-SO235-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'U2', 'DEVICE': 'SOT23-5 MCP73831T-2ACI/OT', 'PACKAGE': 'SOT23-5', 'PARTLETTER': 'U', 'VALUE': 'MCP73831T-2ACI/OT', 'VALUENUMBER': '73831-2/', 'PACKAGENUMBER': '235', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'U2,MCP73831T-2ACI/OT,SOT23-5 MCP73831T-2ACI/OT,SOT23-5,,,'}},
       'U3': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'U3', 'DEVICE': 'MODULE_ESP32-S2-WROVER ESP32-S2-WROVER', 'PACKAGE': 'MODULE_ESP32-S2-WROVER', 'PARTLETTER': 'U', 'VALUE': 'ESP32-S2-WROVER', 'VALUENUMBER': '32-2-', 'PACKAGENUMBER': '322', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'U3,ESP32-S2-WROVER,MODULE_ESP32-S2-WROVER ESP32-S2-WROVER,MODULE_ESP32-S2-WROVER,,,'}},
       'R4': {'OOMPID': 'RESE-0603-X-O472-01', 'FULL': {'DESC': '', 'PART': 'R4', 'DEVICE': '0603-NO 5.1k', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '5.1k', 'VALUENUMBER': '5.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R4,5.1k,0603-NO 5.1k,0603-NO,,,'}},
       'Q5': {'OOMPID': 'UNMATCHED-SO23-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'Q5', 'DEVICE': 'SOT23-3 IRLML0100', 'PACKAGE': 'SOT23-3', 'PARTLETTER': 'Q', 'VALUE': 'IRLML0100', 'VALUENUMBER': '0100', 'PACKAGENUMBER': '233', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'Q5,IRLML0100,SOT23-3 IRLML0100,SOT23-3,,,'}},
       'C5': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C5', 'DEVICE': '0603-NO 0.1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '0.1uF', 'VALUENUMBER': '0.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C5,0.1uF,0603-NO 0.1uF,0603-NO,,,'}},
       'C16': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C16', 'DEVICE': '0603-NO 0.1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '0.1uF', 'VALUENUMBER': '0.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C16,0.1uF,0603-NO 0.1uF,0603-NO,,,'}},
       'C2': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C2', 'DEVICE': '0603-NO 0.1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '0.1uF', 'VALUENUMBER': '0.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C2,0.1uF,0603-NO 0.1uF,0603-NO,,,'}},
       'C15': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C15', 'DEVICE': '0603-NO 0.1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '0.1uF', 'VALUENUMBER': '0.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C15,0.1uF,0603-NO 0.1uF,0603-NO,,,'}},
       'C21': {'OOMPID': 'CAPC-0603-X-NF100-V50', 'FULL': {'DESC': '', 'PART': 'C21', 'DEVICE': '0603-NO 0.1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '0.1uF', 'VALUENUMBER': '0.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C21,0.1uF,0603-NO 0.1uF,0603-NO,,,'}},
       'CHG1': {'OOMPID': 'UNMATCHED-0603-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'CHG1', 'DEVICE': 'CHIPLED_0603_NOOUTLINE ORANGE', 'PACKAGE': 'CHIPLED_0603_NOOUTLINE', 'PARTLETTER': 'CHG', 'VALUE': 'ORANGE', 'VALUENUMBER': '', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'CHG1,ORANGE,CHIPLED_0603_NOOUTLINE ORANGE,CHIPLED_0603_NOOUTLINE,,,'}},
       'SENSE0': {'OOMPID': 'HEAD-JSTPH-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'SENSE0', 'DEVICE': 'JSTPH3 JST PH 3', 'PACKAGE': 'JSTPH3', 'PARTLETTER': 'SENSE', 'VALUE': 'JST PH 3', 'VALUENUMBER': '  3', 'PACKAGENUMBER': '3', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SENSE0,JST PH 3,JSTPH3 JST PH 3,JSTPH3,,,'}},
       'SENSE1': {'OOMPID': 'HEAD-JSTPH-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'SENSE1', 'DEVICE': 'JSTPH3 JST PH 3', 'PACKAGE': 'JSTPH3', 'PARTLETTER': 'SENSE', 'VALUE': 'JST PH 3', 'VALUENUMBER': '  3', 'PACKAGENUMBER': '3', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SENSE1,JST PH 3,JSTPH3 JST PH 3,JSTPH3,,,'}},
       'C13': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C13', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C13,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'C17': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C17', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C17,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'C18': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C18', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C18,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'C11': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C11', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C11,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'C8': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C8', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C8,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'C3': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C3', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C3,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'C4': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C4', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C4,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'C7': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C7', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C7,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'C10': {'OOMPID': 'CAPC-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'C10', 'DEVICE': '0805-NO 10ÂµF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10ÂUF', 'VALUENUMBER': '10Âµ', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C10,10ÂµF,0805-NO 10ÂµF,0805-NO,,,'}},
       'C30': {'OOMPID': 'CAPC-0805-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C30', 'DEVICE': '0805-NO 1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C30,1uF,0805-NO 1uF,0805-NO,,,'}},
       'C23': {'OOMPID': 'CAPC-0805-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C23', 'DEVICE': '0805-NO 1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C23,1uF,0805-NO 1uF,0805-NO,,,'}},
       'C26': {'OOMPID': 'CAPC-0805-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C26', 'DEVICE': '0805-NO 1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C26,1uF,0805-NO 1uF,0805-NO,,,'}},
       'C31': {'OOMPID': 'CAPC-0805-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C31', 'DEVICE': '0805-NO 1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C31,1uF,0805-NO 1uF,0805-NO,,,'}},
       'C25': {'OOMPID': 'CAPC-0805-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C25', 'DEVICE': '0805-NO 1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C25,1uF,0805-NO 1uF,0805-NO,,,'}},
       'C24': {'OOMPID': 'CAPC-0805-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C24', 'DEVICE': '0805-NO 1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C24,1uF,0805-NO 1uF,0805-NO,,,'}},
       'C27': {'OOMPID': 'CAPC-0805-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C27', 'DEVICE': '0805-NO 1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C27,1uF,0805-NO 1uF,0805-NO,,,'}},
       'C19': {'OOMPID': 'CAPC-0805-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C19', 'DEVICE': '0805-NO 1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C19,1uF,0805-NO 1uF,0805-NO,,,'}},
       'C28': {'OOMPID': 'CAPC-0805-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C28', 'DEVICE': '0805-NO 1uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C28,1uF,0805-NO 1uF,0805-NO,,,'}},
       'R5': {'OOMPID': 'RESE-0603-X-O103-01', 'FULL': {'DESC': '', 'PART': 'R5', 'DEVICE': '0603-NO 10K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '10K', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R5,10K,0603-NO 10K,0603-NO,,,'}},
       'R20': {'OOMPID': 'RESE-0603-X-O103-01', 'FULL': {'DESC': '', 'PART': 'R20', 'DEVICE': '0603-NO 10K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '10K', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R20,10K,0603-NO 10K,0603-NO,,,'}},
       'R1': {'OOMPID': 'RESE-0603-X-O103-01', 'FULL': {'DESC': '', 'PART': 'R1', 'DEVICE': '0603-NO 10K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '10K', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R1,10K,0603-NO 10K,0603-NO,,,'}},
       'R9': {'OOMPID': 'RESE-0603-X-O103-01', 'FULL': {'DESC': '', 'PART': 'R9', 'DEVICE': '0603-NO 10K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '10K', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R9,10K,0603-NO 10K,0603-NO,,,'}},
       'R2': {'OOMPID': 'RESE-0603-X-O103-01', 'FULL': {'DESC': '', 'PART': 'R2', 'DEVICE': '0603-NO 10K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '10K', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R2,10K,0603-NO 10K,0603-NO,,,'}},
       'R7': {'OOMPID': 'RESE-0603-X-O103-01', 'FULL': {'DESC': '', 'PART': 'R7', 'DEVICE': '0603-NO 10K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '10K', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R7,10K,0603-NO 10K,0603-NO,,,'}},
       'IC4': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'IC4', 'DEVICE': 'LGA16_3X3MM LIS3DH', 'PACKAGE': 'LGA16_3X3MM', 'PARTLETTER': 'IC', 'VALUE': 'LIS3DH', 'VALUENUMBER': '3', 'PACKAGENUMBER': '1633', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'IC4,LIS3DH,LGA16_3X3MM LIS3DH,LGA16_3X3MM,,,'}},
       'X4': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'X4', 'DEVICE': 'USB_C_CUSB31-CFM2AX-01-X USB C', 'PACKAGE': 'USB_C_CUSB31-CFM2AX-01-X', 'PARTLETTER': 'X', 'VALUE': 'USB C', 'VALUENUMBER': ' ', 'PACKAGENUMBER': '31201', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'X4,USB C,USB_C_CUSB31-CFM2AX-01-X USB C,USB_C_CUSB31-CFM2AX-01-X,,,'}},
       'R18': {'OOMPID': 'RESE-0603-X-O102-01', 'FULL': {'DESC': '', 'PART': 'R18', 'DEVICE': '0603-NO 1K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '1K', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R18,1K,0603-NO 1K,0603-NO,,,'}},
       'R16': {'OOMPID': 'RESE-0603-X-O102-01', 'FULL': {'DESC': '', 'PART': 'R16', 'DEVICE': '0603-NO 1K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '1K', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R16,1K,0603-NO 1K,0603-NO,,,'}},
       'D2': {'OOMPID': 'DIOD-S123-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'D2', 'DEVICE': 'SOD-123 MBR0530', 'PACKAGE': 'SOD-123', 'PARTLETTER': 'D', 'VALUE': 'MBR0530', 'VALUENUMBER': '0530', 'PACKAGENUMBER': '123', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D2,MBR0530,SOD-123 MBR0530,SOD-123,,,'}},
       'D5': {'OOMPID': 'DIOD-S123-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'D5', 'DEVICE': 'SOD-123 MBR0530', 'PACKAGE': 'SOD-123', 'PARTLETTER': 'D', 'VALUE': 'MBR0530', 'VALUENUMBER': '0530', 'PACKAGENUMBER': '123', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D5,MBR0530,SOD-123 MBR0530,SOD-123,,,'}},
       'D3': {'OOMPID': 'DIOD-S123-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'D3', 'DEVICE': 'SOD-123 MBR0530', 'PACKAGE': 'SOD-123', 'PARTLETTER': 'D', 'VALUE': 'MBR0530', 'VALUENUMBER': '0530', 'PACKAGENUMBER': '123', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D3,MBR0530,SOD-123 MBR0530,SOD-123,,,'}},
       'SP1': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'SP1', 'DEVICE': 'BUZZER_SMT_7.5MM 7.5mm SPK', 'PACKAGE': 'BUZZER_SMT_7.5MM', 'PARTLETTER': 'SP', 'VALUE': '7.5mm SPK', 'VALUENUMBER': '7.5 ', 'PACKAGENUMBER': '75', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SP1,7.5mm SPK,BUZZER_SMT_7.5MM 7.5mm SPK,BUZZER_SMT_7.5MM,,,'}},
       'JP2': {'OOMPID': 'HEAD-I01-X-PI02-01', 'FULL': {'DESC': '', 'PART': 'JP2', 'DEVICE': '1X02_ROUND UART', 'PACKAGE': '1X02_ROUND', 'PARTLETTER': 'JP', 'VALUE': 'UART', 'VALUENUMBER': '', 'PACKAGENUMBER': '102', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'JP2,UART,1X02_ROUND UART,1X02_ROUND,,,'}},
       'D1': {'OOMPID': 'DIOD-S323-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'D1', 'DEVICE': 'SOD-323 3.6V', 'PACKAGE': 'SOD-323', 'PARTLETTER': 'D', 'VALUE': '3.6V', 'VALUENUMBER': '3.6', 'PACKAGENUMBER': '323', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D1,3.6V,SOD-323 3.6V,SOD-323,,,'}},
       'D6': {'OOMPID': 'DIOD-S323-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'D6', 'DEVICE': 'SOD-323 3.6V', 'PACKAGE': 'SOD-323', 'PARTLETTER': 'D', 'VALUE': '3.6V', 'VALUENUMBER': '3.6', 'PACKAGENUMBER': '323', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D6,3.6V,SOD-323 3.6V,SOD-323,,,'}},
       'R19': {'OOMPID': 'RESE-0603-X-O473-01', 'FULL': {'DESC': '', 'PART': 'R19', 'DEVICE': '0603-NO 47K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '47K', 'VALUENUMBER': '47', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R19,47K,0603-NO 47K,0603-NO,,,'}},
       'R6': {'OOMPID': 'RESE-0603-X-O473-01', 'FULL': {'DESC': '', 'PART': 'R6', 'DEVICE': '0603-NO 47K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '47K', 'VALUENUMBER': '47', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R6,47K,0603-NO 47K,0603-NO,,,'}},
       'Q3': {'OOMPID': 'UNMATCHED-SO23-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'Q3', 'DEVICE': 'SOT23-R DMG3415U-7', 'PACKAGE': 'SOT23-R', 'PARTLETTER': 'Q', 'VALUE': 'DMG3415U-7', 'VALUENUMBER': '3415-7', 'PACKAGENUMBER': '23', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'Q3,DMG3415U-7,SOT23-R DMG3415U-7,SOT23-R,,,'}},
       'Q1': {'OOMPID': 'UNMATCHED-SO23-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'Q1', 'DEVICE': 'SOT23-R DMG3415U-7', 'PACKAGE': 'SOT23-R', 'PARTLETTER': 'Q', 'VALUE': 'DMG3415U-7', 'VALUENUMBER': '3415-7', 'PACKAGENUMBER': '23', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'Q1,DMG3415U-7,SOT23-R DMG3415U-7,SOT23-R,,,'}},
       'R13': {'OOMPID': 'RESE-0805-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'R13', 'DEVICE': '0805_10MGAP 0.47ohm', 'PACKAGE': '0805_10MGAP', 'PARTLETTER': 'R', 'VALUE': '0.47ohm', 'VALUENUMBER': '0.47', 'PACKAGENUMBER': '080510', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R13,0.47ohm,0805_10MGAP 0.47ohm,0805_10MGAP,,,'}},
       'C6': {'OOMPID': 'CAPC-0603-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C6', 'DEVICE': '0603-NO 1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C6,1uF,0603-NO 1uF,0603-NO,,,'}},
       'C14': {'OOMPID': 'CAPC-0603-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C14', 'DEVICE': '0603-NO 1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C14,1uF,0603-NO 1uF,0603-NO,,,'}},
       'C12': {'OOMPID': 'CAPC-0603-X-UF1-V25', 'FULL': {'DESC': '', 'PART': 'C12', 'DEVICE': '0603-NO 1uF', 'PACKAGE': '0603-NO', 'PARTLETTER': 'C', 'VALUE': '1uF', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C12,1uF,0603-NO 1uF,0603-NO,,,'}},
       'C9': {'OOMPID': 'CAPC-0805-X-UF10-V25', 'FULL': {'DESC': '', 'PART': 'C9', 'DEVICE': '0805-NO 10uF/10V+', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10uF/10V+', 'VALUENUMBER': '10/10+', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C9,10uF/10V+,0805-NO 10uF/10V+,0805-NO,,,'}},
       'SW4': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'SW4', 'DEVICE': 'SPDT_SMT_SSSS811101 SPDT R/A', 'PACKAGE': 'SPDT_SMT_SSSS811101', 'PARTLETTER': 'SW', 'VALUE': 'SPDT R/A', 'VALUENUMBER': ' /', 'PACKAGENUMBER': '811101', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SW4,SPDT R/A,SPDT_SMT_SSSS811101 SPDT R/A,SPDT_SMT_SSSS811101,,,'}},
       'R8': {'OOMPID': 'RESE-0603-X-O472-01', 'FULL': {'DESC': '', 'PART': 'R8', 'DEVICE': '0603-NO 5.1K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '5.1K', 'VALUENUMBER': '5.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R8,5.1K,0603-NO 5.1K,0603-NO,,,'}},
       'R3': {'OOMPID': 'RESE-0603-X-O472-01', 'FULL': {'DESC': '', 'PART': 'R3', 'DEVICE': '0603-NO 5.1K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '5.1K', 'VALUENUMBER': '5.1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R3,5.1K,0603-NO 5.1K,0603-NO,,,'}},
       'R10': {'OOMPID': 'RESE-0603-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'R10', 'DEVICE': '0603-NO 1Meg', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '1Meg', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R10,1Meg,0603-NO 1Meg,0603-NO,,,'}},
       'R11': {'OOMPID': 'RESE-0603-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'R11', 'DEVICE': '0603-NO 1Meg', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '1Meg', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R11,1Meg,0603-NO 1Meg,0603-NO,,,'}},
       'R17': {'OOMPID': 'RESE-0603-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'R17', 'DEVICE': '0603-NO 1Meg', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '1Meg', 'VALUENUMBER': '1', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R17,1Meg,0603-NO 1Meg,0603-NO,,,'}},
       'C1': {'OOMPID': 'CAPC-0805-X-UF10-V25', 'FULL': {'DESC': '', 'PART': 'C1', 'DEVICE': '0805-NO 10uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10uF', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C1,10uF,0805-NO 10uF,0805-NO,,,'}},
       'C20': {'OOMPID': 'CAPC-0805-X-UF10-V25', 'FULL': {'DESC': '', 'PART': 'C20', 'DEVICE': '0805-NO 10uF', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '10uF', 'VALUENUMBER': '10', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C20,10uF,0805-NO 10uF,0805-NO,,,'}},
       'U4': {'OOMPID': 'VREG-SO235-X-KAP2112K-V33D', 'FULL': {'DESC': '', 'PART': 'U4', 'DEVICE': 'SOT23-5 AP2112K-3.3', 'PACKAGE': 'SOT23-5', 'PARTLETTER': 'U', 'VALUE': 'AP2112K-3.3', 'VALUENUMBER': '2112-3.3', 'PACKAGENUMBER': '235', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'U4,AP2112K-3.3,SOT23-5 AP2112K-3.3,SOT23-5,,,'}},
       'R27': {'OOMPID': 'RESE-0603-X-O1003-01', 'FULL': {'DESC': '', 'PART': 'R27', 'DEVICE': '0603-NO 100K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '100K', 'VALUENUMBER': '100', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R27,100K,0603-NO 100K,0603-NO,,,'}},
       'R15': {'OOMPID': 'RESE-0603-X-O1003-01', 'FULL': {'DESC': '', 'PART': 'R15', 'DEVICE': '0603-NO 100K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '100K', 'VALUENUMBER': '100', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R15,100K,0603-NO 100K,0603-NO,,,'}},
       'R26': {'OOMPID': 'RESE-0603-X-O1003-01', 'FULL': {'DESC': '', 'PART': 'R26', 'DEVICE': '0603-NO 100K', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '100K', 'VALUENUMBER': '100', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R26,100K,0603-NO 100K,0603-NO,,,'}},
       'ON0': {'OOMPID': 'UNMATCHED-0603-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'ON0', 'DEVICE': 'CHIPLED_0603_NOOUTLINE GREEN', 'PACKAGE': 'CHIPLED_0603_NOOUTLINE', 'PARTLETTER': 'ON', 'VALUE': 'GREEN', 'VALUENUMBER': '', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'ON0,GREEN,CHIPLED_0603_NOOUTLINE GREEN,CHIPLED_0603_NOOUTLINE,,,'}},
       'SW1': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'SW1', 'DEVICE': 'SPST_TACTILE_RA RA_TACT', 'PACKAGE': 'SPST_TACTILE_RA', 'PARTLETTER': 'SW', 'VALUE': 'RA_TACT', 'VALUENUMBER': '_', 'PACKAGENUMBER': '', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SW1,RA_TACT,SPST_TACTILE_RA RA_TACT,SPST_TACTILE_RA,,,'}},
       'SW3': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'SW3', 'DEVICE': 'SPST_TACTILE_RA RA_TACT', 'PACKAGE': 'SPST_TACTILE_RA', 'PARTLETTER': 'SW', 'VALUE': 'RA_TACT', 'VALUENUMBER': '_', 'PACKAGENUMBER': '', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SW3,RA_TACT,SPST_TACTILE_RA RA_TACT,SPST_TACTILE_RA,,,'}},
       'D4': {'OOMPID': 'DIOD-S123-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'D4', 'DEVICE': 'SOD-123 MBR540', 'PACKAGE': 'SOD-123', 'PARTLETTER': 'D', 'VALUE': 'MBR540', 'VALUENUMBER': '540', 'PACKAGENUMBER': '123', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'D4,MBR540,SOD-123 MBR540,SOD-123,,,'}},
       'L0': {'OOMPID': 'UNMATCHED-0603-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'L0', 'DEVICE': 'CHIPLED_0603_NOOUTLINE RED', 'PACKAGE': 'CHIPLED_0603_NOOUTLINE', 'PARTLETTER': 'L', 'VALUE': 'RED', 'VALUENUMBER': '', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'L0,RED,CHIPLED_0603_NOOUTLINE RED,CHIPLED_0603_NOOUTLINE,,,'}},
       'R14': {'OOMPID': 'RESE-0603-X-O1003-01', 'FULL': {'DESC': '', 'PART': 'R14', 'DEVICE': '0603-NO 100k', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '100k', 'VALUENUMBER': '100', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R14,100k,0603-NO 100k,0603-NO,,,'}},
       'R12': {'OOMPID': 'RESE-0603-X-O1003-01', 'FULL': {'DESC': '', 'PART': 'R12', 'DEVICE': '0603-NO 100k', 'PACKAGE': '0603-NO', 'PARTLETTER': 'R', 'VALUE': '100k', 'VALUENUMBER': '100', 'PACKAGENUMBER': '0603', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'R12,100k,0603-NO 100k,0603-NO,,,'}},
       'CONN1': {'OOMPID': 'HEAD-JSTSH-X-PI04-RS', 'FULL': {'DESC': '', 'PART': 'CONN1', 'DEVICE': 'JST_SH4 STEMMA_I2C_QT', 'PACKAGE': 'JST_SH4', 'PARTLETTER': 'CONN', 'VALUE': 'STEMMA_I2C_QT', 'VALUENUMBER': '_2_', 'PACKAGENUMBER': '4', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'CONN1,STEMMA_I2C_QT,JST_SH4 STEMMA_I2C_QT,JST_SH4,,,'}},
       'L1': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'L1', 'DEVICE': 'INDUCTOR_4X4MM_NR401 10uH', 'PACKAGE': 'INDUCTOR_4X4MM_NR401', 'PARTLETTER': 'L', 'VALUE': '10uH', 'VALUENUMBER': '10', 'PACKAGENUMBER': '44401', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'L1,10uH,INDUCTOR_4X4MM_NR401 10uH,INDUCTOR_4X4MM_NR401,,,'}},
       'X1': {'OOMPID': 'HEAD-JSTPH-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'X1', 'DEVICE': 'JSTPH2_BATT JSTPH', 'PACKAGE': 'JSTPH2_BATT', 'PARTLETTER': 'X', 'VALUE': 'JSTPH', 'VALUENUMBER': '', 'PACKAGENUMBER': '2', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'X1,JSTPH,JSTPH2_BATT JSTPH,JSTPH2_BATT,,,'}},
       'Q2': {'OOMPID': 'UNMATCHED-SO23-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'Q2', 'DEVICE': 'SOT23-R DMG3415', 'PACKAGE': 'SOT23-R', 'PARTLETTER': 'Q', 'VALUE': 'DMG3415', 'VALUENUMBER': '3415', 'PACKAGENUMBER': '23', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'Q2,DMG3415,SOT23-R DMG3415,SOT23-R,,,'}},
       'C29': {'OOMPID': 'CAPC-0805-X-UNMATCHED-V25', 'FULL': {'DESC': '', 'PART': 'C29', 'DEVICE': '0805-NO 4.7uF/25V', 'PACKAGE': '0805-NO', 'PARTLETTER': 'C', 'VALUE': '4.7uF/25V', 'VALUENUMBER': '4.7/25', 'PACKAGENUMBER': '0805', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'C29,4.7uF/25V,0805-NO 4.7uF/25V,0805-NO,,,'}},
       'LED4': {'OOMPID': 'LEDS-4020-RGB-K2812-01', 'FULL': {'DESC': '', 'PART': 'LED4', 'DEVICE': 'WS2812B_4020 WS2812B_4020', 'PACKAGE': 'WS2812B_4020', 'PARTLETTER': 'LED', 'VALUE': 'WS2812B_4020', 'VALUENUMBER': '2812_4020', 'PACKAGENUMBER': '28124020', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'LED4,WS2812B_4020,WS2812B_4020 WS2812B_4020,WS2812B_4020,,,'}},
       'LED5': {'OOMPID': 'LEDS-4020-RGB-K2812-01', 'FULL': {'DESC': '', 'PART': 'LED5', 'DEVICE': 'WS2812B_4020 WS2812B_4020', 'PACKAGE': 'WS2812B_4020', 'PARTLETTER': 'LED', 'VALUE': 'WS2812B_4020', 'VALUENUMBER': '2812_4020', 'PACKAGENUMBER': '28124020', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'LED5,WS2812B_4020,WS2812B_4020 WS2812B_4020,WS2812B_4020,,,'}},
       'LED3': {'OOMPID': 'LEDS-4020-RGB-K2812-01', 'FULL': {'DESC': '', 'PART': 'LED3', 'DEVICE': 'WS2812B_4020 WS2812B_4020', 'PACKAGE': 'WS2812B_4020', 'PARTLETTER': 'LED', 'VALUE': 'WS2812B_4020', 'VALUENUMBER': '2812_4020', 'PACKAGENUMBER': '28124020', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'LED3,WS2812B_4020,WS2812B_4020 WS2812B_4020,WS2812B_4020,,,'}},
       'LED2': {'OOMPID': 'LEDS-4020-RGB-K2812-01', 'FULL': {'DESC': '', 'PART': 'LED2', 'DEVICE': 'WS2812B_4020 WS2812B_4020', 'PACKAGE': 'WS2812B_4020', 'PARTLETTER': 'LED', 'VALUE': 'WS2812B_4020', 'VALUENUMBER': '2812_4020', 'PACKAGENUMBER': '28124020', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'LED2,WS2812B_4020,WS2812B_4020 WS2812B_4020,WS2812B_4020,,,'}},
       'EINK2': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'EINK2', 'DEVICE': 'EINK_290IN EINK_24PIN_290IN', 'PACKAGE': 'EINK_290IN', 'PARTLETTER': 'EINK', 'VALUE': 'EINK_24PIN_290IN', 'VALUENUMBER': '_24_290', 'PACKAGENUMBER': '290', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'EINK2,EINK_24PIN_290IN,EINK_290IN EINK_24PIN_290IN,EINK_290IN,,,'}},
       'SW2': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'SW2', 'DEVICE': 'TACTILE_3X6MM ', 'PACKAGE': 'TACTILE_3X6MM', 'PARTLETTER': 'SW', 'VALUE': '', 'VALUENUMBER': '', 'PACKAGENUMBER': '36', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SW2,,TACTILE_3X6MM ,TACTILE_3X6MM,,,'}},
       'SW7': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'SW7', 'DEVICE': 'TACTILE_3X6MM ', 'PACKAGE': 'TACTILE_3X6MM', 'PARTLETTER': 'SW', 'VALUE': '', 'VALUENUMBER': '', 'PACKAGENUMBER': '36', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SW7,,TACTILE_3X6MM ,TACTILE_3X6MM,,,'}},
       'SW6': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'SW6', 'DEVICE': 'TACTILE_3X6MM ', 'PACKAGE': 'TACTILE_3X6MM', 'PARTLETTER': 'SW', 'VALUE': '', 'VALUENUMBER': '', 'PACKAGENUMBER': '36', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SW6,,TACTILE_3X6MM ,TACTILE_3X6MM,,,'}},
       'SW5': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'SW5', 'DEVICE': 'TACTILE_3X6MM ', 'PACKAGE': 'TACTILE_3X6MM', 'PARTLETTER': 'SW', 'VALUE': '', 'VALUENUMBER': '', 'PACKAGENUMBER': '36', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'SW5,,TACTILE_3X6MM ,TACTILE_3X6MM,,,'}},
       'U1': {'OOMPID': 'UNMATCHED-UNMATCHED-X-UNMATCHED-01', 'FULL': {'DESC': '', 'PART': 'U1', 'DEVICE': 'ALS-PT19-315C ', 'PACKAGE': 'ALS-PT19-315C', 'PARTLETTER': 'U', 'VALUE': '', 'VALUENUMBER': '', 'PACKAGENUMBER': '19315', 'BOM': '', 'OWNER': 'ADAF', 'FULL': 'U1,,ALS-PT19-315C ,ALS-PT19-315C,,,'}}}]
