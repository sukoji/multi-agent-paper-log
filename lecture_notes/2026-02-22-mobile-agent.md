# Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent

> **arXiv 2024** · 읽은 날짜: 2026-02-22  
> 분류: 생성형 · embodied 에이전트

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2401.16158)
- [Summary Note](./2026-02-22-mobile-agent.md)

---

## 한 줄 요약

Vision 기반으로 Android/iOS UI를 탭·스와이프하며 task 수행.

## 배경 · 문제 정의

Mobile GUI는 accessibility tree가 불완전하다. Mobile-Agent는 screenshot + icon detection으로 action을 선택한다.

## 핵심 방법

- Perception: OCR + icon grounding on screenshot
- Planning: break instruction into subgoals
- Action: tap, swipe, type coordinates
- Self-refine loop on execution failure

## 실험 · 결과

- 10+ mobile apps에서 multi-step task 성공
- Multimodal perception ablation significant
- Cross-app generalization partial

## 한계 · 비판적으로 본 점

Screen resolution·OS version sensitive. Privacy risk on real devices.

## TIL — 내가 가져간 점

appagent·cradle과 mobile UI agent 비교 축.

---

*개인 공부 노트입니다.*
