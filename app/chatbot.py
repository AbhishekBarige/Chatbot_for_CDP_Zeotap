import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Function to handle user queries
def handle_query(query):
    query = query.lower()
    
    if "segment" in query:
        return get_segment_solution(query)
    elif "mparticle" in query:
        return get_mparticle_solution(query)
    elif "lytics" in query:
        return get_lytics_solution(query)
    elif "zeotap" in query:
        return get_zeotap_solution(query)
    else:
        return "Sorry, I can't help with that. Please ask about Segment, mParticle, Lytics, or Zeotap."

# Function to scrape Segment documentation
def get_segment_solution(query):
    url = "https://segment.com/docs/?ref=nav"
    return scrape_website(url, query)

# Function to scrape mParticle documentation
def get_mparticle_solution(query):
    url = "https://docs.mparticle.com/"
    return scrape_website(url, query)

# Function to scrape Lytics documentation
def get_lytics_solution(query):
    url = "https://docs.lytics.com/"
    return scrape_website(url, query)

# Function to scrape Zeotap documentation
def get_zeotap_solution(query):
    url = "https://docs.zeotap.com/home/en-us/"
    return scrape_website(url, query)

# Generic scraping function with Selenium fallback
def scrape_website(url, query, use_selenium=False):
    if use_selenium:
        # Initialize Selenium WebDriver
        options = Options()
        options.add_argument('--headless')  # Run in headless mode
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        # Fetch the webpage
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
    else:
        # Fetch the webpage using requests
        response = requests.get(url)
        if response.status_code != 200:
            return "Sorry, I couldn't fetch information from the documentation."
        soup = BeautifulSoup(response.content, 'html.parser')

    # Extract and search relevant text content
    content = []
    for element in soup.find_all(['h1', 'h2', 'h3', 'p', 'a']):
        text = element.get_text().strip().lower()
        if query in text:
            content.append(text)

    # Check if any relevant content is found
    if content:
        return f"Here's some information from {url}:\n" + "\n".join(content[:5])
    else:
        return "Sorry, I couldn't find relevant information in the documentation."

# Example usage
if __name__ == "__main__":
    query = input("Ask a question: ")
    print(handle_query(query))
