from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
# Configure Selenium WebDriver
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)




def get_sydney_events():
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.eventbrite.com.au/d/australia--sydney/events/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    events = [ {
            "title": "Sydney Tech Meetup – June 2025",
            "link": "https://example.com/event1"
        },
        {
            "title": "Harbour Jazz Festival",
            "link": "https://example.com/event2"
        }
    ]
    print("DEBUG: Events fetched:", events)
    for card in soup.select("div.search-event-card-wrapper"):
        title = card.select_one("div.eds-is-hidden-accessible")
        link_tag = card.find("a", href=True)

        if title and link_tag:
            events.append({
                "title": title.get_text(strip=True),
                "link": link_tag["href"]
            })

    return events


def scrape_eventbrite():
    url = "https://www.eventbrite.com.au/d/australia--sydney/all-events/"
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.eds-event-card--consumer')))

    # Scroll to the bottom to load all events
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Extract event details
    events = driver.find_elements(By.CSS_SELECTOR, 'div.eds-event-card--consumer')
    print(f"Found {len(events)} events")

    for event in events[:5]:  # Limit to first 5 events for testing
        try:
            title = event.find_element(By.CSS_SELECTOR, 'div.eds-event-card__formatted-name--is-clamped').text
            date = event.find_element(By.CSS_SELECTOR, 'div.eds-text-bs--fixed').text
            location = event.find_element(By.CSS_SELECTOR, 'div.card-text--truncated__one').text
            print(f"Title: {title}, Date: {date}, Location: {location}")
        except Exception as e:
            print(f"Error extracting event details: {e}")

    driver.quit()

if __name__ == "__main__":
    scrape_eventbrite()
    events = scrape_events()
    print("Scraped Events:", events)

