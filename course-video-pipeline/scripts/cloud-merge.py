# © 2026 Kumar Chandrasekhar, PhD
# Department of General Education & Academic Development Centre
# Mount Royal University, Calgary, Alberta, Canada
#
# Licensed under the MIT License — see LICENSE.md for full terms.
# https://opensource.org/licenses/MIT

#!/usr/bin/env python3
"""
cloud-merge.py — Course Video Pipeline cloud merge
Uses Fal.ai API — no FFmpeg required.

Usage: python cloud-merge.py <slug>
Requires: pip install fal-client requests
API key: set FAL_KEY environment variable
"""

import sys
import os
import json
import time
import requests
from pathlib import Path

try:
    import fal_client
except ImportError:
    print("ERROR: fal-client not installed.")
    print("Run: pip install fal-client")
    sys.exit(1)

# ── EDIT THESE BEFORE RUNNING ────────────────────────────────
END_CARD_LINES = [
    "",                          # Line 1: citation (leave empty if none)
    "AI narration: ElevenLabs",
    "AI visuals: Fal.ai (image-to-video)",
    "© 2026 Instructor Name, Institution",  # ← update this
]
END_CARD_DURATION = 4           # seconds
FADE_DURATION = 0.5             # seconds
# ─────────────────────────────────────────────────────────────

def check_api_key():
    key = os.environ.get('FAL_KEY')
    if not key:
        print("ERROR: FAL_KEY environment variable not set.")
        print("Get your key at https://fal.ai/dashboard/keys")
        print("Then run: export FAL_KEY='your-key-here'  (macOS/Linux)")
        print("         set FAL_KEY=your-key-here        (Windows CMD)")
        sys.exit(1)
    return key

def upload_file(filepath):
    """Upload a file to Fal.ai storage and return the URL."""
    print(f"  Uploading {filepath.name}...")
    url = fal_client.upload_file(str(filepath))
    print(f"  Uploaded: {url}")
    return url

def get_audio_duration_from_api(audio_url):
    """Use Fal.ai to get audio duration without ffprobe."""
    result = fal_client.run(
        "fal-ai/ffmpeg-api/probe",
        arguments={"url": audio_url}
    )
    return float(result.get('duration', 60))

def merge_video_audio(video_url, audio_url, duration):
    """Loop video to audio duration with fades using Fal.ai FFmpeg API."""
    print("  Merging video + audio...")
    fade_out = duration - FADE_DURATION
    result = fal_client.run(
        "fal-ai/ffmpeg-api",
        arguments={
            "inputs": [
                {"url": video_url, "stream_loop": -1},
                {"url": audio_url}
            ],
            "filters": [
                f"fade=t=in:st=0:d={FADE_DURATION}",
                f"fade=t=out:st={fade_out}:d={FADE_DURATION}"
            ],
            "duration": duration,
            "output_format": "mp4"
        }
    )
    return result.get('url') or result.get('video', {}).get('url')

def generate_end_card(lines, duration):
    """Generate end card image via Fal.ai, then convert to short video."""
    active = [l for l in lines if l.strip()]
    text_block = '\n'.join(active)

    print("  Generating end card...")
    # Generate end card as image first
    img_result = fal_client.run(
        "fal-ai/flux/schnell",
        arguments={
            "prompt": f"Black background, white text centered: {text_block}. "
                      "Clean, minimal, professional. No decorations.",
            "image_size": "landscape_16_9",
            "num_inference_steps": 4,
        }
    )
    img_url = img_result['images'][0]['url']

    # Convert static image to short video clip
    vid_result = fal_client.run(
        "fal-ai/kling-video/v2/image-to-video",
        arguments={
            "image_url": img_url,
            "duration": str(duration),
            "prompt": "completely still, no motion, static frame",
        }
    )
    return vid_result.get('video', {}).get('url')

def concatenate_clips(clip_urls):
    """Concatenate multiple video clips."""
    print("  Concatenating clips...")
    result = fal_client.run(
        "fal-ai/ffmpeg-api/concat",
        arguments={
            "inputs": [{"url": u} for u in clip_urls],
            "output_format": "mp4"
        }
    )
    return result.get('url') or result.get('video', {}).get('url')

def download_file(url, output_path):
    """Download the final video."""
    print(f"  Downloading to {output_path.name}...")
    response = requests.get(url, stream=True)
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

def main():
    if len(sys.argv) < 2:
        print("Usage: python cloud-merge.py <slug>")
        sys.exit(1)

    check_api_key()
    slug = sys.argv[1]
    cwd = Path.cwd()

    audio_file = cwd / f"{slug}.mp3"
    video_raw  = cwd / f"{slug}-raw.mp4"
    output     = cwd / f"{slug}.mp4"

    for f in [audio_file, video_raw]:
        if not f.exists():
            print(f"ERROR: Required file not found: {f}")
            sys.exit(1)

    print(f"\nCourse Video Pipeline — Cloud Merge")
    print(f"Slug: {slug}")
    print(f"Note: This will use Fal.ai API credits (~$0.02–0.05)\n")

    # Upload source files
    print("Step 1: Uploading source files...")
    audio_url = upload_file(audio_file)
    video_url = upload_file(video_raw)

    # Get duration
    print("\nStep 2: Getting audio duration...")
    try:
        duration = get_audio_duration_from_api(audio_url)
    except Exception:
        # Fallback: assume 60s if API doesn't support probe
        duration = 60.0
        print("  Could not probe duration — defaulting to 60s")
        print("  Edit duration manually if incorrect")
    print(f"  Duration: {duration:.1f}s")

    # Merge video + audio
    print("\nStep 3: Merging video and audio...")
    merged_url = merge_video_audio(video_url, audio_url, duration)
    print(f"  Merged: {merged_url}")

    # Generate end card
    print("\nStep 4: Generating end card...")
    end_card_url = generate_end_card(END_CARD_LINES, END_CARD_DURATION)
    print(f"  End card: {end_card_url}")

    # Concatenate
    print("\nStep 5: Concatenating main video + end card...")
    final_url = concatenate_clips([merged_url, end_card_url])
    print(f"  Final: {final_url}")

    # Download
    print("\nStep 6: Downloading final video...")
    download_file(final_url, output)

    size_mb = output.stat().st_size / (1024 * 1024)
    print(f"\n✓ Done: {output}")
    print(f"  Size: {size_mb:.1f} MB")

if __name__ == '__main__':
    main()