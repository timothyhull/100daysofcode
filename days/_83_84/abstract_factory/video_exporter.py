#!/usr/bin/env python3
""" Mock video exporter for abstract factory design pattern tests. """

# Imports - Python Standard Library
from abc import ABC, abstractmethod
from os import getcwd
from pathlib import Path

# Constants
AUDIO_DATA = '{audio_data}'
DEFAULT_PATH = getcwd()
VIDEO_DATA = '{video_data}'


# Abstract Factory class to represent the video exporter
class VideoExporter(ABC):
    """ Basic representation of a video exporter. """

    @abstractmethod
    def prepare_export(
        self,
        video_data: str = VIDEO_DATA
    ):
        """ Prepare video data for exporting. """
        pass

    @abstractmethod
    def do_export(
        self,
        folder: Path = DEFAULT_PATH
    ):
        """ Export video file to a folder. """
        pass


# TODO class to represent high-quality video
class HQVideo(VideoExporter):
    """ High-quality video exporter """

    def prepare_export(
        self,
        video_data: str
    ) -> None:
        print('Preparing high-quality video export.')

    def do_export(
        self,
        folder: Path = DEFAULT_PATH
    ) -> None:
        print(f'Exporting high-quality video to "{folder}".')


# TODO class to represent medium-quality video
class MQVideo(VideoExporter):
    """ Medium-quality video exporter """

    def prepare_export(
        self,
        video_data: str
    ) -> None:
        print('Preparing medium-quality video export.')

    def do_export(
        self,
        folder: Path = DEFAULT_PATH
    ) -> None:
        print(f'Exporting medium-quality video to "{folder}".')


# TODO class to represent low-quality video
class LQVideo(VideoExporter):
    """ Low-quality video exporter """

    def prepare_export(
        self,
        video_data: str
    ) -> None:
        print('Preparing low-quality video export.')

    def do_export(
        self,
        folder: Path = DEFAULT_PATH
    ) -> None:
        print(f'Exporting low-quality video to "{folder}".')


# Abstract Factory class to represent the audio exporter
class AudioExporter(ABC):
    """ Basic representation of an audio exporter. """

    @abstractmethod
    def prepare_export(
        self,
        audio_data: str
    ) -> None:
        """ Prepare audio data for exporting. """
        pass

    @abstractmethod
    def do_export(
        self,
        folder: Path
    ) -> None:
        """ Export audio file to a folder. """
        pass


# TODO class to represent high-quality audio
class HQAudio(AudioExporter):
    """ High-quality audio exporter """

    def prepare_export(
        self,
        audio_data: str = AUDIO_DATA
    ) -> None:
        print('Preparing high-quality audio export.')

    def do_export(
        self,
        folder: Path = DEFAULT_PATH
    ) -> None:
        print(f'Exporting high-quality audio to "{folder}".')


# TODO class to represent medium-quality audio
class MQAudio(AudioExporter):
    """ Medium-quality audio exporter """

    def prepare_export(
        self,
        audio_data: str = AUDIO_DATA
    ) -> None:
        print('Preparing medium-quality audio export.')

    def do_export(
        self,
        folder: Path = DEFAULT_PATH
    ) -> None:
        print(f'Exporting medium-quality audio to "{folder}".')


# TODO class to represent low-quality audio
class LQAudio(AudioExporter):
    """ Low-quality audio exporter """

    def prepare_export(
        self,
        audio_data: str = AUDIO_DATA
    ) -> None:
        print('Preparing low-quality audio export.')

    def do_export(
        self,
        folder: Path = DEFAULT_PATH
    ) -> None:
        print(f'Exporting low-quality audio to "{folder}".')


def main() -> None:
    """ Main program. """

    # Collect user input
    quality = input(
        'Choose an export quality (l)ow, (m)edium, or (h)igh: '
    )

    # Create video and audio exporters
    if quality.lower() == 'l':
        video_exporter = LQVideo()
        audio_exporter = LQAudio()

    elif quality.lower() == 'm':
        video_exporter = MQVideo()
        audio_exporter = MQAudio()

    else:
        # Default value: high-quality
        video_exporter = HQVideo()
        audio_exporter = HQAudio()

    # Prepare the export
    video_exporter.prepare_export(
        video_data=VIDEO_DATA
    )
    audio_exporter.prepare_export(
        audio_data=AUDIO_DATA
    )

    # Perform the export
    video_exporter.do_export()
    audio_exporter.do_export()

    return None


if __name__ == '__main__':
    main()
