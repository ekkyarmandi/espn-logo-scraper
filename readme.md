# ESPN Soccer Sport Logo Downloader
This repository is used as one of my data scraping project portfolio.

One of my client require me to write a script to download Soccer Team Logo from [ESPN](https://www.espn.com/soccer/teams/_/league/ENG.1/english-premier-league) as an image file.

After doing some quick scraping test on the website, it seems the image url appear on the browser but not on the `img` tag when using Python GET `requests` library.
``` html
# On the Browser
<img alt="AFC Bournemouth" class="Image Logo Logo__lg" title="AFC Bournemouth" data-mptype="image" src="https://a.espncdn.com/combiner/i?img=/i/teamlogos/soccer/500/349.png&amp;scale=crop&amp;cquality=40&amp;location=origin&amp;w=80&amp;h=80">

# On Python GET request
<img alt="AFC Bournemouth" class="Image Logo Logo__lg" data-mptype="image" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" title="AFC Bournemouth"/>
```

I realize the number 349 from the first html tag above was an id for a team. In this example, 349 was belong to AFC Bournemouth team.

Then I start develop some functions for checking the output folder existance, for making a GET request, query a soup object, and image file downloader.

Instead of trying to find the image url, I think the better solution is to find the team id.

Team id are lay on the `href` attribute on the parent tag as the `img` tag above. Then, I subtitute the 349 with the team id I gathered, download it, and manage the output on the logos folder.

The library I use for developing the script was only using `requests`, `BeautifulSoup`, and `wget`. All the dependencies can be installed using python PIP.
```
pip install -r requirements.txt
```

To test the app, you can run the app.py
```
python app.py
```

You also can change to the other ESPN target URL by changing the variable `url` inside the [app.py](/app.py).
``` python
if __name__ == "__main__":

    # Prepare the URL and make a GET request
    url = "https://www.espn.com/soccer/teams/_/league/ENG.1/english-premier-league"
    soup = get(url)

...
```

You can find me on:   
* [Twitter](https://www.twitter.com/ekkyarmandi)
* [Instagram](https://www.instagram.com/ekkyarmandi)
* [UpWork](https://www.upwork.com/fl/ekkyarmandi)