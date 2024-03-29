import lxml.etree as etree
import csv 
import os


def create_ae_data_dict(xml_to_parse):
    # METADATA PROVIDED BY A&E

    # with open(xml_to_parse, 'rb') as f:
    #     open_xml = f.read()

    # print('\n\t--->XML', xml_to_parse)
    # print('\n\t-----')

    root = etree.fromstring(xml_to_parse)
    # print('\n\t--->', root)

    data_dict = {
        'Series': '',
        'Season': '',
        'Title': '',
        'EpisodeNumber': '',
        'Description': '',
        'SeasonDescription': '',
        'Actor1': '',
        'Actor2': '',
        'Rating': '',
        'Genre': '',
        'Duration': '',
        'ReleaseYear': ''
    }

    for child in root.getchildren():        
        if not child.text == 'N/A':
            if child.tag in data_dict:
                data_dict[child.tag] = child.text

    return data_dict


def create_disney_data_dict(xml_to_parse):
    # METADATA PROVIDED BY DISNEY

    # with open(xml_to_parse, 'rb') as f:
    #     open_xml = f.read()

    root = etree.fromstring(xml_to_parse)

    data_dict = {
        'series': '',
        'series_short_synopsis': '',
        'series_start_year': '',
        'season': '',
        'season_short_synopsis': '',
        'title': '',
        'episode_number': '',
        'runtime': '',
        'short_synopsis': '',
        'genre': '',
        'rating': '',
        'cast': '',
        'physical_release_date': ''
    }

    # data_dict = {
    #     'series_title': '',
    #     'season_number': '',
    #     'episode_title': '',
    #     'episode_position': '',
    #     'season_synopsis_short': '',
    #     'episode_synopsis_short': '',
    #     'production_year': '',
    #     'genre': '',
    #     'rating': '',
    #     'cast': '',
    #     'runtime': '',
    #     'release_date': ''
    # }

    for key in data_dict:
        for element in root.iter(key):
            if element.tag == 'cast':
                list_actor = []
                for actor in element.getchildren():
                    actor_name = actor.get("name")
                    list_actor.append(actor_name)

                data_dict[element.tag] = '; '.join(list_actor)
            else:
                data_dict[element.tag] = element.text

    return data_dict

def create_disney2_data_dict(xml_to_parse):
    # METADATA PROVIDED BY DISNEY

    # with open(xml_to_parse, 'rb') as f:
    #     open_xml = f.read()

    root = etree.fromstring(xml_to_parse)

    # data_dict = {
    #     'series': '',
    #     'series_short_synopsis': '',
    #     'series_start_year': '',
    #     'season': '',
    #     'season_short_synopsis': '',
    #     'title': '',
    #     'episode_number': '',
    #     'runtime': '',
    #     'short_synopsis': '',
    #     'genre': '',
    #     'rating': '',
    #     'cast': '',
    #     'physical_release_date': ''
    # }

    data_dict = {
        'series_title': '',
        'season_number': '',
        'episode_title': '',
        'episode_position': '',
        'season_synopsis_short': '',
        'episode_synopsis_short': '',
        'production_year': '',
        'genre': '',
        'rating': '',
        'cast': '',
        'runtime': '',
        'release_date': ''
    }

    for key in data_dict:
        for element in root.iter(key):
            if element.tag == 'cast':
                list_actor = []
                for actor in element.getchildren():
                    actor_name = actor.get("name")
                    list_actor.append(actor_name)

                data_dict[element.tag] = '; '.join(list_actor)
            else:
                data_dict[element.tag] = element.text
    return data_dict


def create_discovery_data_dict(xml_to_parse):
    """ METADATA PROVIDED BY DISCOVERY """

    # with open(xml_to_parse, 'rb') as f:
    #     open_xml = f.read()

    # open_xml = xml.read()

    root = etree.fromstring(xml_to_parse)

    data_dict = {
        'series_name': '',
        'season_title': '',
        'container_position': '',
        'title': '',
        'release_date': '',
        'season_description': '',
        'description': '',
        'genre': '',
        'rating': '',
        'duration': '',
        'vendor_id': '',
    }

    for key in data_dict:
        for child in root.getchildren():
            k = "{http://apple.com/itunes/importer}" + key
            for ch in child.iter(k):
                tag = ch.tag.split("}")[1]
                data_dict[tag] = ch.text

    return data_dict


def create_viacom_data_dict(xml_to_parse):
    """ METADATA PROVIDED BY VIACOM """

    root = etree.fromstring(xml_to_parse)

    data_dict_viacom = {
        'series_name': '',
        'season_number': '',
        'title': '',
        'container_position_episode': '',
        'season_description': '',
        'episode_short_description': '',
        'contributor': '',
        'rating': '',
        'genre': '',
        'runtime': '',
        'original_release_year': ''
    }

    for key in data_dict_viacom:
        for element in root.iter(key):
            if element.tag == 'contributors':
                list_actor = []
                for actor in element.getchildren():
                    actor_name = actor.get("contributor")
                    list_actor.append(actor_name)

                data_dict_viacom[element.tag] = '; '.join(list_actor)
            else:
                data_dict_viacom[element.tag] = element.text

    return data_dict_viacom
