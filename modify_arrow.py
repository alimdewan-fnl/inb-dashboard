with open("index.html", "r") as f:
    content = f.read()

# Update select arrow colors, we had %236b6860 (which is #6b6860) and want %23ffffff for stark contrast on dark grey
content = content.replace("%236b6860", "%23a1a1aa") # using text-secondary hex

# Chart hover/UI, earlier it checked chart tooltips, but let's make sure it's crisp 
with open("index.html", "w") as f:
    f.write(content)
