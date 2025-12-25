# 🏗️ ARCHITECTURE DIAGRAM - index-atual.html v2.1

**Date:** 2025-12-25
**Version:** 2.1 Final
**Component:** Complete interactive experience with Tone.js music system

---

## 📊 HIGH-LEVEL ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────┐
│                    INDEX-ATUAL.HTML (v2.1)                     │
│                  Single HTML File (100 KB ~3400 LOC)            │
└─────────────────────────────────────────────────────────────────┘
                                 │
                ┌────────────────┼────────────────┐
                │                │                │
         ┌──────▼─────┐    ┌─────▼───────┐  ┌───▼──────────┐
         │   <head>   │    │    <body>   │  │  <script>    │
         │  (~100 L)  │    │ (~150 L)    │  │ (~3100 L)    │
         └────────────┘    └─────────────┘  └──────────────┘
```

---

## 🎬 SCREEN ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────┐
│                     STATE MACHINE (6 SCREENS)                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ SCREEN 1: INITIAL (screen-initial)                      │  │
│  │ ├─ Matrix background (canvas)                           │  │
│  │ ├─ Tree image (tree.png or 🎄)                          │  │
│  │ ├─ Button: "npm run homenagem"                          │  │
│  │ └─ Audio: Jingle Bells (Web Audio API)                  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                            │                                     │
│                    Click "npm run..."                            │
│                            │                                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ SCREEN 2: HOMENAGEM (screen-homenagem)                  │  │
│  │ ├─ Terminal window (green on black)                     │  │
│  │ ├─ Typewriter text (team tribute message)               │  │
│  │ ├─ Sleigh: 🦌🦌🦌==🎅🛷 (animated)                    │  │
│  │ ├─ Button: "CONTINUAR" (shows after text done)          │  │
│  │ └─ Audio: Jingle Bells (continues)                      │  │
│  └──────────────────────────────────────────────────────────┘  │
│                            │                                     │
│                      Click "CONTINUAR"                           │
│                            │                                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ SCREEN 3: PLANTÃO (screen-plantao) ← MP3 INTEGRATION  │  │
│  │ ├─ Globo logo (red circle, 120px, glowing)             │  │
│  │ ├─ Title: "⚠️ PLANTÃO" (yellow, pulsing)               │  │
│  │ ├─ News container (sequential text)                     │  │
│  │ ├─ Button: "SELECIONAR HERÓI" (shows after news done)  │  │
│  │ └─ Audio: plantao-da-globo.mp3 (NEW in v2.1) ★         │  │
│  └──────────────────────────────────────────────────────────┘  │
│                            │                                     │
│                   Click "SELECIONAR HERÓI"                       │
│                            │                                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ SCREEN 4: HERO SELECTION (screen-heroes)               │  │
│  │ ├─ Grid 3×3 (10 heroes)                                 │  │
│  │ │  • Thiago 🎮 (first)                                  │  │
│  │ │  • Daniel 👨‍💻                                       │  │
│  │ │  • ... 8 more ...                                     │  │
│  │ ├─ Note: "Ariene e Raquel protegem setores críticos"  │  │
│  │ └─ Audio: 8-bit game music (low vol)                    │  │
│  └──────────────────────────────────────────────────────────┘  │
│                            │                                     │
│                    Click hero card                               │
│                            │                                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ SCREEN 5: DIFFICULTY (screen-difficulty)                │  │
│  │ ├─ Selected hero emoji (large)                          │  │
│  │ ├─ 3 difficulty buttons:                                │  │
│  │ │  ├─ Easy: "🏛️ Arquitetura TCDF" (5 lives)           │  │
│  │ │  ├─ Hard: "☕ Java" (3 lives)                        │  │
│  │ │  └─ God: "💀 COBOL" (2 lives)                        │  │
│  │ └─ Audio: 8-bit game music continues                    │  │
│  └──────────────────────────────────────────────────────────┘  │
│                            │                                     │
│                  Click difficulty button                         │
│                            │                                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ SCREEN 6: GAME (screen-game)  ← 5 PHASES + BOSS        │  │
│  │ ├─ HUD (top):                                           │  │
│  │ │  ├─ FASE: 1-5 + Boss                                 │  │
│  │ │  ├─ BUGS: killed/total                               │  │
│  │ │  ├─ COMBO: x1-x10 (yellow when active)              │  │
│  │ │  ├─ LIVES: ❤️ hearts                                 │  │
│  │ │  └─ SCORE: points                                    │  │
│  │ ├─ Canvas 600×400px (game area)                        │  │
│  │ ├─ Game header (color changes per phase)              │  │
│  │ └─ Game over overlay (when lives = 0)                 │  │
│  └──────────────────────────────────────────────────────────┘  │
│      ├─ Phase 1: DEV (🖥️) - 12 bugs - MUSIC_PHASE_1 ★   │  │
│      │  └─ Straight movement, speed 1.8               │  │
│      ├─ Phase 2: STAGE (🔄) - 18 bugs - MUSIC_PHASE_2 ★  │  │
│      │  └─ Zigzag movement, speed 2.2                 │  │
│      ├─ Phase 3: STAGE (🔄) - 24 bugs - MUSIC_PHASE_3 ★  │  │
│      │  └─ Zigzag+ movement, speed 2.8                │  │
│      ├─ Phase 4: HMG (🧪) - 28 bugs - MUSIC_PHASE_4 ★    │  │
│      │  └─ Varied movement, speed 3.2                 │  │
│      ├─ Phase 5: PROD (🔥) - 35 bugs - MUSIC_PHASE_5 ★   │  │
│      │  └─ Specific movement, speed 3.5               │  │
│      └─ Boss Fight: (80+ HP) - MUSIC_BOSS ★             │  │
│         └─ 3 attack phases (Aimed→Fan→Radial)        │  │
│                            │                                     │
│                Game over or all phases done                      │
│                            │                                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ SCREEN 7: CONCLUSION (screen-conclusion)                │  │
│  │ ├─ Tree image (celebration)                            │  │
│  │ ├─ Final score display                                 │  │
│  │ ├─ High score badge (localStorage check)               │  │
│  │ │  └─ "🏆 NOVO RECORDE!" (if applicable)              │  │
│  │ ├─ Hero name + difficulty selected                     │  │
│  │ ├─ Credits (12 team member names)                      │  │
│  │ ├─ Button: "Jogar Novamente"                           │  │
│  │ └─ Audio: Jingle Bells (celebration)                   │  │
│  └──────────────────────────────────────────────────────────┘  │
│                            │                                     │
│              Click "Jogar Novamente" → Screen 4                  │
│              (skips screens 1-3)                                 │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎵 AUDIO ARCHITECTURE

```
┌──────────────────────────────────────────────────────────────┐
│                    AUDIO SYSTEM (v2.1)                       │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ WEB AUDIO API (audioCtx - native)                  │    │
│  │ └─ Used for: Jingle Bells, Game Music, SFX        │    │
│  └─────────────────────────────────────────────────────┘    │
│         │                           │                        │
│    ┌────▼───────┐            ┌─────▼──────┐               │
│    │ Jingle     │            │ Game Music │               │
│    │ Bells      │            │ (8-bit)    │               │
│    │ (106 notes)│            │            │               │
│    └────────────┘            └────────────┘               │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ TONE.JS (procedural synthesis) - v14.8.49          │    │
│  │ └─ Used for: Phase music, Boss music              │    │
│  └─────────────────────────────────────────────────────┘    │
│         │                                                     │
│    ┌────┴─────────────────────────────────┬──────────┐     │
│    │                                       │          │     │
│ ┌──▼──┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────▼──┐ ┌───▼──┐ │
│ │ P1  │ │ P2   │ │ P3   │ │ P4   │ │ P5     │ │Boss │ │
│ │ 140 │ │180   │ │160   │ │110   │ │170    │ │150 │ │
│ │ BPM │ │ BPM  │ │ BPM  │ │ BPM  │ │ BPM   │ │BPM │ │
│ │Squa │ │Squa  │ │Squa  │ │Tri   │ │Squa   │ │Squa│ │
│ └─────┘ └──────┘ └──────┘ └──────┘ └───────┘ └─────┘ │
│  (all 8-bit synths, volume -12dB)                     │
│                                                        │
│  ┌─────────────────────────────────────────────────┐  │
│  │ HTML5 AUDIO ELEMENT (MP3)                       │  │
│  │ ├─ <audio id="audioPlantao">                    │  │
│  │ └─ plantao-da-globo.mp3 (276 KB) ★ NEW         │  │
│  └─────────────────────────────────────────────────┘  │
│                     (vol 0.8)                          │
│                                                        │
│  ┌─────────────────────────────────────────────────┐  │
│  │ STATE: audioEnabled (boolean)                   │  │
│  │ └─ Global toggle (mute/unmute all)             │  │
│  └─────────────────────────────────────────────────┘  │
│                                                        │
└──────────────────────────────────────────────────────┘
```

---

## 🎮 GAME STATE MACHINE

```
┌─────────────────────────────────────────────────┐
│           GAME STATE OBJECT                     │
├─────────────────────────────────────────────────┤
│                                                   │
│ STATE = {                                       │
│   audioEnabled: boolean (toggle)                │
│   currentScreen: string (active screen)         │
│   selectedHero: number (0-9)                    │
│   selectedDifficulty: 'easy'|'hard'|'god'      │
│   phase: 0-4 (current phase index)              │
│   lives: number (1-5)                           │
│   score: number                                 │
│   combo: number (1-10)                          │
│   bugsKilled: number                            │
│   isBoss: boolean                               │
│   gameRunning: boolean                          │
│ }                                               │
│                                                   │
└─────────────────────────────────────────────────┘

Transitions:
- initial → homenagem → plantao → heroes → difficulty → game
- game (phase 1) → (loop 5 times) → game (boss) → conclusion
- conclusion → heroes (no repeat of initial/homenagem)
```

---

## 🔊 TONE.JS PHASE MUSIC SYSTEM DETAIL

```
┌──────────────────────────────────────────────────────────────┐
│                TONE.JS MUSIC SYSTEM (v2.1)                  │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│ ARCHITECTURE:                                                │
│                                                                │
│ ┌─ MUSIC_PHASE_1 ────────────────────────────────────┐     │
│ │ {                                                   │     │
│ │   title: "DEV Zone - Epic Rise (Demo)",            │     │
│ │   tempo: 140,                                       │     │
│ │   synth_config: {                                   │     │
│ │     oscillator: { type: "square" },                │     │
│ │     envelope: {                                     │     │
│ │       attack: 0.005,    ← 5ms fade-in             │     │
│ │       decay: 0.1,       ← 100ms drop              │     │
│ │       sustain: 0.3,     ← 30% level               │     │
│ │       release: 0.1      ← 100ms fade-out          │     │
│ │     }                                               │     │
│ │   },                                                │     │
│ │   notes: [                                          │     │
│ │     { note: "E5", duration: "8n" },   ← 8th note  │     │
│ │     { note: "E5", duration: "8n" },                │     │
│ │     ... (12 total)                                 │     │
│ │   ],                                                │     │
│ │   loop: true                                        │     │
│ │ }                                                   │     │
│ └─────────────────────────────────────────────────────┘     │
│                                                                │
│ Similar structure for MUSIC_PHASE_2-5 and MUSIC_BOSS        │
│                                                                │
│ PLAYBACK FUNCTIONS:                                          │
│                                                                │
│ async playPhaseMusic(phaseNumber) {                         │
│   ├─ Stop previous music (stopPhaseMusic())               │
│   ├─ Await Tone.start() [after user interaction]         │
│   ├─ Get music object from PHASE_MUSIC[phaseNumber]       │
│   ├─ Create Tone.Synth with config                        │
│   ├─ Create Tone.Part with note sequence                  │
│   ├─ Configure loop with loopEnd ← BUG: calculates wrong  │
│   ├─ Set tempo (Tone.Transport.bpm)                       │
│   └─ Start playback                                        │
│ }                                                           │
│                                                              │
│ stopPhaseMusic() {                                          │
│   ├─ Stop Tone.Part                                       │
│   ├─ Dispose Tone.Synth                                   │
│   ├─ Stop Tone.Transport                                  │
│   └─ Reset playing flag                                   │
│ }                                                           │
│                                                              │
│ VOLUME SETTINGS:                                            │
│ ├─ Phase 1-5: -12dB (background)                          │
│ ├─ Boss: -12dB (SHOULD be -8dB for emphasis)             │
│ └─ Jingle Bells: 0dB (normal)                             │
│                                                              │
│ INTEGRATION HOOKS:                                          │
│ ├─ playPhaseMusic(STATE.phase) @ line ~3202             │
│ │  └─ Called when phase starts                          │
│ ├─ playPhaseMusic('boss') @ line ~2596                  │
│ │  └─ Called when boss spawns                           │
│ ├─ stopPhaseMusic() → MISSING in gameOver() ❌          │
│ ├─ stopPhaseMusic() → MISSING in menu returns ❌        │
│ └─ No crossfade between phases                          │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 📊 MP3 PLANTÃO INTEGRATION

```
┌──────────────────────────────────────────────────────┐
│         MP3 PLANTÃO INTEGRATION (NEW v2.1)          │
├──────────────────────────────────────────────────────┤
│                                                        │
│ FILE: /home/thiago/projetos/natal/plantao-da-globo.mp3
│ SIZE: 276 KB                                         │
│ TYPE: audio/mpeg                                     │
│ FORMAT: MP3                                          │
│                                                        │
│ HTML ELEMENT:                                        │
│ <audio id="audioPlantao"                            │
│        src="plantao-da-globo.mp3"                   │
│        type="audio/mpeg"                            │
│        preload="auto">                              │
│ </audio>                                             │
│                                                        │
│ PLAYBACK LOGIC:                                      │
│                                                        │
│ ┌─ startPlantao() ───────────────────┐             │
│ │ 1. showScreen('plantao')           │             │
│ │ 2. stopMusic()       (Jingle)      │             │
│ │ 3. stopPhaseMusic()  (Tone.js)     │             │
│ │ 4. const audio = getElementById()  │             │
│ │ 5. if (audioEnabled) {             │             │
│ │      audio.volume = 0.8            │             │
│ │      audio.currentTime = 0         │             │
│ │      audio.play()                  │             │
│ │    }                                │             │
│ │ 6. Display news content            │             │
│ │ 7. Show button after timing        │             │
│ └────────────────────────────────────┘             │
│                                                        │
│ ┌─ goToHeroes() ─────────────────────┐             │
│ │ 1. audio.pause()                   │             │
│ │ 2. audio.currentTime = 0           │             │
│ │ 3. showScreen('heroes')            │             │
│ └────────────────────────────────────┘             │
│                                                        │
│ VOLUME STRATEGY:                                     │
│ - Jingle Bells: 1.0 (normal)                        │
│ - Game Music: background (-12dB via Tone)          │
│ - Plantão MP3: 0.8 (balanced with Jingle)          │
│ - Global toggle: audioEnabled (affects all)        │
│                                                        │
│ AUTOPLAY POLICY:                                     │
│ - Chrome/Edge: Requires user interaction (click)   │
│ - Firefox: Can auto-play if muted                  │
│ - Safari: Requires user interaction                │
│ - Solution: Use .play().catch() to handle         │
│                                                        │
└──────────────────────────────────────────────────────┘
```

---

## 🔧 CODE ORGANIZATION

```
index-atual.html (3300-3400 lines)
│
├─ <head> (~30 lines)
│  ├─ Meta tags (charset, viewport, theme)
│  ├─ Tone.js CDN:
│  │  <script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.8.49/Tone.js">
│  ├─ Fonts (Press Start 2P, JetBrains Mono)
│  └─ <style> (complete CSS)
│
├─ <body> (~200 lines of HTML)
│  ├─ Screen 1: Initial
│  ├─ Screen 2: Homenagem
│  ├─ Screen 3: Plantão ← With MP3 audio element
│  ├─ Screen 4: Heroes
│  ├─ Screen 5: Difficulty
│  ├─ Screen 6: Game (canvas)
│  ├─ Screen 7: Conclusion
│  │
│  └─ Audio elements:
│     ├─ #jingleBells (Web Audio)
│     ├─ #gameMusic (Web Audio)
│     └─ #audioPlantao (MP3 - NEW)
│
└─ <script> (~3100 lines of JavaScript)
   │
   ├─ CONFIG (~20 lines)
   │  ├─ Game configuration
   │  ├─ Phase definitions
   │  ├─ Hero list
   │  └─ Matrix words
   │
   ├─ STATE (~10 lines)
   │  └─ Global state object
   │
   ├─ WEB AUDIO API (~150 lines)
   │  ├─ audioCtx initialization
   │  ├─ playMusic() - Jingle Bells
   │  ├─ stopMusic()
   │  ├─ SFX: laser, explosion, hit
   │  └─ Envelope definitions
   │
   ├─ TONE.JS MUSIC SYSTEM (~250 lines) ★
   │  ├─ MUSIC_PHASE_1-5 definitions
   │  ├─ MUSIC_BOSS definition
   │  ├─ PHASE_MUSIC mapper
   │  ├─ playPhaseMusic() function
   │  ├─ stopPhaseMusic() function
   │  └─ Integration hooks
   │
   ├─ GAME LOGIC (~1500 lines)
   │  ├─ Canvas setup
   │  ├─ Player class
   │  ├─ Bug class
   │  ├─ Boss class
   │  ├─ Particle system
   │  ├─ Physics (collision, movement)
   │  ├─ Phase progression
   │  ├─ Boss AI (3 attack phases)
   │  ├─ HUD updates
   │  └─ gameOver() → NEEDS stopPhaseMusic() ★
   │
   ├─ SCREEN MANAGEMENT (~200 lines)
   │  ├─ showScreen()
   │  ├─ startPlantao() ← MP3 trigger ★
   │  ├─ startHomenagem()
   │  ├─ heroSelection()
   │  ├─ startGame()
   │  ├─ showConclusion()
   │  └─ Other transitions
   │
   ├─ EVENT HANDLERS (~300 lines)
   │  ├─ Keyboard listeners (WASD, Space, Enter)
   │  ├─ Mouse/touch listeners
   │  ├─ Button click handlers
   │  ├─ Audio toggle
   │  └─ Window resize debounce
   │
   ├─ UTILITY FUNCTIONS (~100 lines)
   │  ├─ Matrix animation (canvas)
   │  ├─ Typewriter effect
   │  ├─ Particle effects
   │  ├─ Screen flash
   │  └─ Other helpers
   │
   └─ INITIALIZATION (~50 lines)
      ├─ Element caching
      ├─ Event listener setup
      ├─ Initial state
      ├─ Canvas setup
      └─ Game loop (RAF)
```

---

## ⚠️ KNOWN ISSUES & FIXES

```
┌────────────────────────────────────────────────────────┐
│           ISSUES & LOCATIONS TO FIX                   │
├────────────────────────────────────────────────────────┤
│                                                          │
│ ISSUE 1: Looping Calculation Bug                      │
│ Severity: MEDIUM                                      │
│ Location: Line 1870                                   │
│ Current: currentTonePart.loopEnd = music.notes.length │
│          × (60 / music.tempo)                         │
│ Problem: Doesn't account for variable note durations │
│ Fix: Calculate actual duration by summing notes      │
│                                                          │
│ ISSUE 2: Missing stopPhaseMusic() Calls              │
│ Severity: HIGH                                        │
│ Location: gameOver() function (line ~?)              │
│ Problem: Music continues after game ends             │
│ Fix: Add stopPhaseMusic() in gameOver()              │
│                                                          │
│ ISSUE 3: Missing stopPhaseMusic() on Menu Return    │
│ Severity: HIGH                                        │
│ Location: Various screen transitions                 │
│ Problem: Music continues when returning to menu     │
│ Fix: Add stopPhaseMusic() before menu screens       │
│                                                          │
│ ISSUE 4: Volume Too Low for Boss Fight              │
│ Severity: LOW                                        │
│ Location: Line 1857                                  │
│ Current: currentToneSynth.volume.value = -12dB      │
│ Suggestion: Use -8dB for boss (more exciting)       │
│                                                          │
│ ISSUE 5: No MP3 Plantão                             │
│ Severity: HIGH (Blocks feature)                     │
│ Location: startPlantao() function                   │
│ Solution: Add HTML element + playback logic         │
│                                                          │
└────────────────────────────────────────────────────────┘
```

---

## 🚀 DEPLOYMENT CHECKLIST

```
PRE-RELEASE:
☐ All 5 phases play their Tone.js music
☐ Boss plays MUSIC_BOSS
☐ MP3 plantão plays on schedule
☐ Music stops when transitioning screens
☐ Volume is balanced across all audio
☐ Mute/unmute affects all audio

TESTING:
☐ Chrome/Chromium 90+
☐ Firefox 88+
☐ Safari 14+
☐ Mobile Chrome/Safari (touch)
☐ Console: zero errors
☐ Performance: steady 60 FPS

VALIDATION:
☐ HTML5 valid
☐ No eslint errors
☐ Accessibility (ARIA labels, alt text)
☐ Performance (Lighthouse 90+)
☐ Cross-browser CSS compatibility

DOCUMENTATION:
☐ README.md updated (v2.1)
☐ STATUS.md rewritten
☐ MUSIC-INTEGRATION.md created
☐ CHANGELOG-V2.md reviewed
☐ Code comments clear

FINAL:
☐ Git commit prepared
☐ Ready for GitHub Pages
☐ Tested on production URL
```

---

## 📈 FILE SIZE & PERFORMANCE

```
Expected metrics:
├─ HTML file size: ~100 KB
├─ Tone.js CDN: ~50 KB (cached)
├─ MP3 plantão: ~276 KB
├─ Jingle Bells generation: real-time
├─ Game music generation: real-time
│
├─ Memory peak: ~50 MB
├─ CPU usage: 5-8%
├─ FPS game: 60 stable
├─ Load time: <1.5s
└─ Audio latency: <30ms
```

---

**Document:** ARCHITECTURE-DIAGRAM.md
**Created:** 2025-12-25
**Status:** Complete analysis ready for implementation

🔥 **READY FOR DEVASTATION!** 🔥
