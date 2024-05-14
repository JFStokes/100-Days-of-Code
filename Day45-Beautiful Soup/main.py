from bs4 import BeautifulSoup

with open("Day45-Beautiful Soup/website.html", encoding="utf8") as file:
    # encoding="utf8" prevents UnicodeDecodeError.

    contents = file.read()

# Makes soup with the contents of the html document.
soup = BeautifulSoup(contents, "html.parser")

print("-----------------------------------")
print(soup.title) # Prints title line.
print(soup.title.name) # Prints the name of the tag on the title line.
print(soup.title.string) # Prints the string within the title tag.
print("-----------------------------------")

print(soup.prettify()) # Prints the entire html document with indents.

print(soup.a) # Prints the first anchor tag in the html document.

all_anchor_tags = soup.find_all(name="a") # Makes a list of all "a" tags.

# Loops through each tag in the list.
for anchor in all_anchor_tags:
    print("<----- ANCHOR ----->")
    print(anchor.getText()) # Prints the string inside the tags.
    print(anchor.get("href")) # Prints the link in the "href" value.

# Gets the heading tag.
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading") # The underscore in "class_" so not to class with "class" keyword.
print(section_heading)

# Select the first element with an "a" inside a "p".
company_url = soup.select_one(selector="p a") 
print(company_url)

# Selects the first element with an id of "name".
name = soup.select_one("#name")

# Selects all elements with a class of "heading".
headings = soup.select(".heading")

