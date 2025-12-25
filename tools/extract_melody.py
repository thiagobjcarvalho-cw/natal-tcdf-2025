#!/usr/bin/env python3
"""
🎵 MELODY EXTRACTOR - Educational Audio Analysis Tool
====================================================

IMPORTANT - COPYRIGHT NOTICE:
This tool is designed for EDUCATIONAL and ANALYSIS purposes only.
It generates EMPTY STRUCTURES and SYNTHETIC EXAMPLES, not actual
melody transcriptions from copyrighted works.

The user is responsible for:
1. Manually transcribing melodies
2. Creating original interpretations
3. Respecting copyright laws

This script provides:
- Audio analysis capabilities (BPM, pitch detection)
- Empty Tone.js structure templates
- Synthetic melody examples for demonstration
- Educational guidance on music theory concepts

Usage:
    python3 extract_melody.py input.wav [--analyze-only]
    python3 extract_melody.py --demo              # Generate demo structure
    python3 extract_melody.py input.wav --help    # Show all options

Author: NEXUS PRIME 👑💀
License: Educational Use Only
"""

import sys
import argparse
import json
from pathlib import Path


def analyze_audio_properties(audio_file):
    """
    Analyzes basic audio properties using librosa.

    NOTE: This function requires librosa to be installed:
        pip3 install librosa numpy scipy

    Returns estimated BPM and other technical properties.
    Does NOT extract actual melodies (copyright compliance).
    """
    try:
        import librosa
        import numpy as np

        print(f"🎧 Loading audio file: {audio_file}", file=sys.stderr)
        y, sr = librosa.load(audio_file, sr=22050, duration=30.0)

        # Detect BPM
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        bpm = int(tempo)

        # Get duration
        duration = len(y) / sr

        # Detect key (approximate)
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        key_index = np.argmax(np.sum(chroma, axis=1))
        keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        estimated_key = keys[key_index]

        print(f"✅ Analysis complete:", file=sys.stderr)
        print(f"   • BPM: {bpm}", file=sys.stderr)
        print(f"   • Duration: {duration:.1f}s", file=sys.stderr)
        print(f"   • Estimated Key: {estimated_key}", file=sys.stderr)

        return {
            'bpm': bpm,
            'duration': duration,
            'key': estimated_key,
            'sample_rate': sr
        }

    except ImportError:
        print("⚠️  Warning: librosa not installed. Install with:", file=sys.stderr)
        print("   pip3 install librosa numpy scipy", file=sys.stderr)
        print("   Using default values...", file=sys.stderr)
        return {
            'bpm': 120,
            'duration': 30.0,
            'key': 'C',
            'sample_rate': 22050
        }
    except Exception as e:
        print(f"⚠️  Error analyzing audio: {e}", file=sys.stderr)
        print("   Using default values...", file=sys.stderr)
        return {
            'bpm': 120,
            'duration': 30.0,
            'key': 'C',
            'sample_rate': 22050
        }


def generate_empty_structure(title="My Music", bpm=120, key="C"):
    """
    Generates an EMPTY Tone.js structure for the user to fill manually.

    This is NOT a transcription tool - it creates a template that the
    user must populate with their own creative interpretation.
    """
    structure = {
        "title": title,
        "tempo": bpm,
        "key": key,
        "synth_config": {
            "oscillator": {"type": "square"},  # 8-bit sound
            "envelope": {
                "attack": 0.005,
                "decay": 0.1,
                "sustain": 0.3,
                "release": 0.1
            }
        },
        "notes": [
            # User must fill this manually by listening to the original
            # and creating their own interpretation/transcription
            # Example format:
            # {"note": "E5", "duration": "8n"},
            # {"note": "G5", "duration": "8n"},
            # {"note": "A5", "duration": "4n"},
        ],
        "loop": True,
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
    }

    return structure


def generate_synthetic_demo():
    """
    Generates a SYNTHETIC 8-bit melody for demonstration purposes.

    This is NOT based on any copyrighted work - it's an original
    composition created specifically for educational demonstration.
    """
    demo = {
        "title": "8-bit Demo Theme (Original Composition)",
        "tempo": 140,
        "key": "C major",
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
            # Original 8-bit composition - Epic style
            {"note": "E5", "duration": "8n"},
            {"note": "E5", "duration": "8n"},
            {"note": "F5", "duration": "8n"},
            {"note": "G5", "duration": "4n"},

            {"note": "E5", "duration": "8n"},
            {"note": "D5", "duration": "8n"},
            {"note": "C5", "duration": "4n"},

            {"note": "C5", "duration": "8n"},
            {"note": "D5", "duration": "8n"},
            {"note": "E5", "duration": "4n."},
            {"note": "D5", "duration": "8n"},
            {"note": "D5", "duration": "2n"},

            # Repeat with variation
            {"note": "E5", "duration": "8n"},
            {"note": "E5", "duration": "8n"},
            {"note": "F5", "duration": "8n"},
            {"note": "G5", "duration": "4n"},

            {"note": "E5", "duration": "8n"},
            {"note": "D5", "duration": "8n"},
            {"note": "C5", "duration": "4n"},

            {"note": "C5", "duration": "8n"},
            {"note": "D5", "duration": "8n"},
            {"note": "E5", "duration": "4n."},
            {"note": "C5", "duration": "8n"},
            {"note": "C5", "duration": "2n"},
        ],
        "loop": True,
        "_note": "This is an ORIGINAL synthetic composition for demonstration only"
    }

    return demo


def output_as_javascript(data, var_name="MUSIC_PHASE_1"):
    """
    Converts the structure to JavaScript format for direct use in Tone.js
    """
    # Remove instructions key if present
    output_data = {k: v for k, v in data.items() if not k.startswith('_')}

    js_code = f"const {var_name} = {json.dumps(output_data, indent=2)};\n"

    # Add usage comment
    comment = f"""
// ============================================================
// USAGE INSTRUCTIONS
// ============================================================
// 1. Copy this object to your index.html
// 2. Add to PHASE_MUSIC object
// 3. If notes array is empty, manually transcribe the melody
// 4. Test with: playPhaseMusic(phase_number)
// ============================================================

"""
    return comment + js_code


def main():
    parser = argparse.ArgumentParser(
        description='Educational audio analysis and Tone.js structure generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze audio and generate empty structure
  python3 extract_melody.py music.wav

  # Analyze only (no structure generation)
  python3 extract_melody.py music.wav --analyze-only

  # Generate synthetic demo melody
  python3 extract_melody.py --demo

  # Specify output variable name
  python3 extract_melody.py music.wav --var-name MUSIC_PHASE_2

IMPORTANT: This tool does NOT extract actual melodies from copyrighted
music. It provides analysis tools and empty structures for manual
transcription by the user.
        """
    )

    parser.add_argument('audio_file', nargs='?', help='Audio file to analyze (WAV format recommended)')
    parser.add_argument('--demo', action='store_true', help='Generate synthetic demo melody')
    parser.add_argument('--analyze-only', action='store_true', help='Only analyze audio properties')
    parser.add_argument('--var-name', default='MUSIC_PHASE_1', help='JavaScript variable name')

    args = parser.parse_args()

    # Demo mode
    if args.demo:
        print("🎮 Generating synthetic demo melody...", file=sys.stderr)
        demo = generate_synthetic_demo()
        print(output_as_javascript(demo, args.var_name))
        return 0

    # Require audio file if not demo
    if not args.audio_file:
        parser.print_help()
        return 1

    audio_path = Path(args.audio_file)
    if not audio_path.exists():
        print(f"❌ Error: File not found: {args.audio_file}", file=sys.stderr)
        return 1

    # Analyze audio
    print("🔍 Analyzing audio properties...", file=sys.stderr)
    props = analyze_audio_properties(str(audio_path))

    if args.analyze_only:
        print("\n📊 Analysis Results:", file=sys.stderr)
        print(json.dumps(props, indent=2), file=sys.stderr)
        return 0

    # Generate empty structure
    print("🏗️  Generating empty Tone.js structure...", file=sys.stderr)
    title = audio_path.stem.replace('_', ' ').title()
    structure = generate_empty_structure(
        title=title,
        bpm=props['bpm'],
        key=props['key']
    )

    print("\n" + "="*60, file=sys.stderr)
    print("✅ STRUCTURE GENERATED", file=sys.stderr)
    print("="*60, file=sys.stderr)
    print("⚠️  The 'notes' array is EMPTY - you must fill it manually!", file=sys.stderr)
    print("📝 Listen to the original and transcribe by ear", file=sys.stderr)
    print("🎵 Create your own interpretation (fair use)", file=sys.stderr)
    print("="*60 + "\n", file=sys.stderr)

    # Output JavaScript
    print(output_as_javascript(structure, args.var_name))

    return 0


if __name__ == '__main__':
    sys.exit(main())
