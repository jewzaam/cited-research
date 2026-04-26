// Arithmetic verification for real-cost-at-typical-usage.md consistency review
const total = 49.8e6;
const cache = 32.6e6;

function cost(if_, of_, irate, orate, crate) {
  return (total*if_/1e6)*irate + (total*of_/1e6)*orate + (cache/1e6)*crate;
}

// Worked example 1: 90/10, all Sonnet 4.6
var s_90 = cost(0.9, 0.1, 3, 15, 0.30);
console.log('=== 90/10 Sonnet 4.6 ===');
console.log('Input:', (49.8*0.9).toFixed(2)+'M x 3 =', (49.8*0.9*3).toFixed(2));
console.log('Output:', (49.8*0.1).toFixed(2)+'M x 15 =', (49.8*0.1*15).toFixed(2));
console.log('Cache:', (32.6*0.3).toFixed(2));
console.log('Total:', s_90.toFixed(4), '-> Rounded', Math.round(s_90));

// 80/20 Sonnet
var s_80 = cost(0.8, 0.2, 3, 15, 0.30);
console.log('\n=== 80/20 Sonnet 4.6 ===');
console.log('Input:', (49.8*0.8).toFixed(2)+'M x 3 =', (49.8*0.8*3).toFixed(2));
console.log('Output:', (49.8*0.2).toFixed(2)+'M x 15 =', (49.8*0.2*15).toFixed(2));
console.log('Total:', s_80.toFixed(4), '-> Rounded', Math.round(s_80));

// 70/30 Sonnet
var s_70 = cost(0.7, 0.3, 3, 15, 0.30);
console.log('\n=== 70/30 Sonnet 4.6 ===');
console.log('Total:', s_70.toFixed(4), '-> Rounded', Math.round(s_70));

// All Opus 4.7
console.log('\n=== Opus 4.7 ===');
[[0.9,0.1,'90/10'],[0.8,0.2,'80/20'],[0.7,0.3,'70/30']].forEach(([if_,of_,lbl]) => {
  var v = cost(if_, of_, 5, 25, 0.50);
  console.log(lbl+':', v.toFixed(4), '-> Rounded', Math.round(v));
});

// 50/50 mix 80/20
console.log('\n=== 50/50 Mix 80/20 ===');
var s_full = cost(0.8, 0.2, 3, 15, 0.30);
var o_full = cost(0.8, 0.2, 5, 25, 0.50);
console.log('Sonnet full:', s_full.toFixed(2), '/ 2 =', (s_full/2).toFixed(2));
console.log('Opus full:', o_full.toFixed(2), '/ 2 =', (o_full/2).toFixed(2));
var mix80 = s_full/2 + o_full/2;
console.log('Sum:', mix80.toFixed(2), '-> Rounded', Math.round(mix80));

// 50/50 mix all splits
console.log('\n=== 50/50 Mix all splits ===');
[[0.9,0.1,'90/10'],[0.8,0.2,'80/20'],[0.7,0.3,'70/30']].forEach(([if_,of_,lbl]) => {
  var s = cost(if_, of_, 3, 15, 0.30);
  var o = cost(if_, of_, 5, 25, 0.50);
  var t = (s+o)/2;
  console.log(lbl+':', t.toFixed(4), '-> Rounded', Math.round(t));
});

// GPT-5.4
console.log('\n=== GPT-5.4 (input $2.50, output $15, cache $0.25) ===');
[[0.9,0.1,'90/10'],[0.8,0.2,'80/20'],[0.7,0.3,'70/30']].forEach(([if_,of_,lbl]) => {
  var v = cost(if_, of_, 2.50, 15, 0.25);
  console.log(lbl+':', v.toFixed(4), '-> Rounded', Math.round(v));
});

// Composer 2
console.log('\n=== Cursor Composer 2 (input $0.50, output $2.50, cache $0.20) ===');
[[0.9,0.1,'90/10'],[0.8,0.2,'80/20'],[0.7,0.3,'70/30']].forEach(([if_,of_,lbl]) => {
  var v = cost(if_, of_, 0.50, 2.50, 0.20);
  console.log(lbl+':', v.toFixed(4), '-> Rounded', Math.round(v));
});

// Monthly x30/13
var factor = 30/13;
console.log('\n=== Monthly factor =', factor.toFixed(4));
var table13 = {
  'Sonnet 90/10': 219, 'Sonnet 80/20': 279, 'Sonnet 70/30': 339,
  'Opus 90/10': 366, 'Opus 80/20': 466, 'Opus 70/30': 566,
  'Mix 90/10': 293, 'Mix 80/20': 373, 'Mix 70/30': 453,
  'GPT54 90/10': 194, 'GPT54 80/20': 244, 'GPT54 70/30': 294,
  'C2 90/10': 42, 'C2 80/20': 52, 'C2 70/30': 63,
};
var docMonthly = {
  'Sonnet 90/10': 505, 'Sonnet 80/20': 644, 'Sonnet 70/30': 782,
  'Opus 90/10': 844, 'Opus 80/20': 1075, 'Opus 70/30': 1306,
  'Mix 90/10': 675, 'Mix 80/20': 861, 'Mix 70/30': 1045,
  'GPT54 90/10': 448, 'GPT54 80/20': 563, 'GPT54 70/30': 678,
  'C2 90/10': 97, 'C2 80/20': 120, 'C2 70/30': 145,
};
Object.keys(table13).forEach(k => {
  var computed = Math.round(table13[k] * factor);
  var doc = docMonthly[k];
  var diff = Math.abs(computed - doc);
  console.log(k+': 13d='+table13[k]+' x'+factor.toFixed(3)+'='+computed+' doc='+doc, diff>2?'*** MISMATCH ***':'OK');
});

// Ratio check
console.log('\n=== Opus/Sonnet ratio check ===');
console.log('Input ratio:', (5/3).toFixed(4));
console.log('Output ratio:', (25/15).toFixed(4));
console.log('Cache ratio:', (0.50/0.30).toFixed(4));
console.log('All = 1.6667 (5/3) - true');
// But the cache/non-cache mix differs...
// compute actual ratio
[[0.9,0.1,'90/10'],[0.8,0.2,'80/20'],[0.7,0.3,'70/30']].forEach(([if_,of_,lbl]) => {
  var s = cost(if_, of_, 3, 15, 0.30);
  var o = cost(if_, of_, 5, 25, 0.50);
  console.log(lbl+' actual ratio:', (o/s).toFixed(4), '(all rates are 5/3 so should be exactly 5/3 = 1.6667)');
});
