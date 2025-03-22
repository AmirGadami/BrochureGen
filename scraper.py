from typing import List
import requests
from bs4 import BeautifulSoup

class Website:
    """
    A class to represent a website and extract its title, body content, and links.

    Attributes:
        url (str): The URL of the website.
        title (str): The title of the webpage.
        body (str): The raw HTML content of the webpage.
        links (List[str]): A list of hyperlinks found on the webpage.
        text (str): The extracted readable text content from the webpage.
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }

    def __init__(self, url: str):
        """
        Initializes the Website object by fetching and parsing the webpage.
        
        Args:
            url (str): The URL of the website to fetch.
        """
        self.url = url
        response = requests.get(self.url, headers=self.__class__.headers)
        self.body = response.content
        soup = BeautifulSoup(self.body, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"

        if self.title:
            # Remove irrelevant elements from the webpage body
            for irrelevant in soup.body(['script', 'img', 'style', 'input']):
                irrelevant.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""

        # Extract all links from the webpage
        self.links = [link.get('href') for link in soup.find_all('a') if link.get('href')]

    def get_content(self) -> str:
        """
        Returns a formatted string containing the webpage title and extracted text content.
        
        Returns:
            str: The formatted title and text content of the webpage.
        """
        return f"Webpage Title:\n{self.title}\nWebpage Content:\n{self.text}\n\n"






if __name__ == "__main__":
    url_cnn =  "https://www.cnn.com"
    url_cb = "https://www.youtube.com"


    cnn = Website(url_cnn)
    print(cnn.get_content())