import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update CSS Variables
old_vars = """    :root {
      --bg: #f5f4f1;
      --surface: #ffffff;
      --surface-2: #f0eeea;
      --border: #e2dfd8;
      --text-primary: #1a1916;
      --text-secondary: #6b6860;
      --text-muted: #a8a49e;
      --accent: #1a1916;
      --accent-green: #1a7a4a;
      --accent-red: #b83232;
      --accent-amber: #c47b00;
      --accent-blue: #1d5fa8;
      --tag-green-bg: #ecf7f1;
      --tag-green-text: #1a7a4a;
      --tag-red-bg: #fdf0f0;
      --tag-red-text: #b83232;
      --tag-blue-bg: #edf4fc;
      --tag-blue-text: #1d5fa8;
      --font: 'DM Sans', sans-serif;
      --mono: 'DM Mono', monospace;
      --radius: 10px;
      --radius-sm: 6px;
      --shadow: 0 1px 3px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
      --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.07), 0 2px 4px rgba(0, 0, 0, 0.04);
    }"""

new_vars = """    :root {
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

content = content.replace(old_vars, new_vars)

# 2. Update chart aesthetics (JS mapping & CSS)
content = content.replace("backgroundColor: '#1a1916'", "backgroundColor: '#ffffff'") # current year
content = content.replace("backgroundColor: '#c8c3bb'", "backgroundColor: '#333333'") # last year
content = content.replace("titleColor: '#f9fafb'", "titleColor: '#ffffff'")
content = content.replace("bodyColor: '#d1d5db'", "bodyColor: '#a1a1aa'")
content = content.replace("backgroundColor: '#1a1916'", "backgroundColor: '#161616'") # tooltip bg, may have been replaced, use regex instead

# Let's fix tooltip bg safely using regex
content = re.sub(r"backgroundColor:\s*'#1a1916'(.*?)// current year", r"backgroundColor: '#ffffff'\1// current year", content, flags=re.DOTALL)

# Make sure we got chart background right. The old code was:
# tooltip: {
#   backgroundColor: '#1a1916',
content = content.replace(
    "tooltip: {\n              backgroundColor: '#1a1916',",
    "tooltip: {\n              backgroundColor: '#161616',\n              borderColor: '#333333',\n              borderWidth: 1,"
)
content = content.replace("grid: { color: '#f0eeea', drawBorder: false }", "grid: { color: '#262626', drawBorder: false }")
content = content.replace("ticks: { font: { family: 'DM Sans', size: 11 }, color: '#a8a49e' }", "ticks: { font: { family: 'DM Sans', size: 11 }, color: '#52525b' }")
content = content.replace("ticks: {\n                font: { family: 'DM Sans', size: 11 },\n                color: '#a8a49e',", "ticks: {\n                font: { family: 'DM Sans', size: 11 },\n                color: '#52525b',")

# Update color maps in JS
# var(--accent-green) etc are dynamically set in setColor:
# const map = { green: 'var(--accent-green)', red: 'var(--accent-red)', amber: 'var(--accent-amber)', neutral: 'var(--text-primary)' };
# This logic still works based on our new vars.

# 3. Clean up UI elements like .kpi-label .info-dot
content = content.replace(
    """    .kpi-label .info-dot {
      width: 14px;
      height: 14px;
""",
    """    .kpi-label .info-dot {
      width: 14px;
      height: 14px;
      background: var(--surface-2);
      border: none;
      color: var(--text-primary);
"""
)

# 4. Enhance typography hierarchy
content = content.replace(
    """    .kpi-value {
      font-family: var(--font);
      font-size: 28px;
      font-weight: 700;
      letter-spacing: -0.03em;
""",
    """    .kpi-value {
      font-family: var(--font);
      font-size: 28px;
      font-weight: 500;
      letter-spacing: -0.04em;
"""
)

# 5. Header / logo
content = content.replace(
    """    .logo-mark {
      width: 28px;
      height: 28px;
      background: var(--accent);
""",
    """    .logo-mark {
      width: 28px;
      height: 28px;
      background: var(--text-primary);
"""
)

content = content.replace(
    """    .logo-mark svg {
      width: 14px;
      height: 14px;
      fill: white;
    }""",
    """    .logo-mark svg {
      width: 14px;
      height: 14px;
      fill: #000;
    }"""
)

# Fix chart legend colors in HTML
content = content.replace(
    '<div class="legend-dot" style="background:#c8c3bb"></div>Last Year',
    '<div class="legend-dot" style="background:#333333"></div>Last Year'
)

# Fix badge-amber UI
content = content.replace("background: #fef9ec;", "background: #45240a;")

with open("index.html", "w") as f:
    f.write(content)

