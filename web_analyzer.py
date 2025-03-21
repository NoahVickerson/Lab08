import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import matplotlib.pyplot as plt
url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")


# 3. Data Analysis
print(soup.prettify())

numHeadings = sum(len(soup.find_all(tag)) for tag in ["h1", "h2", "h3", "h4", "h5", "h6"])

numLinks = len(soup.find_all("a"))

numPara = len(soup.find_all("p"))

print(f"Number of headings: {numHeadings}")
print(f"Number of links: {numLinks}")
print(f"Number of paragraphs: {numPara}")

# 4. Keywords Analysis
keyword = input("Enter keyword to be searched for: ").lower()

text = soup.get_text().lower()

count = text.count(" " + keyword + " ")

print(f"Keyword: {keyword}")
print(f"Occurrences in page: {count}")

# 5. Word Frequency Analysis

words = text.split(" ")

word_counts = {word: text.count(" " + word + " ") for word in words}

print("The Top 5 Most Used Words are:")
for i in range(5):
    word = max(word_counts, key=word_counts.get)
    count = word_counts[word]
    del word_counts[word]
    print(f"{word}: {count} times")

exit(1)
# 6. Finding the Longest Paragraph

para = soup.find_all("p")

long_para = ""
max_word_count = 0

for p in para:
    para_text = p.get_text().strip()
    para_words = para_text.split()


    if len(para_words) >= 5 and len(para_words) > max_word_count:
        long_para = para_text
        max_word_count = len(para_words)

if long_para:
    print("The Longest Paragraph: \n")
    print(long_para)
    print("\nWord Count:", max_word_count)

labels = ['Headings', 'Links', 'Paragraphs']
values = [numHeadings, numLinks, numPara]
plt.bar(labels, values)
plt.title('30172306')
plt.ylabel('Count')
plt.show()
