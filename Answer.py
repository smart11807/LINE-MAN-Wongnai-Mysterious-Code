import base64

import base64
data = open("Mysterious.txt").read()
decoded = base64.b64decode(data)

rev = decoded[::-1]
print(rev)

# Answer >> Join:us:at:LINE:MAN:Wongnai <<
