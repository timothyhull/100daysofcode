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


# TODO class that abstracts the video and audio exporters.
class ExporterFactory(ABC):
    """ Factory that represents a combo of video and audio codecs.

        The factory does not maintain any of the instances it creates.
    """

    # Is the @abstractmethod decorator required?
    # @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        """ Returns a new instance of the VideoExporter class. """
        pass

    # Is the @abstractmethod decorator required?
    # @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        """ Returns a new instance of the AudioExporter class. """
        pass


# Concrete factory class that creates lower-quality A/V export objects
class FastExporter(ExporterFactory):
    """ Factory that provides lower-quality, high-speed exports. """

    def get_video_exporter(self) -> VideoExporter:
        """ Returns a new instance of the VideoExporter class. """
        return LQVideo()

    def get_audio_exporter(self) -> AudioExporter:
        """ Returns a new instance of the AudioExporter class. """
        return LQAudio()


# Concrete factory class that creates medium-quality A/V export objects
class MediumExporter(ExporterFactory):
    """ Factory that provides medium-quality, medium-speed exports. """

    def get_video_exporter(self) -> VideoExporter:
        """ Returns a new instance of the VideoExporter class. """
        return MQVideo()

    def get_audio_exporter(self) -> AudioExporter:
        """ Returns a new instance of the AudioExporter class. """
        return MQAudio()


# Concrete factory class that creates higher-quality A/V export objects
class SlowExporter(ExporterFactory):
    """ Factory that provides high-quality, lower-speed exports. """

    def get_video_exporter(self) -> VideoExporter:
        """ Returns a new instance of the VideoExporter class. """
        return HQVideo()

    def get_audio_exporter(self) -> AudioExporter:
        """ Returns a new instance of the AudioExporter class. """
        return HQAudio()


""" Example #1:

    This is an example of the 'main_1' function being responsible for
    too many things.  It is responsible for:

    1. Asking the user for input.
    2. Creating the video and audio exporter objects.
    3. Using the video and audio exporter objects, by way of calling
    their methods that prepare and export audio/video.

    This also means:
        1. The 'main_1' function has to be aware of the existence of
        each class in this file.
        2. Many if/else statements are necessary in order to allow the
        selection of the built-in quality settings, plus any possible
        custom quality settings.
"""


def main_1() -> None:
    """ Main program #1. """

    # Collect user input
    while True:
        quality = input(
            'Choose an export quality (l)ow, (m)edium, or (h)igh: '
        )

        if quality.lower() in {'l', 'm', 'h'}:
            break

        else:
            print('\nUnknown option "{}"\n')

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


def collect_user_input() -> ExporterFactory:
    """ Collect user input.

        Relocated from the main_1 function, to separate user input
        collection from the main application.  Now creates an
        ExporterFactory object, instead of returning a string.
    """

    # Define a factories dictionary, for quick reference
    factories = dict(
        l=FastExporter(),
        m=MediumExporter(),
        h=SlowExporter()
    )

    while True:
        quality = input(
            'Choose an export quality (l)ow, (m)edium, or (h)igh: '
        ).lower()

        if quality not in factories:
            print('\nUnknown option "{}"\n')

        else:
            return factories(quality)


def main_2() -> None:
    """ Main program #2. """

    # Collect user input
    # quality = collect_user_input()

    return None


if __name__ == '__main__':
    main_1()
