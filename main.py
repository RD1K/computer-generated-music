'''
This is the main file of the program.
'''

import pretty_midi, sys
from os import system
from random import randrange, randint, uniform
from pydub import AudioSegment
from pydub.playback import play
from time import sleep
from sys import exit

import generateScale
import chordMaker

# path to the soundfont
chordSfDir = "~/computer-generated-music/'Arachno SoundFont - Version 1.0.sf2'"
melodySfDir = "~/computer-generated-music/'GeneralUser GS v1.471.sf2'"

def mainFunction():
    tempo = randint(80, 160)
    beatLength = 60/tempo
    print("Tempo: " + str(tempo) + " BPM")

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

    # synthesizes the MIDI using the soundfont
    system("fluidsynth -ni %s chords.mid -F chords.wav -r 44100 2>/dev/null" % chordSfDir)
    system("fluidsynth -ni %s melody.mid -F melody.wav -r 44100 2>/dev/null" % melodySfDir)
    chords = AudioSegment.from_wav("chords.wav")
    melody = AudioSegment.from_wav("melody.wav")
    mixed = chords.overlay(melody)
    return mixed

while True:
    mixed = mainFunction()
    system("firefox ezgif-7-121685e37334.gif")
    sleep(0.5)
    play(mixed * 4)
    def choice():
        system("espeak 'Did you like that?' 2>/dev/null &")
        choice = input("Did you like that? (y/n) ")
        if choice == "y":
            system("espeak 'Cool! If you want, copy the MIDI and WAV files to another folder to use them.' 2>/dev/null &")
            print("Cool! If you want, copy the MIDI and WAV files to another folder to use them.")
            exit()
        elif choice == "n":
            print("Let's see if this is any better.")
            system("espeak 'Let's see if this is any better.' 2>/dev/null")
            pass
        else:
            choice()
    choice()
