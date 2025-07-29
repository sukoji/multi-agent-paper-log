### 꼼꼼한 멀티에이전트 논문 TIL · Multi-Agent Paper Log

- **멀티에이전트 LLM** (orchestration, tools, memory, eval) 공부하면서 읽은 논문·프레임워크·벤치마크 정리 저장소입니다.
- 2025년 말부터 하루에 한 편(가끔 TIL 메모) 페이스로 기록 중입니다.
- 질문·오타는 **Issues**에 남겨주세요.

| 폴더 | 설명 |
|------|------|
| [`lecture_notes/`](lecture_notes/) | 논문 리뷰 · TIL 마크다운 |
| [`code_practices/`](code_practices/) | (선택) reproduce 스크립트 · 실험 노트 |

#### 기초 · 추론 & 액션 루프

* **ReAct: Synergizing Reasoning and Acting in Language Models** (ICLR 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2210.03629) / [Reading Note](lecture_notes/2025-11-26-react.md)

* **Improving Factuality and Reasoning in Language Models through Multiagent Debate** (ICML 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2305.14325) / [Reading Note](lecture_notes/2025-12-21-multi-agent-debate.md)

* **MAD: Multi-Agent Debate for Logical Reasoning** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2402.05178) / [Reading Note](lecture_notes/2025-12-23-mad.md)

* **Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate** (arXiv 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2305.19118) / [Reading Note](lecture_notes/2026-01-04-llm-debate.md)

* **MAP-Neo: Highly Capable and Transparent Bilingual Large Language Model Series** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2405.19327) / [Reading Note](lecture_notes/2026-01-08-map-neo.md)

* **Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning** (ACL 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2305.04091) / [Reading Note](lecture_notes/2026-02-11-plan-and-solve.md)

* **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (NeurIPS 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2305.10601) / [Reading Note](lecture_notes/2026-02-13-tree-of-thoughts.md)

* **Consensus Mechanisms in Multi-Agent Systems** (TIL)
  * [Reading Note](lecture_notes/2026-06-24-consensus-agents.md)


#### 멀티에이전트 프레임워크 & 오케스트레이션

* **CAMEL: Communicative Agents for Mind Exploration of Large Language Model Society** (NeurIPS 2023 Workshop)
  * [Original Paper / Resource](https://arxiv.org/abs/2303.17760) / [Reading Note](lecture_notes/2025-12-02-camel.md)

* **MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework** (ICLR 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2308.00352) / [Reading Note](lecture_notes/2025-12-04-metagpt.md)

* **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation** (COLM 2024 / Microsoft)
  * [Original Paper / Resource](https://arxiv.org/abs/2308.08155) / [Reading Note](lecture_notes/2025-12-06-autogen.md)

* **AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors** (ICLR 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2308.10848) / [Reading Note](lecture_notes/2025-12-12-agentverse.md)

* **LangGraph: Stateful Multi-Actor Applications with LLMs** (LangChain Docs / 2024)
  * [Original Paper / Resource](https://langchain-ai.github.io/langgraph/) / [Reading Note](lecture_notes/2025-12-19-langgraph.md)

* **OpenHands: An Open Platform for AI Software Developers as Generalist Agents** (OpenHands Project / 2024)
  * [Original Paper / Resource](https://github.com/All-Hands-AI/OpenHands) / [Reading Note](lecture_notes/2025-12-26-openhands.md)

* **Agent Laboratory: Using LLM Agents as Research Assistants** (arXiv 2025)
  * [Original Paper / Resource](https://arxiv.org/abs/2501.04227) / [Reading Note](lecture_notes/2025-12-28-agent-laboratory.md)

* **Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks** (Microsoft Research / 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2411.04468) / [Reading Note](lecture_notes/2025-12-30-magentic-one.md)

* **CrewAI: Framework for Orchestrating Role-Playing, Autonomous AI Agents** (CrewAI Docs / 2024)
  * [Original Paper / Resource](https://docs.crewai.com/) / [Reading Note](lecture_notes/2026-01-02-crewai.md)

* **LASS: LLM Agent State Space** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2403.09697) / [Reading Note](lecture_notes/2026-02-15-lass.md)

* **OpenAgents: An Open Platform for Language Agents in the Wild** (EMNLP 2023 Demo)
  * [Original Paper / Resource](https://arxiv.org/abs/2309.09117) / [Reading Note](lecture_notes/2026-02-28-openagents.md)

* **AgentStudio: A Toolkit for Building General Virtual Agents** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2406.08629) / [Reading Note](lecture_notes/2026-03-03-agentstudio.md)

* **Orchestrator-Workers Multi-Agent Pattern** (TIL / Anthropic patterns)
  * [Original Paper / Resource](https://docs.anthropic.com/en/docs/build-with-claude/agentic-patterns) / [Reading Note](lecture_notes/2026-04-10-orchestrator-workers.md)

* **Routing Agents: Dynamic Model and Tool Selection** (TIL)
  * [Reading Note](lecture_notes/2026-04-13-routing-agents.md)

* **Hierarchical Multi-Agent Architectures** (TIL)
  * [Reading Note](lecture_notes/2026-04-15-hierarchical-agents.md)

* **smolagents: Minimal Agent Framework by Hugging Face** (Hugging Face / 2025)
  * [Original Paper / Resource](https://github.com/huggingface/smolagents) / [Reading Note](lecture_notes/2026-05-02-smolagents.md)

* **Building Agents with Llama Models** (TIL / Meta Llama)
  * [Original Paper / Resource](https://www.llama.com/docs/) / [Reading Note](lecture_notes/2026-05-05-llama-agent.md)

* **OpenAI Swarm: Educational Multi-Agent Orchestration** (OpenAI / 2024)
  * [Original Paper / Resource](https://github.com/openai/swarm) / [Reading Note](lecture_notes/2026-05-22-openai-swarm.md)

* **OpenAI Agents SDK** (OpenAI / 2025)
  * [Original Paper / Resource](https://openai.github.io/openai-agents-python/) / [Reading Note](lecture_notes/2026-05-24-agents-sdk.md)

* **Parallel Agent Execution Patterns** (TIL)
  * [Reading Note](lecture_notes/2026-06-14-parallel-agents.md)

* **Supervisor Pattern for Multi-Agent Systems** (TIL / LangGraph)
  * [Original Paper / Resource](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/) / [Reading Note](lecture_notes/2026-06-16-supervisor-pattern.md)

* **Handoff Pattern Between Agents** (TIL / OpenAI Swarm)
  * [Original Paper / Resource](https://github.com/openai/swarm) / [Reading Note](lecture_notes/2026-06-18-handoff-pattern.md)


#### 생성형 · embodied 에이전트

* **Voyager: An Open-Ended Embodied Agent with Large Language Models** (TMLR 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2305.16291) / [Reading Note](lecture_notes/2025-12-10-voyager.md)

* **Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2401.16158) / [Reading Note](lecture_notes/2026-02-22-mobile-agent.md)

* **Cradle: Empower Foundation Agents Towards General Computer Control** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2405.16265) / [Reading Note](lecture_notes/2026-02-24-cradle.md)

* **AppAgent: Multimodal Agents as Smartphone Users** (arXiv 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2312.13771) / [Reading Note](lecture_notes/2026-02-26-appagent.md)

* **Developing a Computer Use Model** (Anthropic / 2024)
  * [Original Paper / Resource](https://www.anthropic.com/news/developing-computer-use) / [Reading Note](lecture_notes/2026-05-20-anthropic-computer-use.md)


#### 웹 · GUI · computer-use 에이전트

* **Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2408.07199) / [Reading Note](lecture_notes/2026-01-06-agent-q.md)

* **WebArena: A Realistic Web Environment for Building Autonomous Agents** (ICLR 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2307.13854) / [Reading Note](lecture_notes/2026-01-13-webarena.md)

* **Mind2Web: Towards a Generalist Agent for the Web** (NeurIPS 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2306.08479) / [Reading Note](lecture_notes/2026-01-15-mind2web.md)

* **Agent-E: From Autonomous Web Navigation to General Computer Control** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2407.15711) / [Reading Note](lecture_notes/2026-03-05-agent-e.md)

* **SeeAct: GPT-4V(ision) is a Generalist Web Agent, If Grounded** (ICML 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2401.01614) / [Reading Note](lecture_notes/2026-03-07-seeact.md)

* **WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?** (ICML 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2404.05971) / [Reading Note](lecture_notes/2026-03-09-workarena.md)

* **VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks** (ACL 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2404.05955) / [Reading Note](lecture_notes/2026-03-11-visualwebarena.md)


#### 도구 사용 · API · 코드 실행

* **Toolformer: Language Models Can Teach Themselves to Use Tools** (NeurIPS 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2302.04761) / [Reading Note](lecture_notes/2025-11-30-toolformer.md)

* **HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face** (NeurIPS 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2303.17580) / [Reading Note](lecture_notes/2025-12-15-hugginggpt.md)

* **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering** (NeurIPS 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2405.15793) / [Reading Note](lecture_notes/2025-12-17-swe-agent.md)

* **Gorilla: Large Language Model for API Calls** (NeurIPS 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2305.15334) / [Reading Note](lecture_notes/2026-01-19-gorilla.md)

* **ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs** (NeurIPS 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2307.16789) / [Reading Note](lecture_notes/2026-01-22-toolllm.md)

* **AnyTool: Self-Reflective, Hierarchical Agents for Large-Scale API Tasks** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2402.12165) / [Reading Note](lecture_notes/2026-01-24-anytool.md)

* **Search-Augmented Agents** (TIL)
  * [Reading Note](lecture_notes/2026-04-25-search-agents.md)

* **Executable Code Actions Elicit Better LLM Agents** (ICML 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2402.01030) / [Reading Note](lecture_notes/2026-04-28-codeact.md)

* **Open Interpreter: Natural Language Interface for Code Execution** (Open Source / 2023)
  * [Original Paper / Resource](https://github.com/OpenInterpreter/open-interpreter) / [Reading Note](lecture_notes/2026-04-30-open-interpreter.md)


#### 메모리 · RAG

* **Generative Agents: Interactive Simulacra of Human Behavior** (UIST 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2304.03442) / [Reading Note](lecture_notes/2025-12-08-generative-agents.md)

* **MemGPT: Towards LLMs as Operating Systems** (arXiv 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2310.08560) / [Reading Note](lecture_notes/2026-01-26-memgpt.md)

* **Generative Agents Memory Architecture Deep Dive** (TIL / UIST 2023 follow-up)
  * [Original Paper / Resource](https://arxiv.org/abs/2304.03442) / [Reading Note](lecture_notes/2026-01-28-generative-agents-memory.md)

* **Agent Workflow Memory** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2409.09163) / [Reading Note](lecture_notes/2026-02-04-agent-workflow-memory.md)

* **Retrieval-Augmented Generation for Agents** (TIL / Lewis et al. extension)
  * [Original Paper / Resource](https://arxiv.org/abs/2005.11401) / [Reading Note](lecture_notes/2026-04-19-rag-agents.md)

* **Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection** (ICLR 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2310.11511) / [Reading Note](lecture_notes/2026-04-21-self-rag.md)

* **FreshLLMs: Refreshing LLMs with Search Engine Augmentation** (ACL 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2310.03214) / [Reading Note](lecture_notes/2026-04-23-freshllms.md)

* **Survey on Memory for LLM Agents** (TIL / arXiv surveys)
  * [Original Paper / Resource](https://arxiv.org/abs/2404.13534) / [Reading Note](lecture_notes/2026-06-06-agent-memory-survey.md)

* **Advanced Retrieval Patterns for Agents** (TIL)
  * [Reading Note](lecture_notes/2026-06-08-retrieval-agents.md)

* **Long Context vs Memory for Agents** (TIL)
  * [Reading Note](lecture_notes/2026-06-10-long-context-agents.md)


#### 벤치마크 · 평가 · 관측

* **AgentBench: Evaluating LLMs as Agents** (ICLR 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2308.03688) / [Reading Note](lecture_notes/2026-01-11-agentbench.md)

* **τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains** (Sierra / arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2406.01719) / [Reading Note](lecture_notes/2026-01-17-tau-bench.md)

* **AgentClinic: A Multimodal Agent Benchmark for Clinical Decision Making** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2405.20678) / [Reading Note](lecture_notes/2026-02-19-agentclinic.md)

* **Let's Verify Step by Step** (OpenAI / arXiv 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2305.20050) / [Reading Note](lecture_notes/2026-03-24-verifiers.md)

* **Process Reward Models for Agent Trajectories** (TIL)
  * [Reading Note](lecture_notes/2026-03-26-process-reward.md)

* **A Survey on Evaluation of LLM-based Agents** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2406.11460) / [Reading Note](lecture_notes/2026-03-28-agent-eval-survey.md)

* **Who & When: Detecting Which Agent Fails and When** (TIL / MAS debugging)
  * [Reading Note](lecture_notes/2026-03-31-who-when-harness.md)

* **AgentOps: Observability for AI Agents** (AgentOps Docs / 2024)
  * [Original Paper / Resource](https://docs.agentops.ai/) / [Reading Note](lecture_notes/2026-04-02-agentops.md)

* **LangSmith Tracing for Multi-Agent Workflows** (LangChain / 2024)
  * [Original Paper / Resource](https://docs.smith.langchain.com/) / [Reading Note](lecture_notes/2026-04-04-langsmith-traces.md)

* **Eval Harness Ablation Studies** (TIL / tierforge)
  * [Reading Note](lecture_notes/2026-05-28-eval-harness-ablation.md)

* **Human Studies for Agent Evaluation** (TIL)
  * [Reading Note](lecture_notes/2026-05-30-human-study-agents.md)

* **Cost and Latency Tradeoffs in Multi-Agent Systems** (TIL)
  * [Reading Note](lecture_notes/2026-06-12-cost-latency.md)

* **LLM-as-Judge for Multi-Agent Outputs** (TIL)
  * [Reading Note](lecture_notes/2026-06-22-judge-agents.md)


#### 안전 · 정렬

* **Misalignment Evolution in Self-Improving Agents** (TIL / safety reading)
  * [Reading Note](lecture_notes/2026-02-02-misevolution.md)

* **AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2410.18404) / [Reading Note](lecture_notes/2026-03-13-agentharm.md)

* **Guardrails for AI Agents** (TIL / Guardrails AI)
  * [Original Paper / Resource](https://www.guardrailsai.com/docs) / [Reading Note](lecture_notes/2026-03-16-guardrails-agents.md)

* **Constitutional AI Applied to Tool-Using Agents** (TIL / Anthropic CAI)
  * [Original Paper / Resource](https://www.anthropic.com/research/constitutional-ai) / [Reading Note](lecture_notes/2026-03-18-constitutional-ai-agents.md)

* **Alignment for Agentic Systems** (TIL / alignment survey)
  * [Reading Note](lecture_notes/2026-03-20-agent-alignment.md)

* **RLHF for Tool-Using Language Models** (TIL / industry papers)
  * [Reading Note](lecture_notes/2026-03-22-rlhf-tools.md)

* **Write Gates for Agent Tool Safety** (TIL / production pattern)
  * [Reading Note](lecture_notes/2026-06-04-write-gates.md)


#### 자기진화 · 워크플로 메모리

* **Reflexion: Language Agents with Verbal Reinforcement Learning** (NeurIPS 2023)
  * [Original Paper / Resource](https://arxiv.org/abs/2303.11366) / [Reading Note](lecture_notes/2025-11-28-reflexion.md)

* **A Survey on Self-Evolving Agents** (arXiv 2025)
  * [Original Paper / Resource](https://arxiv.org/abs/2507.02588) / [Reading Note](lecture_notes/2026-01-30-self-evolving-agents.md)

* **AutoAct: Automatic Agent Learning from Scratch** (arXiv 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2401.05252) / [Reading Note](lecture_notes/2026-02-06-autoact.md)

* **Adaptive Agents: Learning to Adapt in Dynamic Environments** (TIL / ICLR 2024 workshop)
  * [Reading Note](lecture_notes/2026-02-17-adaptive-agent.md)


#### MARL · 협업 RL 기초

* **Building Cooperative Embodied Agents Modularly with Large Language Models** (ICLR 2024)
  * [Original Paper / Resource](https://arxiv.org/abs/2307.02485) / [Reading Note](lecture_notes/2026-02-08-collaborative-agents.md)

* **Multi-Agent Reinforcement Learning: Foundations and Modern Approaches** (TIL / MARL textbook)
  * [Reading Note](lecture_notes/2026-05-07-multi-agent-rl.md)

* **Multi-Agent DDPG (MADDPG)** (ICML 2017)
  * [Original Paper / Resource](https://arxiv.org/abs/1706.02275) / [Reading Note](lecture_notes/2026-05-09-maddpg-note.md)

* **Learning Multiagent Communication with Backpropagation** (NeurIPS 2016)
  * [Original Paper / Resource](https://arxiv.org/abs/1605.07736) / [Reading Note](lecture_notes/2026-05-11-commnet.md)

* **QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning** (ICML 2018)
  * [Original Paper / Resource](https://arxiv.org/abs/1803.11485) / [Reading Note](lecture_notes/2026-05-13-qmix.md)

* **LLM-Based Multi-Agent Reinforcement Learning** (TIL / recent surveys)
  * [Reading Note](lecture_notes/2026-05-15-llm-marl.md)


#### 프로토콜 · SDK · 패턴

* **Model Context Protocol (MCP)** (Anthropic / 2024)
  * [Original Paper / Resource](https://modelcontextprotocol.io/) / [Reading Note](lecture_notes/2026-04-06-mcp.md)

* **Agent2Agent (A2A) Protocol** (Google / 2025)
  * [Original Paper / Resource](https://google.github.io/A2A/) / [Reading Note](lecture_notes/2026-04-08-a2a.md)

* **Agent Protocol: Open Standard for Agent Communication** (TIL / community specs)
  * [Reading Note](lecture_notes/2026-05-18-agent-protocol.md)

* **Claude + MCP Integration Patterns** (TIL / Anthropic)
  * [Original Paper / Resource](https://modelcontextprotocol.io/docs) / [Reading Note](lecture_notes/2026-05-26-claude-mcp.md)


#### TIL · 프로젝트 메모

* **sympo — multi-agent PRD to WBS debate** (TIL / own project)
  * [Original Paper / Resource](https://github.com/sukoji/sympo) / [Reading Note](lecture_notes/2026-04-17-sympo-notes.md)

* **awesome-self-evolving-agents curation notes** (TIL / own repo)
  * [Original Paper / Resource](https://github.com/sukoji/awesome-self-evolving-agents) / [Reading Note](lecture_notes/2026-06-02-awesome-agents.md)

* **Common Failure Modes in Production Agents** (TIL / tierforge)
  * [Original Paper / Resource](https://github.com/sukoji/tierforge) / [Reading Note](lecture_notes/2026-06-20-failure-modes.md)

* **Future Papers Reading Queue** (TIL)
  * [Reading Note](lecture_notes/2026-06-26-reading-queue.md)


<details>
<summary>날짜순 전체 인덱스</summary>

| Date | Note |
|------|------|
| 2025-11-26 | [ReAct: Synergizing Reasoning and Acting in Language Models](lecture_notes/2025-11-26-react.md) |
| 2025-11-28 | [Reflexion: Language Agents with Verbal Reinforcement Learning](lecture_notes/2025-11-28-reflexion.md) |
| 2025-11-30 | [Toolformer: Language Models Can Teach Themselves to Use Tools](lecture_notes/2025-11-30-toolformer.md) |
| 2025-12-02 | [CAMEL: Communicative Agents for Mind Exploration of Large Language Model Society](lecture_notes/2025-12-02-camel.md) |
| 2025-12-04 | [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](lecture_notes/2025-12-04-metagpt.md) |
| 2025-12-06 | [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](lecture_notes/2025-12-06-autogen.md) |
| 2025-12-08 | [Generative Agents: Interactive Simulacra of Human Behavior](lecture_notes/2025-12-08-generative-agents.md) |
| 2025-12-10 | [Voyager: An Open-Ended Embodied Agent with Large Language Models](lecture_notes/2025-12-10-voyager.md) |
| 2025-12-12 | [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](lecture_notes/2025-12-12-agentverse.md) |
| 2025-12-15 | [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](lecture_notes/2025-12-15-hugginggpt.md) |
| 2025-12-17 | [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](lecture_notes/2025-12-17-swe-agent.md) |
| 2025-12-19 | [LangGraph: Stateful Multi-Actor Applications with LLMs](lecture_notes/2025-12-19-langgraph.md) |
| 2025-12-21 | [Improving Factuality and Reasoning in Language Models through Multiagent Debate](lecture_notes/2025-12-21-multi-agent-debate.md) |
| 2025-12-23 | [MAD: Multi-Agent Debate for Logical Reasoning](lecture_notes/2025-12-23-mad.md) |
| 2025-12-26 | [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](lecture_notes/2025-12-26-openhands.md) |
| 2025-12-28 | [Agent Laboratory: Using LLM Agents as Research Assistants](lecture_notes/2025-12-28-agent-laboratory.md) |
| 2025-12-30 | [Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks](lecture_notes/2025-12-30-magentic-one.md) |
| 2026-01-02 | [CrewAI: Framework for Orchestrating Role-Playing, Autonomous AI Agents](lecture_notes/2026-01-02-crewai.md) |
| 2026-01-04 | [Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate](lecture_notes/2026-01-04-llm-debate.md) |
| 2026-01-06 | [Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents](lecture_notes/2026-01-06-agent-q.md) |
| 2026-01-08 | [MAP-Neo: Highly Capable and Transparent Bilingual Large Language Model Series](lecture_notes/2026-01-08-map-neo.md) |
| 2026-01-11 | [AgentBench: Evaluating LLMs as Agents](lecture_notes/2026-01-11-agentbench.md) |
| 2026-01-13 | [WebArena: A Realistic Web Environment for Building Autonomous Agents](lecture_notes/2026-01-13-webarena.md) |
| 2026-01-15 | [Mind2Web: Towards a Generalist Agent for the Web](lecture_notes/2026-01-15-mind2web.md) |
| 2026-01-17 | [τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](lecture_notes/2026-01-17-tau-bench.md) |
| 2026-01-19 | [Gorilla: Large Language Model for API Calls](lecture_notes/2026-01-19-gorilla.md) |
| 2026-01-22 | [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](lecture_notes/2026-01-22-toolllm.md) |
| 2026-01-24 | [AnyTool: Self-Reflective, Hierarchical Agents for Large-Scale API Tasks](lecture_notes/2026-01-24-anytool.md) |
| 2026-01-26 | [MemGPT: Towards LLMs as Operating Systems](lecture_notes/2026-01-26-memgpt.md) |
| 2026-01-28 | [Generative Agents Memory Architecture Deep Dive](lecture_notes/2026-01-28-generative-agents-memory.md) |
| 2026-01-30 | [A Survey on Self-Evolving Agents](lecture_notes/2026-01-30-self-evolving-agents.md) |
| 2026-02-02 | [Misalignment Evolution in Self-Improving Agents](lecture_notes/2026-02-02-misevolution.md) |
| 2026-02-04 | [Agent Workflow Memory](lecture_notes/2026-02-04-agent-workflow-memory.md) |
| 2026-02-06 | [AutoAct: Automatic Agent Learning from Scratch](lecture_notes/2026-02-06-autoact.md) |
| 2026-02-08 | [Building Cooperative Embodied Agents Modularly with Large Language Models](lecture_notes/2026-02-08-collaborative-agents.md) |
| 2026-02-11 | [Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning](lecture_notes/2026-02-11-plan-and-solve.md) |
| 2026-02-13 | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](lecture_notes/2026-02-13-tree-of-thoughts.md) |
| 2026-02-15 | [LASS: LLM Agent State Space](lecture_notes/2026-02-15-lass.md) |
| 2026-02-17 | [Adaptive Agents: Learning to Adapt in Dynamic Environments](lecture_notes/2026-02-17-adaptive-agent.md) |
| 2026-02-19 | [AgentClinic: A Multimodal Agent Benchmark for Clinical Decision Making](lecture_notes/2026-02-19-agentclinic.md) |
| 2026-02-22 | [Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent](lecture_notes/2026-02-22-mobile-agent.md) |
| 2026-02-24 | [Cradle: Empower Foundation Agents Towards General Computer Control](lecture_notes/2026-02-24-cradle.md) |
| 2026-02-26 | [AppAgent: Multimodal Agents as Smartphone Users](lecture_notes/2026-02-26-appagent.md) |
| 2026-02-28 | [OpenAgents: An Open Platform for Language Agents in the Wild](lecture_notes/2026-02-28-openagents.md) |
| 2026-03-03 | [AgentStudio: A Toolkit for Building General Virtual Agents](lecture_notes/2026-03-03-agentstudio.md) |
| 2026-03-05 | [Agent-E: From Autonomous Web Navigation to General Computer Control](lecture_notes/2026-03-05-agent-e.md) |
| 2026-03-07 | [SeeAct: GPT-4V(ision) is a Generalist Web Agent, If Grounded](lecture_notes/2026-03-07-seeact.md) |
| 2026-03-09 | [WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?](lecture_notes/2026-03-09-workarena.md) |
| 2026-03-11 | [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](lecture_notes/2026-03-11-visualwebarena.md) |
| 2026-03-13 | [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](lecture_notes/2026-03-13-agentharm.md) |
| 2026-03-16 | [Guardrails for AI Agents](lecture_notes/2026-03-16-guardrails-agents.md) |
| 2026-03-18 | [Constitutional AI Applied to Tool-Using Agents](lecture_notes/2026-03-18-constitutional-ai-agents.md) |
| 2026-03-20 | [Alignment for Agentic Systems](lecture_notes/2026-03-20-agent-alignment.md) |
| 2026-03-22 | [RLHF for Tool-Using Language Models](lecture_notes/2026-03-22-rlhf-tools.md) |
| 2026-03-24 | [Let's Verify Step by Step](lecture_notes/2026-03-24-verifiers.md) |
| 2026-03-26 | [Process Reward Models for Agent Trajectories](lecture_notes/2026-03-26-process-reward.md) |
| 2026-03-28 | [A Survey on Evaluation of LLM-based Agents](lecture_notes/2026-03-28-agent-eval-survey.md) |
| 2026-03-31 | [Who & When: Detecting Which Agent Fails and When](lecture_notes/2026-03-31-who-when-harness.md) |
| 2026-04-02 | [AgentOps: Observability for AI Agents](lecture_notes/2026-04-02-agentops.md) |
| 2026-04-04 | [LangSmith Tracing for Multi-Agent Workflows](lecture_notes/2026-04-04-langsmith-traces.md) |
| 2026-04-06 | [Model Context Protocol (MCP)](lecture_notes/2026-04-06-mcp.md) |
| 2026-04-08 | [Agent2Agent (A2A) Protocol](lecture_notes/2026-04-08-a2a.md) |
| 2026-04-10 | [Orchestrator-Workers Multi-Agent Pattern](lecture_notes/2026-04-10-orchestrator-workers.md) |
| 2026-04-13 | [Routing Agents: Dynamic Model and Tool Selection](lecture_notes/2026-04-13-routing-agents.md) |
| 2026-04-15 | [Hierarchical Multi-Agent Architectures](lecture_notes/2026-04-15-hierarchical-agents.md) |
| 2026-04-17 | [sympo — multi-agent PRD to WBS debate](lecture_notes/2026-04-17-sympo-notes.md) |
| 2026-04-19 | [Retrieval-Augmented Generation for Agents](lecture_notes/2026-04-19-rag-agents.md) |
| 2026-04-21 | [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](lecture_notes/2026-04-21-self-rag.md) |
| 2026-04-23 | [FreshLLMs: Refreshing LLMs with Search Engine Augmentation](lecture_notes/2026-04-23-freshllms.md) |
| 2026-04-25 | [Search-Augmented Agents](lecture_notes/2026-04-25-search-agents.md) |
| 2026-04-28 | [Executable Code Actions Elicit Better LLM Agents](lecture_notes/2026-04-28-codeact.md) |
| 2026-04-30 | [Open Interpreter: Natural Language Interface for Code Execution](lecture_notes/2026-04-30-open-interpreter.md) |
| 2026-05-02 | [smolagents: Minimal Agent Framework by Hugging Face](lecture_notes/2026-05-02-smolagents.md) |
| 2026-05-05 | [Building Agents with Llama Models](lecture_notes/2026-05-05-llama-agent.md) |
| 2026-05-07 | [Multi-Agent Reinforcement Learning: Foundations and Modern Approaches](lecture_notes/2026-05-07-multi-agent-rl.md) |
| 2026-05-09 | [Multi-Agent DDPG (MADDPG)](lecture_notes/2026-05-09-maddpg-note.md) |
| 2026-05-11 | [Learning Multiagent Communication with Backpropagation](lecture_notes/2026-05-11-commnet.md) |
| 2026-05-13 | [QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning](lecture_notes/2026-05-13-qmix.md) |
| 2026-05-15 | [LLM-Based Multi-Agent Reinforcement Learning](lecture_notes/2026-05-15-llm-marl.md) |
| 2026-05-18 | [Agent Protocol: Open Standard for Agent Communication](lecture_notes/2026-05-18-agent-protocol.md) |
| 2026-05-20 | [Developing a Computer Use Model](lecture_notes/2026-05-20-anthropic-computer-use.md) |
| 2026-05-22 | [OpenAI Swarm: Educational Multi-Agent Orchestration](lecture_notes/2026-05-22-openai-swarm.md) |
| 2026-05-24 | [OpenAI Agents SDK](lecture_notes/2026-05-24-agents-sdk.md) |
| 2026-05-26 | [Claude + MCP Integration Patterns](lecture_notes/2026-05-26-claude-mcp.md) |
| 2026-05-28 | [Eval Harness Ablation Studies](lecture_notes/2026-05-28-eval-harness-ablation.md) |
| 2026-05-30 | [Human Studies for Agent Evaluation](lecture_notes/2026-05-30-human-study-agents.md) |
| 2026-06-02 | [awesome-self-evolving-agents curation notes](lecture_notes/2026-06-02-awesome-agents.md) |
| 2026-06-04 | [Write Gates for Agent Tool Safety](lecture_notes/2026-06-04-write-gates.md) |
| 2026-06-06 | [Survey on Memory for LLM Agents](lecture_notes/2026-06-06-agent-memory-survey.md) |
| 2026-06-08 | [Advanced Retrieval Patterns for Agents](lecture_notes/2026-06-08-retrieval-agents.md) |
| 2026-06-10 | [Long Context vs Memory for Agents](lecture_notes/2026-06-10-long-context-agents.md) |
| 2026-06-12 | [Cost and Latency Tradeoffs in Multi-Agent Systems](lecture_notes/2026-06-12-cost-latency.md) |
| 2026-06-14 | [Parallel Agent Execution Patterns](lecture_notes/2026-06-14-parallel-agents.md) |
| 2026-06-16 | [Supervisor Pattern for Multi-Agent Systems](lecture_notes/2026-06-16-supervisor-pattern.md) |
| 2026-06-18 | [Handoff Pattern Between Agents](lecture_notes/2026-06-18-handoff-pattern.md) |
| 2026-06-20 | [Common Failure Modes in Production Agents](lecture_notes/2026-06-20-failure-modes.md) |
| 2026-06-22 | [LLM-as-Judge for Multi-Agent Outputs](lecture_notes/2026-06-22-judge-agents.md) |
| 2026-06-24 | [Consensus Mechanisms in Multi-Agent Systems](lecture_notes/2026-06-24-consensus-agents.md) |
| 2026-06-26 | [Future Papers Reading Queue](lecture_notes/2026-06-26-reading-queue.md) |

</details>
