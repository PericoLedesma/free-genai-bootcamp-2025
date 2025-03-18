#!/usr/bin/env python3
import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi

DEFAULT_URL= "https://www.youtube.com/watch?v=PNTCM7cbrsc"
def extract_video_id(url=DEFAULT_URL):
    """Extracts the YouTube video ID from a URL."""
    regex_patterns = [
        r"youtu\.be\/([^?&]+)",
        r"youtube\.com\/watch\?v=([^?&]+)",
        r"youtube\.com\/embed\/([^?&]+)"
    ]
    for pattern in regex_patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def main():
    if len(sys.argv) < 2:
        print(f"No YouTube URL provided. Using default URL: {DEFAULT_URL}")
        url = DEFAULT_URL
    else:
        url = sys.argv[1]

    video_id = extract_video_id(url)
    if not video_id:
        print("Error: Could not extract video ID from the URL.")
        sys.exit(1)

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        sys.exit(1)

    # # Print each transcript segment
    # for segment in transcript:
    #     print(segment['text'])
    print(transcript)


if __name__ == "__main__":
    main()
