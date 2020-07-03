import sys
import json
import requests

mcLauncherUrl = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

json = requests.get(mcLauncherUrl).json()


def refresh_meta():
    json = requests.get(mcLauncherUrl).json()


def get_latest_version():
    return json["latest"]["release"]


def get_jar_url(version):
    cringe_url = ""
    for i in range(len(json["versions"])):
        if json["versions"][i]["id"] == version:
            cringe_url = json["versions"][i]["url"]
            break
    if cringe_url == "":
        raise Exception("no such version found")
    version_meta = requests.get(cringe_url).json()
    if "server" in version_meta["downloads"]:
        return version_meta["downloads"]["server"]["url"]
    else:
        raise Exception("minecraft version does not have a server")


def get_latest_jar():
    return get_jar_url(get_latest_version())


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "latest":
        print(get_jar_url(get_latest_version()))
    else:
        print(get_jar_url(sys.argv[1]))
