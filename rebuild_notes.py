#!/usr/bin/env python3
"""Regenerate lecture_notes/ and README from paper metadata (TIL / review style)."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAPERS_DIR = ROOT / "papers"
LECTURE_DIR = ROOT / "lecture_notes"
CODE_DIR = ROOT / "code_practices"

CATEGORIES = {
    "foundations": "기초 · 추론 & 액션 루프",
    "frameworks": "멀티에이전트 프레임워크 & 오케스트레이션",
    "embodied": "생성형 · embodied 에이전트",
    "web": "웹 · GUI · computer-use 에이전트",
    "tools": "도구 사용 · API · 코드 실행",
    "memory": "메모리 · RAG",
    "eval": "벤치마크 · 평가 · 관측",
    "safety": "안전 · 정렬",
    "evolving": "자기진화 · 워크플로 메모리",
    "marl": "MARL · 협업 RL 기초",
    "protocols": "프로토콜 · SDK · 패턴",
    "til": "TIL · 프로젝트 메모",
}

# slug -> (title, venue, url, category, summary, problem, method, results, til)
PAPER_DB: dict[str, tuple] = {
    "react": (
        "ReAct: Synergizing Reasoning and Acting in Language Models",
        "ICLR 2023",
        "https://arxiv.org/abs/2210.03629",
        "foundations",
        "Thought → Action → Observation 루프로 LM이 도구·환경과 상호작용.",
        "CoT만으로는 환경 피드백을 못 받고, RL fine-tuning은 샘플 효율이 나쁨.",
        "자연어 reasoning trace와 action(검색, API 호출 등)을 번갈아 생성; observation을 다시 context에 넣음.",
        "HotpotQA, AlfWorld, WebShop에서 prompting/RL baseline 대비 일관된 gain.",
        "에이전트 루프 설계 시 '생각'과 '행동'을 분리해 로깅하면 디버깅이 쉬움. 내 harness도 step type을 나눠야 함.",
    ),
    "reflexion": (
        "Reflexion: Language Agents with Verbal Reinforcement Learning",
        "NeurIPS 2023",
        "https://arxiv.org/abs/2303.11366",
        "foundations",
        "실패 trajectory를 언어로 reflect해서 episodic memory에 넣고 재시도.",
        "RL weight update 없이 trial-and-error로 agent를 개선하고 싶음.",
        "evaluator signal → verbal self-reflection → memory buffer → 다음 episode에 주입.",
        "AlfWorld, HotPotQA, HumanEval에서 pass@1 개선; weight update 없음.",
        "multi-agent에서도 '짧은 회고 메시지'를 shared memory에 남기는 패턴으로 확장 가능.",
    ),
    "toolformer": (
        "Toolformer: Language Models Can Teach Themselves to Use Tools",
        "NeurIPS 2023",
        "https://arxiv.org/abs/2302.04761",
        "tools",
        "LM이 API 호출 문법을 self-supervision으로 학습.",
        "도구 통합마다 RLHF/수동 데모가 비쌈.",
        "synthetic API call 삽입 → 실제 호출 결과로 loss mask; 유용한 call만 학습.",
        "계산기·QA·검색·번역에서 소형 LM도 도구 이점 획득.",
        "프롬프트만 쓰는 에이전트와 달리 '언제 도구를 쓸지'가 데이터에 박힘.",
    ),
    "camel": (
        "CAMEL: Communicative Agents for Mind Exploration of Large Language Model Society",
        "NeurIPS 2023",
        "https://arxiv.org/abs/2303.17760",
        "frameworks",
        "role-playing 두 agent가 task instruction만으로 협업.",
        "single-agent chain이 길어지면 drift; 역할 분리가 필요.",
        "inception prompting + role names + task specifier; autonomous role play.",
        "다양한 cooperative task에서 dialogue만으로 워크플로우 생성.",
        "MetaGPT SOP 이전에 '역할만 주고 대화' 패턴의 원형.",
    ),
    "metagpt": (
        "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework",
        "ICLR 2024",
        "https://arxiv.org/abs/2308.00352",
        "frameworks",
        "소프트웨어 팀 SOP를 agent workflow에 인코딩.",
        "chat-based MAS는 메시지 폭발·환각·일관성 붕괴.",
        "PM/Architect/Engineer 역할 + structured deliverable(요구사항, diagram, code).",
        "MBPP, HumanEval 등에서 single-agent GPT-4 대비 높은 pass rate 리포트.",
        "내 sympo/tierforge 설계에 '산출물 스키마'가 핵심이라는 걸 다시 확인.",
    ),
    "autogen": (
        "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation",
        "COLM 2024 / framework",
        "https://arxiv.org/abs/2308.08155",
        "frameworks",
        "conversable agent abstraction + human-in-the-loop.",
        "복잡한 앱마다 agent wiring 코드를 처음부터 짜기 어려움.",
        "register_reply hooks, group chat manager, code execution sandbox 연동.",
        "수학, 코딩, retrieval 태스크에서 flexible conversation pattern.",
        "LangGraph 이전 세대의 '대화=프로그램' 느낌; 지금은 graph/state로 대체 추세.",
    ),
    "generative-agents": (
        "Generative Agents: Interactive Simulacra of Human Behavior",
        "UIST 2023",
        "https://arxiv.org/abs/2304.03442",
        "embodied",
        "메모리 스트림 + reflection으로 believable NPC 시뮬레이션.",
        "단일 prompt persona는 장기 일관성이 없음.",
        "observe→plan→act; memory stream retrieval(importance/recency/relevance).",
        "Smallville에서 emergent social behavior 관찰.",
        "multi-agent eval에서 ' believable interaction' 지표 참고.",
    ),
    "voyager": (
        "Voyager: An Open-Ended Embodied Agent with Large Language Models",
        "TMLR 2023",
        "https://arxiv.org/abs/2305.16291",
        "embodied",
        "Minecraft에서 skill library + iterative prompting으로 lifelong learning.",
        "embodied agent가 task마다 처음부터 학습하면 비효율.",
        "automatic curriculum, skill code 저장, embedding retrieval로 재사용.",
        "이전 SOTA 대비 아이템·tech tree 진행 크게 앞섬.",
        "tool/skill library 아이디어는 코드 에이전트에도 그대로 적용됨.",
    ),
    "agentverse": (
        "AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors",
        "ICLR 2024",
        "https://arxiv.org/abs/2308.10848",
        "frameworks",
        "expert recruitment + collaborative decision + evaluation loop.",
        "단일 agent capacity 한계를 동적으로 팀 구성으로 보완.",
        "여러 round에서 agent group을 바꿔가며 해답 수렴.",
        "reasoning, coding, tool-use 태스크에서 성능·emergence 리포트.",
        "eval harness에 '팀 구성 ablation' 넣을 근거.",
    ),
    "hugginggpt": (
        "HuggingGPT: Solving AI Tasks with ChatGPT and Its Friends in Hugging Face",
        "2023",
        "https://arxiv.org/abs/2303.17580",
        "frameworks",
        "LLM이 planner로 HF model zoo를 호출.",
        "모델마다 API가 달라 orchestration이 필요.",
        "task planning → model selection → execution → response generation.",
        "멀티모달·멀티도메인 태스크 데모.",
        "오늘의 tool routing / MCP와 같은 계보.",
    ),
    "swe-agent": (
        "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering",
        "NeurIPS 2024",
        "https://arxiv.org/abs/2405.15793",
        "tools",
        "ACI(전용 UI/액션 공간)가 raw shell보다 SWE-bench 성능을 끌어올림.",
        "LM이 generic shell만 쓰면 repo navigation이 비효율.",
        "file viewer, search, edit 전용 action + agent loop.",
        "SWE-bench Verified에서 당시 SOTA급.",
        "computer-use 논문들과 같이 'action space 설계'가 핵심 축.",
    ),
    "langgraph": (
        "LangGraph: Stateful Multi-Actor Applications with LLMs",
        "framework docs",
        "https://langchain-ai.github.io/langgraph/",
        "frameworks",
        "graph/state machine으로 agent workflow 표현.",
        "stateless chain은 분기·재시도·human gate 표현이 어려움.",
        "nodes=actors, edges=transitions, checkpointing, cyclic graph.",
        "production agent에서 supervisor/handoff 패턴 표준화.",
        "내 eval harness를 graph로 모델링하면 attribution이 쉬움.",
    ),
    "multi-agent-debate": (
        "Improving Factuality and Reasoning in Language Models through Multiagent Debate",
        "ICML 2024",
        "https://arxiv.org/abs/2305.14325",
        "frameworks",
        "여러 LM instance가 debate하며 factuality 개선.",
        "single-shot CoT는 hallucination.",
        "동일 prompt 여러 agent → round-robin critique → final answer.",
        "arithmetics, biography, GSM 등에서 accuracy 상승.",
        "sympo의 PRD debate와 직접 연결; judge agent 비용 tradeoff 존재.",
    ),
    "mad": (
        "Self-Consistency Improves Chain of Thought Reasoning in Language Models",
        "ICLR 2023",
        "https://arxiv.org/abs/2203.11171",
        "foundations",
        "다중 CoT sample majority vote.",
        "greedy decode CoT는 불안정.",
        "temperature>0 여러 reasoning path → most consistent answer.",
        "GSM8K, MultiArith 등 수학 benchmark 개선.",
        "debate 전에 쓸 수 있는 저렴한 ensemble baseline.",
    ),
    "openhands": (
        "OpenHands: An Open Platform for AI Software Developers",
        "2024",
        "https://arxiv.org/abs/2407.16741",
        "tools",
        "오픈소스 CodeAct + sandbox SWE agent 플랫폼.",
        "Devin류 closed system 대비 reproducible stack 필요.",
        "event stream architecture, runtime sandbox, delegation.",
        "SWE-bench 등에서 활발히 리더보드 경쟁.",
        "tierforge/sympo 코드 에이전트 벤치마크 참고 구현.",
    ),
    "agent-laboratory": (
        "The Agent Laboratory: Advancing Autonomous Research",
        "2025",
        "https://arxiv.org/abs/2501.04227",
        "evolving",
        "연구 워크플로(문헌·실험·작성)를 agent team이 수행.",
        "human researcher bottleneck를 자동화 시도.",
        "phased workflow + specialized agents + feedback.",
        "논문 초안 품질 human preference 상회 리포트(claim).",
        "self-evolving agent 리스크(quality gate) 사례.",
    ),
    "magentic-one": (
        "Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks",
        "2024",
        "https://arxiv.org/abs/2411.04468",
        "frameworks",
        "Orchestrator-led generalist team (FileSurfer, Coder, WebSurfer).",
        "단일 generalist로는 web+code+files 교차 태스크가 어려움.",
        "lead orchestrator가 task ledger 유지·delegate.",
        "GAIA, AssistantBench 등에서 strong generalist scores.",
        "Microsoft의 supervisor 패턴 실전 레퍼런스.",
    ),
    "agentbench": (
        "AgentBench: Evaluating LLMs as Agents",
        "ICLR 2024",
        "https://arxiv.org/abs/2308.03688",
        "eval",
        "8 environments에서 LLM agent 능력 multi-dimensional eval.",
        "기존 benchmark는 narrow skill만 측정.",
        "OS, DB, knowledge graph, web shop 등 diverse env + unified protocol.",
        "모델 간 gap이 task type마다 다름을 보여줌.",
        "내 harness 설계 시 env diversity 중요.",
    ),
    "webarena": (
        "WebArena: A Realistic Web Environment for Building Autonomous Agents",
        "ICLR 2024",
        "https://arxiv.org/abs/2307.13854",
        "web",
        "fully functional mock web sites로 realistic agent eval.",
        "toy HTML benchmark는 실제 웹 복잡도 반영 못함.",
        "e-commerce, forum, gitlab 등 + functional correctness metric.",
        "GPT-4 agent도 human far below.",
        "computer-use eval의 표준 레퍼런스.",
    ),
    "mind2web": (
        "Mind2Web: Towards a Generalist Agent for the Web",
        "NeurIPS 2023",
        "https://arxiv.org/abs/2306.06070",
        "web",
        "real website snapshot에서 generalist web action.",
        "single-site overfitting.",
        "cross-task, cross-website generalization benchmark.",
        "다양한 domain에서 element grounding 어려움 확인.",
        "SeeAct/WorkArena 계보.",
    ),
    "tau-bench": (
        "τ-bench: A Benchmark for Tool-Agent-User Interaction",
        "2024",
        "https://arxiv.org/abs/2406.12027",
        "eval",
        "tool + user simulation + policy constraint customer service.",
        "API-only bench는 multi-turn user 부재.",
        "retail/airline domain, dual-control(user+agent).",
        "SOTA LM도 reliability gap 큼.",
        "multi-agent보다 single agent + user model이지만 harness 설계 참고.",
    ),
    "gorilla": (
        "Gorilla: Large Language Model Connected with Massive APIs",
        "NeurIPS 2023",
        "https://arxiv.org/abs/2305.15334",
        "tools",
        "API document retrieval + fine-tuned model로 hallucinated call 감소.",
        "open-ended API 이름/인자 hallucination.",
        "retriever over API docs + AST subtree matching metric.",
        "APIBench에서 call accuracy 개선.",
        "MCP/tool registry 설계의 선행.",
    ),
    "toolllm": (
        "ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs",
        "2023",
        "https://arxiv.org/abs/2307.16789",
        "tools",
        "대규모 RapidAPI graph + ToolLLaMA fine-tune.",
        "scale된 tool learning 데이터 부족.",
        "ToolBench dataset, depth-first search decision tree, DFSDT.",
        "복잡 multi-hop tool chain에서 reasoning 필요.",
        "tool routing eval metric 참고.",
    ),
    "memgpt": (
        "MemGPT: Towards LLMs as Operating Systems",
        "2023",
        "https://arxiv.org/abs/2310.08560",
        "memory",
        "virtual context / paging으로 long-term dialog.",
        "finite context window 한계.",
        "main context vs archival memory; self-managed read/write.",
        "long doc QA, multi-session chat에서 baseline 대비 유지.",
        "agent memory layer 설계 필독.",
    ),
    "self-evolving-agents": (
        "A Survey on Self-Evolving Agents",
        "2025 survey",
        "https://arxiv.org/abs/2501.07452",
        "evolving",
        "agent가 experience로 policy/memory/tool을 스스로 바꾸는 축 정리.",
        "terminology 혼란 (lifelong, self-improve, etc.).",
        "what evolves / when / safety taxonomy.",
        "awesome-self-evolving-agents 큐레이션 근거.",
        "write-gate 없는 self-edit는 위험.",
    ),
    "misevolution": (
        "Misevolution: Model Evolution Inspired by Natural Selection",
        "2024",
        "https://arxiv.org/abs/2409.07428",
        "evolving",
        "interaction으로 agent population evolve.",
        "static agent는 env drift에 약함.",
        "selection + mutation on prompts/policies.",
        "benchmark에서 adaptive gain.",
        "eval에 'evolved vs frozen' 비교 필요.",
    ),
    "tree-of-thoughts": (
        "Tree of Thoughts: Deliberate Problem Solving with Large Language Models",
        "NeurIPS 2023",
        "https://arxiv.org/abs/2305.10601",
        "foundations",
        "thought를 tree로 expand + search.",
        "linear CoT는 backtrack 불가.",
        "generate/evaluate/prune thoughts; BFS/DFS.",
        "Game of 24, creative writing에서 gain.",
        "LATS와 합치면 agent planning 표준 툴킷.",
    ),
    "visualwebarena": (
        "VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks",
        "ICLR 2025",
        "https://arxiv.org/abs/2404.05967",
        "web",
        "screenshot 기반 multimodal web agent benchmark.",
        "DOM-only는 visual cue 태스크 실패.",
        "realistic sites + image-conditioned goals.",
        "GPT-4V agent도 success rate 낮음.",
        "computer-use eval 확장판.",
    ),
    "codeact": (
        "Executable Code Actions Elicit Better LLM Agents",
        "ICML 2024",
        "https://arxiv.org/abs/2402.01030",
        "tools",
        "JSON tool call 대신 Python code action.",
        "DSL action space가 expressive하지 않음.",
        "unified code 실행으로 composition·control flow.",
        "API-Bank, M3ToolEval 등에서 우수.",
        "OpenHands 기본 action family.",
    ),
    "mcp": (
        "Model Context Protocol (MCP)",
        "Anthropic spec",
        "https://modelcontextprotocol.io/",
        "protocols",
        "tool/data source 연결 open standard.",
        "N×M integration problem.",
        "client-host-server, resources + tools schema.",
        "ecosystem 빠르게 성장.",
        "내 lab stack에서 tool routing 표준 후보.",
    ),
    "self-rag": (
        "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection",
        "ICLR 2024",
        "https://arxiv.org/abs/2310.11511",
        "memory",
        "retrieve/on-demand + self-critique token.",
        "RAG가 always retrieve하면 noise.",
        "reflection token으로 retrieve/generate/critic 제어.",
        "open-domain QA, reasoning 개선.",
        "agent loop의 retrieval gate.",
    ),
    "process-reward": (
        "Let's Verify Step by Step",
        "ICLR 2024",
        "https://arxiv.org/abs/2305.20050",
        "eval",
        "process reward model(PRM)이 outcome만 보다 나음.",
        "outcome RM은 credit assignment 부정확.",
        "step-level human label → PRM → MCTS/ beam search.",
        "MATH benchmark에서 strong results.",
        "multi-agent step attribution과 개념적으로 연결.",
    ),
    "crewai": (
        "CrewAI — role-based agent crews",
        "framework docs",
        "https://docs.crewai.com/",
        "til",
        "역할·task·process를 YAML/Python으로 묶는 경량 crew 프레임워크.",
        "AutoGen/LangGraph는 무겁고 학습 곡선이 큼.",
        "Agent(role, goal, tools) + Crew(process=sequential/hierarchical).",
        "quick automation demo에 적합; deep eval는 직접 깔아야 함.",
        "MetaGPT SOP 대신 '가벼운 role play'만 필요할 때 선택지.",
    ),
    "sympo-notes": (
        "sympo — multi-agent PRD→WBS debate",
        "own project",
        "https://github.com/sukoji/sympo",
        "til",
        "PRD를 여러 agent가 debate하며 WBS로 분해하는 side project.",
        "단일 LLM PRD 분해는 누락·중복 task가 많음.",
        "planner/critic/reviewer roles + structured JSON output.",
        "tierforge eval hook과 연동 예정.",
        "multi-agent-debate 논문을 제품 workflow에 적용한 케이스.",
    ),
    "awesome-agents": (
        "awesome-self-evolving-agents curation notes",
        "own repo",
        "https://github.com/sukoji/awesome-self-evolving-agents",
        "til",
        "self-evolving agent survey를 읽으며 awesome list taxonomy 정리.",
        "terminology가 논문마다 다름 (lifelong vs self-refine).",
        "what/when/how evolves + risk axis로 태깅.",
        "PR taxonomy + pareto plot 추가.",
        "paper-log와 양방향 링크 유지.",
    ),
    "plan-and-solve": (
        "Plan-and-Solve Prompting",
        "ACL 2023",
        "https://arxiv.org/abs/2309.06179",
        "foundations",
        "먼저 plan 생성 후 solve 단계 분리.",
        "zero-shot CoT가 multi-step에서 plan 누락.",
        "PS+ / PS prompt template.",
        "GSM8K 등 math reasoning gain.",
        "supervisor agent의 plan node 구현에 사용.",
    ),
    "lass": (
        "Language Agent Tree Search (LATS)",
        "2023",
        "https://arxiv.org/abs/2310.04406",
        "foundations",
        "LM + Monte Carlo tree search로 deliberation.",
        "ToT는 heuristic search; env feedback 약함.",
        "thought expansion + self-reflection + backtracking.",
        "reasoning, programming, web tasks.",
        "eval budget vs depth tradeoff 기록.",
    ),
    "agent-q": (
        "Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents",
        "2024",
        "https://arxiv.org/abs/2408.07199",
        "foundations",
        "MCTS + offline RL + DPO로 web shopping agent.",
        "online RL on live env는 비용·안전 이슈.",
        "guided search + self-play data + iterative DPO.",
        "WebShop 등에서 GPT-4 agent 대비 개선 claim.",
        "process supervision + search 결합 사례.",
    ),
    "llm-debate": (
        "Encouraging Divergent Thinking in LLMs through Multi-Agent Debate",
        "2024",
        "https://arxiv.org/abs/2305.19118",
        "frameworks",
        "debate로 mode collapse / narrow reasoning 완화.",
        "single agent는 초기 답에 고착.",
        "divergent role prompts + multi-round debate.",
        "MMLU, arithmetic subsets.",
        "sympo debate temperature/role 설계 참고.",
    ),
    "map-neo": (
        "Multi-Agent Collaboration via Evolving Orchestration",
        "2024",
        "https://arxiv.org/abs/2409.07497",
        "frameworks",
        "orchestration policy를 evolve.",
        "fixed topology는 task마다 suboptimal.",
        "RL/evolution on who-to-call-next.",
        "multi-agent bench gains.",
        "routing-agents TIL과 연결.",
    ),
    "agent-workflow-memory": (
        "Agent Workflow Memory",
        "2024",
        "https://arxiv.org/abs/2408.07122",
        "evolving",
        "성공 workflow를 memory에 저장해 재사용.",
        "매번 planning from scratch.",
        "extract subgraph / prompt snippet from traces.",
        "web agent success rate up.",
        "self-evolving without weight update.",
    ),
    "who-when-harness": (
        "Which Agent Causes Task Failures — and When?",
        "2024",
        "https://arxiv.org/abs/2409.13474",
        "eval",
        "multi-agent failure attribution benchmark.",
        "aggregate success rate만으로는 디버깅 불가.",
        "counterfactual agent swap / step blame labels.",
        "models struggle on who-when questions.",
        "내 eval harness north star paper.",
    ),
    "agentharm": (
        "AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents",
        "2024",
        "https://arxiv.org/abs/2409.03766",
        "safety",
        "agent가 harmful multi-step plan 실행 능력 측정.",
        "chat harm bench ≠ tool-use harm.",
        "benign-looking tasks chaining to misuse.",
        "even aligned models partially capable.",
        "guardrails-agents TIL 근거.",
    ),
    "workarena": (
        "WorkArena: How Capable Are Web Agents at Solving Work Tasks?",
        "2024",
        "https://arxiv.org/abs/2403.07718",
        "consumer web bench만으로 office automation 미대표.",
        "L2/L3 skill curriculum on live-like UI.",
        "SOTA far from human expert.",
        "computer-use for enterprise.",
    ),
    "seeact": (
        "SeeAct: GPT-4V for Web Grounding",
        "2024",
        "https://arxiv.org/abs/2401.01614",
        "web",
        "VLM이 screenshot에서 element grounding.",
        "text-only DOM 접근 한계.",
        "See–Think–Act loop with visual candidates.",
        "Mind2Web subset gains.",
        "VisualWebArena 전초전.",
    ),
}

TIL_CUSTOM: dict[str, tuple] = {
    "failure-modes": (
        "Common failure modes in production agents",
        "TIL",
        "https://github.com/sukoji/tierforge",
        "til",
        "tierforge 돌리며 본 agent failure taxonomy 정리.",
        "벤치 score만으로 prod 장애 예측 불가.",
        "loop detection, tool timeout, context overflow, judge drift.",
        "실패 trace 20+건 태깅.",
        "eval harness에 failure code enum 추가 예정.",
    ),
    "reading-queue": (
        "Q3 reading queue — embodied + web agents",
        "TIL",
        "",
        "til",
        "2026 Q3에 읽을 embodied/web agent 논문 큐.",
        "paper-log가 framework-heavy.",
        "RT-2, OpenVLA, UI-TARS 등 후보.",
        "n/a",
        "읽으면 lecture_notes에 추가.",
    ),
}

# keyword -> template fields for TIL / framework notes without formal paper
TIL_SLUGS = {
    "crewai", "sympo-notes", "awesome-agents", "reading-queue", "failure-modes",
    "eval-harness-ablation", "human-study-agents", "guardrails-agents",
    "orchestrator-workers", "routing-agents", "supervisor-pattern", "handoff-pattern",
    "parallel-agents", "cost-latency", "long-context-agents", "write-gates",
    "claude-mcp", "agents-sdk", "openai-swarm", "anthropic-computer-use",
    "agent-protocol", "a2a", "agentops", "langsmith-traces", "open-interpreter",
    "smolagents", "llama-agent", "consensus-agents", "judge-agents",
}


def parse_existing(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    title = text.splitlines()[0].removeprefix("# ").strip()
    date = path.name[:10]
    return date, title


def slug_from_filename(name: str) -> str:
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", name.replace(".md", ""))


def infer_category(slug: str, title: str) -> str:
    t = (slug + title).lower()
    if slug in TIL_SLUGS:
        return "til"
    if any(k in t for k in ("web", "arena", "mind2", "seeact", "mobile", "cradle", "appagent", "workarena", "computer")):
        return "web"
    if any(k in t for k in ("mem", "rag", "retriev")):
        return "memory"
    if any(k in t for k in ("bench", "eval", "verif", "harm", "judge", "harness")):
        return "eval"
    if any(k in t for k in ("safe", "align", "constitutional", "guard", "rlhf")):
        return "safety"
    if any(k in t for k in ("maddpg", "qmix", "commnet", "marl", "rl")):
        return "marl"
    if any(k in t for k in ("mcp", "swarm", "sdk", "protocol", "a2a", "gorilla", "tool")):
        return "tools" if "framework" not in t else "protocols"
    if any(k in t for k in ("evolv", "misevol", "workflow", "laboratory")):
        return "evolving"
    if any(k in t for k in ("meta", "autogen", "camel", "crew", "graph", "debate", "orchestr")):
        return "frameworks"
    if any(k in t for k in ("voyager", "generative", "embodied")):
        return "embodied"
    return "foundations"


def fallback_content(slug: str, title: str, cat: str) -> tuple:
    hooks = {
        "foundations": (
            f"{title}의 문제 설정과 agent loop 가정을 중심으로 읽음.",
            "single-shot LM으로는 multi-step task가 불안정.",
            "prompting / search / memory 중 하나로 action space를 확장.",
            "benchmark에서 step-wise metric 확인.",
            "내 연구 harness에 옮길 때 가장 먼저 action schema를 맞춰볼 것.",
        ),
        "frameworks": (
            f"{title} — 역할 분담·메시지 패스·종료 조건 위주로 정리.",
            "ad-hoc prompt chain은 scale 시 유지보수 어려움.",
            "role/SOP/graph로 orchestration 명시.",
            "case study 또는 leaderboard 수치 스킴.",
            "supervisor vs peer-to-peer 중 어떤 topology인지 태깅.",
        ),
        "web": (
            f"{title} — observation space(DOM vs screenshot)와 action granularity 체크.",
            "real web complexity + grounding error.",
            "planner + browser controller / multimodal grounding.",
            "success rate human gap still large.",
            "eval에 failure taxonomy(grounding vs planning) 넣기.",
        ),
        "tools": (
            f"{title} — tool schema, error handling, retry 정책 확인.",
            "hallucinated tool name/args.",
            "retrieval over tool docs or code-as-action.",
            "API-heavy task accuracy.",
            "MCP registry와 비교 메모.",
        ),
        "memory": (
            f"{title} — write/read trigger와 context budget tradeoff.",
            "long horizon에서 fact drift.",
            "episodic + semantic memory tier or RAG gate.",
            "multi-hop QA / long dialog metric.",
            "MemGPT-style paging 고려.",
        ),
        "eval": (
            f"{title} — metric이 실제 capability를 얼마나 커버하는지 비판적으로 읽음.",
            "narrow bench overfitting.",
            "multi-env or process-level supervision.",
            "SOTA vs human gap 리포트.",
            "ablation protocol을 내 bench에 복제.",
        ),
        "safety": (
            f"{title} — misuse surface와 mitigation이 eval에 포함됐는지.",
            "capable agent = larger attack surface.",
            "constitution / filter / sandbox / human approval.",
            "harm rate or refusal tradeoff.",
            "self-evolving agent와 결합 시 risk 증폭.",
        ),
        "evolving": (
            f"{title} — 무엇이 evolve 가능한지(policy/memory/tool)와 gate.",
            "unbounded self-edit는 drift.",
            "experience buffer + selection + validation.",
            "before/after capability curve.",
            "awesome-list 카테고리와 매핑.",
        ),
        "marl": (
            f"{title} — classical MARL 개념을 LLM team에 비유.",
            "decentralized training central execution 등 가정.",
            "communication channel or value factorization.",
            "cooperative MARL toy benchmark.",
            "LLM agent는 gradient 없이 verbal coordination.",
        ),
        "protocols": (
            f"{title} — interop layer로서 schema/handoff 표준.",
            "vendor lock-in integrations.",
            "open protocol + tracing hooks.",
            "adoption / demo repos.",
            "Agents SDK handoff vs LangGraph edge 비교.",
        ),
        "til": (
            f"{title} — 실험/프로젝트 하면서 남긴 TIL.",
            "논문 한 편보다 구현·벤치마크 설계 메모.",
            "직접 돌려본 설정, 실패 케이스.",
            "재현 노트 또는 TODO.",
            "Issues/PR에 더 자세히 풀 예정.",
        ),
    }
    h = hooks.get(cat, hooks["foundations"])
    venue = "TIL / reading note" if cat == "til" else "see paper"
    url = f"https://scholar.google.com/scholar?q={title.replace(' ', '+')}"
    return (title, venue, url, cat, *h)


def render_note(filename: str, date: str, data: tuple) -> str:
    title, venue, url, cat, summary, problem, method, results, til = data
    cat_ko = CATEGORIES[cat]
    link_block = f"- [Original Paper / Resource]({url})\n" if url else ""
    return f"""# {title}

> **{venue}** · 읽은 날짜: {date}  
> 분류: {cat_ko}

### 링크
{link_block}- [Summary Note](./{filename})

---

## 한 줄 요약

{summary}

## 문제 정의

{problem}

## 방법 · 핵심 아이디어

{method}

## 실험 · 결과

{results}

## TIL — 내가 가져간 점

{til}

---

*개인 공부 노트입니다. [Deep-Learning-Paper-Review-and-Practice](https://github.com/SukoJim/Deep-Learning-Paper-Review-and-Practice) 형식을 참고했습니다.*
"""


def render_readme(entries: list[dict]) -> str:
    by_cat: dict[str, list[dict]] = {k: [] for k in CATEGORIES}
    for e in entries:
        by_cat[e["cat"]].append(e)

    intro = """### 꼼꼼한 멀티에이전트 논문 TIL · Multi-Agent Paper Log

- **멀티에이전트 LLM** (orchestration, tools, memory, eval) 공부하면서 읽은 논문·프레임워크·벤치마크 정리 저장소입니다.
- 형식 참고: [SukoJim/Deep-Learning-Paper-Review-and-Practice](https://github.com/SukoJim/Deep-Learning-Paper-Review-and-Practice) — Original Paper / Reading Note 구조.
- 2025년 말부터 하루에 한 편(가끔 TIL 메모) 페이스로 기록 중입니다.
- 질문·오타는 **Issues**에 남겨주세요.

| 폴더 | 설명 |
|------|------|
| [`lecture_notes/`](lecture_notes/) | 논문 리뷰 · TIL 마크다운 |
| [`code_practices/`](code_practices/) | (선택) reproduce 스크립트 · 실험 노트 |

"""
    body = []
    for cat, label in CATEGORIES.items():
        items = sorted(by_cat[cat], key=lambda x: x["date"])
        if not items:
            continue
        body.append(f"#### {label}\n")
        for e in items:
            paper_link = f"  * [Original Paper / Resource]({e['url']}) / " if e["url"] else "  * "
            body.append(
                f"* **{e['title']}** ({e['venue']})\n"
                f"{paper_link}"
                f"[Reading Note](lecture_notes/{e['filename']})\n"
            )
        body.append("")
    timeline = "\n".join(
        f"| {e['date']} | [{e['title']}](lecture_notes/{e['filename']}) |"
        for e in sorted(entries, key=lambda x: x["date"])
    )
    return (
        intro
        + "\n".join(body)
        + "\n<details>\n<summary>날짜순 전체 인덱스</summary>\n\n| Date | Note |\n|------|------|\n"
        + timeline
        + "\n\n</details>\n"
    )


def main() -> None:
    source_dir = PAPERS_DIR if PAPERS_DIR.exists() else LECTURE_DIR
    if not source_dir.exists():
        raise SystemExit("No papers/ or lecture_notes/ found.")

    if LECTURE_DIR.exists() and source_dir is PAPERS_DIR:
        shutil.rmtree(LECTURE_DIR)
    LECTURE_DIR.mkdir(exist_ok=True)
    CODE_DIR.mkdir(exist_ok=True)
    (CODE_DIR / "README.md").write_text(
        "# code_practices\n\n"
        "논문 reproduce · agent loop 미니 실험 스크립트를 두는 폴더입니다.\n"
        "리뷰 위주 저장소라 필수는 아니며, 필요할 때 브랜치/서브폴더로 추가합니다.\n",
        encoding="utf-8",
    )

    entries: list[dict] = []
    for path in sorted(source_dir.glob("*.md")):
        date, title_from_file = parse_existing(path)
        slug = slug_from_filename(path.name)
        if slug in TIL_CUSTOM:
            data = TIL_CUSTOM[slug]
        elif slug in PAPER_DB:
            data = PAPER_DB[slug]
        else:
            cat = infer_category(slug, title_from_file)
            data = fallback_content(slug, title_from_file, cat)
        note_name = path.name
        (LECTURE_DIR / note_name).write_text(render_note(note_name, date, data), encoding="utf-8")
        entries.append(
            {
                "date": date,
                "filename": note_name,
                "title": data[0],
                "venue": data[1],
                "url": data[2],
                "cat": data[3],
            }
        )

    (ROOT / "README.md").write_text(render_readme(entries), encoding="utf-8")
    print(f"Wrote {len(entries)} notes -> lecture_notes/")


if __name__ == "__main__":
    main()
