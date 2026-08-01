from pyfiglet import Figlet

NAME = "HARSH KORI"

fig = Figlet(font="slant")
ascii_art = fig.renderText(NAME)

lines = ascii_art.splitlines()

width = 900
line_height = 22
height = len(lines) * line_height + 40

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<style>
text {{
font-family: monospace;
font-size:18px;
fill:#58a6ff;
}}
</style>

<rect width="100%" height="100%" fill="#0d1117"/>

<defs>
<clipPath id="wipe">
<rect width="0" height="{height}">
<animate
attributeName="width"
from="0"
to="{width}"
dur="2s"
fill="freeze"/>
</rect>
</clipPath>
</defs>

<g clip-path="url(#wipe)">
'''

y = 30

for line in lines:
    svg += f'<text x="20" y="{y}">{line}</text>\n'
    y += line_height

svg += "</g></svg>"

with open("name.svg", "w") as f:
    f.write(svg)

print("Done! SVG saved as name.svg")