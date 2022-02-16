from music21 import note
from music21.note import Note

NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
OCTAVES = list(range(11))
NOTES_IN_OCTAVE = len(NOTES)


def number_to_note(number: int) -> Note:
    octave = (number // NOTES_IN_OCTAVE) - 1
    note_name = NOTES[number % NOTES_IN_OCTAVE]
    return note.Note(note_name + octave.__str__())


def note_to_number(note: Note) -> int:
    result = NOTES.index(note.name.capitalize())
    result += (NOTES_IN_OCTAVE * (note.octave + 1))
    return result
