import os

def create_svg():
    width = 960
    height = 560
    
    # Margin and bounds
    m_top = 80
    m_bottom = 490
    m_left = 70
    m_right = 850
    chart_w = m_right - m_left
    chart_h = m_bottom - m_top
    
    p_min = 1.0820
    p_max = 1.0915
    p_range = p_max - p_min
    
    def to_y(p):
        return m_bottom - ((p - p_min) / p_range) * chart_h
    
    # Candles: (open, high, low, close, time)
    candles = [
        (1.0905, 1.0910, 1.0888, 1.0892, '09:00'),
        (1.0892, 1.0898, 1.0875, 1.0878, '10:00'),
        (1.0878, 1.0885, 1.0862, 1.0865, '11:00'),
        (1.0865, 1.0870, 1.0848, 1.0850, '12:00'),
        (1.0850, 1.0855, 1.0838, 1.0840, '13:00'),
        # Key Pinbar candle at index 5
        (1.0840, 1.0850, 1.0828, 1.0846, '14:00'),
        # Confirmation candle
        (1.0848, 1.0872, 1.0845, 1.0870, '15:00'),
        (1.0870, 1.0890, 1.0868, 1.0888, '16:00'),
        (1.0888, 1.0895, 1.0880, 1.0885, '17:00'),
        (1.0885, 1.0912, 1.0882, 1.0905, '18:00'),
    ]
    
    num_c = len(candles)
    step_x = chart_w / (num_c + 1)
    
    candle_coords = []
    for i, c in enumerate(candles):
        cx = m_left + (i + 1) * step_x
        candle_coords.append((cx, c))
        
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background-color: #131722; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">')
    
    # Defs / filters / gradients
    svg.append('''
    <defs>
        <linearGradient id="supportGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#2962ff" stop-opacity="0.25"/>
            <stop offset="100%" stop-color="#2962ff" stop-opacity="0.05"/>
        </linearGradient>
        <linearGradient id="riskGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f23645" stop-opacity="0.18"/>
            <stop offset="100%" stop-color="#f23645" stop-opacity="0.05"/>
        </linearGradient>
        <linearGradient id="rewardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#089981" stop-opacity="0.05"/>
            <stop offset="100%" stop-color="#089981" stop-opacity="0.2"/>
        </linearGradient>
        <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.5"/>
        </filter>
        <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#f59e0b" />
        </marker>
    </defs>
    ''')
    
    # Background Grid
    svg.append('<!-- Grid -->')
    price_levels = [1.0830, 1.0850, 1.0870, 1.0890, 1.0910]
    for p in price_levels:
        y = to_y(p)
        svg.append(f'<line x1="{m_left}" y1="{y:.1f}" x2="{m_right}" y2="{y:.1f}" stroke="#2a2e39" stroke-width="1" stroke-dasharray="3,3"/>')
        svg.append(f'<text x="{m_right + 12}" y="{y + 4:.1f}" fill="#787b86" font-size="11" font-family="monospace">{p:.4f}</text>')

    # Header / Title Bar
    svg.append('<!-- Header -->')
    svg.append(f'<rect x="0" y="0" width="{width}" height="55" fill="#1e222d"/>')
    svg.append(f'<circle cx="30" cy="28" r="7" fill="#2962ff"/>')
    svg.append(f'<text x="50" y="33" fill="#d1d4dc" font-size="16" font-weight="700">EUR/USD • 1H</text>')
    svg.append(f'<text x="180" y="33" fill="#089981" font-size="14" font-weight="600">1.0870 (+0.32%)</text>')
    svg.append(f'<text x="340" y="33" fill="#9598a1" font-size="13">Bài học minh họa: Mô hình nến Pin Bar đảo chiều tại Hỗ trợ (Support)</text>')

    # Support Zone
    supp_top_p = 1.0836
    supp_bot_p = 1.0826
    sy_top = to_y(supp_top_p)
    sy_bot = to_y(supp_bot_p)
    svg.append('<!-- Support Zone -->')
    svg.append(f'<rect x="{m_left}" y="{sy_top:.1f}" width="{chart_w}" height="{sy_bot - sy_top:.1f}" fill="url(#supportGrad)" stroke="#2962ff" stroke-width="1.5" stroke-dasharray="4,4"/>')
    svg.append(f'<rect x="{m_left + 15}" y="{sy_top - 20:.1f}" width="180" height="20" rx="3" fill="#2962ff" fill-opacity="0.8"/>')
    svg.append(f'<text x="{m_left + 22}" y="{sy_top - 6:.1f}" fill="#ffffff" font-size="11" font-weight="600">🛡️ VÙNG HỖ TRỢ (SUPPORT ZONE)</text>')

    # Trade Execution Box (RR 1:2)
    entry_p = 1.0850
    sl_p = 1.0825
    tp_p = 1.0900
    
    t_box_x = candle_coords[5][0] + 15
    t_box_w = candle_coords[-1][0] - t_box_x + 30
    
    y_entry = to_y(entry_p)
    y_sl = to_y(sl_p)
    y_tp = to_y(tp_p)
    
    svg.append('<!-- Trade Box TP / SL -->')
    # Profit Box
    svg.append(f'<rect x="{t_box_x:.1f}" y="{y_tp:.1f}" width="{t_box_w:.1f}" height="{y_entry - y_tp:.1f}" fill="url(#rewardGrad)" stroke="#089981" stroke-width="1" stroke-dasharray="2,2"/>')
    # Risk Box
    svg.append(f'<rect x="{t_box_x:.1f}" y="{y_entry:.1f}" width="{t_box_w:.1f}" height="{y_sl - y_entry:.1f}" fill="url(#riskGrad)" stroke="#f23645" stroke-width="1" stroke-dasharray="2,2"/>')

    # Lines for Entry, SL, TP
    # Entry
    svg.append(f'<line x1="{t_box_x:.1f}" y1="{y_entry:.1f}" x2="{m_right}" y2="{y_entry:.1f}" stroke="#2962ff" stroke-width="2"/>')
    svg.append(f'<rect x="{m_right + 5}" y="{y_entry - 11:.1f}" width="88" height="22" rx="3" fill="#2962ff"/>')
    svg.append(f'<text x="{m_right + 10}" y="{y_entry + 4:.1f}" fill="#ffffff" font-size="10" font-weight="700">ENTRY: 1.0850</text>')
    
    # TP
    svg.append(f'<line x1="{t_box_x:.1f}" y1="{y_tp:.1f}" x2="{m_right}" y2="{y_tp:.1f}" stroke="#089981" stroke-width="2"/>')
    svg.append(f'<rect x="{m_right + 5}" y="{y_tp - 11:.1f}" width="88" height="22" rx="3" fill="#089981"/>')
    svg.append(f'<text x="{m_right + 10}" y="{y_tp + 4:.1f}" fill="#ffffff" font-size="10" font-weight="700">TP (+50p): 1.0900</text>')

    # SL
    svg.append(f'<line x1="{t_box_x:.1f}" y1="{y_sl:.1f}" x2="{m_right}" y2="{y_sl:.1f}" stroke="#f23645" stroke-width="2"/>')
    svg.append(f'<rect x="{m_right + 5}" y="{y_sl - 11:.1f}" width="88" height="22" rx="3" fill="#f23645"/>')
    svg.append(f'<text x="{m_right + 10}" y="{y_sl + 4:.1f}" fill="#ffffff" font-size="10" font-weight="700">SL (-25p): 1.0825</text>')

    # Ratio badge
    badge_x = t_box_x + 10
    badge_y = y_entry - 10
    svg.append(f'<rect x="{badge_x}" y="{badge_y - 18}" width="100" height="20" rx="3" fill="#131722" stroke="#2962ff" stroke-width="1"/>')
    svg.append(f'<text x="{badge_x + 8}" y="{badge_y - 4}" fill="#089981" font-size="11" font-weight="700">Tỷ lệ R:R = 1 : 2</text>')

    # Draw Candlesticks
    svg.append('<!-- Candlesticks -->')
    c_width = 24
    
    for i, (cx, (op, hi, lo, cl, tm)) in enumerate(candle_coords):
        is_bull = cl >= op
        c_color = "#089981" if is_bull else "#f23645"
        
        y_hi = to_y(hi)
        y_lo = to_y(lo)
        y_op = to_y(op)
        y_cl = to_y(cl)
        
        y_top_body = min(y_op, y_cl)
        body_h = max(abs(y_cl - y_op), 2)
        
        # Wick
        svg.append(f'<line x1="{cx:.1f}" y1="{y_hi:.1f}" x2="{cx:.1f}" y2="{y_lo:.1f}" stroke="{c_color}" stroke-width="2"/>')
        
        # Body
        svg.append(f'<rect x="{cx - c_width/2:.1f}" y="{y_top_body:.1f}" width="{c_width}" height="{body_h:.1f}" fill="{c_color}" rx="1"/>')
        
        # Time label on bottom
        svg.append(f'<text x="{cx:.1f}" y="{m_bottom + 25}" fill="#787b86" font-size="11" text-anchor="middle">{tm}</text>')
        
        # Highlight Pinbar (index 5)
        if i == 5:
            # Highlight circle
            svg.append(f'<circle cx="{cx:.1f}" cy="{y_lo - 10:.1f}" r="18" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>')
            # Callout Arrow & Text
            svg.append(f'<path d="M {cx - 30:.1f} {y_lo + 45:.1f} L {cx - 5:.1f} {y_lo + 8:.1f}" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>')
            svg.append(f'<rect x="{cx - 150:.1f}" y="{y_lo + 48:.1f}" width="200" height="42" rx="5" fill="#1e222d" stroke="#f59e0b" stroke-width="1.5" filter="url(#shadow)"/>')
            svg.append(f'<text x="{cx - 140:.1f}" y="{y_lo + 66:.1f}" fill="#f59e0b" font-size="12" font-weight="700">★ Nến PIN BAR RÚT CHÂN</text>')
            svg.append(f'<text x="{cx - 140:.1f}" y="{y_lo + 82:.1f}" fill="#d1d4dc" font-size="10">Râu nến dài từ chối giá tại Support</text>')

    # Footer note
    svg.append(f'<rect x="{m_left}" y="{height - 35}" width="{chart_w}" height="25" rx="4" fill="#1e222d"/>')
    svg.append(f'<text x="{m_left + 15}" y="{height - 18}" fill="#787b86" font-size="11">📌 Quy tắc: Chờ nến Pin Bar đóng cửa kiểm tra vùng hỗ trợ ➔ Mua khi nến tiếp theo phá đỉnh Pin Bar ➔ SL dưới đáy nến ➔ TP tại kháng cự kế tiếp.</text>')

    svg.append('</svg>')
    
    content = '\n'.join(svg)
    
    out_path = '/Users/kyanh/Documents/ForexTut/charts/demo_pinbar.svg'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated SVG: {out_path} ({len(content)} bytes)")

create_svg()
