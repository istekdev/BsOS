from hashlib import sha256
import json, os, requests

def verify():
  if not os.path.exists("metadata.json"):
    return False
  else:
    return True

def verifyHash():
  if verify() == True:
    with open("metadata.json", "r") as r:
      metadata = json.load(r)

    static = (metadata["name"].encode("utf-8") + metadata["version"].to_bytes((metadata["name"].bit_length() + 7) // 8, "big") + metadata["created"].to_bytes((metadata["name"].bit_length() + 7) // 8, "big") + metadata["directory"].encode("utf-8") + metadata["update"].encode("utf-8"))
    if sha256(static) == metadata["verifyHash"]:
      return "Hash Verified"
    else:
      return "Hash Invalid"
  else:
    return "metadata.json Unavailable"

def upd():
  if verify() == True:
    with open("metadata.json", "r") as r:
      metadata = json.load(r)
    verified = None
    err = None
    try:
      connect = requests.get(metadata["directory"])
      connect.raise_for_status()
      cJ = connect.json()
      verified = bool(cJ)
    except Exception as e:
      err = e
    if verified == True and err == None:
      connect = requests.get(metadata["directory"]).json()
      if connect["version"] != metadata["version"]:
        return "Update"
      else:
        return "No Need"
  else:
    return "metadata.json Unavailable"
