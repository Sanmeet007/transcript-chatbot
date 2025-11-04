from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled


def fetch_transcript(video_id: str):
    ytt_api = YouTubeTranscriptApi()
    ytt_transcript = ytt_api.fetch(video_id)
    return " ".join(
        map(
            lambda x: x["text"],
            ytt_transcript.to_raw_data(),
        ),
    )  # type: ignore
