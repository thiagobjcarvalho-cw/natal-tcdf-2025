# ⚡ QUICK REFERENCE - index-atual.html Implementation

**Version:** 2.1 Final
**Status:** Ready to implement

---

## 🎯 ANSWERS TO 4 KEY QUESTIONS

### Q1: Tone.js fixes in current index.html?

✅ **FULLY IMPLEMENTED** (lines 1671-1905)

**Summary:**
- Tone.js 14.8.49 CDN loaded
- 6 music objects defined (MUSIC_PHASE_1-5 + MUSIC_BOSS)
- All phases have unique synth configs
- playPhaseMusic() and stopPhaseMusic() functions working
- Volume: -12dB (background music level)

**Issues found:**
1. Looping calculation bug (doesn't account for variable note durations)
2. stopPhaseMusic() not called in gameOver() and menu returns
3. Volume could be higher for boss fight

---

### Q2: Plantão screen structure?

✅ **CLEAR STRUCTURE** (lines 1194-1205 HTML + 515-565 CSS)

**Layout:**
```
┌─────────────────────────┐
│  Globo Logo (red 120px) │
│  ⚠️ PLANTÃO (flash)     │
│  News container         │
│  [▶ SELECIONAR HERÓI]   │
└─────────────────────────┘
```

**Visual:**
- Red circle: `#ff4444` with 30px glow
- Title: 48px, yellow, pulsing animation (0.5s scale)
- Button: standard green/cyan style

**Behavior:**
- Displays news sequentially
- Shows button after timing
- Click advances to heroes

---

### Q3: MP3 playback integration?

⚠️ **NEEDS IMPLEMENTATION**

**Simple solution (recommended):**

```html
<!-- Add to <body> -->
<audio id="audioPlantao" src="plantao-da-globo.mp3" type="audio/mpeg"></audio>
```

```javascript
// In startPlantao()
function startPlantao() {
    showScreen("plantao");
    stopMusic();          // Stop Jingle Bells
    stopPhaseMusic();     // Stop any Tone.js

    const audio = document.getElementById('audioPlantao');
    if (STATE.audioEnabled) {
        audio.volume = 0.8;
        audio.currentTime = 0;
        audio.play().catch(e => console.log("Autoplay blocked"));
    }
    // ... rest of logic
}

// Stop when leaving
document.getElementById('btnSelectHero').addEventListener('click', () => {
    document.getElementById('audioPlantao').pause();
    showScreen('heroes');
});
```

**File location:** `/home/thiago/projetos/natal/plantao-da-globo.mp3` (276 KB)

---

### Q4: Documentation updates needed?

📝 **3 FILES TO UPDATE**

**1. README.md (v1.2 → v2.1)**
```markdown
- Update version badge: 2.1
- Expand "Novidades v2.1" section
- Add link to MUSIC-SYSTEM.md
```

**2. STATUS.md (completely outdated)**
```markdown
- Change v1.2 → v2.1
- Change "50% pronto" → "100% pronto"
- Update TELA 3 section with MP3 info
- Remove old "PENDÊNCIAS" section
```

**3. Create new: MUSIC-INTEGRATION.md**
```markdown
- Overview of Tone.js integration
- MP3 integration details
- Integration points (hooks)
- Troubleshooting guide
```

---

## 📂 KEY FILES & LOCATIONS

```
/home/thiago/projetos/natal/
├── index.html (current v2.0)
│   ├── Tone.js CDN (line 20)
│   ├── TONE.JS PHASE MUSIC (lines 1671-1905)
│   ├── Screen plantão (lines 1194-1205)
│   ├── Screen initial (lines 1143-1161)
│   ├── Screen homenagem (lines 1164-1186)
│   └── Game canvas (line 1264)
│
├── plantao-da-globo.mp3 (276 KB) ← NEEDED
├── MUSIC-SYSTEM.md (complete documentation)
├── CHANGELOG-V2.md (mentions v2.1)
├── README.md (needs v2.1 update)
└── STATUS.md (needs complete rewrite)

Created (analysis):
├── PLAN-INDEX-ATUAL.md (execution plan)
├── ANALYSIS-SUMMARY.md (detailed findings)
└── QUICK-REFERENCE.md (this file)
```

---

## 🔧 IMPLEMENTATION CHECKLIST

### Phase 1: MP3 Integration (40 min)
- [ ] Add `<audio id="audioPlantao">` element
- [ ] Add startPlantao() logic
- [ ] Add stopPlantao() logic
- [ ] Test audio playback
- [ ] Test mute/unmute functionality

### Phase 2: Tone.js Fixes (30 min)
- [ ] Fix looping calculation bug
- [ ] Add stopPhaseMusic() to gameOver()
- [ ] Add stopPhaseMusic() to menu returns
- [ ] Adjust volume for boss fight
- [ ] Test all phase transitions

### Phase 3: Testing (20 min)
- [ ] Test Firefox
- [ ] Test Safari
- [ ] Test mobile (touch)
- [ ] Console: zero errors
- [ ] Performance: 60 FPS

### Phase 4: Documentation (30 min)
- [ ] Update README.md badges
- [ ] Rewrite STATUS.md
- [ ] Create MUSIC-INTEGRATION.md
- [ ] Review CHANGELOG-V2.md
- [ ] Update links in all docs

### Phase 5: Finalize (20 min)
- [ ] Run prettier/lint
- [ ] Final QA
- [ ] Create commit message
- [ ] Ready for deployment

**Total: ~2.5 hours**

---

## 🎵 TONE.JS QUICK FACTS

**Current Implementation:**
```
Phase 1 (DEV):     140 BPM, square, 12 notes
Phase 2 (STAGE):   180 BPM, square, 7 notes
Phase 3 (STAGE):   160 BPM, square, 9 notes
Phase 4 (HMG):     110 BPM, triangle, 6 notes
Phase 5 (PROD):    170 BPM, square, 9 notes
Boss Fight:        150 BPM, square, 14 notes
```

**Volume:** -12dB (background level)

**Bug:** Looping uses `notes.length × (60/tempo)` which doesn't account for variable note durations

**Hooks:**
- playPhaseMusic(STATE.phase) @ line ~3202 ✅
- playPhaseMusic('boss') @ line ~2596 ✅
- stopPhaseMusic() missing in gameOver() ❌
- stopPhaseMusic() missing in menu returns ❌

---

## 📱 SCREEN FLOW

```
Initial
  ↓ (Jingle Bells)
Homenagem
  ↓ (Jingle Bells)
Plantão
  ↓ (MP3 plantao-da-globo) ← NEW
Heroes Selection
  ↓
Difficulty Selection
  ↓
Game Phase 1 (MUSIC_PHASE_1)
  ↓
Game Phase 2 (MUSIC_PHASE_2)
  ↓
Game Phase 3 (MUSIC_PHASE_3)
  ↓
Game Phase 4 (MUSIC_PHASE_4)
  ↓
Game Phase 5 (MUSIC_PHASE_5)
  ↓
Boss Fight (MUSIC_BOSS)
  ↓
Conclusion
  ↓ (Jingle Bells again)
Loop
```

---

## ⚠️ KNOWN ISSUES & FIXES

| Issue | Severity | Location | Fix |
|-------|----------|----------|-----|
| Looping calculation wrong | Medium | Line 1870 | Calculate actual duration |
| stopPhaseMusic() missing | High | gameOver() | Add stop call |
| stopPhaseMusic() missing | High | Menu returns | Add stop call |
| Volume too low boss | Low | Line 1857 | Use -8dB for boss |
| No MP3 plantão | High | startPlantao() | Add audio element + code |

---

## 🚀 DEPLOYMENT CHECKLIST

**Before pushing to production:**
- [ ] All 5 game phases work with their music
- [ ] Boss music plays correctly
- [ ] MP3 plantão plays on schedule
- [ ] Mute/unmute affects all audio
- [ ] No console errors
- [ ] 60 FPS maintained
- [ ] Mobile touch works
- [ ] All browsers tested

---

## 📚 DOCUMENTATION FILES

**In project:**
1. `PLAN-INDEX-ATUAL.md` - Full execution plan (80 items)
2. `ANALYSIS-SUMMARY.md` - Detailed findings (1000+ lines)
3. `QUICK-REFERENCE.md` - This file (quick lookup)

**Existing:**
1. `MUSIC-SYSTEM.md` - Complete music documentation
2. `CHANGELOG-V2.md` - Change history
3. `README.md` - Main docs (needs update)
4. `STATUS.md` - Project status (needs rewrite)

---

## 💾 FILES TO CREATE/MODIFY

```
MODIFY:
├── index.html
│   ├── Add: <audio id="audioPlantao">
│   ├── Add: stopPhaseMusic() calls
│   └── Fix: looping calculation
├── README.md
│   └── Update v2.1 section
└── STATUS.md
    └── Complete rewrite (v2.0→v2.1)

CREATE:
└── MUSIC-INTEGRATION.md
    └── Integration guide for future

KEEP (already good):
├── MUSIC-SYSTEM.md
├── CHANGELOG-V2.md
└── plantao-da-globo.mp3
```

---

## 🎯 SUCCESS CRITERIA

✅ index-atual.html complete when:
1. All 5 phases have unique Tone.js music
2. Boss fight has its own music
3. MP3 plantão plays correctly
4. No music leaks between screens
5. Volume is balanced
6. Documentation updated
7. Zero console errors
8. 60 FPS maintained
9. Works on all browsers
10. Ready for GitHub Pages deployment

---

## 🔗 QUICK NAVIGATION

- **Full Plan:** [PLAN-INDEX-ATUAL.md](PLAN-INDEX-ATUAL.md)
- **Detailed Analysis:** [ANALYSIS-SUMMARY.md](ANALYSIS-SUMMARY.md)
- **Music Docs:** [MUSIC-SYSTEM.md](MUSIC-SYSTEM.md)
- **Changes:** [CHANGELOG-V2.md](CHANGELOG-V2.md)

---

**Created:** 2025-12-25
**Status:** Ready for implementation
**Estimated time:** 2.5 hours

🔥 **LET'S GO!** 🔥
