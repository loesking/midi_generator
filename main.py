import random
from mido import Message
from mido.midifiles import *
from music21 import *
from pyo import Server, Notein, MidiAdsr, MToF, Osc, SquareTable, STRev

import midoMusic21Converter


def main():
    mid = create_midi_file_with_single_track()
    append_random_note_of_given_key_to_track(key.Key('C'), mid.tracks[0], 5)
    mid.save('testmidi.mid')
    play_midi_file('testmidi.mid')


def create_midi_file_with_single_track() -> MidiFile:
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    return mid


def append_random_note_of_given_key_to_track(desired_key: key.Key, track: MidiTrack, i: int) -> None:
    for _ in range(i):
        note_value = midoMusic21Converter.note_to_number(random.choices(desired_key.chord.notes)[0])
        track.append(Message('note_on', note=note_value, velocity=64, time=0))
        track.append(Message('note_off', note=note_value, velocity=127, time=480))


def play_midi_file(filename: str) -> None:
    s = Server().boot().start()
    mid = Notein()
    amp = MidiAdsr(mid["velocity"])
    pit = MToF(mid["pitch"])
    osc = Osc(SquareTable(), freq=pit, mul=amp).mix(1)
    rev = STRev(osc, revtime=1, cutoff=4000, bal=0.2).out()
    mid = MidiFile(filename)
    for message in mid.play():
        s.addMidiEvent(*message.bytes())


if __name__ == '__main__':
    main()
