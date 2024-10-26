"""
This program is designed to scape the reviews from a commerce website, clean the data, and store the reviews in another text file.
The URLs are pulled from a text file, and then pulled into this python program
For this project, I will be using the Google Pixel smartphone as the product I am examining.

"""

import requests
from bs4 import BeautifulSoup

# Open all of the output files using a dictionary, makes it simple to store and map to
# The Encoding 'utf-8' assists the scapper in handling special characters such as emojis to prevent errors when cleaning the website
model_files = {
    "Pixel4": open("Pixel4_Reviews.txt", "w", encoding="utf-8"),
    "Pixel5": open("Pixel5_Reviews.txt", "w", encoding="utf-8"),
    "Pixel6": open("Pixel6_Reviews.txt", "w", encoding="utf-8"),
    "Pixel7": open("Pixel7_Reviews.txt", "w", encoding="utf-8"),
    "Pixel8": open("Pixel8_Reviews.txt", "w", encoding="utf-8")
}

# Open the websites text file to read URLs or skips line if blank
with open("websites.txt", "r") as websites:
    #This for loop runs for the duration of the program going through every URL in the websites.txt file
    for url in websites:
        url = url.strip()  
        if not url:
            continue  

        # Determine which model of Google Pixel the scrapper is looking at 
        if "Pixel-4" in url:
            output_file = model_files["Pixel4"]
        elif "Pixel-5" in url:
            output_file = model_files["Pixel5"]
        elif "Pixel-6" in url:
            output_file = model_files["Pixel6"]
        elif "Pixel-7" in url:
            output_file = model_files["Pixel7"]
        elif "Pixel-8" in url:
            output_file = model_files["Pixel8"]
        else:
            print(f"Unknown model in URL: {url}")
            continue

        # Finds the URL and gives the website contents to Beautiful Soup to be cleaned
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, "lxml")

        # Finds the titles and bodys of each review
        for review in soup.find_all("div", class_="ebay-review-section"):
            title_element = review.find("h3", class_="review-item-title")
            if title_element:
                title = title_element.text.strip()
            else:
                title = "No title"

            body_element = review.find("p", class_="review-item-content rvw-wrap-spaces")
            if body_element:
                body = body_element.text.strip()
            else:
                body = "No content"

            # Write title and body to the text files
            output_file.write(f"Title: {title}\n")
            output_file.write(f"Review: {body}\n")
            output_file.write("\n" + "-"*25 + "\n\n")  

# Closes all output files after scraping
for file in model_files.values():
    file.close()
