from llm import create_brochure




company_name = input(" Enter the company Name: " ,)
company_url = input(" Enter the company Website: " )



if not company_url.startswith('https:'):
    company_url = "https://"+company_url+'\n\n'


create_brochure(company_name,company_url)