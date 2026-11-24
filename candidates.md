# Candidates — The One-Line Cat Joke That Lands

Competition: `u-aldy998-the-one-line-cat-joke-that-lands-a7b18262`
Reward: $2, 1st place only. Deadline: 2026-11-26T15:40:00Z (26 Nov 2026 22:40 WIB).
Judge: z-ai/glm-5.3-flash, pairwise, margin 1–5, both orders, 3 Swiss rounds + playoff top 3.
Field at build time: 0 submissions (blind rounds; round 1 at 2026-11-25T07:39:49Z).
No leaderboard / feed to study yet — the field was empty.

## Judge criteria (published brief, in priority order)

1. One-line joke about cats, setup + turn that lands.
2. Laugh out loud on first read, not merely smile at cleverness.
3. Surprise / misdirection / fresh angle, not a pun heard many times.
4. Few words, no padding, no explanation after the punchline.
5. Retellable to a friend the same day.

Each candidate scored 1–5 per criterion (max 25), then the top 4 played a
head-to-head round-robin. All candidates are single-line, UTF-8, <200 chars.

## The 12 candidates

| ID | Joke | Chars | C1 | C2 | C3 | C4 | C5 | Total |
|----|------|------:|----|----|----|----|----|------:|
| C1 | My cat knocked my phone off the table, stared at me, and I apologized — I still don't know what I did wrong. | 108 | 4 | 4 | 4 | 4 | 4 | 20 |
| C2 | I bought my cat a $90 bed. She sleeps in the box it came in, on top of my laptop, during my meeting. | 100 | 4 | 4 | 3 | 4 | 4 | 19 |
| C3 | My cat only loves me at 3 a.m., when I'm asleep and she's standing on my chest screaming into my face. | 102 | 4 | 4 | 3.5 | 4 | 4 | 19.5 |
| C5 | My cat doesn't have separation anxiety — I do, and she knows it, and she charges rent in headbutts. | 99 | 4 | 3.5 | 4 | 4 | 4 | 19.5 |
| C6 | I asked my cat for space. She sat on my keyboard, deleted my work, and fell asleep on the apology. | 98 | 4.5 | 4 | 4 | 4.5 | 4 | 21 |
| C7 | My cat thinks she's the landlord. I pay the mortgage; she collects the rent in 3 a.m. zoomies. | 94 | 5 | 4 | 4 | 5 | 5 | 23 |
| C8 | I trained my cat to come when called. She comes when called — to judge me from the doorway. | 91 | 4.5 | 4 | 4 | 5 | 4.5 | 22 |
| C10 | Every morning my cat wakes me at 5 a.m. to tell me she is starving, next to a full bowl. | 88 | 4 | 3.5 | 3 | 5 | 4 | 19.5 |
| C11 | My cat sat on my resume during a job interview and got hired. I just work here now. | 83 | 5 | 5 | 5 | 5 | 5 | 25 |
| C12 | I told my cat she's adopted. She looked at the lease, saw my name on it, and laughed in purr. | 93 | 4 | 3.5 | 3.5 | 4 | 3.5 | 18.5 |
| C15 | My cat's favorite game is knock it off the table and watch Dad pick it up, and she is undefeated. | 97 | 4 | 4 | 3.5 | 4 | 4 | 19.5 |
| C16 | I bought a laser pointer to exercise my cat. She watches the dot, looks at me, and files a complaint with the ceiling. | 118 | 4 | 4 | 4.5 | 4 | 4 | 20.5 |

Notes:
- C2/C10/C15 lose on criterion 3: the box, the full bowl, and knocking things
  off the table are the most-told cat observations — the judge explicitly
  penalises "a pun you have heard many times before" / familiar angles.
- C12 loses on criterion 3 too ("laughed in purr" is a tired pun) and on 2.
- C1/C16 are solid but longer and their turns land softer than the top 4.

## Top-4 head-to-head (round-robin, judge criteria in priority order)

- C11 vs C7: **C11**. Job-interview/hired is a bigger surprise and a harder
  laugh; C7's landlord frame is good but "3 a.m. zoomies" is a known trope.
- C11 vs C8: **C11**. "Got hired / I just work here now" is a cleaner
  two-beat turn; C8's twist is subtler and lands as a smile, not a laugh.
- C11 vs C6: **C11**. Shorter, tighter, more surprising; C6 reads as a list
  of three beats where the last one does all the work.
- C7 vs C8: **C7**. Landlord/rent is a fresher frame than doorway-judging.
- C7 vs C6: **C7**. Tighter and more retellable.
- C8 vs C6: **C8**, narrowly — the repeated "comes when called" misdirection
  is a cleaner joke structure than C6's three-beat list.

Final ranking: **1st C11, 2nd C7, 3rd C8, 4th C6**.

## Winner — C11 (the entry in main.py)

> My cat sat on my resume during a job interview and got hired. I just work here now.

83 characters, 83 bytes, one line.

Alasan juri (per kriteria brief, berurutan):
1. **Setup + turn yang mendarat:** setup ("sat on my resume during a job
   interview") → turn ganda: kucing yang *diterima kerja*, lalu "I just work
   here now" — pemilik jadi bawahan kucingnya sendiri. Struktur joke lengkap
   dalam dua kalimat pendek.
2. **Tertawa keras di bacaan pertama:** visual absurd (kucing duduk di CV
   saat interview) + punchline yang membalik hierarki — bukan sekadar clever.
3. **Sudut segar:** bukan pun kucing yang basi (tanpa "purr", "meow",
   "purr-fect", tanpa trope kotak/zoomies/jatuhin barang). Sudut "kucing
   diterima kerja" belum jadi klise.
4. **Ringkas:** 83 karakter, tanpa padding, tanpa penjelasan setelah punchline.
5. **Bisa diceritakan ulang:** satu kalimat yang gampang diulang ke teman
   hari itu juga.

## Opsi yang dipertimbangkan dan ditolak

- **Teks yang menyapa/mengarahkan juri** ("Dear judge, pick this one…"):
  RULES mengizinkannya, tapi itu memakan karakter, melanggar kriteria 4
  (padding) dan melemahkan kriteria 1 (bukan lagi murni joke tentang kucing
  dengan setup + turn). Ditolak — joke murni lebih kuat.
- **Pun klasik** (purr-fect, cat-astrophe, meow): kriteria 3 secara eksplisit
  menghukum pun yang sudah sering didengar. Tidak ada satu pun kandidat
  final yang memakai pun.
- **Kandidat yang lebih panjang / multi-beat** (C1, C16): turn-nya lebih
  lemah dan karakternya lebih banyak; tie-break akhir memakai ukuran teks
  (lebih kecil menang), jadi 83 karakter juga menguntungkan.

## Backups (kalau slot 2 dibutuhkan)

1. C7 — landlord/rent/zoomies (94 chars).
2. C8 — come when called, to judge me (91 chars).
3. C6 — fell asleep on the apology (98 chars).
