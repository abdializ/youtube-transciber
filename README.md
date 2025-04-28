# YouTube Video Transcriber

A simple Python tool to extract and format transcripts from YouTube videos. I made this in one sitting around 1 hour, because youtube api is new to me. But have fun anyone seeing this

## Features

- Extract transcript from any YouTube video with available captions
- Display timestamps in [mm:ss] format alongside each line of speech
- Displays the YouTube video title
- Save transcripts automatically to a text file
- Support for various YouTube URL formats and raw video IDs
- Graceful error handling for videos without captions

## Installation

1. Make sure you have Python 3 installed
2. Install the required dependencies:
3. I would advise creating a virtual enviroment rather globally. 

```bash
pip install -r requirements.txt
```

## Usage purposes

Run the script and follow the prompts:

```bash
python youtube_transcriber.py
```

When prompted, paste a YouTube URL (any format) or just the video ID.

The transcript with the video title will be displayed in the terminal and automatically saved to `transcript_with_timestamps.txt` in the same directory.

## Examples

The tool accepts:
- Full YouTube URLs: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- Short YouTube URLs: `https://youtu.be/dQw4w9WgXcQ`
- Raw video IDs: `dQw4w9WgXcQ` # youtube-transciber
