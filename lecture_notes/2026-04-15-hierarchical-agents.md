# Hierarchical Multi-Agent Architectures

> **TIL** · 읽은 날짜: 2026-04-15  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Summary Note](./2026-04-15-hierarchical-agents.md)

---

## 한 줄 요약

Manager-subordinate delegation tree와 message flow 정리.

## 배경 · 문제 정의

Flat debate는 O(n²) message다. Hierarchy는 bandwidth를 줄이고 책임을 localize한다.

## 핵심 방법

- Tree depth 2-3 typical: exec → lead → worker
- Upward summary, downward directive message types
- Manager agent with broader tools, workers narrow
- Compare vs flat CrewAI group

## 실험 · 결과

- Token use 30% lower than flat 5-agent chat
- Single manager failure catastrophic
- Depth 3+ latency increases

## 한계 · 비판적으로 본 점

Org chart design still manual. Cross-branch coordination weak.

## TIL — 내가 가져간 점

crewai hierarchical process 실험과 매핑.

---

*개인 공부 노트입니다.*
