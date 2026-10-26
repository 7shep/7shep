"""Rewrite the dev log section of README.md from recent public commits.

Standard library only. Reads public repos owned by USER, keeps commits
authored by USER in the last DAYS days, and groups them by day and repo.
Set GITHUB_TOKEN for a higher API rate limit.
"""

import json
import os
import re
import sys
import urllib.request
from collections import OrderedDict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

USER = "7shep"
DAYS = 14
MAX_DAYS_SHOWN = 6
MAX_PER_REPO = 4
TZ = ZoneInfo("America/Toronto")
SKIP_REPOS = {USER}
SKIP_TYPES = {"docs", "chore", "test", "tests", "style", "ci", "build"}
SKIP_SUBJECTS = re.compile(r"^(merge\b|initial commit$|update (readme|todos)\b)", re.I)
CONVENTIONAL = re.compile(r"^(\w+)(?:\(([^)]*)\))?!?:\s*(.+)$")

README = Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!-- devlog:start -->", "<!-- devlog:end -->"


def api(path):
    req = urllib.request.Request("https://api.github.com" + path)
    req.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def clean(subject):
    """Return a display line for a commit subject, or None to skip it."""
    if SKIP_SUBJECTS.match(subject):
        return None
    m = CONVENTIONAL.match(subject)
    if not m:
        return subject[0].upper() + subject[1:]
    kind, scope, text = m.groups()
    if kind.lower() in SKIP_TYPES:
        return None
    text = text[0].upper() + text[1:]
    return f"{text} <sub>`{scope}`</sub>" if scope else text


def collect(now):
    since = (now - timedelta(days=DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ")
    repos = api(f"/users/{USER}/repos?type=owner&sort=pushed&per_page=100")
    days = {}
    for repo in repos:
        if repo["private"] or repo["archived"] or repo["name"] in SKIP_REPOS:
            continue
        if repo["pushed_at"] < since:
            continue
        commits = api(f"/repos/{USER}/{repo['name']}/commits?author={USER}&since={since}&per_page=100")
        for c in commits:
            if len(c["parents"]) > 1:
                continue
            line = clean(c["commit"]["message"].split("\n", 1)[0].strip())
            if not line:
                continue
            when = datetime.fromisoformat(c["commit"]["author"]["date"].replace("Z", "+00:00"))
            day = when.astimezone(TZ).date()
            days.setdefault(day, OrderedDict()).setdefault(repo["name"], []).append(line)
    return days


def render(days, now):
    if not days:
        return "_Quiet couple of weeks. Probably studying._"
    out = []
    for day in sorted(days, reverse=True)[:MAX_DAYS_SHOWN]:
        out.append(f"#### {day.strftime('%a, %b')} {day.day}")
        for repo, lines in days[day].items():
            url = f"https://github.com/{USER}/{repo}"
            out.append(f"**[{repo}]({url})**")
            for line in lines[:MAX_PER_REPO]:
                out.append(f"- {line}")
            extra = len(lines) - MAX_PER_REPO
            if extra > 0:
                out.append(f"- <sub>[+{extra} more]({url}/commits?author={USER})</sub>")
            out.append("")
    stamp = now.astimezone(TZ).strftime("%b %d, %Y")
    out.append(f"<sub>Auto-written from my public commits · updated {stamp}</sub>")
    return "\n".join(out)


def main():
    now = datetime.now(timezone.utc)
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit(f"README.md needs {START} and {END} markers")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    body = render(collect(now), now)
    new = f"{head}{START}\n{body}\n{END}{tail}"
    # Ignore the timestamp so an unchanged log doesn't make a commit.
    strip = lambda s: re.sub(r"updated [A-Z][a-z]{2} \d\d, \d{4}", "", s)
    if strip(new) != strip(text):
        README.write_text(new, encoding="utf-8")
        print("README.md updated")
    else:
        print("No changes")


if __name__ == "__main__":
    main()
