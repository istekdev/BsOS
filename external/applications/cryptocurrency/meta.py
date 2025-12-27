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

def weight():
  with open("metadata.json", "r") as r:
    metadata = json.load(r)
  weights = []
  for files in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), files)
    if os.path.isfile(path):
      weights.append(os.path.getsize(path))
  weights = sum(weights)
  metadata["weight"] = weights
  
  static = (metadata["name"].encode("utf-8") + metadata["version"].to_bytes((metadata["version"].bit_length() + 7) // 8, "big") + metadata["created"].to_bytes((metadata["created"].bit_length() + 7) // 8, "big") + metadata["directory"].encode("utf-8") + metadata["update"].encode("utf-8") + weight.to_bytes((weight.bit_length() + 7) // 8, "big"))
  metadata["verifyHash"] = sha256(static).hexdigest()
  with open("metadata.json", "w") as w:
    json.dump(metadata, w, indent=4)
