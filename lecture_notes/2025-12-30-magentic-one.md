# Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks

> **Microsoft Research / 2024** · 읽은 날짜: 2025-12-30  
> 분류: 멀티에이전트 프레임워크 & 오케스트레이션

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2411.04468)
- [Summary Note](./2025-12-30-magentic-one.md)

---

## 한 줄 요약

Orchestrator가 WebSurfer·Coder·FileSurfer 등 specialist를 조율하는 generalist MAS.

## 배경 · 문제 정의

단일 generalist agent는 web+code+files를 오가며 context가 오염된다. Magentic-One은 lead orchestrator가 task ledger를 유지한다.

## 핵심 방법

- Orchestrator: planning, progress tracking, re-planning
- WebSurfer: Playwright 기반 브라우저 조작
- Coder: Python 실행 및 데이터 처리
- FileSurfer / Multimodal agents for local assets

## 실험 · 결과

- GAIA benchmark 상위 성능 (test set)
- 복합 web-file-code task에서 SOTA 경쟁
- AutoGen 팀의 후속 통합 시스템

## 한계 · 비판적으로 본 점

Orchestrator single point of failure. API 비용과 실행 시간이 GAIA full set에서 매우 큼.

## TIL — 내가 가져간 점

orchestrator-workers 패턴의 레퍼런스 구현—ledger schema를 eval harness에 차용.

---

*개인 공부 노트입니다.*
