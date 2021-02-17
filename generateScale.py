'''
This file contains data such as all of the music notes, common chord progressions and the formulas
for different scales. It also determines the notes in a scale based on the key and mode.
'''

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
scales = ['Major', 'Minor']

# formulas for major/natural minor scales (2 being a whole step and 1 being a half step)
majorFormula = [2, 2, 1, 2, 2, 2]
minorFormula =  [2, 1, 2, 2, 1, 2]

# generates the notes in the scale based on key and mode
def minorScale(key):
    scaleNotes = []
    scaleNotes.append(key)
    keyIndex = notes.index(key)
    for item in minorFormula:
        keyIndex += item
        if keyIndex > 11:
            keyIndex -= 12
        scaleNotes.append(notes[keyIndex])
    return scaleNotes

def majorScale(key):
    scaleNotes = []
    scaleNotes.append(key)
    keyIndex = notes.index(key)
    for item in majorFormula:
        keyIndex += item
        if keyIndex > 11:
            keyIndex -= 12
        scaleNotes.append(notes[keyIndex])
    return scaleNotes
