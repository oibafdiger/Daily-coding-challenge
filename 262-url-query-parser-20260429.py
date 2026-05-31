def parse_url_query(url):
    # 1. Nur den Teil nach dem '?' extrahieren
    query_string = url.split('?')

    # 2. Ein leeres Dictionary erstellen
    params = {}

    # 3. Die Parameter trennen und verarbeiten
    for param in query_string[1].split('&'):
        # split('=') gibt eine Liste zurück, z.B. ['name', 'Alice']
        key, value = param.split('=')
    
        # Hinzufügen zum Dictionary
        params[key] = value
    print(params)
    return params


parse_url_query("https://example.com/search?name=Alice&age=30")


'''
URL Query Parser
Given a URL that contains a query string, parse the query string into an object (or dictionary) of key-value pairs.

The query string begins after the "?",
each parameter is separated by "&",
each key/value pair is separated by "="
For example, given "https://example.com/search?name=Alice&age=30", return:

{
  "name": "Alice",
  "age": "30"
}
All values should be returned as strings.

Tests:
Passed:1. parse_url_query("https://example.com/search?name=Alice&age=30") should return {"name": "Alice", "age": "30"}
Passed:2. parse_url_query("https://freecodecamp.org/learn?skill=programming&language=python") should return {"skill": "programming", "language": "python"}
Passed:3. parse_url_query("https://freecodecamp.org/items?category=books&sort=asc&page=2") should return {"category": "books", "sort": "asc", "page": "2"}
Passed:4. parse_url_query("https://example.com?redirect=freecodecamp.org/learn&when=now") should return {"redirect": "freecodecamp.org/learn", "when": "now"}
'''
