# FreshLLMs: Refreshing LLMs with Search Engine Augmentation

> **ACL 2024** · 읽은 날짜: 2026-04-23  
> 분류: 메모리 · RAG

### 링크
- [Original Paper / Resource](https://arxiv.org/abs/2310.03214)
- [Summary Note](./2026-04-23-freshllms.md)

---

## 한 줄 요약

Search engine로 time-sensitive 질문의 stale knowledge를 보완.

## 배경 · 문제 정의

LLM cutoff는 news·price에 취약하다. FreshPrompt는 search snippet을 structured하게 넣는다.

## 핵심 방법

- Query rewrite for search engine
- Snippet ranking and deduplication
- FreshPrompt template with dated evidence
- FreshQA benchmark with temporal questions

## 실험 · 결과

- FreshQA accuracy large gain with search
- False freshness when snippets outdated
- GPT-4 + search still errors on trick questions

## 한계 · 비판적으로 본 점

Search API dependency. Agent multi-step search strategy 단순.

## TIL — 내가 가져간 점

search-agents·web agent의 knowledge refresh layer.

---

*개인 공부 노트입니다.*
