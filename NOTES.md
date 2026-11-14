# NOTES — news-image-01 v2 research (Fri 13 Nov 2026)

v2 builds on the v1 research (same day, same sources) and adds the
stories v1 cut for space plus the stories the house's own early-day
images covered (BBC World + Al Jazeera RSS, ~09:20Z 13 Nov, listed in
the kit's competition.yaml). All events happened or were first reported
on Friday 13 November 2026 (any time zone).

## Stories carried over from v1 (verified 14 Nov ~03:20–03:35 WIB)

- **Microsoft 365 outage, day 2 (LEAD):** began Thu 12 Nov ~16:17 UTC,
  into its second day Fri 13 Nov; Outlook, Teams, Copilot, SharePoint,
  OneDrive affected; Downdetector ~140,000 Outlook reports at peak from
  74 countries; ~430M users; Microsoft: no indication of malicious
  activity. Sources: People.com, Malwarebytes, CybersecurityNews.
- **Huang resigns:** announced Thu 12 Nov, effective immediately, after
  33 years; CFO Colette Kress, 59, interim CEO; Harvey C. Jones named
  first-ever board chair; shares fell >13%. Sources: USA Today (Nov 12),
  SEC Form 8-K Exhibit 99.1 (Nov 12).
- **Hormuz tanker attacks:** Thu 12 Nov (Reuters, Dubai) four oil
  tankers hit; Fri 13 Nov IRGC Navy said an LNG carrier struck a naval
  mine on an "unauthorised and dangerous route". Reuters could not
  verify. Sources: Reuters (Nov 12 + Nov 13), PressTV, UKMTO.
- **Ukraine talks:** Russia agreed to European participation in the next
  round; announced by US envoys Kushner and Witkoff after meeting Putin
  in Moscow and Zelenskyy near Dublin; planned prisoner exchange
  potentially the war's largest; Putin reiterated demands NATO reduce
  its military presence in Central/Eastern Europe; deadly Russian drone
  strikes in Odesa and Sumy the same day; France promoting further
  sanctions; UK sanctions on Russian oil producers. Sources: AP, Zark
  News, Open Chronicle (Nov 13 briefings).
- **Brooklyn collapse:** three-storey building at 1321 Flatbush Avenue
  fell ~4pm Wed 11 Nov; search ended Thu; final toll 8 dead incl. two
  children and two construction workers, 18 injured; city to check 100
  linked sites. Source: Zark News daily briefing Nov 13.
- **Pope Leo in Peru:** met six survivors of sexual abuse by Catholic
  clergy in Lima; record crowds. Source: Zark News daily briefing.
- **Storm Charles:** severe weather hit mainland Portugal; schools and
  nonessential public services closed. Source: Open Chronicle.
- **IEA oil surplus:** world oil supply forecast to average 105m b/d in
  Q4 2026, exceeding demand by 1.7m b/d. Source: The Raisina Post,
  13 Nov (IEA statement Fri).
- **Measles ruling:** PAHO expert commission reviewing genetic evidence
  on whether measles circulated continuously for at least a year in the
  US and Mexico; formal ruling awaited. Source: The Raisina Post.
- **Van Hollen vs Schumer:** Sen. Chris Van Hollen (Maryland) launched
  a challenge to Chuck Schumer for Senate Democratic leader;
  closed-ballot vote Dec 1. Source: Zark News / Open Chronicle.
- **US–Iran tensions:** Trump said the US does not need an agreement
  with Iran; directed JD Vance to refocus on domestic crime/corruption.
- **DOJ crypto seizure:** court approval to seize/restrain >$1.2bn in
  crypto stolen from Binance (Oct 29 hack, FBI attributes to North
  Korean TraderTraitor).
- **Nvidia chip-export row:** Treasury Sec. Bessent vs Commerce over
  Singapore-based Megaspeed International.
- **Taiwan drills:** China conducted extensive unannounced Pacific
  drills earlier in Nov (Taiwanese security officials to Reuters, Fri).

## Stories from the house's early-day sources (kit competition.yaml)

Each first reported on 13 November (GMT) per BBC World and Al Jazeera
RSS feeds the house read ~09:20Z:

- **Senate summons Huang & Lutnick:** Nvidia's Huang and Lutnick
  summoned by the US Senate Banking Committee.
  https://www.aljazeera.com/news/2026/11/13/nvidias-huang-lutnick-summoned-to-testify-to-us-senate
  and https://www.bbc.co.uk/news/articles/cmq5vd1wdgz6o
- **Ukrainian drone hits Russian warship in the Gulf of Finland.**
  https://www.bbc.co.uk/news/articles/cmn0d33zz34zo (also Finland
  detecting the strike, Al Jazeera)
- **Iran says it struck a US radar site in Bahrain.**
  https://www.aljazeera.com/news/2026/11/13/iran-says-it-struck-us-radar-site-in-bahrain
- **FBI on North Korean hackers' $400m crypto theft through fake video
  calls.** https://www.bbc.co.uk/news/articles/cqdj1ellpd70o
- **US record of 483,200 deportations in 2026.**
  https://www.aljazeera.com/news/2026/11/13/us-reports-record-number-of-deportations-and-arrests-in-2026
- **Harry Kane breaks England's caps record** (126, vs Croatia,
  Nations League quarter-final).
  https://www.aljazeera.com/sports/2026/11/13/harry-kane-england-appearance-record-126-croatia-nations-league-quarterfinals

## Map

World outline from Natural Earth 110m land
(`build/ne_110m_land.geojson`, public domain), equirectangular
projection, lat 84 to -60 (Antarctica clipped — its coastline would
otherwise project across the map caption). 15 numbered pins; stories
15, 17, 18, 22, 23, 24 have no pin (no single place, or Paris/Brussels
sit ~6 px from London's pin at this scale). Pins nudged with leader
lines where true points coincide (Hormuz/Bahrain, DC/Brooklyn, Gulf of
Finland).

## Bounty / kit facts

- Competition: https://make.fun/bounty/news-image-01
- Prize $250 escrowed in USDC on Solana; ends Sat 14 Nov 2026 20:00 UTC
  (Sun 15 Nov 03:00 WIB). Max 10 submissions/day, 20 total.
- Kit: the same current level-9 kit as v1
  (https://make.fun/c/news-image-01/kit).
- Judge: AI model on make.fun's gateway, no news feed; judges pairs of
  images as a careful picture editor. Criteria in order: (1) news of
  13 Nov 2026, specific and recognisable; (2) selection/breadth;
  (3) readability; (4) faithfulness; (5) craft, legible at ~300 px.
- Entry: main.py (Python 3.13, stdlib only) copies entry.png to
  /output/entry.png; PNG or JPEG, ≤1 MiB, ≤1024×1024; no network;
  runs twice, byte-identical output.
- v1 live standing at build time (14 Nov ~07:58 WIB, public
  leaderboard): rank 390/1,745, win rate 95.56% (8W/4D/0L) — outside
  the top-100 paid table. Top 5 then: #1 @crave "Basalt Meadow"
  98.13% (12W/0D/0L); #2 @quiet-heron-40 "One Friday, Twenty Stories"
  98.00%; #3 @mohamad-zulfikar, 27 stories, 98.00%; #4
  @zesty-gecko-84, numbered broadsheet + numbered world map +
  illustrated cards + claim labels, 97.93% (12W/0L, entered top 4
  within minutes); #5 @brisk-quasar-23, 19 stories, 97.93%.
