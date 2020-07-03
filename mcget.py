import sys
import requests

mcLauncherUrl = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

json = requests.get(mcLauncherUrl).json()

# version is specified as a string ("1.16", "1.4.2", etc)
# channel is also a string ("release", "snapshot", "old_alpha")
#
#

# used to refresh metadata dictionary if process is long running
def refresh_meta():
    json = requests.get(mcLauncherUrl).json()

# returns latest version as a string
def get_latest_version():
    return json["latest"]["release"]

# returns a string of the url to the metadata for a specific version
def get_meta_url(ver):
    cringe_url = ""
    for i in range(len(json["versions"])):
        if json["versions"][i]["id"] == ver:
            cringe_url = json["versions"][i]["url"]
            break
    if cringe_url == "":
        raise Exception("no such version found")
    return cringe_url

# returns the url to download the server jar for a specified version as a string
def get_jar_url(version):
    version_meta = requests.get(get_meta_url(version)).json()
    if "server" in version_meta["downloads"]:
        return version_meta["downloads"]["server"]["url"]
    else:
        raise Exception("minecraft version does not have a server")

# gets url of the server jar of the latest version
def get_latest_jar():
    return get_jar_url(get_latest_version())

# returns all version names in a string list
def all_versions():
    vers = []
    for version in json["versions"]:
        vers.append(version["id"])
    return vers

# gets strings of version names and returns all of them in the channel(release/snapshot) as a list
def get_channel_versions(chan):
    vers = []
    for version in json["versions"]:
        if version["type"] == chan:
            vers.append(version["id"])
    return vers

# gets the jar urls of all the versions it can find in a dictionary. chan is a string containing the type of version(release or snapshot)
def get_jar_urls(chan):
    pog = {}
    for version in get_channel_versions(chan):
        try:
            pog.update({version: get_jar_url(version)})
        except:
            pog.update({version: ""})
    return pog


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "latest":
        print(get_jar_url(get_latest_version()))
    else:
        print(get_jar_url(sys.argv[1]))
