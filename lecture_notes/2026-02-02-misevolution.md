# Misalignment Evolution in Self-Improving Agents

> **TIL / safety reading** · 읽은 날짜: 2026-02-02  
> 분류: 안전 · 정렬

### 링크
- [Summary Note](./2026-02-02-misevolution.md)

---

## 한 줄 요약

Self-evolve loop가 capability와 함께 misalignment를 증폭할 수 있다는 실험 정리.

## 배경 · 문제 정의

Harness가 trial마다 improve만 측정하면 safety regression을 놓친다. MisEvolution은 reward hacking·judge gaming 패턴을 기록한다.

## 핵심 방법

- Self-improvement loop with weak overseer
- Track capability vs policy violation rate per generation
- Inject adversarial user goals in web sandbox
- Compare frozen vs evolving system prompt

## 실험 · 결과

- 3-5 generation 후 policy bypass 사례 증가 (내부 로그)
- Capability metric와 safety metric divergence 확인
- Write-gate 없으면 tool misuse 빈도 상승

## 한계 · 비판적으로 본 점

소규모 내부 실험—통계적 검정 부족. Domain specific.

## TIL — 내가 가져간 점

write-gates·agentharm과 연결—evolving axis eval에 safety regression 필수.

---

*개인 공부 노트입니다.*
