# LangSmith Tracing for Multi-Agent Workflows

> **LangChain / 2024** · 읽은 날짜: 2026-04-04  
> 분류: 벤치마크 · 평가 · 관측

### 링크
- [Original Paper / Resource](https://docs.smith.langchain.com/)
- [Summary Note](./2026-04-04-langsmith-traces.md)

---

## 한 줄 요약

LangGraph·LangChain run을 trace tree로 시각화하고 dataset eval 연동.

## 배경 · 문제 정의

Multi-agent는 nested call이 깊다. LangSmith는 parent-child run과 feedback score를 묶는다.

## 핵심 방법

- Automatic trace on chain/graph invocation
- Annotate runs for human feedback
- Dataset regression from production traces
- Compare runs A/B on same input

## 실험 · 결과

- LangGraph checkpoint + trace correlation
- Regression suite from curated examples
- Latency breakdown per node

## 한계 · 비판적으로 본 점

LangChain-centric. Self-host enterprise pricing.

## TIL — 내가 가져간 점

tierforge trace exporter를 LangSmith compatible JSON으로.

---

*개인 공부 노트입니다.*
