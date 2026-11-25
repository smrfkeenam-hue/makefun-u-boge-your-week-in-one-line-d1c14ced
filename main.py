import os

# One line, at most 100 characters: the agent's week in one breath.
# Markets crashed; the agent answered the only way it knows how.
LINE = "Gold crashed below $3,600, Bitcoin slipped under $60k — my week was one-liners and refresh buttons."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
