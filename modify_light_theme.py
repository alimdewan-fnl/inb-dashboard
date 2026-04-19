import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update CSS Variables for Light Monochrome xAI feel
old_vars = """    :root {
      /* xAI-Inspired Monochrome Theme */
      --bg: #000000;
      --surface: #0a0a0a;
      --surface-2: #161616;
      --border: #262626;
      --text-primary: #ffffff;
      --text-secondary: #a1a1aa;
      --text-muted: #52525b;
      --accent: #ffffff;
      /* Restrained stark functional colors */
      --accent-green: #4ade80;
      --accent-red: #f87171;
      --accent-amber: #fbbf24;
      --accent-blue: #60a5fa;
      --tag-green-bg: #064e3b;
      --tag-green-text: #34d399;
      --tag-red-bg: #450a0a;
      --tag-red-text: #f87171;
      --tag-blue-bg: #1e3a8a;
      --tag-blue-text: #60a5fa;
      --font: 'DM Sans', -apple-system, sans-serif;
      --mono: 'DM Mono', Menlo, monospace;
      /* Futuristic stark edges */
      --radius: 0px;
      --radius-sm: 0px;
      --shadow: none;
      --shadow-md: none;
    }"""

new_vars = """    :root {
      /* xAI-Inspired Light Mode Minimal Theme */
      --bg: #f9f9f9;
      --surface: #ffffff;
      --surface-2: #f0f0f0;
      --border: #e0e0e0;
      --text-primary: #000000;
      --text-secondary: #52525b;
      --text-muted: #a1a1aa;
      --accent: #000000;
      /* Restrained stark functional colors */
      --accent-green: #16a34a;
      --accent-red: #dc2626;
      --accent-amber: #d97706;
      --accent-blue: #2563eb;
      --tag-green-bg: #dcfce7;
      --tag-green-text: #16a34a;
      --tag-red-bg: #fee2e2;
      --tag-red-text: #dc2626;
      --tag-blue-bg: #dbeafe;
      --tag-blue-text: #2563eb;
      --font: 'DM Sans', -apple-system, sans-serif;
      --mono: 'DM Mono', Menlo, monospace;
      /* Futuristic stark edges */
      --radius: 0px;
      --radius-sm: 0px;
      --shadow: none;
      --shadow-md: none;
    }"""

content = content.replace(old_vars, new_vars)

# 2. Revert charting aesthetics mappings
# tooltip: {
#   backgroundColor: '#161616',
#   borderColor: '#333333',

content = content.replace(
    "backgroundColor: '#ffffff'", # current year line
    "backgroundColor: '#000000'"
)
content = content.replace(
    "backgroundColor: '#333333'", # last year line
    "backgroundColor: '#e5e5e5'"
)

content = content.replace(
    "tooltip: {\n              backgroundColor: '#161616',\n              borderColor: '#333333',\n              borderWidth: 1,",
    "tooltip: {\n              backgroundColor: '#ffffff',\n              borderColor: '#e0e0e0',\n              borderWidth: 1,"
)
content = content.replace("titleColor: '#ffffff'", "titleColor: '#000000'")
content = content.replace("bodyColor: '#a1a1aa'", "bodyColor: '#52525b'")
content = content.replace("grid: { color: '#262626', drawBorder: false }", "grid: { color: '#f0f0f0', drawBorder: false }")
content = content.replace("color: '#52525b'", "color: '#a1a1aa'")

# 3. Logo/UI text tweaks back to dark-on-light
content = content.replace(
    """    .logo-mark {
      width: 28px;
      height: 28px;
      background: var(--text-primary);""",
    """    .logo-mark {
      width: 28px;
      height: 28px;
      background: var(--text-primary);"""
) # No change needed because var(--text-primary) handles it automatically now

content = content.replace(
    """    .logo-mark svg {
      width: 14px;
      height: 14px;
      fill: #000;
    }""",
    """    .logo-mark svg {
      width: 14px;
      height: 14px;
      fill: #fff;
    }"""
)

# Fix chart legend colors in HTML
content = content.replace(
    '<div class="legend-dot" style="background:#333333"></div>Last Year',
    '<div class="legend-dot" style="background:#e5e5e5"></div>Last Year'
)

# Fix badge UI tweaks explicitly written
content = content.replace("background: #45240a;", "background: #fef3c7;")

# Fix arrow color in SVG for select
content = content.replace("%23a1a1aa", "%2352525b")

with open("index.html", "w") as f:
    f.write(content)

