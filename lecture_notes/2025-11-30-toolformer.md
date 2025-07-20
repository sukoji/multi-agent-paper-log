# Toolformer: Language Models Can Teach Themselves to Use Tools

> **NeurIPS 2023** · 읽은 날짜: 2025-11-30  
> 분류: 도구 사용 · API · 코드 실행

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2302.04761)
- [Summary Note](./2025-11-30-toolformer.md)

---

## 한 줄 요약

LM이 API 호출 문법을 self-supervision으로 학습.

## 문제 정의

도구 통합마다 RLHF/수동 데모가 비쌈.

## 방법 · 핵심 아이디어

synthetic API call 삽입 → 실제 호출 결과로 loss mask; 유용한 call만 학습.

## 실험 · 결과

계산기·QA·검색·번역에서 소형 LM도 도구 이점 획득.

## TIL — 내가 가져간 점

프롬프트만 쓰는 에이전트와 달리 '언제 도구를 쓸지'가 데이터에 박힘.

---

*개인 공부 노트입니다. [Deep-Learning-Paper-Review-and-Practice](https://github.com/SukoJim/Deep-Learning-Paper-Review-and-Practice) 형식을 참고했습니다.*
