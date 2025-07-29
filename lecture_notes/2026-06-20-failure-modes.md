# Common Failure Modes in Production Agents

> **TIL / tierforge** · 읽은 날짜: 2026-06-20  
> 분류: TIL · 프로젝트 메모

### 링크
- [Original Paper / Resource](https://github.com/sukoji/tierforge)
- [Summary Note](./2026-06-20-failure-modes.md)

---

## 한 줄 요약

tierforge 돌리며 본 agent failure taxonomy 정리.

## 배경 · 문제 정의

벤치 score만으로 prod 장애 예측 불가. Loop detection, tool timeout, context overflow, judge drift를 태깅했다.

## 핵심 방법

- loop detection, tool timeout, context overflow, judge drift
- Failure code enum in trace schema
- 20+ production-like traces manually tagged
- Cross-tab with benchmark pass/fail

## 실험 · 결과

- 실패 trace 20+건 태깅
- Loop detection이 가장 흔한 prod failure
- Bench pass but prod fail cases documented

## 한계 · 비판적으로 본 점

Private traces—public reproducibility limited.

## TIL — 내가 가져간 점

eval harness에 failure code enum 추가 예정.

---

*개인 공부 노트입니다.*
