import requests
from bs4 import BeautifulSoup
import pandas as pd

#Target URL
url = "https://books.toscrape.com/"

#Send request to website
response = requests.get(url)

#Check request status if 200 then successful
print("Status Code:", response.status_code)

#Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

#Find all product cards
books = soup.find_all("article", class_="product_pod")

print("Books found:", len(books))

#Empty list to store data
book_list = []

#Loop through each book
for book in books:

    # Book title
    title = book.h3.a["title"]

    # Book price
    price = book.find("p", class_="price_color").text

    # Availability
    availability = book.find("p", class_="instock availability").text.strip()

    # Append data to list
    book_list.append({
        "product_name": title,
        "price": price,
        "availability": availability
    })

#Convert list to DataFrame
df = pd.DataFrame(book_list)

#Save data to CSV
df.to_csv("books_data.csv", index=False)

#Display output
print(df.head())
print("DataFrame shape:", df.shape)
print("books_data.csv file created successfully")


df = pd.read_csv("books_data.csv")

# Clean price column safely
df["price"] = df["price"].str.replace("[^0-9.]", "", regex=True).astype(float)

print(df.head())
print(df.dtypes)






