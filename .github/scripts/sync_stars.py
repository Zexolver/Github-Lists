#!/usr/bin/env python3
"""Diff Zexolver's GitHub stars against repos already listed in this repo,
appending anything new to a triage file for manual sorting."""

import os
import re
import sys
import urllib.request
import json
from pathlib import Path

USERNAME = "Zexolver"
REPO_ROOT = Path(__file__).resolve().parents[2]
TRIAGE_FILE = REPO_ROOT / "Linux" / "Ricing" / "Unsorted-New-Stars.md"
URL_RE = re.compile(r"github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
TOKEN = os.environ.get("GITHUB_TOKEN")


def api_get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read()), resp.headers


def fetch_all_stars(username):
    stars, page = [], 1
    while True:
        data, _ = api_get(f"https://api.github.com/users/{username}/starred?per_page=100&page={page}")
        if not data:
            break
        stars.extend(data)
        page += 1
    return stars


def already_listed():
    listed = set()
    for md in REPO_ROOT.rglob("*.md"):
        if ".github" in md.parts:
            continue
        for owner, repo in URL_RE.findall(md.read_text(errors="ignore")):
            listed.add(f"{owner.lower()}/{repo.lower()}")
    return listed


def main():
    stars = fetch_all_stars(USERNAME)
    listed = already_listed()

    new_stars = []
    for repo in stars:
        full_name = repo["full_name"]
        if full_name.lower() not in listed:
            new_stars.append(repo)

    if not new_stars:
        print("No new stars to triage.")
        return

    lines = []
    if TRIAGE_FILE.exists():
        lines.append(TRIAGE_FILE.read_text().rstrip("\n"))
    else:
        lines.append("## Newly starred repos, not yet sorted into a category\n"
                      "#### Auto-populated by .github/workflows/sync-stars.yml — sort these into real lists, then remove them here.")

    for repo in new_stars:
        lang = repo.get("language") or "?"
        desc = (repo.get("description") or "").strip()
        entry = f"\n- {repo['html_url']}\n    - Language: {lang}"
        if desc:
            entry += f"\n    - {desc}"
        lines.append(entry)

    TRIAGE_FILE.parent.mkdir(parents=True, exist_ok=True)
    TRIAGE_FILE.write_text("\n".join(lines) + "\n")
    print(f"Added {len(new_stars)} new starred repo(s) to {TRIAGE_FILE.relative_to(REPO_ROOT)}")

    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a") as f:
            f.write(f"new_count={len(new_stars)}\n")


if __name__ == "__main__":
    sys.exit(main())
