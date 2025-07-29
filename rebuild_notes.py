#!/usr/bin/env python3
"""Regenerate lecture_notes/ and README from paper_db.json."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAPERS_DIR = ROOT / "papers"
LECTURE_DIR = ROOT / "lecture_notes"
CODE_DIR = ROOT / "code_practices"
DB_PATH = ROOT / "paper_db.json"

CATEGORIES = {
    "foundations": "기초 · 추론 & 액션 루프",
    "frameworks": "멀티에이전트 프레임워크 & 오케스트레이션",
    "embodied": "생성형 · embodied 에이전트",
    "web": "웹 · GUI · computer-use 에이전트",
    "tools": "도구 사용 · API · 코드 실행",
    "memory": "메모리 · RAG",
    "eval": "벤치마크 · 평가 · 관측",
    "safety": "안전 · 정렬",
    "evolving": "자기진화 · 워크플로 메모리",
    "marl": "MARL · 협업 RL 기초",
    "protocols": "프로토콜 · SDK · 패턴",
    "til": "TIL · 프로젝트 메모",
}


def load_db() -> dict:
    with open(DB_PATH, encoding="utf-8") as f:
        return json.load(f)


def slug_from_filename(name: str) -> str:
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", name.replace(".md", ""))


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {x}" for x in items)


def render_note(filename: str, date: str, entry: dict) -> str:
    title = entry["title"]
    venue = entry["venue"]
    url = entry.get("url", "")
    cat = entry["category"]
    cat_ko = CATEGORIES.get(cat, cat)
    link_block = f"- [Original Paper / Resource]({url})\n" if url else ""

    return f"""# {title}

> **{venue}** · 읽은 날짜: {date}  
> 분류: {cat_ko}

### 링크
{link_block}- [Summary Note](./{filename})

---

## 한 줄 요약

{entry["summary"]}

## 배경 · 문제 정의

{entry["background"]}

## 핵심 방법

{bullets(entry["method"])}

## 실험 · 결과

{bullets(entry["results"])}

## 한계 · 비판적으로 본 점

{entry["limitations"]}

## TIL — 내가 가져간 점

{entry["til"]}

---

*개인 공부 노트입니다.*
"""


def render_readme(entries: list[dict]) -> str:
    by_cat: dict[str, list[dict]] = {k: [] for k in CATEGORIES}
    for e in entries:
        by_cat[e["cat"]].append(e)

    intro = """### 꼼꼼한 멀티에이전트 논문 TIL · Multi-Agent Paper Log

- **멀티에이전트 LLM** (orchestration, tools, memory, eval) 공부하면서 읽은 논문·프레임워크·벤치마크 정리 저장소입니다.
- 2025년 말부터 하루에 한 편(가끔 TIL 메모) 페이스로 기록 중입니다.
- 질문·오타는 **Issues**에 남겨주세요.

| 폴더 | 설명 |
|------|------|
| [`lecture_notes/`](lecture_notes/) | 논문 리뷰 · TIL 마크다운 |
| [`code_practices/`](code_practices/) | (선택) reproduce 스크립트 · 실험 노트 |

"""
    body = []
    for cat, label in CATEGORIES.items():
        items = sorted(by_cat[cat], key=lambda x: x["date"])
        if not items:
            continue
        body.append(f"#### {label}\n")
        for e in items:
            paper_link = f"  * [Original Paper / Resource]({e['url']}) / " if e["url"] else "  * "
            body.append(
                f"* **{e['title']}** ({e['venue']})\n"
                f"{paper_link}"
                f"[Reading Note](lecture_notes/{e['filename']})\n"
            )
        body.append("")

    timeline = "\n".join(
        f"| {e['date']} | [{e['title']}](lecture_notes/{e['filename']}) |"
        for e in sorted(entries, key=lambda x: x["date"])
    )
    return (
        intro
        + "\n".join(body)
        + "\n<details>\n<summary>날짜순 전체 인덱스</summary>\n\n| Date | Note |\n|------|------|\n"
        + timeline
        + "\n\n</details>\n"
    )


def main() -> None:
    db = load_db()
    source_dir = PAPERS_DIR if PAPERS_DIR.exists() else LECTURE_DIR
    if not source_dir.exists():
        raise SystemExit("No papers/ or lecture_notes/ found.")

    if LECTURE_DIR.exists() and source_dir is PAPERS_DIR:
        shutil.rmtree(LECTURE_DIR)
    LECTURE_DIR.mkdir(exist_ok=True)
    CODE_DIR.mkdir(exist_ok=True)
    (CODE_DIR / "README.md").write_text(
        "# code_practices\n\n"
        "논문 reproduce · agent loop 미니 실험 스크립트를 두는 폴더입니다.\n"
        "리뷰 위주 저장소라 필수는 아니며, 필요할 때 브랜치/서브폴더로 추가합니다.\n",
        encoding="utf-8",
    )

    entries: list[dict] = []
    missing: list[str] = []
    for path in sorted(source_dir.glob("*.md")):
        slug = slug_from_filename(path.name)
        if slug not in db:
            missing.append(slug)
            continue
        entry = db[slug]
        date = path.name[:10]
        note_name = path.name
        (LECTURE_DIR / note_name).write_text(render_note(note_name, date, entry), encoding="utf-8")
        entries.append(
            {
                "date": date,
                "filename": note_name,
                "title": entry["title"],
                "venue": entry["venue"],
                "url": entry.get("url", ""),
                "cat": entry["category"],
            }
        )

    if missing:
        raise SystemExit(f"Missing paper_db entries: {missing}")

    (ROOT / "README.md").write_text(render_readme(entries), encoding="utf-8")
    print(f"Wrote {len(entries)} notes -> lecture_notes/")


if __name__ == "__main__":
    main()
