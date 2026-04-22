# Music Player and Playlist Scheduler

# Class representing a single track
class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist

        # Parse 'mm:ss' → total seconds
        mins, secs = map(int, duration.split(":"))
        self.seconds = mins * 60 + secs

    # Property to convert seconds → 'mm:ss'
    @property
    def formatted_duration(self):
        mins = self.seconds // 60
        secs = self.seconds % 60
        return f"{mins}:{secs:02d}"

    # Dunder method for string representation
    def __str__(self):
        return f"{self.title} by {self.artist} [{self.formatted_duration}]"


# Class representing playlist
class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    # Add track to playlist
    def add(self, track):
        self.tracks.append(track)

    # Remove track from playlist
    def remove(self, track):
        if track in self.tracks:
            self.tracks.remove(track)

    # Total duration of playlist → 'mm:ss'
    def total_duration(self):
        total_seconds = sum(t.seconds for t in self.tracks)
        mins = total_seconds // 60
        secs = total_seconds % 60
        return f"{mins}:{secs:02d}"

    # Longest track
    def longest_track(self):
        return max(self.tracks, key=lambda t: t.seconds)

    # Shortest track
    def shortest_track(self):
        return min(self.tracks, key=lambda t: t.seconds)

    # Average duration → 'mm:ss'
    def average_duration(self):
        total_seconds = sum(t.seconds for t in self.tracks)
        avg = total_seconds // len(self.tracks)
        mins = avg // 60
        secs = avg % 60
        return f"{mins}:{secs:02d}"

    # Tracks shorter than given seconds
    def tracks_under(self, limit):
        return [t.title for t in self.tracks if t.seconds < limit]

    # Summary of playlist
    def summary(self):
        return f"{self.name} | {len(self.tracks)} tracks | Total: {self.total_duration()} | Avg: {self.average_duration()}"


# Main execution
def main():
    try:
        tracks = [
            Track("Blinding Lights", "The Weeknd", "3:20"),
            Track("Levitating", "Dua Lipa", "3:23"),
            Track("Stay", "Kid LAROI", "2:21"),
            Track("Peaches", "Justin Bieber", "3:18"),
            Track("Good 4 U", "Olivia Rodrigo", "2:58"),
        ]

        playlist = Playlist("Evening Vibes")

        # Add tracks to playlist
        for t in tracks:
            playlist.add(t)

        # Outputs
        print(str(tracks[0]))                     # String representation
        print(tracks[0].seconds)                 # Duration in seconds

        print(playlist.total_duration())         # Total duration
        print(playlist.longest_track())          # Longest track
        print(playlist.shortest_track())         # Shortest track
        print(playlist.average_duration())       # Average duration
        print(playlist.tracks_under(200))        # Tracks under 200 sec
        print(playlist.summary())                # Summary

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()