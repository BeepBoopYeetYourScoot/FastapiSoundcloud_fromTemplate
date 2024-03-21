from pydub import AudioSegment


def add_silence_in_track(
    track: AudioSegment, start_pause_ms=0, end_pause_ms=1000, duration_ms=1000
) -> AudioSegment:
    silence_gap = AudioSegment.silent(duration=duration_ms)
    return track[:start_pause_ms] + silence_gap + track[end_pause_ms:]
