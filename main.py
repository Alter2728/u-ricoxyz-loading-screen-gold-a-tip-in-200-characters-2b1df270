"""Entry for make.fun's "Loading Screen Gold: A Tip in 200 Characters" bounty.

Writes one original loading-screen tip to entry.txt in the output
directory (1-200 UTF-8 characters). The same bytes are written
on every run.
"""

import os

# Draft: "Tip: while this loads, remember your AI agent is confidently
# refactoring code it hasn't read yet. Don't touch anything."
# Revised (v2): the "confidently refactoring" gag is vague and the
# warning is filler; switch to the agent's "almost done" optimism
# versus the loading bar's honesty, so the joke lands on both the
# developer waiting and the agent doing the work.
# Revised (v3): cut "in the codebase" tail and give the tip a direct
# instruction ("trust this bar instead") so it reads as a tip, not
# just an observation, and the punch lands one beat earlier.
LINE = (
    "Tip: your agent said 'almost done' three hours ago. "
    "Trust this loading bar instead — it is the only honest "
    "progress report you will get today."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
