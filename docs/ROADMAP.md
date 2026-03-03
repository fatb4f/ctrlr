## Objective (16 months): maximize “hireability signal” for modern SWE roles adjacent to agents

Target roles this curriculum supports (pick one label for your resume later, but train for overlap):

* **AI Product Engineer / LLM Application Engineer**
* **MLOps / LLMOps Engineer**
* **Platform/Infra Engineer (AI workloads)**

This aligns with where hiring has been trending: teams want people who can **ship AI features into real products**, not just prototype models. Broad workforce reports also keep emphasizing **AI + big data + tech literacy** as fast-growing skill areas. ([World Economic Forum][1])

---

## Near-Term Focus (Week Of March 3, 2026)

With `spawn:memory` now in a usable state, execution priority is:

1. **Fast-ramp core SWE skills**: Python, databases, API design, and data handling.
2. **Use Spawn agentic work as curriculum substrate**: remaining patterns in `spawn` should also feed `mesh` implementation choices.
3. **Protect fixed deadline**: `INF1220 TP1` due **Friday, March 6, 2026**.

### This-week execution split

* `INF1220 TP1`: first-class priority until submitted.
* `spawn`: only high-leverage, low-risk pattern work that supports roadmap learning outcomes.
* New scope: defer anything not improving either TP1 delivery or Python/DB/API/data ramp.

---

## Program guardrails (apply to every phase)

### Definition of Done template (per project)

Each project is only “done” when it includes:

* [ ] Working demo path (`README` + one-command run path)
* [ ] CI green (lint + tests + integration smoke)
* [ ] Measurable SLOs documented (latency, reliability, cost)
* [ ] Evaluation baseline + threshold (for AI outputs)
* [ ] Security baseline (auth/authz, secret handling, input validation)
* [ ] Ops baseline (logs, traces/metrics, failure mode notes)
* [ ] Architecture/tradeoff note (short ADR or design memo)

### Kill / continue rule (monthly)

At month-end, each active project must pass a signal check:

* Keep if it improves portfolio signal for target roles.
* Pivot if progress is good but signal is weak.
* Archive if it cannot demonstrate measurable outcomes within 2 more weeks.

### Project scorecard (0–5 each)

* Correctness and test depth
* Eval quality and regression discipline
* Operability (observability + runbooks)
* Security posture
* Documentation/demo quality

Target: no capstone below average **4/5** across categories.

---

## The “deep dive” pillars (what you’ll be judged on)

1. **Core SWE execution**: Python/TypeScript, APIs, testing, databases, debugging, code review habits.
2. **Agentic systems**: deterministic workflows + agent loops, tool use, memory/state, safety/guardrails. (OpenAI Agents SDK, LangGraph patterns) ([OpenAI Developers][2])
3. **Production AI/LLMOps**: evaluation, tracing/observability, deployment, incident hygiene.

   * Eval-driven iteration (Ragas / MLflow GenAI eval) ([Ragas][3])
   * Standard telemetry for GenAI (OpenTelemetry semconv) ([OpenTelemetry][4])
4. **Cloud-native fundamentals**: Docker + Kubernetes + CI/CD + security basics (still the common substrate for production systems, including AI workloads). ([CNCF][5])

---

## 16-month roadmap (deliverables-first)

### Phase 1 (Months 1–4): SWE foundation + “small agents that ship”

**Skills**

* Python depth (typing, packaging, async, logging), Git, Linux, HTTP, SQL
* Testing discipline: unit/integration, mocks, golden tests for prompts
* Small services: FastAPI (or equivalent), Postgres, Redis

**Deliverables**

* **Project A (Month 2):** “CLI agent” that automates a real workflow (files, tickets, notes), with tests + docs + release tag.
* **Project B (Month 4):** “API-first agent service” (auth, rate limit, structured outputs), deployed on a single VPS or container host.

**Acceptance criteria**

* P95 request latency budget defined and met (document exact number).
* Integration tests run in CI for at least one end-to-end path.
* Cost note includes estimated run-cost per 100 requests.

**Hiring signal**

* Clean repo, CI green, readable README, clear “how to run”, issue tracker with 10–20 closed issues.

---

### Phase 2 (Months 5–8): Agentic workflows + RAG + tool integration

**Skills**

* Agent patterns: tool routing, retries, fallbacks, state machines vs free-form loops (LangGraph “workflows vs agents”) ([LangChain Docs][6])
* OpenAI Agents SDK primitives: tools, handoffs, tracing ([OpenAI Developers][2])
* RAG fundamentals: chunking, embeddings, retrieval strategies, reranking, caching
* Tool interoperability: **MCP** (increasingly common for “plug-in” tool ecosystems) ([GitHub][7])

**Deliverables**

* **Project C (Month 6):** RAG app with measurable quality target (answer relevance, citation correctness).
* **Project D (Month 8):** Multi-step agent workflow (stateful) with at least 5 tools; include an MCP server or client integration.

**Quality bar**

* Add **evaluation-driven development**: baseline dataset + metrics with Ragas. ([Ragas][3])

**Interview loop starts here (not Month 13)**

* Weekly: one debugging drill + one system-design prompt + one short implementation drill.
* Track misses in a “gaps log” and feed next week’s learning tasks from it.

---

### Phase 3 (Months 9–12): Productionization (LLMOps) + Kubernetes + observability

**Skills**

* Containers, CI/CD, secrets, config, migrations
* Kubernetes basics: deployments, services, ingress/gateway, autoscaling
* Observability: traces/metrics/logs; GenAI spans via OpenTelemetry conventions ([OpenTelemetry][4])
* LLM/agent evaluation & monitoring with MLflow GenAI eval or equivalent ([MLflow][8])

**Deliverables**

* **Project E (Month 10):** “Production-ready agent service” on Kubernetes (helm/kustomize), with:

  * tracing, dashboards, alert rules
  * load test script + capacity notes
* **Project F (Month 12):** “LLMOps harness”: offline eval + online monitoring + regression gate in CI.

**Acceptance criteria**

* SLOs and alert thresholds are explicit and tested with one fault-injection scenario.
* Rollback path documented and exercised once.
* Incident mini-runbook exists for top 3 failure modes.

**Why this is high ROI**
Kubernetes is widely reported as the backbone for modern infrastructure and is heavily used for AI workloads in production contexts. ([CNCF][5])

---

### Phase 4 (Months 13–16): Specialize + job-market execution

Pick **one** specialization so your profile is crisp:

**Option 1 — LLM App Engineer (product)**

* Capstone: customer-facing app with guardrails, cost controls, latency targets, and eval gates.

**Option 2 — LLMOps / Platform**

* Capstone: internal “agent platform” (templates, tool registry, eval pipelines, observability defaults).

**Option 3 — Edge/IoT + agents (if you want to connect to your IoT interest)**

* Capstone: “fleet assistant” that diagnoses device health from logs/metrics, creates actions, and integrates with deployment/OTA pipelines (can be simulated if you don’t want hardware).

**Job-market execution (starts Month 13, not Month 16)**

* Week-by-week interview loop: system design + debugging + practical take-home style builds
* Public portfolio polish: 2–3 repos only, each with demo video + architecture diagram + metrics page
* 30–50 targeted applications/month + direct outreach

**Portfolio proof requirements**

For each of the 2–3 flagship repos:

* 2–5 minute demo video
* Architecture diagram
* Metrics/eval snapshot
* One postmortem or major tradeoff write-up

---

## Weekly cadence (ADHD/DCD-friendly, low context-switch)

Use a fixed rhythm and keep WIP tiny.

**Default week (10–12 hrs/week)**

* **1 build block (3–4h):** implement one vertical slice
* **1 hardening block (3–4h):** tests, edge cases, perf, docs
* **1 eval/ops block (2–3h):** add metrics, dashboards, alerts, cost/latency notes
* **1 career block (1–2h):** write a short “work log”, update resume bullets, small networking action

**Rules that keep momentum**

* Max **3 tasks in progress**
* Every task has a 2-line **Definition of Done**
* Prefer **text-first artifacts** (Markdown, Mermaid diagrams) over heavy diagram tools (helps DCD + reduces friction)
* Keep a visible **budget line** per project (tokens, compute, tooling)

---

## Minimum portfolio set (what “good” looks like)

By Month 16 you want **3 strong artifacts**:

1. **Agentic workflow repo** (OpenAI Agents SDK or LangGraph) with traces and tool integrations ([OpenAI Developers][2])
2. **RAG repo** with an evaluation dataset + Ragas metrics + regression gates ([Ragas][3])
3. **Production repo** deployed to Kubernetes with OpenTelemetry GenAI spans + monitoring notes ([OpenTelemetry][4])

Each repo should include:

* clear owner-style README
* measurable outcomes
* ops + security baseline notes
* one explicit “what I would improve next” section

---

## If you want a “day 1” starting point (first 2 weeks)

* Set up one mono-repo template: app + tests + CI + Docker + makefile/tasks
* Ship a tiny tool-using agent (even a CLI) and publish a release
* Add one evaluation loop (even if it’s crude) and make it run in CI

If you share (1) how many hours/week you can sustain and (2) whether you want the end role to skew **product**, **platform**, or **IoT/edge**, I can collapse this into a week-by-week syllabus with concrete project prompts and “done” criteria.

[1]: https://www.weforum.org/publications/the-future-of-jobs-report-2025/?utm_source=chatgpt.com "The Future of Jobs Report 2025 | World Economic Forum"
[2]: https://developers.openai.com/api/docs/guides/agents-sdk/?utm_source=chatgpt.com "Agents SDK | OpenAI API"
[3]: https://docs.ragas.io/en/stable/?utm_source=chatgpt.com "Ragas"
[4]: https://opentelemetry.io/docs/specs/semconv/gen-ai/?utm_source=chatgpt.com "Semantic conventions for generative AI systems"
[5]: https://www.cncf.io/announcements/2026/01/20/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey/?utm_source=chatgpt.com "Kubernetes Established as the De Facto 'Operating System ..."
[6]: https://docs.langchain.com/oss/python/langgraph/workflows-agents?utm_source=chatgpt.com "Workflows and agents - Docs by LangChain"
[7]: https://github.com/modelcontextprotocol/modelcontextprotocol?utm_source=chatgpt.com "Specification and documentation for the Model Context ..."
[8]: https://mlflow.org/docs/latest/genai/eval-monitor/?utm_source=chatgpt.com "Evaluating LLMs/Agents with MLflow"
