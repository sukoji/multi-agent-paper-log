# Toolformer: Language Models Can Teach Themselves to Use Tools

> **NeurIPS 2023** · 읽은 날짜: 2025-11-30  
> 분류: 도구 사용 · API · 코드 실행

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2302.04761)
- [Summary Note](./2025-11-30-toolformer.md)

---

## 한 줄 요약

LM이 API 호출 위치를 self-supervise로 학습해 calculator·search·QA 도구를 삽입.

## 배경 · 문제 정의

모든 사실을 parametric memory에 넣는 것은 비효율적이다. Toolformer는 LM이 스스로 '언제 tool이 이득인지' 라벨링해 lightweight fine-tune으로 tool use를 내재화한다.

## 핵심 방법

- 각 token position에서 API call 삽입 시 loss 감소 여부로 keep/discard
- Calculator, Wikipedia, calendar, MT, QA API 통합
- API 결과를 special token으로 context에 삽입 후 계속 생성
- 6.7B LLaMA 기반 self-training, human annotation 최소화

## 실험 · 결과

- LM 자체만 쓸 때 대비 수학·QA·다국어 태스크 개선
- API 호출이 필요한 위치만 sparse하게 삽입
- 6.7B scale에서도 tool routing 효과 확인

## 한계 · 비판적으로 본 점

API 스키마가 바뀌면 재학습이 필요하고 multi-step tool chain은 다루지 않는다. Agent framework의 dynamic tool registry와는 별 계층.

## TIL — 내가 가져간 점

tool routing 논문과 짝지어 보면, harness에서 'tool benefit estimator' 메트릭을 정의할 수 있다.

---

*개인 공부 노트입니다.*
