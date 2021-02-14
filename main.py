'''
This is the main file of the program.
'''

import pretty_midi
from os import system
from random import randrange, randint, uniform
# from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

import generateScale
import chordMaker
import animation

tempo = randint(80, 160)
beatLength = 60/tempo
print("Tempo: " + str(tempo) + " BPM")

# path to the soundfont
chordSfDir = "~/Documents/HackathonProject/'Arachno SoundFont - Version 1.0.sf2'"
melodySfDir = "~/Documents/HackathonProject/'GeneralUser GS v1.471.sf2'"
drumSfDir = "~/Documents/HackathonProject/'Snare.SF2'"

# randomly chooses key and scale
scaleType = generateScale.scales[randrange(len(generateScale.scales))]
keyChoice = generateScale.notes[randrange(len(generateScale.notes))]
print("Key: " + keyChoice + " " + scaleType + "\n")

# determines notes based on key and scale
if scaleType == "Minor":
    scaleNotes = generateScale.minorScale(keyChoice)
elif scaleType == "Major":
    scaleNotes = generateScale.majorScale(keyChoice)

# creates the pretty_midi object
pianoChords = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# sets the name based on MIDI standards
piano_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
piano = pretty_midi.Instrument(program=piano_program)

startTime = 0
previousNoteNumber = 0

chordProgressionRoots = []
for x in range(1,5):
    chordProgressionRoots.append(scaleNotes[randrange(1,7)])
chordDict = chordMaker.buildChord(chordProgressionRoots, scaleNotes)

startTime = 0
for key, value in chordDict.items():
    for note_name in value:
        nameWithoutOct = note_name
        lowestOctave = randint(3,4)
        for x in range(lowestOctave,6): # plays the notes in multiple octaves
            note_name = nameWithoutOct + str(x)
            note_number = pretty_midi.note_name_to_number(note_name)
            note = pretty_midi.note_name_to_number(note_name)
            velocity = randint(105,127)
            delay = round(uniform(0,0.05), 3) # generates a random amount of delay to make it sound more natural/realistic
            note = pretty_midi.Note(velocity = velocity, pitch = note_number, start = (startTime + delay), end = startTime + (4*beatLength))
            piano.notes.append(note)
    startTime += 4*beatLength # each chord plays for 4 beats, which is equal to 1 measure since it's in 4/4

pianoChords.instruments.append(piano)
pianoChords.write("chords.mid")

# creates the pretty_midi object
pianoMelody = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# sets the name based on MIDI standards
piano_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
piano = pretty_midi.Instrument(program=piano_program)

for x in range(0,4):
    startTime = beatLength/2 + (beatLength * x * 4) # makes it start at the next measure
    # ensures that it doesn't play after the new chord starts until supposed to:
    while startTime < (beatLength * 4 * (x+1)):
        noteIndex = randrange(len(scaleNotes))
        note_name = scaleNotes[noteIndex] + "5"
        note_number = pretty_midi.note_name_to_number(note_name)
        note = pretty_midi.note_name_to_number(note_name)
        velocity = randint(105,127)
        delay = round(uniform(0,0.05), 3) # generates a random amount of delay to make it sound more natural/realistic
        length = (beatLength/2)*(randint(1,4))
        note = pretty_midi.Note(velocity = velocity, pitch = note_number, start = (startTime + delay), end = (startTime + length))
        piano.notes.append(note)
        startTime += length

pianoMelody.instruments.append(piano)
pianoMelody.write("melody.mid")

# # creates the pretty_midi object
# drumPattern = pretty_midi.PrettyMIDI(initial_tempo=tempo)
#
# # sets the name based on MIDI standards
# drum_program = pretty_midi.instrument_name_to_program("Synth Drum")
# drum = pretty_midi.Instrument(program=drum_program)

# for x in range(0,4):
#     for y in range(0,62,2):
#         truefalse = randint(2,12)
#         if truefalse == 2:
#             velocity = randint(110,120)
#             delay = round(uniform(0,0.05), 3) # generates a random amount of delay to make it sound more natural/realistic
#             note = pretty_midi.Note(velocity = velocity, pitch = 60, start = (y*(beatLength/4)), end = ((y*(beatLength/4)) + (beatLength/4)))
#             drum.notes.append(note)
#             startTime += beatLength
#         else:
#             pass
#     for y in range(1,63,2):
#         truefalse = randint(2,12)
#         if truefalse == 2:
#             velocity = randint(110,120)
#             delay = round(uniform(0,0.05), 3) # generates a random amount of delay to make it sound more natural/realistic
#             note = pretty_midi.Note(velocity = velocity, pitch = 60, start = (y*(beatLength/4)), end = ((y*(beatLength/4)) + (beatLength/4)))
#             drum.notes.append(note)
#             startTime += beatLength
#         else:
#             pass
#
# drumPattern.instruments.append(drum)
# drumPattern.write("drums.mid")

# synthesizes the MIDI using the soundfont
system("fluidsynth -ni %s chords.mid -F chords.wav -r 44100 2>/dev/null" % chordSfDir)
chords = AudioSegment.from_wav("chords.wav")

system("fluidsynth -ni %s melody.mid -F melody.wav -r 44100 2>/dev/null" % melodySfDir)
melody = AudioSegment.from_wav("melody.wav")

# system("fluidsynth -ni %s drums.mid -F drums.wav -r 44100 2>/dev/null" % drumSfDir)
# drums = AudioSegment.from_wav("drums.wav")

mixed = chords.overlay(melody)
# mixed = mixed.overlay(drums)
play(mixed * 4)
