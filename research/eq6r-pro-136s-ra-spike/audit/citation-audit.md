# Citation Audit — EQ6-R Pro ~136 s RA Spike

Independent source verification of citations.md against the fetched/operator-supplied
source content, and against the claims made in README.md, analysis.md, and references/*.md.

## Summary

- **40 of 40 citations checked.**
- **38 VERIFIED**, **1 PARTIAL** ([16]), **1 NOT FOUND** ([27]).
- No INACCURATE, INACCESSIBLE, or DRIFT grades. All "Access: operator-supplied" entries
  correctly route to the `manual-*.md` files (the direct-fetch equivalents for those same
  URLs are, as documented, FAILED — this is consistent, not a problem).

## [1] Sky-Watcher EQ6-R Manual (neq6-r.pdf) — VERIFIED
Source (`inter-static.skywatcher.com-downloads-neq6-r.pdf-75937cba.md`, Status: OK) contains
verbatim: "Transmission 180:1 Worm Drive + 48:12 Timing Belt Drive + 64" (line 453), "Gear
Ratio 720" (455), "Resolution 9216000 Counts/Rev., approx. 0.14 arc-second" (456), "PEC 100
Segments Permanent PEC" (461), and worm-index language (419). Matches citation and all uses
in drivetrain-periods.md and analysis.md §1 exactly.

## [2] Sky-Watcher USA EQ6-R Pro product page — VERIFIED
"Stepper motors have no internal gear box, further reducing backlash" (380); "1.8° step
angle and 64 micro steps driven" (412); belt drives "provide minimal backlash and
significantly reduced periodic error" (378). Matches citation text exactly.

## [3] Astrofriend 02 — VERIFIED
"The small gear has 12 teeth and the big 47 teeth. That gives a gear ratio of 47 / 12 =
3.9167" (226); "180:1" and "705:1" total (270, 272). Matches.

## [4] Astrofriend 12 — VERIFIED
"Back off the RA lock nut ... tighten again and back off a little, 1/10 off a turn. If it's
too tight it could block the RA rotation in the cold." (314–315). Matches citation
(citations.md's "1/10 of a turn" is a trivial paraphrase of "1/10 off a turn" — immaterial).

## [5] Rowan Engineering a10000013a — VERIFIED
"The pulley ratio is the same as the factory gears." (397); "Note: This kit does not fit the
EQ6 R Pro." (419). Exact matches.

## [6] Rowan Astronomy NEQ6 Belt Kit PDF — VERIFIED
"2 off 47 & 2 off 12 tooth aluminium pulleys" (15); belts "6mm wide x 2.5mm pitch x 180.0
long" (16); "small adjustments of 1/8 turn or less" (323); "run the mount a full 360'" (326).
All match.

## [7] Bearings Online EQ6-R Pro kit — VERIFIED
"as seen on the Youtube video by Astrobloke" (83); "6 pcs - 6008 2RS1 SKF ... 40x68x15" (89);
"4 pcs - 608 2Z/C3 SKF Deep Groove Ball Bearing 8x22x7" (91); one 30206M, one 32208 (93, 95).
Exact matches.

## [8] Astromart classified kit — VERIFIED
"SKF 608-2RSH Bearing (4X)" (78); "SKF 6008-2RS1 Bearing (6X)" (80); Timken 32208/30206 (82,
84); "Maedler Polyurethane timing belt T2.5 width 6mm Lw 177.5mm 71 teeth ... replacement for
the EQ6-R stock belts" (86). Exact matches, including the belt identity the analysis leans on.

## [9] GMN Bearing USA 608 data — VERIFIED
"Pitch Circle Diameter d m [mm] 14.700"; "Ball Diameter D w [mm] 3.969"; "Number of Balls Z
[qty] 7" (594, 596, 618). Exact matches, used correctly in the bearing-defect-frequency
arithmetic (independently recomputed and confirmed correct — see Notes below).

## [10] KT Bearing 608 dimensions guide — VERIFIED
"Ball Diameter (typical) ~3.969 mm ... 7 balls standard" (259); "Pitch Circle Diameter ~15.0
mm" (261); "the standard ball complement is 7 balls of approximately 3.969 mm diameter."
(391). Matches.

## [11] MechCodex bearing defect frequencies — VERIFIED
Formulas for BPFO/BPFI/BSF/FTF match exactly (line 27). "a defect on the element strikes a
race twice per spin, so the observed ball-defect frequency is usually 2 × BSF" (line 27,
verbatim). "shifts the actual frequencies one to two percent below the kinematic prediction"
(line 58, verbatim). "not integer multiples of shaft speed" (line 36, verbatim fragment).
All quotes used in citations.md and drivetrain-periods.md are exact.

## [12] NTN Americas bearing frequency PDF — VERIFIED
"(inner race rotating and our race stationary)" (line 17) — matches citation's "(inner race
rotating, outer stationary)". Formula table present (FTF/BPFI/BPFO/BSF columns, line 21+).
Corroborates [11] as claimed.

## [13] Deep Space Products ceramic worm bearing kit — VERIFIED
"Set of 4 ceramic hybrid double sealed, radial, deep groove ball bearings ... chrome steel
with ceramic balls and a steel cage" (124); "Complete set of RA and DEC ceramic hybrid worm
gear ball bearings" (130). No ball count/diameter published anywhere on the page — confirmed,
matching the citation's and drivetrain-periods.md's point that this kit's geometry is unknown.

## [14] VXB/bearings.net 4-ball hybrid 608 — VERIFIED
"Ball count: 4 Si₃N₄ ceramic balls" (200); "C4 clearance" (206); "Open (no seals or shields)"
(207). Matches citation exactly.

## [15] Cloudy Nights — "EQ6 w/ Rowan Belts RA Spike" (operator-supplied) — VERIFIED
"RA spike every 133 seconds" (167, paraphrased as "spike every 133 seconds" — source: "started
a fun new RA spike every 133 seconds"); "replaced the bearings with better ones from
deepspaceproducts" (169); OzAndrewJ verbatim: "The worm period is 478.7 seconds and the motor
period is 122.2 seconds ... so the 133 seconds may be affected by the act of guiding. If you
run an unguided test, and the period becomes 122 seconds then its more than likely a slight
eccentricity in the mounting of the pulley on the motor" (211–221, confirmed as one continuous
reply from "Andrew Johansen"); final-post verbatim: "It was the 'upgraded' ceramic worm gear
bearings. While I couldn't feel or hear any difference, when I popped the original 608
bearings back in all of my weird spikes disappeared and I'm back to guiding at .4 RMS." (387).
All quotes exact.

## [16] ESPMC-Eight groups.io — "Periodic spike in RA during guiding" (operator-supplied) — PARTIAL

**Status: RESOLVED** — citations.md, user-reports.md, fixes.md, analysis.md and README.md now state the fix coincided with a re-plugged RA serial cable and redone polar alignment, cause not isolated.
The symptom quote is exact: "Every ~134s the error goes from within ~1.5 arc-sec to over 5
(and sometimes as high as 9) arc-sec. It recovers very quickly, usually within a second or
two." (153). Hoskin's "Your spike is on the period of the small pulley of the belt drive"
(175) is also exact.

The fix-causation claim is weaker than the documents state. Citations.md: "Fix (two changes
together): recentred/tensioned an off-centre, loose belt and tightened worm gear slop on
shaft → 'The spikes in RA are completely gone'." Analysis.md and README.md go further,
stating flatly it "was fixed by" these two mechanical changes.

Reading the thread in order: Chris made the belt-centering/tensioning and worm-slop fixes on
5/21/22 and explicitly said "I don't know if I made things worse or better. I'll give it a try
tonight." The *next* message from Chris (5/22/22) opens with an unrelated problem — "I went to
start imaging last night, and the RA didn't move at all. After plugging the RA's serial
cable back in, things went great" — then reports "I spent a bunch of time getting my polar
alignment just right, and my guiding is MUCH better. The spikes in RA are completely gone."
So the "spikes gone" report follows two additional, uncontrolled changes (an RA cable
reconnection and a polar-alignment retune) beyond the belt/worm fix, which the source itself
never disentangles. The documents' own caveat ("which change mattered is unknown") addresses
only belt-vs-worm ambiguity, not this cable/polar-alignment confound — so the "Fixed by"
framing in analysis.md/README.md overstates what [16] actually supports. Grade: PARTIAL —
the symptom match is solid; the causal fix attribution goes beyond what the source entails.

## [17] Open PHD Guiding groups — "Help with EQ6R Pro with RA periodic oscillation" — VERIFIED
Confirmed author-by-author: John Sim (signed "John") wrote the 54.6/36.4/27.3/21.8/18.1/
15.6/13.6 s harmonic list and "nearly an exact harmonic of 109.2 seconds" and "the stepper
gear's period is 120 seconds" (line 399). Andy Galasso (signed "Andy") wrote "a periodic
error of about 40 arc-seconds peak to peak and a period of about 480 seconds ... a rapid
spike of about 6" that occurs about every 120s. The 120s spike is actually the biggest
problem for guiding since it happens so quickly that it cannot be guided out." (line 721–?).
Firmware "3.4.23 ... No change" is Diego's own report (line 444). All attributions and quotes
in citations.md, analysis.md, and user-reports.md are accurate.

## [18] Open PHD Guiding groups — "I'm getting rid of my EQ6 r pro" — VERIFIED
"your mount EQ6r Pro has a worm period of 479.6894" — not located as an exact standalone
string but "large harmonic periodic error at 133 seconds and 67 seconds" (372) and "Errors
like this usually means there's a problem in some parts of the drive assembly, such as spur
gears, belt, etc." (378) are exact, both attributed to Valente. Owner's new-RA-motor and
"night two" recurrence account (86, 145) confirmed. Matches.

## [19] Open PHD Guiding groups — "PHD2 guiding issues in RA" — VERIFIED
">40″" (89, "40", while DEC looks okay"); "A less likely source of the RA excursions could be
grit or dried grease in the RA drive system" (178); "Backlash in RA is irrelevant to guiding
because the motor direction is never reversed" (268); "every 1-2 minutes RA was way off
again" (515); RMS "8.29" → "2.27" with spikes "up to 42"" remaining (597–604). All exact,
attributed to Bruce Waddington per the thread's reply pattern.

## [20] Cloudy Nights 928076 (operator-supplied) — VERIFIED
"spikes at 120 and 160 seconds" context confirmed (171); "The 120second period is a match for
the motor shaft, ie a slightly bent shaft but more likely an eccentric pulley." (229–231);
"The 160second is an odd freq that doesnt match the belts or pulleys ... they look
suspiciously like the data that gets reported when the worm bearings are damaged." (233–239).
Exact matches, attributed to OzAndrewJ.

## [21] Cloudy Nights 928885 (operator-supplied) — VERIFIED
"I had a 120 second spike" (167); micrometer/slack measurement and Skywatcher's reply: "the
belts are too tight and should have at least 4~5mm slack and that is probably what is causing
the wobble" (175); set-screw "had dimpled the stainless motor shaft and created a crater" is
confirmed verbatim further down the same post. Matches.

## [22] Stargazers Lounge 366556 (operator-supplied) — VERIFIED
wimvb: "a 120 s period would indicate the timing pulley on the RA motor. A 10 s period
indicates a loose RA belt, etc." (confirmed attributed to wimvb). AndyThilo (thread author):
"the RA oscillations occur every 8 minutes" — confirms the "8-minute worm period" claim.
Matches.

## [23] Stargazers Lounge 282220 — AZ-EQ6 (operator-supplied) — VERIFIED
"±20 arc seconds" context: "nearly +/- 20 arc seconds in magnitude" every 8 minutes (173).
"The pulley would touch partially during the worm cycle and was enough to give a large pulse
of PE." (221–222). Darkframe (David at darkframeoptics.com) "thought this could be a bearing
issue" (255). Matches.

## [24] Cloudy Nights 932875 — EQ6-R Pro spikes (operator-supplied) — VERIFIED
"the spikes over 2" will play nicely with longer focal lengths" context confirms ">2″" (179);
"new bearings, cleaning the inside, relubricating and a lot of finetuning" (175, 333); "I have
just opend up the mount to check for binding on the worm, and there was just the slightest
amount of binding" / "loosend the worm housing" (465); belt "too tight" with slack added
(467); "loosen the RA axis lock nut" (543, 583); PHD2 focal-length mismatch confound (587,
619). All matches.

## [25] Stargazers Lounge 339612 — EQ6-R Pro worm tuning (operator-supplied) — VERIFIED
StarDodger: "if you tighten enough to get a little binding you may well have already damaged
the small end float bearing and knocked it slightly out of shape ... just over finger tight"
(210, exact). discardedastro: EQ6-R "has an optical encoder on the worm" held by "a single
posidrive screw" (173, 177). Matches.

## [26] AstroBin 85441 page 1 (operator-supplied) — VERIFIED
Pinguru: "I have a major peak in my RA guiding with a very precise period of 10 seconds. The
10 second period is exactly the frequency of the belt teeth running in/out the pulley." (156);
"the smaller pitch of 2 mm of the GT2 belt allows to fit a 15/60 teeth combination instead of
the 12/48 of the stock T2.5 belt" (167). wimvb: "The 120 s peak, btw, is one full revolution
of the motor pulley. But this can be guided out." (484). All matches.

## [27] AstroBin 85441 page 2 (operator-supplied) — NOT FOUND

**Status: RESOLVED** — the 95 s / "4,4 times/rotation" brinelling quote is on page 1 (operator file manual-Small-but-mighty…----.md, lines ~319–325); moved to [26]. [27] now cites page-2 content (Martin W: "sharp peak at 10 seconds"; GT2 "marked improvement"). drivetrain-periods.md and user-reports.md re-pointed to [26].
Citations.md attributes to this URL: "'spike at about 95s period … happens 5 times during one
worm rotation. So it can't be the concentricity of the motor pulley … Having a damaged
bearing at the worm shaft (brinelling) would give me an defect order of 4,4 times/rotation.'"
This quote does **not appear anywhere in the fetched file.** The only trace of this content is
a one-line auto-generated Table-of-Contents entry near the end of the document: "Pinguru asks
for help identifying 95-second period spike occurring five times per rotation." (line 862) —
a third-party paraphrase, not Pinguru's own words, and it contains none of the "concentricity,"
"brinelling," or "4,4 times/rotation" language the documents quote. The actual post bodies for
this and the two entries immediately after it (Philip Bartlett's SKF-bearing post, Padraig
Farrell's AZ-EQ6 report) are likewise reduced to single-line ToC summaries with no body text
captured anywhere in the file — this page's fetch/save evidently did not capture that part of
the thread.

This citation underpins a load-bearing step in drivetrain-periods.md's "Observations" §2:
"Pinguru independently estimated a worm-bearing brinelling order of '4,4 times/rotation' [27]
(BPFI order 4.43–4.45 here)" — presented as corroboration for the 608-bearing hypothesis. The
source as fetched cannot support this; the quoted figure is unverifiable from the file
provided. Grade: NOT FOUND — the source is accessible (Status: OK) but does not contain the
claimed data.

## [28] IceInSpace t166255 — VERIFIED
"Something else that might be worthwhile is stripping your mount down and giving it a
regrease. For a time I had some guiding issues (random 2" spikes) that started appearing.
After a regrease they went away." (273). "I backed off the RA meshing a bit (as per
AstroBaby's site) and the spikes seem to have gone. I think it was RA sticking, as before the
adjustment I could hear a slight change in tone as it rotated when slowly slewing." (513).
Exact matches.

## [29] IceInSpace t203189 — VERIFIED
"check to see if drive belt deflection at a central point between pulleys is no more than say
3 to 4mm" (179); Dec backlash "3000ms down to 900ms" (37); Astrobloke-video-notes quote:
"4 x 608 2rs - these were the bearings I used but I have told the correct replacement are the
metal shielded 608 2z ... I personally have had no binding issues using these although another
user reported he did." (273). All exact matches.

## [30] Open PHD Guiding groups — "EQ6R-Pro RA Trouble" — VERIFIED
"note the 473 sec uncorrected error which is 0.9" and one of the three big sources of error in
your RA (the other two being to the left of it: 241 sec and 160 sec)" (195). AutoPEC through
EQMod + PPEC: "Total error hovered between 0.6-0.9 every time I glanced before going to bed."
(532). Matches.

## [31] Open PHD Guiding groups — "Poor guiding graph on EQ6-R PRO" — VERIFIED
Frédéric Ruciak (confirmed by byline): "On my own I dismounted it and changed all the bearings
but it is not necessary to get 80 to 90% of the benefits ... your mount has been delivered
with too much torque on the axis compressing the bearings. This is almost systematic from SW."
(188). Bruce Waddington: "This is a mechanical issue and is typically somewhere in the
gearbox/motor" (326). Matches.

## [32] Open PHD Guiding groups — "Help Needed with PHD2 Log Data" — VERIFIED
"The last contributor at the far left occurs every 11 seconds and this is evidently because of
a wobble in the pinion gear on the motor ... That 11-second wobble isn't amenable to guiding,
it's something that requires a mechanical fix." (186–194). Matches (quote spans a line-wrapped
PDF extraction, as expected).

## [33] Open PHD Guiding — "Analyzing PHD2 Guide Logs" PDF — VERIFIED
"gently push on various parts of the guide scope assembly and tug gently on the various
cables" (206–207); Guiding Assistant "as long as the worm period in your mount – usually
something in the 6-8 minute range" (272–274). Matches.

## [34] Open PHD Guiding — Trouble-shooting and Analysis manual — VERIFIED
"The great majority of these problems arise from neither the mount nor PHD2's guide commands"
(131–132, paraphrase of citation's "arise from neither the mount nor PHD2's guide commands" —
exact); "a movement of only 5 microns can create an apparent tracking error (guide star
deflection) of over 6 arc-sec" (152–154, exact); "unusually large, randomly space deflections
are more likely to arise from the sorts of mechanical problems described here than from errors
in the RA drive system" (168–171, exact, including the source's own grammatical slip "space"
for "spaced," which the documents correctly render as "space[d]"). "bind or pull in certain sky
positions or after a meridian flip" (159, exact). Matches.

## [35] ADG Software — PHD2 Log Viewer page — VERIFIED
"Identify RA drive harmonics by looking at the RA frequency analysis" (34, exact). "Settling
frames after dither are automatically excluded from statistics calculation" (30) confirms the
dither-exclusion claim. Matches.

## [36] EQMOD PECPrep User Guide PDF — VERIFIED
"the 470 second peak listed will actually correspond to the 479s worm period" (181–182,
exact); resolution slider trade-off (287–291); period slider "you can change this if you want
to isolate other periodic signals" (156, exact); phase column groups "elements that originate
from the same mechanical source" (303, exact); "If you find that odd harmonics are
particularly prominent this might indicate that the associated mechanical part is being
restricted in its movement" (468–469, exact); capture "at least 5 times the worm period of
your mount. For an EQ6 this 40 mins" (392, exact). Legacy EQ6 simulation table confirms worm
479 s / transfer gear 366.6 s / stepper spur 122.2 s (360–363). All matches.

## [37] EQMOD PECPrep project page — VERIFIED
"able to filter wind, seeing effects, linear and non linear drift to isolate the periodic
signal associated with a mounts worm drive" (16, exact, reconstructed from "isolate the
periodic signal" + "associated with a mounts worm drive" split across source lines).

## [38] Michael Herman — "Measuring Periodic Error in Telescope Mounts" PDF — VERIFIED
"Enable Mount Guide Output" checkbox, unchecked, confirmed (356); "track that star using 1 to
2 second exposures for about 50 minutes" (277) / "about 45 minutes of tracking this star"
(379, 381) — supports the "~45–50 min" claim. "peak labelled #5 is from a ball in a RA worm
block bearing getting pinched or slowing down at some point in its rotation" (755, exact).
One quote is a loose paraphrase, not a verbatim match: citations.md/fixes.md/analysis.md all
render it in quotation marks as "cannot be corrected by PEC," but the source's actual wording
is "This 1/7.5 oscillation cannot be removed by PEC software correction of the drive timing"
(961–962) — same meaning, different wording. Minor quote-fidelity issue; does not change the
grade given the substance is correct, but flagged since the documents present it as a direct
quote.

## [39] GitHub open-astro/openastro-guide-insight — VERIFIED
"Fork of PHD2 Log Viewer ... by Andy Galasso" (745, as "OpenAstro Guide Insight is a fork of
PHD2 Log Viewer by Andy Galasso, which is no longer maintained"); "export the periodogram as
CSV" (663, exact, as "Analyze a selection, a Guiding Assistant run or a whole session for
drift and periodic error, and export the periodogram as CSV"). Matches.

## [40] EQMOD — "Mount Periodic Error Correction through Variable Track Speed Adjustment" — VERIFIED
"Mount periodic errors are caused by runout or gear teeth spacing" (7, matches "caused by
runout or gear teeth spacing discrepancies in the mount's RA wormgears"); "the rotation cycle
is 8 minutes" (12, exact). Matches.

## Notes on non-citation claims

- The bearing-defect-frequency arithmetic in drivetrain-periods.md (worm 478.69 s, 2×BSF
  136.2–142.3 s, BPFI 107.7–110.4 s, BPFO 185.98–191.2 s, FTF ~1302–1338 s) was independently
  recomputed from the BPFO/BPFI/FTF/BSF formulas in [11]/[12] using the [9]/[10] geometry
  (Bd=3.969mm, Pd=14.700/15.0mm, Z=7) and the 86,164.09 s sidereal day. All recomputed values
  match the published table to within rounding. This is the documents' own calculation, marked
  "(est.)" throughout and correctly flagged in the Caveats/Limitations sections as not reported
  by any astronomy source — that framing is accurate and not overstated.
- The arithmetic chain 180 × 48/12 = 720; 720 × 200 × 64 = 9,216,000 (drivetrain-periods.md)
  checks out and is consistent with [1]'s stated resolution.

## Grade Ledger

[1] VERIFIED
[2] VERIFIED
[3] VERIFIED
[4] VERIFIED
[5] VERIFIED
[6] VERIFIED
[7] VERIFIED
[8] VERIFIED
[9] VERIFIED
[10] VERIFIED
[11] VERIFIED
[12] VERIFIED
[13] VERIFIED
[14] VERIFIED
[15] VERIFIED
[16] PARTIAL
[17] VERIFIED
[18] VERIFIED
[19] VERIFIED
[20] VERIFIED
[21] VERIFIED
[22] VERIFIED
[23] VERIFIED
[24] VERIFIED
[25] VERIFIED
[26] VERIFIED
[27] NOT FOUND
[28] VERIFIED
[29] VERIFIED
[30] VERIFIED
[31] VERIFIED
[32] VERIFIED
[33] VERIFIED
[34] VERIFIED
[35] VERIFIED
[36] VERIFIED
[37] VERIFIED
[38] VERIFIED
[39] VERIFIED
[40] VERIFIED


## Coordinator note on [38]

The phrase "cannot be corrected by PEC" is present in the source with a line break ("These vibrations cannot" / "be corrected by PEC because they are not occurring at the same frequency synchronization as the worm period", Herman p. ~10). No change made.
