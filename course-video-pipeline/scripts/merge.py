# © 2026 Kumar Chandrasekhar, PhD
# Department of General Education & Academic Development Centre
# Mount Royal University, Calgary, Alberta, Canada
#
# Licensed under the MIT License — see LICENSE.md for full terms.
# https://opensource.org/licenses/MIT

#!/usr/bin/env python3
"""
merge.py — Course Video Pipeline merge script
Cross-platform (macOS, Windows, Linux)
Requires: ffmpeg installed and on PATH

Usage: python merge.py <slug>
Example: python merge.py ugst1001-p2s1-analogy-forgetting-curve

End card text: edit END_CARD_LINES below before running.
"""

import sys
import os
import shutil
import subprocess
import platform
from pathlib import Path

# ── EDIT THESE BEFORE RUNNING ────────────────────────────────
END_CARD_LINES = [
    "",                          # Line 1: citation (leave empty if none)
    "AI narration: ElevenLabs",
    "AI visuals: Fal.ai (image-to-video)",
    "© 2026 Instructor Name, Institution",  # ← update this
]
END_CARD_DURATION = 4           # seconds
FADE_DURATION_VIDEO = 0.5       # seconds
FADE_DURATION_AUDIO = 0.3       # seconds
# ─────────────────────────────────────────────────────────────

def check_ffmpeg():
    if not shutil.which('ffmpeg') or not shutil.which('ffprobe'):
        print("ERROR: ffmpeg/ffprobe not found on PATH.")
        print("See references/ffmpeg-setup.md for installation instructions.")
        sys.exit(1)

def get_duration(filepath):
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'default=noprint_wrappers=1:nokey=1', str(filepath)],
        capture_output=True, text=True
    )
    return float(result.stdout.strip())

def find_font():
    """Find a suitable system font cross-platform."""
    system = platform.system()
    candidates = []
    if system == 'Windows':
        candidates = [
            r'C:\Windows\Fonts\arial.ttf',
            r'C:\Windows\Fonts\calibri.ttf',
            r'C:\Windows\Fonts\segoeui.ttf',
        ]
    elif system == 'Darwin':  # macOS
        candidates = [
            '/System/Library/Fonts/Helvetica.ttc',
            '/Library/Fonts/Arial.ttf',
            '/System/Library/Fonts/SFNS.ttf',
        ]
    else:  # Linux
        candidates = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
            '/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf',
        ]
    for path in candidates:
        if os.path.exists(path):
            return path
    print("WARNING: No system font found. End card text may not render.")
    print("Install DejaVu fonts or edit find_font() in merge.py.")
    return candidates[0] if candidates else ''

def escape_drawtext(text):
    """Escape special characters for FFmpeg drawtext filter."""
    return text.replace('\\', '\\\\').replace(':', '\\:').replace("'", "\\'") \
               .replace(',', '\\,').replace('[', '\\[').replace(']', '\\]')

def build_drawtext_filter(lines, font, duration):
    """Build FFmpeg drawtext filter for end card."""
    # Filter out empty lines, calculate vertical positions
    active = [(i, l) for i, l in enumerate(lines) if l.strip()]
    n = len(active)
    line_height = 44
    total_height = (n - 1) * line_height
    sizes = [28, 22, 22, 20]
    colors = ['white', 'gray', 'gray', 'gray']

    filters = []
    for rank, (orig_idx, line) in enumerate(active):
        y_offset = (rank - n // 2) * line_height - (line_height // 2 if n % 2 == 0 else 0)
        size = sizes[min(orig_idx, len(sizes)-1)]
        color = colors[min(orig_idx, len(colors)-1)]
        escaped = escape_drawtext(line)
        filters.append(
            f"drawtext=text='{escaped}'"
            f":fontcolor={color}:fontsize={size}"
            f":x=(w-text_w)/2:y=(h-text_h)/2+{y_offset}"
            f":fontfile='{font}'"
        )

    fade_in = f"fade=t=in:st=0:d=0.5"
    fade_out = f"fade=t=out:st={duration - 0.5}:d=0.5"
    return ','.join(filters + [fade_in, fade_out])

def run(cmd, desc=''):
    print(f"\n→ {desc}" if desc else '')
    print(' '.join(str(c) for c in cmd))
    result = subprocess.run(cmd, capture_output=False)
    if result.returncode != 0:
        print(f"ERROR: FFmpeg failed on step: {desc}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python merge.py <slug>")
        print("Example: python merge.py ugst1001-p2s1-analogy-forgetting-curve")
        sys.exit(1)

    check_ffmpeg()
    slug = sys.argv[1]
    cwd = Path.cwd()

    audio_file = cwd / f"{slug}.mp3"
    video_raw  = cwd / f"{slug}-raw.mp4"
    no_card    = cwd / f"{slug}-nocard.mp4"
    end_card   = cwd / f"{slug}-endcard.mp4"
    concat_txt = cwd / "concat.txt"
    output     = cwd / f"{slug}.mp4"

    # Validate inputs
    for f in [audio_file, video_raw]:
        if not f.exists():
            print(f"ERROR: Required file not found: {f}")
            sys.exit(1)

    duration = get_duration(audio_file)
    print(f"\nAudio duration: {duration:.2f}s")
    fade_out_start_v = duration - FADE_DURATION_VIDEO
    fade_out_start_a = duration - FADE_DURATION_AUDIO
    font = find_font()
    print(f"Using font: {font}")

    # Step 1: Loop video to audio length with fades
    run([
        'ffmpeg', '-y',
        '-stream_loop', '-1', '-i', str(video_raw),
        '-i', str(audio_file),
        '-t', str(duration),
        '-vf', f'fade=t=in:st=0:d={FADE_DURATION_VIDEO},'
               f'fade=t=out:st={fade_out_start_v}:d={FADE_DURATION_VIDEO}',
        '-af', f'afade=t=in:st=0:d={FADE_DURATION_AUDIO},'
               f'afade=t=out:st={fade_out_start_a}:d={FADE_DURATION_AUDIO}',
        '-c:v', 'libx264', '-c:a', 'aac', '-shortest',
        str(no_card)
    ], 'Step 1: Loop video + add fades')

    # Step 2: Generate end card
    drawtext = build_drawtext_filter(END_CARD_LINES, font, END_CARD_DURATION)
    run([
        'ffmpeg', '-y',
        '-f', 'lavfi',
        '-i', f'color=c=black:size=1920x1080:duration={END_CARD_DURATION}:rate=24',
        '-vf', drawtext,
        str(end_card)
    ], 'Step 2: Generate end card')

    # Step 3: Concatenate
    concat_txt.write_text(
        f"file '{no_card.as_posix()}'\nfile '{end_card.as_posix()}'\n"
    )
    run([
        'ffmpeg', '-y',
        '-f', 'concat', '-safe', '0', '-i', str(concat_txt),
        '-c:v', 'libx264', '-c:a', 'aac',
        str(output)
    ], 'Step 3: Concatenate main video + end card')

    # Cleanup
    for f in [no_card, end_card, concat_txt]:
        f.unlink(missing_ok=True)

    size_mb = output.stat().st_size / (1024 * 1024)
    print(f"\n✓ Done: {output}")
    print(f"  Size: {size_mb:.1f} MB")
    if size_mb > 10:
        print("  WARNING: File exceeds 10MB. Consider re-encoding with -crf 28.")

if __name__ == '__main__':
    main()