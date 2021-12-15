#list of languages: c, cshell, objectivec, cplusplus, csharp, java, go, swift, php, typescript
import requests, os
from dotenv import load_dotenv

load_dotenv()

def getCode(language):
    # link for github search by language is as follows https://github.com/search?q=extension%3A${language_extension}&type=Code
    #TODO: 
    # get into results
    # get raw file
    # save code as txt (perhaps add a cutoff point)
    # archive url as to not use the same thing twice
    # maybe even archive the creator for bigger variety
    # check against url and creator? to make sure same thing isnt added twice
    #programming language:{language} -> searches for all files with extension


    url = "https://api.github.com/search/code?q=repo:Ventoy+language:{language}"

    headers = {
        'Authorization': '{ACCESS_TOKEN}'
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

getCode("c")