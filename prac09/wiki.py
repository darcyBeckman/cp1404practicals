import wikipedia

wikisearch = input("Search wiki: ")
while wikisearch != "":
    try:
        wikipage = wikipedia.page(wikisearch)
        print(wikipage.title)
        print(wikipedia.summary(wikisearch, sentences=3))
        print(wikipage.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    wikisearch = input("Search wiki: ")
