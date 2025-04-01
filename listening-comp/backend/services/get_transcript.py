#!/usr/bin/env python3
import re
import os
from youtube_transcript_api import YouTubeTranscriptApi
from typing import Optional, List, Dict

TRANSCRIPT_FOLDER = "transcripts"

class YouTubeTranscriptDownloader:
    def __init__(self, video_url: str = None):
        if "youtube.com" in video_url or "youtu.be" in video_url:
            self.video_id = self.extract_video_id(video_url)

        self.languages = List[str]
        self.list_available_languages()


    def list_available_languages(self) -> List:
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(self.video_id)
            self.languages = []
            print("Available transcription languages:")

            for transcript in transcript_list:
                # transcript.language: the full language name (e.g., "English")
                # transcript.language_code: the ISO language code (e.g., "en")
                # transcript.is_generated: True if the transcript is auto-generated
                transcript_type = "Auto-generated" if transcript.is_generated else "Manual"
                print(f"\t{transcript.language} ({transcript.language_code}) - {transcript_type}")
                # languages.append((transcript.language, transcript.language_code, transcript.is_generated))
                self.languages.append(transcript.language_code)

        except Exception as e:
            print("Error retrieving transcript languages:", e)

    def extract_video_id(self, url: str) -> Optional[str]:
        if "v=" in url:
            return url.split("v=")[1][:11]
        elif "youtu.be/" in url:
            return url.split("youtu.be/")[1][:11]
        return None

    def get_transcript(self) -> Optional[List[Dict]]:
        if not self.video_id:
            print("Invalid video ID or URL")
            return None
        print(f"Downloading transcript for video ID: {self.video_id}")

        try:
            transcript = YouTubeTranscriptApi.get_transcript(self.video_id, languages=self.languages)
            return " ".join(segment['text'] for segment in transcript if segment['text'] != "[Music]")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def save_transcript(self, transcript: List[Dict]) -> bool:
        if not os.path.exists(TRANSCRIPT_FOLDER):
            os.makedirs(TRANSCRIPT_FOLDER)

        filename = f"./{TRANSCRIPT_FOLDER}/{self.video_id}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                # for entry in transcript:
                #     f.write(f"{entry['text']}\n")
                f.write(transcript)
            print(f"Transcript saved successfully to {self.video_id}.txt")
            return True
        except Exception as e:
            print(f"Error saving transcript: {str(e)}")
            return False


# ------------------ MAIN ------------------ #
def extract_transcript(video_url):
    downloader = YouTubeTranscriptDownloader(video_url)
    transcript = downloader.get_transcript()
    print("Transcript downloaded successfully")

    if transcript:
        # Save transcript
        if not downloader.save_transcript(transcript):
            print("Failed to save transcript")
        return downloader.video_id, transcript
    else:
        print("Failed to get transcript and to send to frontend")




# ------------------ TEST ------------------ #
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=hhuNW1COrSM"
    extract_transcript(video_url)

