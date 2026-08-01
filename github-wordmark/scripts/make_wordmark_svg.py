import pyfiglet

NAME = "HARSH KORI"

fig = pyfiglet.Figlet(font="slant")
ascii_art = fig.renderText(NAME)

lines = ascii_art.splitlines()

width = 1000
height = len(lines) * 25 + 40

svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<rect width="100%" height="100%" fill="#0d1117"/>

<style>
text {{
    fill:#58a6ff;
    font-family:Consolas,monospace;
    font-size:20px;
}}
</style>
"""

y = 35

for line in lines:
    svg += f'<text x="20" y="{y}">{line}</text>\n'
    y += 25

svg += "</svg>"

with open("output/harsh_kori.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("SVG Created Successfully!")