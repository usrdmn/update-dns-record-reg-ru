import requests
import json
import os

def get_external_ip():
    """Get the external IP address of this machine"""
    api_url = 'http://httpbin.org/ip'
    response = requests.get(api_url)
    print(f"External IP address: {response.json()['origin']}")
    return response.json()["origin"]

def update_dns_record(ip):
    """Update or set A record for the specified domain at Reg.RU"""
    
    reg_ru_username = os.environ.get('REG_RU_USERNAME')
    reg_ru_password = os.environ.get('REG_RU_PASSWORD')
    domain_name = os.environ.get('DOMAIN_NAME')

    if not all([reg_ru_username, reg_ru_password, domain_name]):
        print("Error: Environment variables are missing. Please set:")
        print("- REG_RU_USERNAME")
        print("- REG_RU_PASSWORD")
        print("- DOMAIN_NAME")
        exit(1)

    api_endpoint = f'https://api.reg.ru/api/regru2/zone/add_alias'
    data = {
        'input_data': json.dumps({
            'username': reg_ru_username,
            'password': reg_ru_password,
            'domains': [
                {'dname': domain_name}
            ],
            'subdomain': '@',
            'ipaddr': ip,
            'output_content_type': 'plain'
        }),
        'input_format': 'json'
    }
    
    print(f"Payload being sent to Reg.RU:")
    print(json.dumps(data['input_data'], indent=4))
    
    response = requests.post(api_endpoint, data=data)
    print(f"Response from Reg.RU:")
    print(response.text.strip())
    
    if response.json()['result'] == 'success':
        answer = response.json().get('answer')
        domains = answer.get('domains', [])

        # Check for real errors
        for domain in domains:
            error_code = domain.get('error_code')
            error_text = domain.get('error_text')

            if error_code and error_text:
                print(f"Error updating DNS records: {error_text}")
                return False

        print("DNS record updated successfully")
        return True
    else:
        print(f"Failed to update DNS record: {response.text.strip()}")
    
    return False

def main():
    external_ip = get_external_ip()
    result = update_dns_record(external_ip)

    if not result:
        exit(1)

if __name__ == '__main__':
    import os
    main()
