"""Rewrite the block between the activity markers in README.md with recent public pushes."""
import json
import os
import re
import sys
import urllib.request

USER = os.environ.get("GITHUB_REPOSITORY_OWNER", "harshit-05")
START, END = "<!--START_ACTIVITY-->", "<!--END_ACTIVITY-->"
LIMIT = 5


def fetch_events():
    req = urllib.request.Request(
        f"https://api.github.com/users/{USER}/events/public?per_page=100",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def render(events):
    lines, seen = [], set()
    for ev in events:
        if ev["type"] != "PushEvent":
            continue
        repo = ev["repo"]["name"]
        if repo == f"{USER}/{USER}" or repo in seen:
            continue
        commits = ev["payload"].get("commits") or []
        if not commits:
            continue
        seen.add(repo)
        msg = commits[-1]["message"].splitlines()[0][:80]
        lines.append(f"- [{repo}](https://github.com/{repo}): {msg} ({ev['created_at'][:10]})")
        if len(lines) == LIMIT:
            break
    return "\n".join(lines) or "_No recent public activity._"


def main(path="README.md", events=None):
    text = open(path, encoding="utf-8").read()
    pattern = re.compile(f"{re.escape(START)}.*?{re.escape(END)}", re.S)
    if not pattern.search(text):
        sys.exit(f"markers {START} / {END} not found in {path}")
    block = f"{START}\n{render(events if events is not None else fetch_events())}\n{END}"
    new = pattern.sub(lambda _: block, text)
    if new != text:
        open(path, "w", encoding="utf-8").write(new)


if __name__ == "__main__":
    main()
