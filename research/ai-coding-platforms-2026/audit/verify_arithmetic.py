"""Arithmetic verification script for real-cost-at-typical-usage.md consistency review."""

print('=== WORKED EXAMPLE 1: 90/10, all Sonnet 4.6 ===')
total_tokens = 49.8e6
input_frac = 0.90
output_frac = 0.10
cache = 32.6e6

input_tokens = total_tokens * input_frac
output_tokens = total_tokens * output_frac

sonnet_input = 3.0   # /M
sonnet_output = 15.0 # /M
sonnet_cache_read = 0.30 # /M

cost_input = (input_tokens / 1e6) * sonnet_input
cost_output = (output_tokens / 1e6) * sonnet_output
cost_cache = (cache / 1e6) * sonnet_cache_read

print(f'  Input: {input_tokens/1e6:.2f}M x $3 = ${cost_input:.2f}')
print(f'  Output: {output_tokens/1e6:.2f}M x $15 = ${cost_output:.2f}')
print(f'  Cache: {cache/1e6:.2f}M x $0.30 = ${cost_cache:.2f}')
total = cost_input + cost_output + cost_cache
print(f'  Total = ${total:.2f}')
print(f'  Rounded = ${round(total):.0f}')
print()

print('=== WORKED EXAMPLE 2: 80/20, all Sonnet 4.6 ===')
input_frac2 = 0.80
output_frac2 = 0.20
input_tokens2 = total_tokens * input_frac2
output_tokens2 = total_tokens * output_frac2
cost_input2 = (input_tokens2 / 1e6) * sonnet_input
cost_output2 = (output_tokens2 / 1e6) * sonnet_output
cost_cache2 = (cache / 1e6) * sonnet_cache_read
total2 = cost_input2 + cost_output2 + cost_cache2
print(f'  Input: {input_tokens2/1e6:.2f}M x $3 = ${cost_input2:.2f}')
print(f'  Output: {output_tokens2/1e6:.2f}M x $15 = ${cost_output2:.2f}')
print(f'  Cache: ${cost_cache2:.2f}')
print(f'  Total = ${total2:.2f}, Rounded = ${round(total2):.0f}')
print()

print('=== WORKED EXAMPLE 3: 70/30, all Sonnet 4.6 ===')
input_frac3 = 0.70
output_frac3 = 0.30
input_tokens3 = total_tokens * input_frac3
output_tokens3 = total_tokens * output_frac3
cost_input3 = (input_tokens3 / 1e6) * sonnet_input
cost_output3 = (output_tokens3 / 1e6) * sonnet_output
cost_cache3 = (cache / 1e6) * sonnet_cache_read
total3 = cost_input3 + cost_output3 + cost_cache3
print(f'  Total = ${total3:.2f}, Rounded = ${round(total3):.0f}')
print()

print('=== ALL OPUS 4.7: 90/10, 80/20, 70/30 ===')
opus_input = 5.0
opus_output = 25.0
opus_cache_read = 0.50

for split_label, if_, of_ in [('90/10', 0.9, 0.1), ('80/20', 0.8, 0.2), ('70/30', 0.7, 0.3)]:
    it = total_tokens * if_
    ot = total_tokens * of_
    ci = (it / 1e6) * opus_input
    co = (ot / 1e6) * opus_output
    cc = (cache / 1e6) * opus_cache_read
    tot = ci + co + cc
    print(f'  {split_label}: ${tot:.2f} -> Rounded ${round(tot):.0f}')
print()

print('=== 50/50 OPUS+SONNET MIX: 80/20 (Worked Example 2 from doc) ===')
input_tokens_80 = total_tokens * 0.80
output_tokens_80 = total_tokens * 0.20

sonnet_full = (input_tokens_80/1e6)*3 + (output_tokens_80/1e6)*15 + (cache/1e6)*0.30
opus_full = (input_tokens_80/1e6)*5 + (output_tokens_80/1e6)*25 + (cache/1e6)*0.50
total_mix = sonnet_full/2 + opus_full/2

print(f'  Half of sonnet 80/20 total: half of ${sonnet_full:.2f} = ${sonnet_full/2:.2f}')
print(f'  Half of opus 80/20 total: half of ${opus_full:.2f} = ${opus_full/2:.2f}')
print(f'  Sum = ${total_mix:.2f}, Rounded = ${round(total_mix):.0f}')
print()
print(f'  Doc says: sonnet total = 278.70 -> computed = {sonnet_full:.2f}')
print(f'  Doc says: opus total = 465.50 -> computed = {opus_full:.2f}')
print()

print('=== 50/50 MIX: all splits ===')
for split_label, if_, of_ in [('90/10', 0.9, 0.1), ('80/20', 0.8, 0.2), ('70/30', 0.7, 0.3)]:
    it = total_tokens * if_
    ot = total_tokens * of_
    s = (it/1e6)*3 + (ot/1e6)*15 + (cache/1e6)*0.30
    o = (it/1e6)*5 + (ot/1e6)*25 + (cache/1e6)*0.50
    t = (s + o) / 2
    print(f'  {split_label}: ${t:.2f} -> Rounded ${round(t):.0f}')
print()

print('=== GPT-5.4 rates ===')
# GPT-5.4: $2.50/$0.25/$15
gpt54_input = 2.50
gpt54_output = 15.0
gpt54_cache = 0.25

for split_label, if_, of_ in [('90/10', 0.9, 0.1), ('80/20', 0.8, 0.2), ('70/30', 0.7, 0.3)]:
    it = total_tokens * if_
    ot = total_tokens * of_
    ci = (it/1e6) * gpt54_input
    co = (ot/1e6) * gpt54_output
    cc = (cache/1e6) * gpt54_cache
    tot = ci + co + cc
    print(f'  GPT-5.4 {split_label}: ${tot:.2f} -> Rounded ${round(tot):.0f}')
print()

print('=== Cursor Composer 2 rates ===')
# Composer 2: $0.50/$0.20/$2.50
c2_input = 0.50
c2_output = 2.50
c2_cache = 0.20

for split_label, if_, of_ in [('90/10', 0.9, 0.1), ('80/20', 0.8, 0.2), ('70/30', 0.7, 0.3)]:
    it = total_tokens * if_
    ot = total_tokens * of_
    ci = (it/1e6) * c2_input
    co = (ot/1e6) * c2_output
    cc = (cache/1e6) * c2_cache
    tot = ci + co + cc
    print(f'  Composer 2 {split_label}: ${tot:.2f} -> Rounded ${round(tot):.0f}')
print()

print('=== MONTHLY EXTRAPOLATION: x30/13 ===')
factor = 30.0 / 13.0
print(f'  Factor = {factor:.4f}')

table_13day = {
    'All Sonnet 4.6 90/10': 219,
    'All Sonnet 4.6 80/20': 279,
    'All Sonnet 4.6 70/30': 339,
    'All Opus 4.7 90/10': 366,
    'All Opus 4.7 80/20': 466,
    'All Opus 4.7 70/30': 566,
    '50/50 90/10': 293,
    '50/50 80/20': 373,
    '50/50 70/30': 453,
    'All GPT-5.4 90/10': 194,
    'All GPT-5.4 80/20': 244,
    'All GPT-5.4 70/30': 294,
    'All Composer 2 90/10': 42,
    'All Composer 2 80/20': 52,
    'All Composer 2 70/30': 63,
}

monthly_doc = {
    'All Sonnet 4.6 90/10': 505,
    'All Sonnet 4.6 80/20': 644,
    'All Sonnet 4.6 70/30': 782,
    'All Opus 4.7 90/10': 844,
    'All Opus 4.7 80/20': 1075,
    'All Opus 4.7 70/30': 1306,
    '50/50 90/10': 675,
    '50/50 80/20': 861,
    '50/50 70/30': 1045,
    'All GPT-5.4 90/10': 448,
    'All GPT-5.4 80/20': 563,
    'All GPT-5.4 70/30': 678,
    'All Composer 2 90/10': 97,
    'All Composer 2 80/20': 120,
    'All Composer 2 70/30': 145,
}

print()
print('Monthly extrapolation check (13-day x 2.308):')
for key in table_13day:
    expected_monthly = round(table_13day[key] * factor)
    doc_monthly = monthly_doc.get(key, 'N/A')
    diff = abs(expected_monthly - doc_monthly) if doc_monthly != 'N/A' else 'N/A'
    flag = '*** MISMATCH ***' if isinstance(diff, int) and diff > 2 else ''
    print(f'  {key}: 13d=${table_13day[key]} x{factor:.3f} = ${expected_monthly} (doc says ${doc_monthly}) {flag}')
print()

print('=== Opus/Sonnet 5/3 ratio check ===')
# input: Opus $5 / Sonnet $3 = 1.667x
# output: Opus $25 / Sonnet $15 = 1.667x
# cache: Opus $0.50 / Sonnet $0.30 = 1.667x
print(f'  Input ratio Opus/Sonnet: {5/3:.4f} (should be 1.6667)')
print(f'  Output ratio Opus/Sonnet: {25/15:.4f} (should be 1.6667)')
print(f'  Cache ratio Opus/Sonnet: {0.50/0.30:.4f} (should be 1.6667)')
print()

# Spot check cells from the table
print('Spot check: Opus 4.7 90/10 should be 5/3 x Sonnet 90/10 = 5/3 x 219 =', round(219 * 5/3))
print('Spot check: Opus 4.7 80/20 should be 5/3 x Sonnet 80/20 = 5/3 x 279 =', round(279 * 5/3))
print('Spot check: Opus 4.7 70/30 should be 5/3 x Sonnet 70/30 = 5/3 x 339 =', round(339 * 5/3))
print()
print('Doc says Opus 4.7 90/10 = 366, 80/20 = 466, 70/30 = 566')
print('But cache is different: Sonnet cache $0.30, Opus cache $0.50, ratio 0.50/0.30 =', round(0.50/0.30, 4))
print('So ratio is not exactly 5/3 due to cache component...')
print()

# More precise check: compute exact ratio
for split_label, if_, of_ in [('90/10', 0.9, 0.1), ('80/20', 0.8, 0.2), ('70/30', 0.7, 0.3)]:
    it = total_tokens * if_
    ot = total_tokens * of_
    s_exact = (it/1e6)*3 + (ot/1e6)*15 + (cache/1e6)*0.30
    o_exact = (it/1e6)*5 + (ot/1e6)*25 + (cache/1e6)*0.50
    ratio = o_exact / s_exact
    print(f'  {split_label}: Sonnet exact = ${s_exact:.4f}, Opus exact = ${o_exact:.4f}, ratio = {ratio:.4f}')
