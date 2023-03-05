from fileinput import filename
import os

pageFolder = os.getcwd() + "/pages"

def loadPage(endpoint):
    filename = endpoint + ".html"
    page = pageFolder + "/" +filename
    
    if endpoint == "/":
        indexPage = pageFolder + "/index.html"
        file = open(indexPage)
        pageContent = file.read()
        print("index")
        return pageContent
        pageContent.close()
    else:
        try:
            file = open(page)
            pageContent = file.read()
            print("found")
            return pageContent
        except FileNotFoundError:
            response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
            print("not found")
            return response
    
    