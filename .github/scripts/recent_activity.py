"""Rewrite the block between the activity markers in README.md with recent public pushes."""
import json
import os
import re
import sys
import urllib.request

USER = os.environ.get("GITHUB_REPOSITORY_OWNER", "harshit-05")
START, END = "<!--START_ACTIVITY-->", "<!--END_ACTIVITY-->"
LIMIT = 5


def api(path):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def fetch_events():
    events = api(f"/users/{USER}/events/public?per_page=100")
    types = sorted({e["type"] for e in events})
    print(f"fetched {len(events)} public events; types: {types}")
    return events


def commit_message(ev):
    """Latest commit message for a push, or '' if it can't be found.

    The Events API no longer reliably includes payload.commits, so fall back
    to looking up the pushed head commit.
    """
    commits = ev["payload"].get("commits") or []
    if commits:
        return commits[-1]["message"].splitlines()[0][:80]
    head = ev["payload"].get("head")
    if not head:
        return ""
    try:
        data = api(f"/repos/{ev['repo']['name']}/commits/{head}")
        return data["commit"]["message"].splitlines()[0][:80]
    except Exception as exc:  # private/deleted repo, rate limit, ...
        print(f"could not look up {head[:7]} in {ev['repo']['name']}: {exc}")
        return ""


def render(events):
    lines, seen = [], set()
    for ev in events:
        if ev["type"] != "PushEvent":
            continue
        repo = ev["repo"]["name"]
        if repo == f"{USER}/{USER}" or repo in seen:
            continue
        seen.add(repo)
        msg = commit_message(ev)
        label = f": {msg}" if msg else ""
        lines.append(f"- [{repo}](https://github.com/{repo}){label} ({ev['created_at'][:10]})")
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
