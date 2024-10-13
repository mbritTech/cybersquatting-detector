from tldextract import extract

from collectors import spaindomains_collector, dnpedia_collector
from filtering import principal_filter, list_filtering
from utils import config


#### KEYWORDS FILTERING - DNPEDIA ####
def keyword_filtering_dnpedia():
    scraped_domains = dnpedia_collector.scraping_process("top")
    domains_to_filter = dnpedia_collector.get_domains(scraped_domains)

    for domain in domains_to_filter:
        have_match, match = principal_filter.filtering_proccess(domain, config.KEYWORDS_LIST_GENERAL)

        if have_match:
            print(f"Match del dominio |{domain}| con la keyword {match}")
        # else:
        #     print(f"El dominio |{domain}| no ha hecho match")


#### KEYWORDS FILTERING - DOMINIOS.ES ####
def keyword_filtering_spain():
    collected_domains = spaindomains_collector.get_domains_from_file(
        "https://www.dominios.es/sites/dominios/files/2024-01/Alt_es_202312.xls.csv")

    for counter, domain in enumerate(collected_domains, start=1):
        # print(f"Filtrando el dominio {counter} -> {domain}")
        have_match, match = principal_filter.filtering_proccess(domain, config.KEYWORDS_LIST_ES)
        if have_match:
            print(f"Match del dominio |{domain}| con la keyword {match}")
        # else:
        #     print(f"El dominio |{domain}| no ha hecho match")


#### LIST FILTERING #### mailfreeonline.com, magamail.com, superrito.com, 10minutemail.net, 1secmail.net
def warninglist_filtering():
    scraped_domains = dnpedia_collector.scraping_process("xyz")
    collected_domains = dnpedia_collector.get_domains(scraped_domains)
    # collected_domains = spaindomains_collector.get_spanish_domains("https://www.dominios.es/sites/dominios/files/2024-01/Alt_es_202312.xls.csv")

    domains_for_filtering = list_filtering.get_domains_from_list("https://raw.githubusercontent.com/MISP/misp"
                                                                 "-warninglists/main/lists/disposable-email/list.json")
    # domains_for_filtering = list_filtering.get_domains_from_list("https://raw.githubusercontent.com/MISP/misp"
    #                                                              "-warninglists/main/lists/alexa/list.json")

    for domain in collected_domains:
        domain_extraction = extract(domain, include_psl_private_domains=True)
        subdomain, main_domain, tld = domain_extraction.subdomain, domain_extraction.domain, domain_extraction.suffix

        have_match, match = principal_filter.filtering_proccess(main_domain, domains_for_filtering, "domain")
        if have_match:
            print(f"Match del dominio |{domain}| con la keyword {match}")
        # else:
        #     print(f"El dominio |{domain}| no ha hecho match")


#### LIST FILTERING - TWEETFEED ####
def tweetfeed_filtering():
    # scraped_domains = dnpedia_collector.scraping_process("xyz")
    # collected_domains = dnpedia_collector.get_domains(scraped_domains)
    collected_domains = spaindomains_collector.get_domains_from_file(
        "https://www.dominios.es/sites/dominios/files/2024-10/alt_es_202409.xls.csv")
    domains_for_filtering = list_filtering.get_suspicious_domains_tweetfeed()

    for domain in collected_domains:
        domain_extraction = extract(domain, include_psl_private_domains=True)
        subdomain, main_domain, tld = domain_extraction.subdomain, domain_extraction.domain, domain_extraction.suffix

        have_match, match = principal_filter.filtering_proccess(main_domain, domains_for_filtering, "domain")
        if have_match:
            print(f"Match del dominio |{domain}| con la keyword {match}")
        # else:
        #     print(f"El dominio |{domain}| no ha hecho match")


if __name__ == '__main__':
    tweetfeed_filtering()
    # warninglist_filtering()
    # keyword_filtering_spain()
    # keyword_filtering_dnpedia()
