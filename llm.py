import os
import json
from scraper import Website 
from openai import OpenAI
from config import MODEL
from IPython.display import Markdown, display

# Initialize OpenAI client
openai = OpenAI()


# System prompt for filtering relevant links
link_system_prompt = """
You are provided with a list of links found on a webpage. 
You are able to decide which of the links would be most relevant to include in a brochure about the company, 
such as links to an About page, or a Company page, or Careers/Jobs pages.
You should respond in JSON as in this example:
{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page", "url": "https://another.full.url/careers"}
    ]
}
"""


# System prompt for generating company brochure
system_prompt = """
You are an assistant that analyzes the contents of several relevant pages from a company website 
and creates a short brochure about the company for prospective customers, investors, and recruits. 
Respond in markdown. Include details of company culture, customers, and careers/jobs if you have the information.
"""







def get_links_user_prompt(website: Website) -> str:
    """
    Generates a user prompt to extract relevant links from a given website.
    
    Args:
        website (Website): The website object containing extracted links.
    
    Returns:
        str: A formatted user prompt.
    """
    user_prompt = f"Here is the list of links on the website of {website.url} - "
    user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. "
    user_prompt += "Do not include Terms of Service, Privacy, email links.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(website.links)
    return user_prompt





def get_links(url: str) -> dict:
    """
    Extracts relevant company-related links from the given URL.
    
    Args:
        url (str): The website URL to scrape.
    
    Returns:
        dict: A JSON object containing relevant links and their types.
    """
    website = Website(url)
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {'role': 'system', 'content': link_system_prompt},
            {'role': 'user', 'content': get_links_user_prompt(website)}
        ],
        response_format={'type': 'json_object'}
    )
    result = response.choices[0].message.content
    return json.loads(result)






def get_all_details(url: str) -> str:
    """
    Gathers and formats the content of the landing page and other relevant pages.
    
    Args:
        url (str): The URL of the website.
    
    Returns:
        str: A formatted string containing extracted website details.
    """
    result = "Landing page:\n"
    result += Website(url).get_content()
    links = get_links(url)
    print("Found links:", links)
    for link in links.get("links", []):
        result += f"\n\n{link['type']}\n\n"
        result += Website(link['url']).get_content()
    return result






def get_brochure_user_prompt(company_name: str, url: str) -> str:
    """
    Creates a user prompt to generate a company brochure.
    
    Args:
        company_name (str): The name of the company.
        url (str): The company website URL.
    
    Returns:
        str: A formatted user prompt.
    """
    user_prompt = f"You are looking at a company called: {company_name}\n"
    user_prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
    user_prompt += get_all_details(url)
    user_prompt = user_prompt[:5000]  # Truncate if more than 5,000 characters
    return user_prompt





def create_brochure(company_name: str, url: str):
    """
    Generates and displays a company brochure using OpenAI's model.
    
    Args:
        company_name (str): The name of the company.
        url (str): The company website URL.
    """
    if url and not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    stream = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ],
        stream=True
    )
    # result = response.choices[0].message.content
    response = ''
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        # response = response.replace('```markdown', '').replace('```', '')
        yield response



if __name__ == '__main__':
    create_brochure('CNN',  "https://www.cnn.com")

