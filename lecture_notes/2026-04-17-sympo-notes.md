# sympo — multi-agent PRD to WBS debate

> **TIL / own project** · 읽은 날짜: 2026-04-17  
> 분류: TIL · 프로젝트 메모

### 링크
- [Original Paper / Resource](https://github.com/sukoji/sympo)
- [Summary Note](./2026-04-17-sympo-notes.md)

---

## 한 줄 요약

PRD를 planner/critic/reviewer agent가 debate하며 WBS로 분해하는 side project.

## 배경 · 문제 정의

단일 LLM PRD 분해는 누락·중복 task가 많다. sympo는 multi-agent-debate를 제품 workflow에 적용한다.

## 핵심 방법

- planner/critic/reviewer roles + structured JSON output
- Debate rounds on task completeness and dependencies
- WBS schema with estimates and owners
- tierforge eval hook 연동 예정

## 실험 · 결과

- Manual review에서 누락 task 감소 (qualitative)
- JSON schema validation으로 parse error 거의 제거
- 3-round debate가 cost/s quality sweet spot

## 한계 · 비판적으로 본 점

아직 formal benchmark 없음. Domain은 software PRD에 편향.

## TIL — 내가 가져간 점

multi-agent-debate 논문을 실제 제품에 적용한 케이스—paper-log와 양방향 링크.

---

*개인 공부 노트입니다.*
