import sys
import requests

mcLauncherUrl = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

json = requests.get(mcLauncherUrl).json()


def refresh_meta():
    json = requests.get(mcLauncherUrl).json()


def get_latest_version():
    return json["latest"]["release"]


def get_meta_url(ver):
    cringe_url = ""
    for i in range(len(json["versions"])):
        if json["versions"][i]["id"] == ver:
            cringe_url = json["versions"][i]["url"]
            break
    if cringe_url == "":
        raise Exception("no such version found")
    return cringe_url


def get_jar_url(version):
    version_meta = requests.get(get_meta_url(version)).json()
    if "server" in version_meta["downloads"]:
        return version_meta["downloads"]["server"]["url"]
    else:
        raise Exception("minecraft version does not have a server")


def get_latest_jar():
    return get_jar_url(get_latest_version())


def all_versions():
    vers = []
    for version in json["versions"]:
        vers.append(version["id"])
    return vers


def get_channel_versions(chan):
    vers = []
    for version in json["versions"]:
        if version["type"] == chan:
            vers.append(version["id"])
    return vers


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
