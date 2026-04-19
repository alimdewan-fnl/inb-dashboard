import re

with open("index.html", "r") as f:
    content = f.read()

# CHANGE 1: MONTHLY REVENUE TREND
content = content.replace(
    '<div class="chart-subtitle">Revenue Earned vs Invoiced · YTD</div>',
    '<!-- CHANGE 1: Subtitle update -->\n              <div class="chart-subtitle">Monthly Earned Revenue Trend vs Last Year</div>'
)

content = content.replace(
    '<div class="legend-dot" style="background:var(--accent)"></div>Earned',
    '<!-- CHANGE 1: Legend update -->\n                <div class="legend-dot" style="background:var(--accent)"></div>Current Year'
)

content = content.replace(
    '<div class="legend-dot" style="background:#c8c3bb"></div>Invoiced',
    '<div class="legend-dot" style="background:#c8c3bb"></div>Last Year'
)

# CHANGE 1: JS for Chart
js_chart_old = """    const baseEarned = [820, 910, 1050, 980, 1120, 1280, 1050, 970, 1100, 900, 0, 0];
    const baseInvoiced = [760, 860, 980, 900, 1050, 1200, 980, 920, 1020, 830, 0, 0];

    function buildChart(earned, invoiced) {"""
js_chart_new = """    // CHANGE 1: New dataset and updated parameters for chart
    const baseEarned = [820, 910, 1050, 980, 1120, 1280, 1050, 970, 1100, 900, 0, 0];
    const baseEarnedLY = [750, 840, 960, 910, 1020, 1150, 990, 890, 1010, 850, 900, 950];

    function buildChart(currentYear, lastYear) {"""
content = content.replace(js_chart_old, js_chart_new)

content = content.replace("label: 'Earned',", "label: 'Current Year',")
content = content.replace("data: earned,", "data: currentYear,")
content = content.replace("label: 'Invoiced',", "label: 'Last Year',")
content = content.replace("data: invoiced,", "data: lastYear,")

# CHANGE 2: PIPELINE COVERAGE
content = content.replace(
    '<span class="kpi-badge badge-green">+0.2 vs target</span>',
    '<!-- CHANGE 2: Removed +0.2 vs target badge -->'
)

# CHANGE 3: LABEL UPDATE
content = content.replace(
    '<div class="kpi-label">New vs Existing <span class="info-dot">i</span></div>',
    '<!-- CHANGE 3: Label update -->\n          <div class="kpi-label">New vs Existing Business <span class="info-dot">i</span></div>'
)

# CHANGE 4: PROFITABILITY KPI RESTRUCTURE
# move YTD Gross Margin % to top row
gm_pct_card = """        <div class="kpi-card">
          <div class="kpi-label">YTD Gross Margin % <span class="info-dot">i</span></div>
          <div class="kpi-value" id="val-gm-pct" style="color:var(--accent-green)">31.2%</div>
          <div style="margin-top: 10px; display: flex; align-items: center; gap: 8px;">
            <span style="font-size:13px; font-weight:600; color:var(--accent-green)">+4.5%</span>
            <span style="font-size:12px; font-weight:500; color:var(--text-secondary)">YoY Growth</span>
          </div>
          <div class="tooltip">
            <div class="tooltip-tag">Metric</div>
            <div class="tooltip-name">Gross Margin %</div>
            <div class="tooltip-def">Margin as a percentage of revenue — key indicator of delivery efficiency.</div>
            <div class="tooltip-formula">Gross_Margin% = ((Revenue - Cost_of_Delivery) / Revenue) × 100</div>
          </div>
        </div>"""

content = content.replace(gm_pct_card, "")

strategic_grid = '<div class="kpi-grid kpi-grid-4">'
content = content.replace(strategic_grid, '<!-- CHANGE 4: Upgrade to 5 columns -->\n      <div class="kpi-grid kpi-grid-5">', 1)

# insert gm_pct_card at end of strategic section 
# find the closing div of the last card in strategic
yoy_card_end = """        <div class="kpi-card">
          <div class="kpi-label">YoY Growth % <span class="info-dot">i</span></div>
          <div class="kpi-value badge-green" id="val-yoy" style="color:var(--accent-green)">+8.4%</div>
          <span class="kpi-badge badge-green">↑ Same period</span>
          <div class="tooltip">
            <div class="tooltip-tag">Metric</div>
            <div class="tooltip-name">YoY Growth %</div>
            <div class="tooltip-def">Percentage change in revenue compared to the same period in the prior year.</div>
            <div class="tooltip-formula">YoY_Growth = ((Current_Year_Revenue - Previous_Year_Revenue) /
              Previous_Year_Revenue) × 100</div>
          </div>
        </div>"""

content = content.replace(yoy_card_end, yoy_card_end + "\n\n        <!-- CHANGE 4: Moved YTD Gross Margin % here -->\n" + gm_pct_card)

# Insert Contribution Margin in profitability where gm_pct_card was (actually after gm card)
cm_card = """        <!-- CHANGE 4: Add Contribution Margin -->
        <div class="kpi-card">
          <div class="kpi-label">Contribution Margin <span class="info-dot">i</span></div>
          <div class="kpi-value" id="val-cm" style="color:var(--text-primary)">42.5%</div>
          <div class="tooltip">
            <div class="tooltip-tag">Metric</div>
            <div class="tooltip-name">Contribution Margin</div>
            <div class="tooltip-def">Measures revenue remaining after direct delivery and attributable costs.</div>
            <div class="tooltip-formula">Contribution_Margin = ((Revenue - Direct_Costs) / Revenue) × 100</div>
          </div>
        </div>"""

content = content.replace("""        <div class="kpi-card">
        <div class="kpi-label">Avg Margin / Project <span class="info-dot">i</span></div>""", 
cm_card + "\n\n" + """      <div class="kpi-card">
        <div class="kpi-label">Avg Margin / Project <span class="info-dot">i</span></div>""")

# CHANGE 5: AVG MARGIN PROGRESS BAR
avg_margin_block = """      <div class="kpi-card">
        <div class="kpi-label">Avg Margin / Project <span class="info-dot">i</span></div>
        <div class="kpi-value" id="val-avg-margin">$18.2k</div>
        <div class="progress-wrap">
          <div class="progress-track">
            <div class="progress-fill prog-dark" style="width:72%"></div>
          </div>
          <span class="progress-pct">72%</span>
        </div>"""
new_avg_margin_block = """      <!-- CHANGE 5: Avg Margin per project progress bar removed -->
      <div class="kpi-card">
        <div class="kpi-label">Avg Margin / Project <span class="info-dot">i</span></div>
        <div class="kpi-value" id="val-avg-margin">$18.2k</div>"""
content = content.replace(avg_margin_block, new_avg_margin_block)


# CHANGE 6: REMOVE YTD REVENUE INVOICED KPI
invoiced_block = """        <div class="kpi-card">
          <div class="kpi-label">YTD Revenue Invoiced <span class="info-dot">i</span></div>
          <div class="kpi-value large" id="val-ytd-invoiced">$8.4M</div>
          <div class="kpi-sub" style="margin-top:10px; margin-bottom:4px">% of Annual Goal</div>
          <div class="progress-wrap" style="margin-top:0">
            <div class="progress-track">
              <div class="progress-fill prog-blue" id="prog-ytd-invoiced" style="width:56%"></div>
            </div>
            <span class="progress-pct" id="pct-ytd-invoiced">56%</span>
          </div>
          <div class="kpi-sub" style="margin-top:10px; margin-bottom:4px">% of YTD Goal</div>
          <div class="progress-wrap" style="margin-top:0">
            <div class="progress-track">
              <div class="progress-fill prog-green" id="prog-ytd-invoiced-ytd" style="width:84%"></div>
            </div>
            <span class="progress-pct" id="pct-ytd-invoiced-ytd">84%</span>
          </div>
          <div class="tooltip">
            <div class="tooltip-tag">Metric</div>
            <div class="tooltip-name">YTD Revenue Invoiced</div>
            <div class="tooltip-def">Total invoice amounts issued from January through the selected period.</div>
            <div class="tooltip-formula">YTD_Revenue_Invoiced = SUM(Invoice_Amount)</div>
          </div>
        </div>"""
content = content.replace(invoiced_block, "<!-- CHANGE 6: Removed YTD Revenue Invoiced -->")

# Also change kpi-grid-4 to kpi-grid-3 in revenue section
rev_section = '<section id="revenue">'
rev_idx = content.find(rev_section)
grid4_idx = content.find('<div class="kpi-grid kpi-grid-4"', rev_idx)
content = content[:grid4_idx] + '<!-- CHANGE 6: Update grid to rebalance layout -->\n      <div class="kpi-grid kpi-grid-3"' + content[grid4_idx + len('<div class="kpi-grid kpi-grid-4"'):]

# CHANGE 7: MONTH FILTER IMPROVEMENT
# Replace old select with custom multiple select
old_month_select = """      <select id="filterMonth" onchange="updateDashboard()">
        <option value="all">All Months</option>
        <option value="1">January</option>
        <option value="2">February</option>
        <option value="3">March</option>
        <option value="4">April</option>
        <option value="5">May</option>
        <option value="6">June</option>
        <option value="7">July</option>
        <option value="8">August</option>
        <option value="9">September</option>
        <option value="10">October</option>
        <option value="11">November</option>
        <option value="12">December</option>
      </select>"""

new_month_select = """      <!-- CHANGE 7: Month Filter Improvement UI -->
      <div class="custom-select" id="monthFilterContainer">
        <div class="select-selected" id="monthSelectText" onclick="toggleOptionSelect()">All Months</div>
        <div class="select-items select-hide" id="monthOptions">
          <label><input type="checkbox" value="all" checked onchange="handleMonthChange(this)"> All Months</label>
          <label><input type="checkbox" value="1" onchange="handleMonthChange(this)"> January</label>
          <label><input type="checkbox" value="2" onchange="handleMonthChange(this)"> February</label>
          <label><input type="checkbox" value="3" onchange="handleMonthChange(this)"> March</label>
          <label><input type="checkbox" value="4" onchange="handleMonthChange(this)"> April</label>
          <label><input type="checkbox" value="5" onchange="handleMonthChange(this)"> May</label>
          <label><input type="checkbox" value="6" onchange="handleMonthChange(this)"> June</label>
          <label><input type="checkbox" value="7" onchange="handleMonthChange(this)"> July</label>
          <label><input type="checkbox" value="8" onchange="handleMonthChange(this)"> August</label>
          <label><input type="checkbox" value="9" onchange="handleMonthChange(this)"> September</label>
          <label><input type="checkbox" value="10" onchange="handleMonthChange(this)"> October</label>
          <label><input type="checkbox" value="11" onchange="handleMonthChange(this)"> November</label>
          <label><input type="checkbox" value="12" onchange="handleMonthChange(this)"> December</label>
        </div>
      </div>"""
content = content.replace(old_month_select, new_month_select)

# Add custom select CSS
css_to_add = """
    /* MULTI-SELECT CSS */
    .custom-select {
      position: relative;
      font-family: var(--font);
    }
    .select-selected {
      background-color: var(--surface-2);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 6px 28px 6px 10px;
      font-size: 13px;
      font-weight: 500;
      color: var(--text-primary);
      cursor: pointer;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%236b6860' stroke-width='2'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
      background-repeat: no-repeat;
      background-position: right 8px center;
      min-width: 120px;
      user-select: none;
    }
    .select-items {
      position: absolute;
      background-color: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      top: 100%;
      left: 0;
      right: 0;
      z-index: 99;
      max-height: 250px;
      overflow-y: auto;
      box-shadow: var(--shadow-md);
      margin-top: 4px;
      padding: 4px;
    }
    .select-hide {
      display: none;
    }
    .select-items label {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 6px 8px;
      font-size: 13px;
      cursor: pointer;
      border-radius: 4px;
    }
    .select-items label:hover {
      background-color: var(--surface-2);
    }
"""
content = content.replace("/* HEADER */", css_to_add + "\n    /* HEADER */")

# JS for Custom select and filtering logic
new_js = """
    // ── FILTER LOGIC ─────────────────────────────────────────────────────────────
    // CHANGE 7 & 8: Month filter interaction & aggregation logic
    function toggleOptionSelect() {
      document.getElementById("monthOptions").classList.toggle("select-hide");
    }

    document.addEventListener("click", function (e) {
      const container = document.getElementById("monthFilterContainer");
      if (container && !container.contains(e.target)) {
        document.getElementById("monthOptions").classList.add("select-hide");
      }
    });

    let selectedMonths = ['all'];

    function handleMonthChange(checkbox) {
      const val = checkbox.value;
      const checkboxes = document.querySelectorAll('#monthOptions input');
      
      if (val === 'all') {
        if (checkbox.checked) {
          selectedMonths = ['all'];
          checkboxes.forEach(cb => { if (cb.value !== 'all') cb.checked = false; });
        } else {
          checkbox.checked = true; // Prevent unchecking all
        }
      } else {
        const allCb = Array.from(checkboxes).find(cb => cb.value === 'all');
        if (checkbox.checked) {
          allCb.checked = false;
          selectedMonths = selectedMonths.filter(m => m !== 'all');
          selectedMonths.push(val);
        } else {
          selectedMonths = selectedMonths.filter(m => m !== val);
          if (selectedMonths.length === 0) {
            allCb.checked = true;
            selectedMonths = ['all'];
          }
        }
      }
      
      const text = selectedMonths.includes('all') ? 'All Months' : (selectedMonths.length === 1 ? 'Month ' + selectedMonths[0] : selectedMonths.length + ' Months');
      document.getElementById('monthSelectText').textContent = text;
      
      updateDashboard();
    }
"""

content = content.replace("// ── FILTER LOGIC ─────────────────────────────────────────────────────────────", new_js)

# Updating the reset button
content = content.replace("document.getElementById('filterMonth').value = 'all';", """      selectedMonths = ['all'];
      document.querySelectorAll('#monthOptions input').forEach(cb => { cb.checked = cb.value === 'all'; });
      document.getElementById('monthSelectText').textContent = 'All Months';""")

# Update dashboard function
update_dashboard_code = """function updateDashboard() {
      const d = getKey();
      
      // CHANGE 8: Aggregation logic for selected months
      let scaleFactor = 1;
      let monthFactor = 1;
      
      if (!selectedMonths.includes('all')) {
        let totalBaseEarned = baseEarned.slice(0, 10).reduce((a, b) => a + b, 0); // Active months
        let selectedBaseEarned = selectedMonths.reduce((sum, m) => sum + baseEarned[parseInt(m) - 1], 0);
        if (totalBaseEarned > 0) {
          monthFactor = selectedBaseEarned / totalBaseEarned;
        }
      }
      
      // We scale raw volume KPIs using the monthFactor
      const rawEarnedObj = parseFloat(d.ytdE.replace('$', '').replace('M', '')) * monthFactor;
      const fmtEarned = '$' + rawEarnedObj.toFixed(1) + 'M';
      
      const rawPipelineObj = parseFloat(d.pipeline.replace('$', '').replace('M', '')) * monthFactor;
      const fmtPipeline = '$' + rawPipelineObj.toFixed(1) + 'M';

      setVal('val-unit-goal', d.goal);
      setVal('val-forecast', d.forecast);
      setVal('val-runrate', d.runrate); // Run rate stays same or similar, keep static for simplicity
      setVal('val-yoy', d.yoy); setColor('val-yoy', d.yoyColor);
      setVal('val-ytd-earned', fmtEarned);
      // setVal('val-ytd-invoiced', d.ytdI); // Removed
      setVal('val-pipeline', fmtPipeline);
      setVal('val-coverage', d.coverage); setColor('val-coverage', d.coverageColor);
      setVal('val-winrate', d.winrate); setColor('val-winrate', d.winColor);
      setVal('val-dealsize', d.dealsize);
      setVal('val-gm', d.gm);
      setVal('val-gm-pct', d.gmPct); setColor('val-gm-pct', d.gmPctColor);
      setVal('val-gm-yoy', d.gmYoy); setColor('val-gm-yoy', d.gmYoyColor);
      setVal('val-avg-margin', d.avgMargin);
      setVal('val-rev-fte', d.revFte);
      setVal('val-fte-total', d.fteT);
      setVal('val-fte-billable', d.fteB);
      setVal('val-fte-support', d.fteS);

      // progress bars
      const ep = document.getElementById('prog-ytd-earned');
      const epc = document.getElementById('pct-ytd-earned');
      const epy = document.getElementById('prog-ytd-earned-ytd');
      const epyc = document.getElementById('pct-ytd-earned-ytd');

      if (ep) { ep.style.width = Math.round(d.pctE * monthFactor) + '%'; epc.textContent = Math.round(d.pctE * monthFactor) + '%'; }
      if (epy) { epy.style.width = Math.round(d.pctEYtd * monthFactor) + '%'; epyc.textContent = Math.round(d.pctEYtd * monthFactor) + '%'; }

      // chart: scale based on BU
      const scale = d.fteT / 29;
      
      // Filter chart data based on selected months
      let earned = [...baseEarned];
      let lastYearEarned = [...baseEarnedLY];
      
      if (!selectedMonths.includes('all')) {
        earned = earned.map((v, i) => selectedMonths.includes(String(i + 1)) ? v : 0);
        lastYearEarned = lastYearEarned.map((v, i) => selectedMonths.includes(String(i + 1)) ? v : 0);
      }
      
      earned = earned.map(v => v ? Math.round(v * scale) : 0);
      lastYearEarned = lastYearEarned.map(v => v ? Math.round(v * scale) : 0);
      
      buildChart(earned, lastYearEarned);"""

old_update_code = """function updateDashboard() {
      const d = getKey();
      setVal('val-unit-goal', d.goal);
      setVal('val-forecast', d.forecast);
      setVal('val-runrate', d.runrate);
      setVal('val-yoy', d.yoy); setColor('val-yoy', d.yoyColor);
      setVal('val-ytd-earned', d.ytdE);
      setVal('val-ytd-invoiced', d.ytdI);
      setVal('val-pipeline', d.pipeline);
      setVal('val-coverage', d.coverage); setColor('val-coverage', d.coverageColor);
      setVal('val-winrate', d.winrate); setColor('val-winrate', d.winColor);
      setVal('val-dealsize', d.dealsize);
      setVal('val-gm', d.gm);
      setVal('val-gm-pct', d.gmPct); setColor('val-gm-pct', d.gmPctColor);
      setVal('val-gm-yoy', d.gmYoy); setColor('val-gm-yoy', d.gmYoyColor);
      setVal('val-avg-margin', d.avgMargin);
      setVal('val-rev-fte', d.revFte);
      setVal('val-fte-total', d.fteT);
      setVal('val-fte-billable', d.fteB);
      setVal('val-fte-support', d.fteS);

      // progress bars
      const ep = document.getElementById('prog-ytd-earned');
      const ip = document.getElementById('prog-ytd-invoiced');
      const epc = document.getElementById('pct-ytd-earned');
      const ipc = document.getElementById('pct-ytd-invoiced');
      const epy = document.getElementById('prog-ytd-earned-ytd');
      const epyc = document.getElementById('pct-ytd-earned-ytd');
      const ipy = document.getElementById('prog-ytd-invoiced-ytd');
      const ipyc = document.getElementById('pct-ytd-invoiced-ytd');

      if (ep) { ep.style.width = d.pctE + '%'; epc.textContent = d.pctE + '%'; }
      if (ip) { ip.style.width = d.pctI + '%'; ipc.textContent = d.pctI + '%'; }
      if (epy) { epy.style.width = (d.pctEYtd || 0) + '%'; epyc.textContent = (d.pctEYtd || 0) + '%'; }
      if (ipy) { ipy.style.width = (d.pctIYtd || 0) + '%'; ipyc.textContent = (d.pctIYtd || 0) + '%'; }

      // chart: scale based on BU
      const scale = d.fteT / 29;
      const earned = baseEarned.map(v => v ? Math.round(v * scale) : 0);
      const invoiced = baseInvoiced.map(v => v ? Math.round(v * scale) : 0);
      buildChart(earned, invoiced);"""

content = content.replace(old_update_code, update_dashboard_code)

with open("index.html", "w") as f:
    f.write(content)

