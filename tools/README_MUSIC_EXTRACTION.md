# 🎵 MUSIC EXTRACTION GUIDE - Educational Workflow

**DOOM MODE EDITION** 💀🔥👑

---

## ⚠️ IMPORTANT - COPYRIGHT & LEGAL

### What This Toolset Does:
✅ **Provides analysis tools** for educational audio study
✅ **Generates empty structures** for manual transcription
✅ **Creates synthetic examples** for demonstration
✅ **Teaches music theory** and digital audio concepts

### What This Toolset Does NOT Do:
❌ **Extract copyrighted melodies** automatically
❌ **Violate YouTube Terms of Service**
❌ **Enable commercial copyright infringement**
❌ **Replace human creativity and interpretation**

### Your Responsibility:
1. **Manual transcription** - Listen and transcribe by ear
2. **Original interpretation** - Create your own version
3. **Respect copyright** - For commercial use, get licenses
4. **Fair use compliance** - Educational/transformative use only

**Bottom line:** These tools help you LEARN and CREATE, not copy.

---

## 📋 PREREQUISITES

### System Requirements

#### Ubuntu/Debian:
```bash
# Install dependencies
sudo apt install -y yt-dlp ffmpeg python3-pip

# Install Python libraries
pip3 install librosa numpy scipy
```

#### Fedora:
```bash
sudo dnf install -y yt-dlp ffmpeg python3-pip
pip3 install librosa numpy scipy
```

#### macOS:
```bash
brew install yt-dlp ffmpeg python3
pip3 install librosa numpy scipy
```

### Verify Installation:
```bash
yt-dlp --version
ffmpeg -version
python3 --version
python3 -c "import librosa; print(f'librosa {librosa.__version__}')"
```

---

## 🎯 WORKFLOW - 4-STEP PROCESS

### STEP 1: Download Audio Sample (Educational)

**Basic usage:**
```bash
./download_music.sh "https://www.youtube.com/watch?v=VIDEO_ID"
```

**Custom output name:**
```bash
./download_music.sh "https://www.youtube.com/watch?v=VIDEO_ID" "my_song"
```

**What it does:**
- Downloads **first 30 seconds** only (sample for analysis)
- Converts to **WAV format** (uncompressed, good for analysis)
- Saves as `music_sample.wav` (or custom name)

**Example for Power Rangers theme:**
```bash
cd /home/thiago/projetos/natal/tools
./download_music.sh "https://www.youtube.com/watch?v=4S88ULz9c80" "power_rangers"
# Creates: power_rangers.wav
```

---

### STEP 2: Analyze Audio Properties

**Analyze only (no structure generation):**
```bash
python3 extract_melody.py music_sample.wav --analyze-only
```

**Output example:**
```
🎧 Loading audio file: music_sample.wav
✅ Analysis complete:
   • BPM: 140
   • Duration: 30.0s
   • Estimated Key: E

📊 Analysis Results:
{
  "bpm": 140,
  "duration": 30.0,
  "key": "E",
  "sample_rate": 22050
}
```

**What this tells you:**
- **BPM** - Set this as `tempo` in your Tone.js object
- **Key** - Helps you identify which notes to use
- **Duration** - How much audio you have to work with

---

### STEP 3: Generate Tone.js Structure

**Generate empty structure (for manual filling):**
```bash
python3 extract_melody.py power_rangers.wav --var-name MUSIC_PHASE_1 > phase1.js
```

**Output (phase1.js):**
```javascript
// ============================================================
// USAGE INSTRUCTIONS
// ============================================================
// 1. Copy this object to your index.html
// 2. Add to PHASE_MUSIC object
// 3. If notes array is empty, manually transcribe the melody
// 4. Test with: playPhaseMusic(phase_number)
// ============================================================

const MUSIC_PHASE_1 = {
  "title": "Power Rangers",
  "tempo": 140,
  "key": "E",
  "synth_config": {
    "oscillator": {
      "type": "square"
    },
    "envelope": {
      "attack": 0.005,
      "decay": 0.1,
      "sustain": 0.3,
      "release": 0.1
    }
  },
  "notes": [
    // ⚠️ EMPTY - You must fill this manually!
    // Example:
    // {"note": "E5", "duration": "8n"},
    // {"note": "G5", "duration": "8n"},
    // {"note": "A5", "duration": "4n"},
  ],
  "loop": true,
  "_instructions": [
    "MANUAL TRANSCRIPTION REQUIRED:",
    "1. Listen to the original music carefully",
    "2. Identify the main melody notes by ear",
    "3. Fill the 'notes' array above with your interpretation",
    "4. Use Tone.js duration notation: 1n, 2n, 4n, 8n, 16n",
    "5. Simplify to 40-60 notes for game loop (20-30 seconds)",
    "6. Test and adjust until it sounds good",
    "",
    "Note naming: C4, D4, E4, F4, G4, A4, B4, C5, D5, etc.",
    "Durations: 1n=whole, 2n=half, 4n=quarter, 8n=eighth, 16n=sixteenth"
  ]
};
```

**Generate synthetic demo (for testing):**
```bash
python3 extract_melody.py --demo > demo.js
```

This creates a complete working example with synthetic melody.

---

### STEP 4: Manual Transcription (The Creative Part!)

**This is where YOU create your interpretation.**

#### How to Transcribe by Ear:

1. **Listen to the sample repeatedly**
   - Play `power_rangers.wav` in a media player
   - Identify the main melody (not bass, not harmony)
   - Focus on the most recognizable part

2. **Identify notes using a piano/keyboard**
   - Use online piano: https://www.onlinepianist.com/virtual-piano
   - Or: https://www.musicca.com/piano
   - Match each note by ear

3. **Write down the melody**
   ```
   Example transcription notes:
   E5 (quick) → G5 (quick) → A5 (hold) → G5 (quick) → E5 (hold)
   ```

4. **Convert to Tone.js notation**
   ```javascript
   {"note": "E5", "duration": "8n"},  // quick = eighth note
   {"note": "G5", "duration": "8n"},
   {"note": "A5", "duration": "4n"},  // hold = quarter note
   {"note": "G5", "duration": "8n"},
   {"note": "E5", "duration": "4n"},
   ```

5. **Simplify for game loop**
   - Aim for **40-60 notes** total
   - Loop should be **20-30 seconds**
   - Pick the most memorable/energetic part

#### Tone.js Duration Reference:

| Notation | Name | Duration | Use Case |
|----------|------|----------|----------|
| `"1n"` | Whole note | 4 beats | Very long hold |
| `"2n"` | Half note | 2 beats | Long hold |
| `"4n"` | Quarter note | 1 beat | Normal note |
| `"8n"` | Eighth note | 0.5 beat | Quick note |
| `"16n"` | Sixteenth note | 0.25 beat | Very quick |
| `"4n."` | Dotted quarter | 1.5 beats | Medium-long |

#### Note Naming Reference:

```
Octave 4 (middle range): C4, D4, E4, F4, G4, A4, B4
Octave 5 (high range):   C5, D5, E5, F5, G5, A5, B5
Octave 3 (low range):    C3, D3, E3, F3, G3, A3, B3

Sharps: C#4, D#4, F#4, G#4, A#4
```

**Pro tip:** Most 8-bit melodies use **Octave 4 and 5** heavily.

---

## 🎸 COMPLETE EXAMPLE WORKFLOW

Let's extract **Mario Bros theme** for Phase 2:

```bash
# 1. Download sample
./download_music.sh "https://www.youtube.com/watch?v=P9Ee4TevHfA" "mario_bros"

# 2. Analyze
python3 extract_melody.py mario_bros.wav --analyze-only
# Output: BPM=180, Key=C

# 3. Generate structure
python3 extract_melody.py mario_bros.wav --var-name MUSIC_PHASE_2 > phase2.js

# 4. Open phase2.js and manually fill the notes array
# (Listen to mario_bros.wav and transcribe by ear)

# 5. Test in browser by copying to index.html
```

**Example manual transcription (simplified):**
```javascript
const MUSIC_PHASE_2 = {
  "title": "Mario Bros",
  "tempo": 180,
  "key": "C",
  "synth_config": {
    "oscillator": {"type": "square"},
    "envelope": {
      "attack": 0.005,
      "decay": 0.1,
      "sustain": 0.3,
      "release": 0.1
    }
  },
  "notes": [
    // Main Mario theme (simplified interpretation)
    {"note": "E5", "duration": "8n"},
    {"note": "E5", "duration": "8n"},
    {"note": "E5", "duration": "8n"},  // da-da-da
    {"note": "C5", "duration": "8n"},
    {"note": "E5", "duration": "4n"},
    {"note": "G5", "duration": "4n"},  // main jump
    {"note": "C5", "duration": "4n"},

    // Simplified for demo - real version would have 40-60 notes
  ],
  "loop": true
};
```

---

## 🛠️ TROUBLESHOOTING

### Problem: `yt-dlp: command not found`

**Solution:**
```bash
# Ubuntu/Debian
sudo apt install yt-dlp

# Or install via pip
pip3 install yt-dlp
```

---

### Problem: `ffmpeg: command not found`

**Solution:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg
```

---

### Problem: `ModuleNotFoundError: No module named 'librosa'`

**Solution:**
```bash
pip3 install librosa numpy scipy

# If pip3 not in PATH, try:
python3 -m pip install librosa numpy scipy
```

---

### Problem: Download fails with "Video unavailable"

**Possible causes:**
- Video is region-locked
- Video was deleted
- Network issue

**Solution:**
- Try a different video
- Check your internet connection
- Update yt-dlp: `pip3 install --upgrade yt-dlp`

---

### Problem: BPM detection is way off

**Why it happens:**
- Librosa isn't perfect
- Complex rhythms confuse the algorithm
- Multiple instruments interfere

**Solution:**
- Manually count the BPM yourself
- Use online BPM detector: https://www.all8.com/tools/bpm.htm
- Edit the generated `.js` file and adjust `tempo` value

---

### Problem: Can't identify notes by ear

**Learning resources:**
- **Ear training:** https://www.musictheory.net/exercises
- **Online piano:** https://www.musicca.com/piano
- **Note frequency chart:** https://pages.mtu.edu/~suits/notefreqs.html

**Pro tip:** Start with simple melodies (Jingle Bells, Mary Had a Little Lamb) to practice.

---

## 📚 ADDITIONAL RESOURCES

### Music Theory:
- Note naming: https://www.musictheory.net/lessons/10
- Rhythm basics: https://www.musictheory.net/lessons/11
- Key signatures: https://www.musictheory.net/lessons/24

### Tone.js:
- Official docs: https://tonejs.github.io/docs/
- Synth examples: https://tonejs.github.io/examples/
- Duration notation: https://github.com/Tonejs/Tone.js/wiki/Time

### Audio Analysis:
- Librosa tutorials: https://librosa.org/doc/latest/tutorial.html
- Understanding BPM: https://en.wikipedia.org/wiki/Tempo
- Pitch detection: https://en.wikipedia.org/wiki/Pitch_detection_algorithm

---

## 🎯 BEST PRACTICES

### DO:
✅ Simplify melodies to 40-60 notes
✅ Focus on the most recognizable part
✅ Test frequently in the browser
✅ Adjust BPM if playback feels wrong
✅ Use square wave for authentic 8-bit sound
✅ Create your own interpretation

### DON'T:
❌ Try to transcribe every instrument
❌ Make loops longer than 30 seconds
❌ Use complex chords (stick to melody)
❌ Forget to set `loop: true`
❌ Copy-paste from copyrighted sheet music
❌ Use automated melody extraction on copyrighted works

---

## 💀 NEXUS PRIME TIPS

**From the trenches of 978 órgãos destroyed:**

1. **Start simple** - Test with Jingle Bells first, then tackle epic themes
2. **Use the demo** - Run `--demo` to see a working example
3. **Test early, test often** - Copy to index.html and play every 10 notes
4. **BPM matters** - Wrong tempo ruins everything, test different values
5. **Square waves rule** - 8-bit = square oscillator, always
6. **Loop smartly** - Make sure loop point sounds natural
7. **KISS principle** - 50 good notes > 200 mediocre notes

**Energy level:** ∞ KAMEHAMEHAAAA
**Bug tolerance:** -999,999,999,999
**Brotherhood:** ETERNAL

---

🔥 **BORA DESGRAÇAR COM MÚSICAS ÉPICAS!** 🔥

💀👑 **I WALK BESIDE YOU!** 👑💀
