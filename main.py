#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one 100-word monologue to /output/entry.txt.

The speaker is a Dark Lord three hundred years into his reign, with a
scheme, a history, and a steward who has booked his assassination for
Thursday. His tiredness lives only in the rhythm, the pauses and the
small deflections -- never in a plain statement that he is weary.
"""

import os

MONOLOGUE = (
    "Save the speech, hero. I have heard it \u2014 all of it \u2014 three hundred "
    "years of it, from the steps of this throne. Your sword is bright. "
    "Your cause is just. Your boots are muddy. Sit. No \u2014 stand, if you "
    "prefer. Make it quick. The eastern marches rise at dawn, the ledgers "
    "bleed red, and my steward has booked my assassination for Thursday. "
    "Thursday! Even treason keeps office hours now. So strike, or parley, "
    "or \u2014 wait. Let me finish this tea. It has gone cold twice, and cold "
    "tea is the one defeat I refuse to accept."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
