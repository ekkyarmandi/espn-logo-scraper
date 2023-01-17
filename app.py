import requests
from bs4 import BeautifulSoup
from wget import download
import urllib
import os


def check_logos_folder(path):
    "Check if logos folder exists, if not create it"

    path = f"logos/{path}"
    if not os.path.exists(path):
        os.makedirs(path)


def get(url):
    "Make a GET request to the URL and return soup object"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def split_id(url):
    "Split the ID from the URL"

    splits = url.split("/")
    return splits[-1], splits[-2]


def espn_img_downloader(url, path):
    "Download the image from the URL and save it to logos folder"

    team_name, team_id = split_id(url)
    src = f"https://a.espncdn.com/combiner/i?img=/i/teamlogos/soccer/500/{team_id}.png"
    filename = os.path.join("logos", path, f"{team_name}.png")
    if not os.path.exists(filename):
        try:
            download(src, filename, bar=None)
            print(f"Downloaded {team_name} logo")
        except urllib.error.HTTPError:
            print(f"Error downloading {team_name} logo")


if __name__ == "__main__":

    # Prepare the URL and make a GET request
    url = "https://www.espn.com/soccer/teams/_/league/ENG.1/english-premier-league"
    soup = get(url)

    # Check if logos folder exists, if not create it
    path = url.split("/")[-1].replace("-", " ").title()
    check_logos_folder(path)

    # Find all the teams and download their logos
    teams = soup.select(".Wrapper a.AnchorLink > h2")
    for team in teams:
        a = team.findParent("a")
        href = a.get("href")
        espn_img_downloader(href, path)
