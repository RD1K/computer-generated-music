# computer-generated-music

This project was begun as part of a hackathon. It randomly generates original piano music and plays it. Also, the audio for the chords and the melody are written to WAV files which you can use in your own music. The patterns are written to MIDI files which you can use with other virtual instruments or samples to create music, using a DAW.

## Example
See a screen recording of this project [here](https://vimeo.com/513632892).

## Setup

To run this program, the `pretty_midi` and `pydub` libraries have to be installed. You can do this via PIP.

Some additional packages have to be installed: [`sox`](http://sox.sourceforge.net/), [`espeak`](http://espeak.sourceforge.net/), and [`fluidsynth`](https://www.fluidsynth.org/).

After this, `git clone` this repository. Then, click [this link](https://www.arachnosoft.com/main/download.php?id=soundfont), download the Soundfont, and then download the Soundfont from [here](http://www.schristiancollins.com/generaluser.php) as well. Extract the files as necessary, and then transfer the .sf2 files to the folder where you have this repository downloaded. Then open main.py and edit the variables at the top, which are the paths to the Soundfont files, to the path it's installed to on your computer. If you're on Linux, it should work without having to change the variables. Now, you can run main.py and use the program.
