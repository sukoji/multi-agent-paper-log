# VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks

> **ACL 2024** · 읽은 날짜: 2026-03-11  
> 분류: 웹 · GUI · computer-use 에이전트

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2404.05955)
- [Summary Note](./2026-03-11-visualwebarena.md)

---

## 한 줄 요약

WebArena를 visual observation 중심 task로 확장.

## 배경 · 문제 정의

많은 web task는 이미지·차트를 읽어야 한다. VisualWebArena는 vision-required intent를 추가한다.

## 핵심 방법

- 910 vision-grounded tasks on WebArena sites
- Success via backend + visual state check
- Compare screenshot vs accessibility agents
- Annotate minimal visual reasoning chain

## 실험 · 결과

- Best multimodal agent ~16% success (초기)
- Text-only agents near zero on vision subset
- Product comparison tasks especially hard

## 한계 · 비판적으로 본 점

Annotation cost high. Visual check brittle to theme changes.

## TIL — 내가 가져간 점

seeact·webarena 트릴로지 완성—tierforge web suite 기본 세트.

---

*개인 공부 노트입니다.*
