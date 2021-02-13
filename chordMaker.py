'''
This file creates chords based on root notes.
'''

chordDict = {}

import generateScale

def buildChord(rootNotes, scaleNotes):
    progress = 1
    for note in rootNotes:
        try:
            note2 = scaleNotes[scaleNotes.index(note) + 2]
        except: # if adding 2 makes it out of range of the list, this makes it wrap around
            note2 = scaleNotes[scaleNotes.index(note) - 6]
        try:
            note3 = scaleNotes[scaleNotes.index(note) + 2]
        except:
            note3 = scaleNotes[scaleNotes.index(note) - 6]
        chordDict['chord' + str(progress)] = [note, note2, note3]
        progress += 1
