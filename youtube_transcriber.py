#!/usr/bin/env python3

import re
import sys
from datetime import timedelta
try:
    from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
    from pytube import YouTube
except ImportError:
    print("Error: Required packages not found.")
    print("Please install them using: pip install -r requirements.txt")
    sys.exit(1)

def extract_video_id(url):
    """
    Extract the YouTube video ID from different URL formats or raw ID.
    Supports:
    - Full YouTube URLs (https://www.youtube.com/watch?v=VIDEO_ID)
    - Short YouTube URLs (https://youtu.be/VIDEO_ID)
    - Raw video IDs
    """
    # Check if input might be a raw video ID (typically 11 characters)
    if re.match(r'^[A-Za-z0-9_-]{11}$', url):
        return url
    
    # Extract from standard YouTube URL
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    if match:
        return match.group(1)
    
    return None

def get_video_title(video_id):
    """Fetch video title from YouTube"""
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        yt = YouTube(url)
        return yt.title
    except Exception as e:
        print(f"Warning: Could not fetch video title: {str(e)}")
        return None

def format_timestamp(seconds):
    """Convert seconds to [mm:ss] format"""
    time_obj = timedelta(seconds=seconds)
    minutes, seconds = divmod(int(time_obj.total_seconds()), 60)
    return f"[{minutes:02d}:{seconds:02d}]"

def get_transcript(video_id):
    """Fetch transcript for a YouTube video"""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except NoTranscriptFound:
        print(f"Error: No transcript found for video ID: {video_id}")
        return None
    except TranscriptsDisabled:
        print(f"Error: Transcripts are disabled for video ID: {video_id}")
        return None
    except Exception as e:
        print(f"Error: Failed to fetch transcript: {str(e)}")
        return None

def display_and_save_transcript(transcript, video_id, video_title):
    """Display transcript in the terminal and save to a file"""
    if not transcript:
        return False
    
    # Prepare formatted transcript
    formatted_lines = []
    
    # Display video title if available
    title_header = f"Title: {video_title}" if video_title else f"Video ID: {video_id}"
    print(f"\n--- TRANSCRIPT ---")
    print(f"{title_header}\n")
    
    for item in transcript:
        timestamp = format_timestamp(item['start'])
        text = item['text']
        formatted_line = f"{timestamp} {text}"
        formatted_lines.append(formatted_line)
        print(formatted_line)
    
    # Save to file
    filename = "transcript_with_timestamps.txt"
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            if video_title:
                file.write(f"Title: {video_title}\n")
            file.write(f"Video ID: {video_id}\n\n")
            file.write("\n".join(formatted_lines))
        print(f"\nTranscript saved to {filename}")
        return True
    except Exception as e:
        print(f"\nError: Failed to save transcript to file: {str(e)}")
        return False

def main():
    print("YouTube Video Transcriber")
    print("-------------------------")
    url = input("Paste a YouTube URL or video ID: ").strip()
    
    video_id = extract_video_id(url)
    if not video_id:
        print("Error: Could not extract a valid YouTube video ID.")
        sys.exit(1)
    
    print(f"Fetching data for video ID: {video_id}")
    
    # Get video title
    video_title = get_video_title(video_id)
    if video_title:
        print(f"Video title: {video_title}")
    
    # Get transcript
    transcript = get_transcript(video_id)
    
    if transcript:
        display_and_save_transcript(transcript, video_id, video_title)
    else:
        print("Could not process transcript. Please try another video.")

if __name__ == "__main__":
    main() 