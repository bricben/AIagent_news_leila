import newspaper

SOURCES = [
    "https://www.bloomberg.com",
    "https://www.ft.com",
    "https://www.reuters.com",
    "https://www.wsj.com",
    "https://www.imf.org",
    "https://www.bis.org"
]

KEYWORDS = ["central bank", "monetary policy", "sovereign wealth fund", "IMF", "ECB", "rate", "inflation", "macroeconomic"]

def scrape_financial_news():
    articles = []
    for url in SOURCES:
        paper = newspaper.build(url, memoize_articles=False)
        for article in paper.articles[:10]:
            try:
                article.download()
                article.parse()
                if any(keyword.lower() in article.text.lower() for keyword in KEYWORDS):
                    articles.append({
                        "title": article.title,
                        "text": article.text,
                        "url": article.url
                    })
            except:
                continue
    return articles