import pretty_midi
from playsound import playsound
from os import system
from random import randint

drumSfDir = "~/Documents/HackathonProject/'6252-Rock%20drums.sf2'"

tempo = randint(80, 160)
beatLength = 60/tempo
drumPattern = pretty_midi.PrettyMIDI(initial_tempo=tempo)

drum_program = pretty_midi.instrument_name_to_program("Synth Drum")
drum = pretty_midi.Instrument(program=drum_program)

for x in range(36,40):
    note = pretty_midi.Note(velocity = 100, pitch = x, start = (x*(beatLength/4)), end = ((x*(beatLength/4)) + (beatLength/4)))
    drum.notes.append(note)
    drumPattern.instruments.append(drum)
    drumPattern.write("drums.mid")

    system("fluidsynth -ni %s drums.mid -F drums.wav -r 44100 2>/dev/null" % drumSfDir)
    print(x)
    playsound("drums.wav")
