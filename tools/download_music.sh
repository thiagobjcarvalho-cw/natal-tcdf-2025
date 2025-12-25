#!/bin/bash
# ============================================================================
# 🎵 MUSIC DOWNLOAD TOOL - Educational Audio Sampling
# ============================================================================
#
# IMPORTANT - COPYRIGHT NOTICE:
# This tool is for EDUCATIONAL and ANALYSIS purposes only.
# Downloaded samples are for:
#   - Personal study and analysis
#   - Manual transcription practice
#   - Creating original interpretations
#
# DO NOT:
#   - Redistribute downloaded content
#   - Use samples directly in commercial projects
#   - Violate YouTube's Terms of Service
#
# The user is responsible for respecting copyright laws and platform policies.
#
# ============================================================================
# Usage:
#   ./download_music.sh "https://www.youtube.com/watch?v=..."
#   ./download_music.sh "VIDEO_URL" [output_name]
# ============================================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if yt-dlp is installed
if ! command -v yt-dlp &> /dev/null; then
    echo -e "${RED}❌ Error: yt-dlp not found!${NC}"
    echo ""
    echo "Install with:"
    echo "  Ubuntu/Debian: sudo apt install yt-dlp"
    echo "  Fedora: sudo dnf install yt-dlp"
    echo "  macOS: brew install yt-dlp"
    echo "  pip: pip3 install yt-dlp"
    exit 1
fi

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo -e "${RED}❌ Error: ffmpeg not found!${NC}"
    echo ""
    echo "Install with:"
    echo "  Ubuntu/Debian: sudo apt install ffmpeg"
    echo "  Fedora: sudo dnf install ffmpeg"
    echo "  macOS: brew install ffmpeg"
    exit 1
fi

# Check arguments
if [ $# -lt 1 ]; then
    echo -e "${YELLOW}Usage:${NC}"
    echo "  $0 \"VIDEO_URL\" [output_name]"
    echo ""
    echo -e "${YELLOW}Example:${NC}"
    echo "  $0 \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\""
    echo "  $0 \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\" \"my_song\""
    exit 1
fi

URL="$1"
OUTPUT_NAME="${2:-music_sample}"

echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}🎵 MUSIC DOWNLOAD TOOL${NC}"
echo -e "${BLUE}============================================${NC}"
echo ""
echo -e "${YELLOW}⚠️  EDUCATIONAL USE ONLY${NC}"
echo -e "${YELLOW}⚠️  Respect copyright and platform ToS${NC}"
echo ""
echo -e "${GREEN}URL:${NC} $URL"
echo -e "${GREEN}Output:${NC} ${OUTPUT_NAME}.wav"
echo -e "${GREEN}Duration:${NC} First 30 seconds"
echo ""

# Download audio (first 30 seconds, WAV format)
echo -e "${BLUE}📥 Downloading audio...${NC}"
yt-dlp \
    --extract-audio \
    --audio-format wav \
    --audio-quality 0 \
    --postprocessor-args "ffmpeg:-ss 0 -t 30" \
    --output "${OUTPUT_NAME}.%(ext)s" \
    --no-playlist \
    --quiet \
    --progress \
    "$URL"

# Check if download succeeded
if [ ! -f "${OUTPUT_NAME}.wav" ]; then
    echo -e "${RED}❌ Download failed!${NC}"
    exit 1
fi

# Get file size
FILE_SIZE=$(du -h "${OUTPUT_NAME}.wav" | cut -f1)

echo ""
echo -e "${GREEN}✅ Download complete!${NC}"
echo -e "${GREEN}📁 File:${NC} ${OUTPUT_NAME}.wav (${FILE_SIZE})"
echo ""
echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}NEXT STEPS:${NC}"
echo -e "${BLUE}============================================${NC}"
echo "1. Analyze the audio:"
echo "   python3 extract_melody.py \"${OUTPUT_NAME}.wav\" --analyze-only"
echo ""
echo "2. Generate Tone.js structure:"
echo "   python3 extract_melody.py \"${OUTPUT_NAME}.wav\" > output.js"
echo ""
echo "3. Manually transcribe the melody by listening"
echo "   and fill the 'notes' array in output.js"
echo ""
echo -e "${YELLOW}⚠️  Remember: Create your own interpretation!${NC}"
echo -e "${BLUE}============================================${NC}"
