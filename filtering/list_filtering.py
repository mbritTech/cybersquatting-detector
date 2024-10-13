import requests


def get_domains_from_list(url_of_list):
    domains_list = requests.get(url_of_list)
    domains_json = domains_list.json()['list']
    
    return domains_json


def get_suspicious_domains_tweetfeed():
    domains_list = requests.get("https://api.tweetfeed.live/v1/year/domain/phishing")
    domains_json = domains_list.json()
    
    suspicious_domains_for_filtering = []
    for domain in domains_json:
        suspicious_domains_for_filtering.append(domain["value"])
    
    return suspicious_domains_for_filtering
