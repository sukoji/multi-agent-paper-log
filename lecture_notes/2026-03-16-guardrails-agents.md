# Guardrails for AI Agents

> **TIL / Guardrails AI** · 읽은 날짜: 2026-03-16  
> 분류: 안전 · 정렬

### 링크
- [Original Paper / Resource](https://www.guardrailsai.com/docs)
- [Summary Note](./2026-03-16-guardrails-agents.md)

---

## 한 줄 요약

Structured output validator와 policy rail로 agent action을 runtime에 제한.

## 배경 · 문제 정의

LLM agent는 schema 위반·PII leak·금지 action을 그대로 실행한다. Guardrails는 pre/post hook으로 trajectory를 검열한다.

## 핵심 방법

- RAIL spec으로 output schema·constraint 정의
- On-fail: reask, fix, filter, exception
- Integrate with LangChain/LlamaIndex agent loops
- Custom validator for tool args

## 실험 · 결과

- PII detection rail blocks leaks in demo traces
- JSON schema compliance near 100% with reask
- Latency overhead 50-200ms per step

## 한계 · 비판적으로 본 점

Rule maintenance burden. Adversarial bypass via indirect prompts.

## TIL — 내가 가져간 점

write-gates 구현 참고—tierforge에 rail pass/fail counter.

---

*개인 공부 노트입니다.*
