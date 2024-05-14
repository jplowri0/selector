import csv
from colorama import Fore, Style

def get_user_input(category_mappings):
    options = '\n'.join([f'Press "{key}" for {value}' for key, value in category_mappings.items()])
    ignore_next = f"{Fore.GREEN}Press 'N' for Next{Style.RESET_ALL}\n{Fore.GREEN}Press 'I' for Ignore{Style.RESET_ALL}"
    print(options)
    print()
    print(ignore_next)
    print()
    print()

    while True:
        user_input = input(f"Enter your choice: ").upper()
        if user_input in category_mappings:
            return category_mappings[user_input]
        elif user_input == 'N':
            return 'Next'
        elif user_input == 'I':
            return 'Ignore'
        else:
            print("Warning - Incorrect entry")

def classify_url(url, classifications, csv_writer, category_mappings):
    while True:
        user_input = get_user_input(category_mappings)

        if user_input == 'Next':
            break  # Move to the next URL

        if user_input == 'Ignore':
            break  # Ignore this URL

        if user_input in classifications:
            classifications[user_input] = 1

    csv_writer.writerow([url] + list(classifications.values()))

def main(output_csv_path):
    classifications = {
        'Malware': 0,
        'Reversing': 0,
        'PenTest': 0,
        'OSCP': 0,
        'WriteUps': 0,
        'Vulnerabilities': 0,
        'PoC': 0,
        'Ransomware': 0,
        'Isreal/Gaza': 0,
        'CTI': 0,
        'Pivoting': 0,
        'Darkweb / Markets': 0,
        'Tools': 0,
        'Groups': 0,
        'Threat Hunting': 0,
        'Phishing': 0,
        'Geopolitical': 0,
        'Attribution': 0,
        'Advice': 0,
        'InfoWar': 0,
        'Australia': 0,
        'Forensics': 0,
        'CTFs': 0,
        'Fraud': 0,
        'Ukraine': 0,
        'SIEM': 0,
        'Networking': 0,
        'OSINT': 0,
        'Hardware': 0,
        'Business': 0,
        'CounterOps': 0,
        'Intrustions': 0,
        'Privacy': 0,
        'LOLBINS': 0,
        'Incident Response': 0,
        'Detections': 0,
        'Artificial Intelligence': 0
    }

    category_mappings = {
        'M': 'Malware',
        'R': 'Reversing',
        'T': 'PenTest',
        'O': 'OSCP',
        'W': 'WriteUps',
        'V': 'Vulnerabilities',
        'P': 'PoC',
        'RAN': 'Ransomware',
        'IG': 'Isreal/Gaza',
        'C': 'CTI',
        'PI': 'Pivoting',
        'D': 'Darkweb / Markets',
        'H': 'Tools',
        'G': 'Groups',
        'TH': 'Threat Hunting',
        'PH': 'Phishing',
        'GEO': 'Geopolitical',
        'A': 'Attribution',
        'AD': 'Advice',
        'IN': 'InfoWar',
        'AUS': 'Australia',
        'F': 'Forensics',
        'CTF': 'CTFs',
        'FR': 'Fraud',
        'U': 'Ukraine',
        'S': 'SIEM',
        'NET': 'Networking',
        'O': 'OSINT',
        'HA': 'Hardware',
        'B': 'Business',
        'CO': 'CounterOps',
        'I': 'Intrustions',
        'PVC': 'Privacy',
        'L': 'LOLBINS',
        'IR': 'Incident Response',
        'DE': 'Detections',
        'AI':'Artificial Intelligence'
    }

    classifications_header = ['URL'] + list(classifications.keys())

    with open(output_csv_path, 'w', newline='') as output_csv_file:
        csv_writer = csv.writer(output_csv_file)
        csv_writer.writerow(classifications_header)

        while True:
            url = input("Enter URL (or 'q' to quit): ")
            if url.lower() == 'q':
                break
            classifications = {category: 0 for category in classifications}
            classify_url(url, classifications, csv_writer, category_mappings)

if __name__ == "__main__":
    main("output.csv")

