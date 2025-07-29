# Search-Augmented Agents

> **TIL** · 읽은 날짜: 2026-04-25  
> 분류: 도구 사용 · API · 코드 실행

### 링크
- [Summary Note](./2026-04-25-search-agents.md)

---

## 한 줄 요약

Web search를 planning loop에 통합한 research agent 설계.

## 배경 · 문제 정의

Single search call은 complex research에 부족하다. Agent는 query decompose→search→read→synthesize를 반복한다.

## 핵심 방법

- Subquery generation from main goal
- Search API (Serper, Bing) with rate limit
- Source credibility heuristic
- Stop when coverage score plateaus

## 실험 · 결과

- Multi-hop QA F1 +20% vs one-shot search
- Query drift after 5+ iterations
- Citation accuracy still weak

## 한계 · 비판적으로 본 점

SEO spam vulnerability. No standard eval besides custom QA.

## TIL — 내가 가져간 점

freshllms + ReAct—tierforge research task template.

---

*개인 공부 노트입니다.*
