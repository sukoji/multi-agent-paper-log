# Developing a Computer Use Model

> **Anthropic / 2024** · 읽은 날짜: 2026-05-20  
> 분류: 생성형 · embodied 에이전트

### 링크
- [Original Paper / Resource](https://www.anthropic.com/news/developing-computer-use)
- [Summary Note](./2026-05-20-anthropic-computer-use.md)

---

## 한 줄 요약

Claude가 screenshot 보고 mouse/keyboard를 API로 조작하는 computer use.

## 배경 · 문제 정의

Universal UI automation은 vision+action이 필요하다. Anthropic은 tool로 computer_20241022를 제공한다.

## 핵심 방법

- Screenshot → model → tool_use (click, type, scroll)
- Coordinate system scaled to display
- Beta safety constraints and confirm gates
- Eval on internal OSWorld-style tasks

## 실험 · 결과

- OSWorld 등 benchmark competitive scores
- Real desktop demo workflows
- API in public beta

## 한계 · 비판적으로 본 점

Latency, cost, prompt injection via malicious sites.

## TIL — 내가 가져간 점

cradle·seeact·tierforge desktop suite baseline.

---

*개인 공부 노트입니다.*
