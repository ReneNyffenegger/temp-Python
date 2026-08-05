import tinysoundfont
import time

synth = tinysoundfont.Synth()
sfid = synth.sfload('/usr/share/sounds/sf2/TimGM6mb.sf2')
synth.program_select(0, sfid, 0, 0)         # channel, sfid, bank, preset
synth.start()                               # starts audio thread
synth.noteon(0, 60, 100)                    # channel, MIDI note, velocity
time.sleep(1.0)                             # hold the note
