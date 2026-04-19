import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update CSS Variables for Linear Light Mode
old_vars = """    :root {
      /* Linear-Inspired Dark Theme */
      --bg: #08090a;
      --surface: #0f1011;
      --surface-2: #191a1b;
      --border: rgba(255,255,255,0.05);
      --text-primary: #f7f8f8;
      --text-secondary: #d0d6e0;
      --text-muted: #8a8f98;
      --accent: #5e6ad2;
      
      /* Semantic tags */
      --accent-green: #27a644;
      --accent-red: #dc2626;
      --accent-amber: #d97706;
      --accent-blue: #7170ff;
      
      --tag-green-bg: background: transparent;
      --tag-green-text: #10b981;
      
      --tag-red-bg: transparent;
      --tag-red-text: #dc2626;
      
      --tag-blue-bg: transparent;
      --tag-blue-text: #7170ff;
      
      --font: 'Inter Variable', 'Inter', 'SF Pro Display', -apple-system, sans-serif;
      --mono: 'Berkeley Mono', ui-monospace, Menlo, monospace;
      
      --radius: 8px;
      --radius-sm: 6px;
      --shadow: rgba(0,0,0,0.2) 0px 0px 0px 1px;
      --shadow-md: rgba(0,0,0,0.4) 0px 2px 4px;
    }"""

new_vars = """    :root {
      /* Linear-Inspired Light Theme */
      --bg: #f7f8f8;
      --surface: #ffffff;
      --surface-2: #f3f4f5;
      --border: rgba(0,0,0,0.08); /* Linear Light Border Standard */
      --text-primary: #111315;
      --text-secondary: #5e6166;
      --text-muted: #8a8f98;
      --accent: #5e6ad2;
      
      /* Semantic tags */
      --accent-green: #27a644;
      --accent-red: #dc2626;
      --accent-amber: #d97706;
      --accent-blue: #5e6ad2;
      
      --tag-green-bg: background: transparent;
      --tag-green-text: #27a644;
      
      --tag-red-bg: transparent;
      --tag-red-text: #dc2626;
      
      --tag-blue-bg: transparent;
      --tag-blue-text: #5e6ad2;
      
      --font: 'Inter Variable', 'Inter', 'SF Pro Display', -apple-system, sans-serif;
      --mono: 'Berkeley Mono', ui-monospace, Menlo, monospace;
      
      --radius: 8px;
      --radius-sm: 6px;
      --shadow: rgba(0,0,0,0.04) 0px 1px 2px, rgba(0,0,0,0.02) 0px 0px 0px 1px;
      --shadow-md: rgba(0,0,0,0.06) 0px 4px 8px, rgba(0,0,0,0.03) 0px 0px 0px 1px;
    }"""

if old_vars in content:
    content = content.replace(old_vars, new_vars)
else:
    content = re.sub(r"    :root \{.*?\n    \}", new_vars, content, flags=re.DOTALL)

# Modify chart colors for light mode
content = content.replace("backgroundColor: '#f7f8f8'", "backgroundColor: '#111315'") # current year
content = content.replace("backgroundColor: 'rgba(255,255,255,0.08)'", "backgroundColor: 'rgba(0,0,0,0.06)'") # last year
content = content.replace("backgroundColor: '#191a1b'", "backgroundColor: '#ffffff'") # tooltip bg
content = content.replace("borderColor: 'rgba(255,255,255,0.08)'", "borderColor: 'rgba(0,0,0,0.08)'") # tooltip border
content = content.replace("titleColor: '#f7f8f8'", "titleColor: '#111315'")
content = content.replace("bodyColor: '#d0d6e0'", "bodyColor: '#5e6166'")
content = content.replace("grid: { color: 'rgba(255,255,255,0.05)'", "grid: { color: 'rgba(0,0,0,0.04)'")
content = content.replace("background: rgba(255,255,255,0.02);", "background: #ffffff;")
content = content.replace("background-color: rgba(255,255,255,0.02);", "background-color: #ffffff;")

# Replace legend dots
content = content.replace('<div class="legend-dot" style="background:#f7f8f8"></div>', '<div class="legend-dot" style="background:#111315"></div>')
content = content.replace('<div class="legend-dot" style="background:rgba(255,255,255,0.08)"></div>', '<div class="legend-dot" style="background:rgba(0,0,0,0.06)"></div>')

content = content.replace("fill: #f7f8f8;", "fill: #111315;") # Logo
content = content.replace("stroke='%23d0d6e0'", "stroke='%235e6166'") # Select arrow
content = content.replace("border: 1px solid rgba(255,255,255,0.08);", "border: 1px solid rgba(0,0,0,0.08);")

with open("index.html", "w") as f:
    f.write(content)
