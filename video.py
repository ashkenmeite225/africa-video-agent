
from pathlib import Path
from moviepy import ColorClip, TextClip, CompositeVideoClip

def create_video():
    output_dir = Path("videos")
    output_dir.mkdir(exist_ok=True)

    background = ColorClip(
        size=(1080, 1920),
        color=(20, 25, 45),
        duration=10
    )

    title = TextClip(
        text="L'HISTOIRE DE L'AFRIQUE",
        font_size=75,
        color="white",
        size=(900, None),
        method="caption"
    ).with_duration(10).with_position("center")

    video = CompositeVideoClip([background, title])
    video.write_videofile(
        str(output_dir / "premiere_video.mp4"),
        fps=24,
        codec="libx264",
        audio=False
    )

if __name__ == "__main__":
    create_video()
