# import collectors.dnpedia_collector
# import utils.config as config

def filtering_proccess(domain_for_filter, keywords_list_for_check, filter_type="keyword"):

    is_match = False
    match_list = []
    
    if filter_type == "keyword":
        for keyword in keywords_list_for_check:
            if keyword in domain_for_filter:
                is_match = True
                match_list.append(keyword)

    elif filter_type == "domain":
        for keyword in keywords_list_for_check:
            if domain_for_filter in keyword: 
                is_match = True
                match_list.append(keyword)

    else:
        print("No has escogido un tipo de filtrado correcto")
    
    return is_match, match_list

