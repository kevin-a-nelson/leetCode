

def generate_bc(url, separator):
    url = url.split("/")

    if "index" in url[-1]:
        url.pop()

    home = '<a href="/">HOME</a>'
    
    paths = []
    contents = url[1:-1]
    hrefs = []
    for content in contents:
        hrefs.append(content)
        href = "/".join(hrefs)
        text = hrefs[-1].upper()

        if "-" in text:
            text = text.split("-")
            text = list(filter(lambda str: len(str) > 2, text))
            text = list(map(lambda str: str[0], text))
            text = "".join(text)

        path = f"<a href=\"/{href}/\">{text}</a>"
        paths.append(path)

    path = separator.join(paths)
    
    text = url[-1].upper()
    for char in "?.#":
        if char in text:
            text = text[:text.find(char)]
    
    text = text.replace('-', " ")
    active = f"<span class=\"active\">{text}</span>"
    
    bread_crumbs = separator.join([home, path, active])
    return bread_crumbs

print("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi")
print(generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + "))
print('<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>')