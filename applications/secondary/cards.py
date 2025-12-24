import json, time, os, shutil
from pathlib import Path

with open("./config.json", "r") as r:
  config = json.load(r)

def install():
  os.makedirs(f"/local/users/{config["system"]["loggedIn"]}/apps/cards", exist_ok=True)
  shutil.copytree(f"/external/applications/cards", f"/local/users/{config["system"]["loggedIn"]}/apps/cards", dirs_exist_ok=True)

def update():
  shutil.copytree(f"https://github.com/istekdev/BsOS/blob/main/external/applications/cards", f"/local/users/{config["system"]["loggedIn"]}/apps/cards", dirs_exist_ok=True)

def uninstall():
  shutil.rmtree(f"/local/users/{config["system"]["loggedIn"]}/apps/cards")
