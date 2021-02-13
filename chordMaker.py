'''
This file creates chords based on the degree, key, and scale.
'''

import generateScale

def buildChord(chordProgression, scaleNotes):
    chordDict = {}
    rootNotes = []
    for number in chordProgression:
        rootNote = scaleNotes[number - 1]
        rootNotes.append(rootNote)
    progress = 1
    for note in rootNotes:
        print(note)
        try:
            note2 = scaleNotes[scaleNotes.index(note) + 2]
        except: # if adding 2 makes it out of range of the list, this makes it wrap around
            note2 = scaleNotes[scaleNotes.index(note) - 5]
        try:
            note3 = scaleNotes[scaleNotes.index(note2) + 2]
        except:
            note3 = scaleNotes[scaleNotes.index(note2) - 5]
        chordDict['chord' + str(progress)] = [note, note2, note3]
        progress += 1
    return chordDict
