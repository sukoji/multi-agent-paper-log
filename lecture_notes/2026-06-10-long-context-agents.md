# Long Context vs Memory for Agents

> **TIL** · 읽은 날짜: 2026-06-10  
> 분류: 메모리 · RAG

### 링크
- [Summary Note](./2026-06-10-long-context-agents.md)

---

## 한 줄 요약

1M context window가 external memory를 대체하는지 ablation.

## 배경 · 문제 정의

Gemini·Claude long context hype. Agent는 needle vs haystack보다 cumulative tool log가 문제다.

## 핵심 방법

- Fill context with synthetic tool traces to 200k tokens
- Compare full context vs MemGPT-style tiered
- Tasks: find earlier error, summarize project state
- Cost and latency measurement

## 실험 · 결과

- Long context wins on single-hop recall
- Tiered memory wins on cost at 500k+ equiv
- Lost-in-middle on middle tool outputs

## 한계 · 비판적으로 본 점

Model-specific behavior. Synthetic traces may not match prod.

## TIL — 내가 가져간 점

memgpt·cost-latency 결정에 직접 영향.

---

*개인 공부 노트입니다.*
