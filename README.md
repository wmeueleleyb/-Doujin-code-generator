# -Anime-sauce-finder
How this program works is simple. A random six digit number is generated and attached to the end of a link,
the program uses the request module to check the http status of the link and see whether there's an error or not,
if there isn't an error the tags of the doujinshi are scraped using beautifulsoup and displayed to the user and asks
whether to open the website in your browser or generate another one, the program then opens the website in the desired
web browser in private browsing mode.
