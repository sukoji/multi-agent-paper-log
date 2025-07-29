# OpenHands: An Open Platform for AI Software Developers as Generalist Agents

> **OpenHands Project / 2024** · 읽은 날짜: 2025-12-26  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://github.com/All-Hands-AI/OpenHands)
- [Summary Note](./2025-12-26-openhands.md)

---

## 한 줄 요약

Docker sandbox 안에서 코드·브라우저·shell을 다루는 오픈소스 generalist dev agent.

## 배경 · 문제 정의

SWE-bench 경쟁 구현이 분산돼 재현이 어렵다. OpenHands(구 OpenDevin)는 통합 runtime과 UI로 community benchmark를 모은다.

## 핵심 방법

- Event stream architecture: action ↔ observation loop
- Sandboxed bash, browser, Jupyter, VSCode plugin
- AgentHub에 CodeAct, browsing agent 등 plug-in
- Evaluation harness for SWE-bench, GAIA 등

## 실험 · 결과

- SWE-bench Lite 상위권 점수 다수 reproduction
- Web browsing + coding 복합 task 지원
- 활발한 OSS 기여와 leaderboard

## 한계 · 비판적으로 본 점

Sandbox escape·비용·장시간 job 안정성 이슈. Multi-agent는 아직 실험적.

## TIL — 내가 가져간 점

tierforge runner target 중 하나—failure-modes taxonomy를 OpenHands trace에 태깅 중.

---

*개인 공부 노트입니다.*
