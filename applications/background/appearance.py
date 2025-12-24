import random

def cursed():
  raw = random.randint(1, 0xFFFFFF)
  return f"#{raw:06x}"
