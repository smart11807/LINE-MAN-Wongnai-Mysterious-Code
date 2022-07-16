import base64
import numpy as np

import base64
data = open("Mysterious.txt").read()
decoded = base64.b64decode(data)

rev = decoded[::-1]
print(rev)
