import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Provide Notion Style CSS Variables
old_vars = """    :root {
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

new_vars = """    :root {
      /* Notion-Inspired Theme */
      --bg: #ffffff;
      --surface: #ffffff;
      --surface-2: #f6f5f4;
      --border: rgba(0,0,0,0.1);
      --text-primary: rgba(0,0,0,0.95);
      --text-secondary: #615d59;
      --text-muted: #a39e98;
      --accent: #0075de;
      
      /* Semantic tags */
      --accent-green: #1aae39;
      --accent-red: #dd5b00;
      --accent-amber: #e5a000;
      --accent-blue: #0075de;
      
      --tag-green-bg: background: rgba(26,174,57,0.1);
      --tag-green-text: #1aae39;
      
      --tag-red-bg: rgba(221,91,0,0.1);
      --tag-red-text: #dd5b00;
      
      --tag-blue-bg: #f2f9ff;
      --tag-blue-text: #097fe8;
      
      --font: 'Inter', -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      --mono: 'DM Mono', Menlo, monospace;
      
      --radius: 12px;
      --radius-sm: 4px;
      --shadow: rgba(0,0,0,0.04) 0px 4px 18px, rgba(0,0,0,0.027) 0px 2.025px 7.85px, rgba(0,0,0,0.02) 0px 0.8px 2.93px, rgba(0,0,0,0.01) 0px 0.175px 1.04px;
      --shadow-md: rgba(0,0,0,0.01) 0px 1px 3px, rgba(0,0,0,0.02) 0px 3px 7px, rgba(0,0,0,0.02) 0px 7px 15px, rgba(0,0,0,0.04) 0px 14px 28px, rgba(0,0,0,0.05) 0px 23px 52px;
    }"""

if old_vars in content:
    content = content.replace(old_vars, new_vars)
else:
    # Use regex if indentation changed slightly
    content = re.sub(r"    :root \{.*?\n    \}", new_vars, content, flags=re.DOTALL)

# 2. Typography updates
content = content.replace(
    """    .kpi-value {
      font-family: var(--font);
      font-size: 28px;
      font-weight: 500;
      letter-spacing: -0.04em;""",
    """    .kpi-value {
      font-family: var(--font);
      font-size: 28px;
      font-weight: 700;
      letter-spacing: -0.25px;"""
)

content = content.replace(
    """    .kpi-value.large {
      font-size: 36px;
    }""",
    """    .kpi-value.large {
      font-size: 40px;
      letter-spacing: -1.0px;
    }"""
)

# Replace the info dot background from the light theme mod
content = content.replace(
    """    .kpi-label .info-dot {
      width: 14px;
      height: 14px;
      background: var(--surface-2);
      border: none;
      color: var(--text-primary);
      border-radius: 50%;""",
    """    .kpi-label .info-dot {
      width: 14px;
      height: 14px;
      border: 1px solid var(--border);
      border-radius: 50%;
      background: transparent;
      color: var(--text-muted);"""
)

# Fix charts: replace styling back to Notion
content = content.replace(
    "backgroundColor: '#000000'",
    "backgroundColor: 'rgba(0,0,0,0.95)'"
)
content = content.replace(
    "backgroundColor: '#e5e5e5'",
    "backgroundColor: 'rgba(0,0,0,0.05)'"
)
content = content.replace(
    "tooltip: {\n              backgroundColor: '#ffffff',\n              borderColor: '#e0e0e0',\n              borderWidth: 1,",
    "tooltip: {\n              backgroundColor: '#ffffff',\n              borderColor: 'rgba(0,0,0,0.1)',\n              borderWidth: 1,"
)
content = content.replace("titleColor: '#000000'", "titleColor: 'rgba(0,0,0,0.95)'")
content = content.replace("bodyColor: '#52525b'", "bodyColor: '#615d59'")
content = content.replace("grid: { color: '#f0f0f0', drawBorder: false }", "grid: { color: 'rgba(0,0,0,0.03)', drawBorder: false }")
content = content.replace("color: '#a1a1aa'", "color: '#a39e98'")
content = content.replace("color: '#52525b'", "color: '#615d59'") # axis text

# Update badge formatting
content = content.replace(
    """    .kpi-badge {
      display: inline-flex;
      align-items: center;
      gap: 3px;
      font-size: 11px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 4px;
    }""",
    """    .kpi-badge {
      display: inline-flex;
      align-items: center;
      gap: 3px;
      font-size: 12px;
      font-weight: 600;
      padding: 4px 8px;
      border-radius: 9999px;
      letter-spacing: 0.125px;
    }"""
)

# Badge colors
content = content.replace("background: #fef3c7;", "background: rgba(229,160,0,0.1);")

content = content.replace("fill: #fff;", "fill: rgba(0,0,0,0.95);")
content = content.replace("background: var(--text-primary);", "background: transparent;")
content = content.replace('<div class="legend-dot" style="background:#e5e5e5"></div>', '<div class="legend-dot" style="background:rgba(0,0,0,0.05)"></div>')
content = content.replace('<div class="legend-dot" style="background:var(--accent)"></div>', '<div class="legend-dot" style="background:rgba(0,0,0,0.95)"></div>')

content = content.replace("var(--bg)", "#ffffff")
# Make header border
content = content.replace("border-bottom: 1px solid var(--border);", "border-bottom: 1px solid rgba(0,0,0,0.05);")

# Update select chevron to match Notion
content = re.sub(r'fill=\\\'none\\\' stroke=\\\'%23.*?\\\'', r"fill=\'none\' stroke=\'%23615d59\'", content)


with open("index.html", "w") as f:
    f.write(content)

