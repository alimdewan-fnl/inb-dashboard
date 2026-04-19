import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update CSS Variables for Linear Theme
old_vars = """    :root {
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
      
      --tag-green-bg: rgba(26,174,57,0.1);
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

new_vars = """    :root {
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

if old_vars in content:
    content = content.replace(old_vars, new_vars)
else:
    content = re.sub(r"    :root \{.*?\n    \}", new_vars, content, flags=re.DOTALL)

# 2. Add structural styling to the body for Linear's specific cv01, ss03 OpenType features
content = content.replace(
    """    body {
      font-family: var(--font);
      background: #ffffff;
      color: var(--text-primary);""",
    """    body {
      font-family: var(--font);
      background: var(--bg);
      color: var(--text-primary);
      font-feature-settings: "cv01", "ss03";"""
)

# Fix KPI card rendering
content = content.replace("background: var(--surface);", "background: rgba(255,255,255,0.02);")

# Typography tightening
content = content.replace(
    """    .kpi-value {
      font-family: var(--font);
      font-size: 28px;
      font-weight: 700;
      letter-spacing: -0.25px;""",
    """    .kpi-value {
      font-family: var(--font);
      font-size: 28px;
      font-weight: 510;
      letter-spacing: -0.704px;"""
)

content = content.replace(
    """    .kpi-value.large {
      font-size: 40px;
      letter-spacing: -1.0px;
    }""",
    """    .kpi-value.large {
      font-size: 40px;
      font-weight: 510;
      letter-spacing: -1.056px;
    }"""
)

# 3. Chart JS refactor to completely fix issues
# It might fail due to syntax, replace the entire BuildChart segment natively.
# Let's extract the chart options and datasets and replace them clean.

chart_block_regex = r"function buildChart\(currentYear, lastYear\) \{.*?\n    \}"

clean_chart_block = """function buildChart(currentYear, lastYear) {
      const ctx = document.getElementById('revenueChart');
      if (window._revChart) window._revChart.destroy();
      window._revChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: months,
          datasets: [
            {
              label: 'Current Year',
              data: currentYear,
              backgroundColor: '#f7f8f8',
              borderRadius: 4,
              borderSkipped: false,
              barThickness: 10,
            },
            {
              label: 'Last Year',
              data: lastYear,
              backgroundColor: 'rgba(255,255,255,0.08)',
              borderRadius: 4,
              borderSkipped: false,
              barThickness: 10,
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: '#191a1b',
              borderColor: 'rgba(255,255,255,0.08)',
              borderWidth: 1,
              titleColor: '#f7f8f8',
              bodyColor: '#d0d6e0',
              padding: 10,
              cornerRadius: 6,
              callbacks: {
                label: ctx => ` ${ctx.dataset.label}: $${ctx.parsed.y}k`
              }
            }
          },
          scales: {
            x: {
              grid: { display: false },
              border: { display: false },
              ticks: { font: { family: 'Inter Variable' }, color: '#8a8f98' }
            },
            y: {
              grid: { color: 'rgba(255,255,255,0.05)', drawBorder: false },
              border: { display: false, dash: [4, 4] },
              ticks: {
                font: { family: 'Inter Variable' },
                color: '#8a8f98',
                callback: v => v ? `$${v}k` : ''
              }
            }
          }
        }
      });
    }"""

content = re.sub(chart_block_regex, clean_chart_block, content, flags=re.DOTALL)

# Refactor legend colors for html blocks
content = content.replace('<div class="legend-dot" style="background:rgba(0,0,0,0.95)"></div>', '<div class="legend-dot" style="background:#f7f8f8"></div>')
content = content.replace('<div class="legend-dot" style="background:rgba(0,0,0,0.05)"></div>', '<div class="legend-dot" style="background:rgba(255,255,255,0.08)"></div>')
content = content.replace('<div class="legend-dot" style="background:#d6d2cb"></div>', '<div class="legend-dot" style="background:rgba(255,255,255,0.08)"></div>')

content = content.replace("background: rgba(229,160,0,0.1);", "background: transparent; border: 1px solid rgba(255,255,255,0.08);")

# Change select custom appearance back to dark theme
content = content.replace("background-color: var(--surface-2);", "background-color: rgba(255,255,255,0.02);")
content = content.replace("background-color: var(--surface);", "background-color: var(--surface-2);")
content = re.sub(r"stroke=\'%23.*?\'", "stroke='%23d0d6e0'", content)

content = content.replace("border-bottom: 1px solid rgba(0,0,0,0.05);", "border-bottom: 1px solid var(--border);")
content = content.replace("fill: rgba(0,0,0,0.95);", "fill: #f7f8f8;")

with open("index.html", "w") as f:
    f.write(content)

