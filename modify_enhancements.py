import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update .kpi-card CSS
card_css_old = r"""    \.kpi-card \{
      background: \#ffffff;
      border: 1px solid rgba\(0,0,0,0\.08\);
      border-radius: var\(--radius\);
      padding: 18px 20px;
      position: relative;
      cursor: default;
      transition: border-color 0\.15s, box-shadow 0\.15s;
      box-shadow: var\(--shadow\);
    \}"""
    
# Since box-shadow was defined in my python script as `box-shadow: var(--shadow);` but I might have altered it.
# Let's cleanly replace the properties using regex targeting the block.

def replace_cards(m):
    return """    .kpi-card {
      background: #ffffff;
      border: 1px solid rgba(0,0,0,0.12);
      border-radius: var(--radius);
      padding: 18px 20px;
      position: relative;
      cursor: default;
      transition: border-color 0.15s, box-shadow 0.15s;
      box-shadow: rgba(0,0,0,0.08) 0px 4px 12px, rgba(0,0,0,0.04) 0px 1px 3px;
    }"""

content = re.sub(r"    \.kpi-card \{.*?\}", replace_cards, content, flags=re.DOTALL)

def replace_charts(m):
    return """    .chart-card {
      background: #ffffff;
      border: 1px solid rgba(0,0,0,0.12);
      border-radius: var(--radius);
      padding: 22px 24px;
      box-shadow: rgba(0,0,0,0.08) 0px 4px 12px, rgba(0,0,0,0.04) 0px 1px 3px;
    }"""

content = re.sub(r"    \.chart-card \{.*?\}", replace_charts, content, flags=re.DOTALL)

# 2. Update chart data
content = re.sub(r"const baseEarned \= \[.*?\];", "const baseEarned = [820, 890, 950, 920, 1050, 1120, 1080, 1150, 1220, 1180, 1300, 1420];", content)
content = re.sub(r"const baseEarnedLY \= \[.*?\];", "const baseEarnedLY = [750, 810, 880, 850, 970, 1020, 990, 1050, 1110, 1080, 1180, 1250];", content)


with open("index.html", "w") as f:
    f.write(content)

