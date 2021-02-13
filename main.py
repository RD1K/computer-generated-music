'''
This is the main file of the program.
'''

import pretty_midi
from os import system
from random import randrange, randint, uniform
from playsound import playsound
from pysndfx import AudioEffectsChain

import generateScale
import chordMaker

tempo = randint(80, 150)
beatLength = 60/tempo
print("Tempo: " + str(tempo) + " BPM")

# path to the soundfont
sfDir = "~/Documents/HackathonProject/'GeneralUser GS v1.471.sf2'"

# randomly chooses key and scale
scaleType = generateScale.scales[randrange(len(generateScale.scales))]
keyChoice = generateScale.notes[randrange(len(generateScale.notes))]
print("Key: " + keyChoice + " " + scaleType + "\n")

# determines notes based on key and scale
if scaleType == "Minor":
    scaleNotes = generateScale.minorScale(keyChoice)
elif scaleType == "Major":
    scaleNotes = generateScale.majorScale(keyChoice)

print(scaleNotes)

# creates the pretty_midi object
pianoMelody = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# sets the name based on MIDI standards
piano_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
piano = pretty_midi.Instrument(program=piano_program)

startTime = 0
previousNoteNumber = 0

chordProgression = generateScale.chordProgressions[randrange(len(generateScale.chordProgressions))]
chordDict = chordMaker.buildChord(chordProgression, scaleNotes)

startTime = 0
for key, value in chordDict.items():
    print(value)
    for note_name in value:
        nameWithoutOct = note_name
        for x in range(4,6):
            note_name = nameWithoutOct + str(x)
            note_number = pretty_midi.note_name_to_number(note_name)
            note = pretty_midi.note_name_to_number(note_name)
            velocity = randint(105,127)
            delay = round(uniform(0,0.05), 3) # generates a random amount of delay to make it sound more natural/realistic
            note = pretty_midi.Note(velocity = velocity, pitch = note_number, start = (startTime + delay), end = startTime + (4*beatLength))
            piano.notes.append(note)
    startTime += 4*beatLength # each chord plays for 4 beats, which is equal to 1 measure since it's in 4/4

pianoMelody.instruments.append(piano)
pianoMelody.write("pianoMelody.mid")

# synthesizes the MIDI using the soundfont
system("fluidsynth -ni %s pianoMelody.mid -F output.wav -r 44100 2>/dev/null" % sfDir)

playsound("output.wav")
