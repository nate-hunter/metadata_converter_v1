from demo.helper_methods import create_dictionarys
import lxml.etree as etree
import csv
import os


def handle_xml(studio, xml):
    list_data = []
    studio_error = ''

    if studio.lower() == "a&e":
        ae_dict = create_dictionarys.create_ae_data_dict(xml)
        return ae_dict
        # list_data.append(ae_dict)
    elif studio.lower() == "disney":
        disney_dict = create_dictionarys.create_disney_data_dict(xml)
        return disney_dict
        # list_data.append(disney_dict)
    elif studio.lower() == "disney2":
        disney_dict = create_dictionarys.create_disney2_data_dict(xml)
        return disney_dict
        # list_data.append(disney_dict)
    elif studio.lower() == 'discovery':
        discovery_dict = create_dictionarys.create_discovery_data_dict(xml)
        return discovery_dict
        # list_data.append(discovery_dict)
    elif studio.lower() == 'viacom':
        viacom_dict = create_dictionarys.create_viacom_data_dict(xml)
        return viacom_dict
        # list_data.append(discovery_dict)
    else:
        print("- '" + studio + "' is not set up to convert XMLs to CSV at this time.")
        # break

    return list_data

def process_directory(directory, studio):
    """ TAKES A DIRECTORY OF XML METADATA AND OUTPUTS A LIST WHICH IS USED BY `write_to_csv()`."""
    
    list_data = []
    studio_error = ''

    for filename in os.scandir(directory):
        if filename.is_file() and filename.name.endswith('.xml'):
            file = os.path.join(directory, filename)
            if studio.lower() == "a&e":
                ae_dict = create_dictionarys.create_ae_data_dict(file)
                list_data.append(ae_dict)
                studio_name = studio.upper()
            elif studio.lower() == "disney":
                disney_dict = create_dictionarys.create_disney_data_dict(file)
                list_data.append(disney_dict)
                studio_name = studio.upper()
            elif studio.lower() == "disney2":
                disney_dict = create_dictionarys.create_disney2_data_dict(file)
                list_data.append(disney_dict)
                studio_name = studio.upper()
            elif studio.lower() == 'discovery':
                discovery_dict = create_dictionarys.create_discovery_data_dict(file)
                list_data.append(discovery_dict)
                studio_name = studio.upper()
            elif studio.lower() == 'viacom':
                viacom_dict = create_dictionarys.create_viacom_data_dict(file)
                list_data.append(viacom_dict)
                studio_name = studio.upper()    
            else:
                studio_error = "'" + studio + "' is not set up to convert XMLs to CSV at this time."
                break    

    return list_data