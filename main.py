'''
This is the main file of the program.
'''

import pretty_midi
from os import system
from random import randrange, randint
from playsound import playsound
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

# for note_name in scaleNotes:
#     note_number = pretty_midi.note_name_to_number(note_name + "5")
#     if note_number < previousNoteNumber:
#         note_number += 12
#     note = pretty_midi.Note(velocity=127, pitch = note_number, start=startTime, end=(beatLength))
#     piano.notes.append(note)
#     startTime += beatLength
#     previousNoteNumber = note_number

chordProgressionRoots = []
for x in range(1,8):
    chordProgressionRoots.append(scaleNotes[randrange(1,7)])

chordDict = chordMaker.buildChord(chordProgressionRoots, scaleNotes)

startTime = 0
for key, value in chordDict.items():
    print(value)


pianoMelody.instruments.append(piano)
pianoMelody.write("pianoMelody.mid")

# synthesizes the MIDI using the soundfont
system("fluidsynth -ni %s pianoMelody.mid -F output.wav -r 44100 2>/dev/null" % sfDir)
playsound("output.wav")
