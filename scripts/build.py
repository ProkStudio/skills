# -*- coding: utf-8 -*-
# Assembles a curated agent-skills repo from cloned sources.
import os, re, io, json, shutil

SRC = r"D:\skills-src"
DST = r"D:\skills"

IGNORE = shutil.ignore_patterns(".git", "node_modules", "__pycache__", "*.pyc")
SKIP_WALK = set([".git", "node_modules", ".claude", ".codex", ".gemini", ".hermes",
                 ".vibe", ".claude-plugin", ".codex-plugin", ".github", "__pycache__"])

CATS = {
 "video": ["remotion-best-practices","remotion-captions","remotion-create","remotion-docs",
   "remotion-interactivity","remotion-maps","remotion-markup","remotion-multimedia",
   "remotion-render","remotion-saas","remotion-studio","remotion-upgrade",
   "video-downloader","demo-video","slack-gif-creator"],
 "media-design": ["image-enhancer","imagen","elevenlabs","google-tts","algorithmic-art",
   "canvas-design","theme-factory","brand-guidelines","design-system"],
 "web": ["frontend-design","web-artifacts-builder","webapp-testing","artifacts-builder",
   "full-page-screenshot","browser-automation","universal-scraping-architect","a11y-audit"],
 "docs": ["docx","pdf","pptx","xlsx","doc-coauthoring","internal-comms","md-document",
   "md-review","md-slides","markdown-html-orchestrator","changelog-generator",
   "content-research-writer","runbook-generator"],
 "engineering": ["code-reviewer","pr-review-expert","tdd-guide","focused-fix","code-tour",
   "codebase-onboarding","monorepo-navigator","tech-debt-tracker","performance-profiler",
   "spec-driven-workflow","zero-hallucination-coder","strict-api","api-design-reviewer",
   "api-test-suite-builder","coverage","interview-system-designer","epic-design",
   "tech-stack-evaluator","senior-backend","senior-frontend","senior-fullstack",
   "senior-qa","senior-ml-engineer","senior-computer-vision","senior-data-engineer",
   "senior-data-scientist","embedded-iot-mentor"],
 "devops": ["docker-development","kubernetes-operator","helm-chart-builder",
   "ci-cd-pipeline-builder","terraform-patterns","chaos-engineering","feature-flags-architect",
   "observability-designer","slo-architect","incident-commander","incident-response",
   "env-secrets-manager","secrets-vault-manager","aws-solution-architect",
   "azure-cloud-architect","gcp-cloud-architect","git-worktree-manager","senior-devops"],
 "security": ["security-guidance","skill-security-auditor","ai-security","cloud-security",
   "red-team","security-pen-testing","threat-detection","dependency-auditor",
   "senior-security","senior-secops","adversarial-reviewer"],
 "data": ["postgres","mysql","mssql","sql-database-assistant","database-designer",
   "database-schema-designer","migration-architect","snowflake-development","google-sheets",
   "statistical-analyst","data-quality-auditor","rag-architect","llm-cost-optimizer"],
 "testing": ["skill-tester","ship-gate"],
 "collaboration": ["handoff","human-gate"],
 "architecture": ["senior-architect"],
 "research": ["deep-research","deepread","dossier","litreview","notebooklm","autoresearch-agent"],
 "meta": ["skill-creator","mcp-builder","mcp-server-builder","claude-api","academy-guide",
   "write-a-skill","skill-doctor","book-to-skill","agent-designer","agent-workflow-designer",
   "agent-harness","agent-memory","memory-engineering","prompt-governance","self-eval",
   "self-improving-agent","workflow-builder","board","eval","claude-coach",
   "discernment-nudge","senior-prompt-engineer"],
 "integrations": ["gmail","google-calendar","google-docs","google-drive","google-slides",
   "google-chat","telegram","whatsapp","atlassian","azure-devops","outline",
   "apple-container","jules","grok-build","manus","stripe-integration-expert",
   "file-organizer","meeting-insights-analyzer"],
 "productivity": ["capture","deep-work","inbox-triage","meetings","reflect","weekly-review"],
}
NAME2CAT = {}
for c, ns in CATS.items():
    for n in ns:
        NAME2CAT[n] = c

ALI = ["agent-harness","agent-memory","board","eval","autoresearch-agent","book-to-skill",
 "chaos-engineering","claude-coach","code-tour","data-quality-auditor","demo-video",
 "docker-development","feature-flags-architect","handoff","helm-chart-builder","human-gate",
 "kubernetes-operator","llm-cost-optimizer","memory-engineering","prompt-governance",
 "security-guidance","skill-doctor","agent-designer","agent-workflow-designer",
 "api-design-reviewer","api-test-suite-builder","browser-automation","ci-cd-pipeline-builder",
 "codebase-onboarding","database-designer","database-schema-designer","dependency-auditor",
 "env-secrets-manager","focused-fix","full-page-screenshot","git-worktree-manager",
 "mcp-server-builder","migration-architect","monorepo-navigator","observability-designer",
 "performance-profiler","pr-review-expert","rag-architect","runbook-generator",
 "secrets-vault-manager","self-eval","ship-gate","skill-security-auditor","skill-tester",
 "slo-architect","spec-driven-workflow","sql-database-assistant","statistical-analyst",
 "strict-api","tech-debt-tracker","terraform-patterns","universal-scraping-architect",
 "workflow-builder","write-a-skill","zero-hallucination-coder","interview-system-designer",
 "a11y-audit","adversarial-reviewer","ai-security","aws-solution-architect",
 "azure-cloud-architect","cloud-security","code-reviewer","coverage","epic-design",
 "gcp-cloud-architect","incident-commander","incident-response","red-team",
 "security-pen-testing","self-improving-agent","senior-architect","senior-backend",
 "senior-computer-vision","senior-data-engineer","senior-data-scientist","senior-devops",
 "senior-frontend","senior-fullstack","senior-ml-engineer","senior-prompt-engineer",
 "senior-qa","senior-secops","senior-security","snowflake-development",
 "stripe-integration-expert","tdd-guide","tech-stack-evaluator","threat-detection",
 "embedded-iot-mentor","capture","deep-work","inbox-triage","meetings","reflect",
 "weekly-review","deepread","dossier","litreview","design-system","md-document",
 "md-review","md-slides","markdown-html-orchestrator"]

COMPOSIO = ["video-downloader","image-enhancer","file-organizer","changelog-generator",
 "meeting-insights-analyzer","content-research-writer","artifacts-builder"]

REPOS = [
 {"dir":"remotion-skills","url":"https://github.com/remotion-dev/skills",
  "license":"See source repo (remotion-dev/skills)","cat":"video","allow":"*","roots":["skills"]},
 {"dir":"remotion-claude-skill","url":"https://github.com/haidrrrry/claude-remotion-skill",
  "license":"MIT","cat":"video","allow":"*","roots":None},
 {"dir":"anthropics-skills","url":"https://github.com/anthropics/skills",
  "license":"See per-skill LICENSE / THIRD_PARTY_NOTICES.md in source repo",
  "cat":"docs","allow":"*","roots":["skills"]},
 {"dir":"superpowers-skills","url":"https://github.com/obra/superpowers-skills",
  "license":"MIT","cat":"meta","allow":"*","roots":["skills"]},
 {"dir":"composio-awesome","url":"https://github.com/ComposioHQ/awesome-claude-skills",
  "license":"See source repo","cat":"media-design","allow":COMPOSIO,"roots":None},
 {"dir":"sanjay-ai-skills","url":"https://github.com/sanjay3290/ai-skills",
  "license":"MIT","cat":"integrations","allow":"*","roots":["skills"]},
 {"dir":"alirezarezvani-skills","url":"https://github.com/alirezarezvani/claude-skills",
  "license":"MIT","cat":"engineering","allow":ALI,
  "roots":["engineering","engineering-team","productivity","research","markdown-html"]},
]

SKIP_NAMES = set(["template","template-skill","sample-skill","spec"])


def read_front(path):
    try:
        txt = io.open(path, encoding="utf-8", errors="replace").read()
    except Exception:
        return None, None
    name = None
    desc = None
    s = txt.lstrip()
    if s.startswith("---"):
        body = s[3:]
        end = body.find("\n---")
        fm = body[:end] if end != -1 else body[:3000]
        m = re.search(r"^name:\s*(.+)$", fm, re.M)
        if m:
            name = m.group(1).strip().strip('"').strip("'")
        m = re.search(r"^description:\s*([\s\S]*?)(?=\n[A-Za-z_-]+:\s|\Z)", fm, re.M)
        if m:
            desc = " ".join(m.group(1).split()).strip().strip('"').strip("'")
    if not desc:
        for line in txt.splitlines():
            line = line.strip()
            if line and not line.startswith("---") and not line.startswith("#"):
                desc = line[:400]
                break
    return name, desc


def clip(s, n):
    if not s:
        return ""
    s = s.replace("|", "\\|").replace("\n", " ")
    return s if len(s) <= n else s[: n - 3].rstrip() + "..."


skills_root = os.path.join(DST, "skills")
if os.path.isdir(skills_root):
    shutil.rmtree(skills_root)
os.makedirs(skills_root)
os.makedirs(os.path.join(DST, "licenses"), exist_ok=True)

taken = {}
records = []
dupes = []
issues = []

for repo in REPOS:
    root = os.path.join(SRC, repo["dir"])
    if not os.path.isdir(root):
        issues.append("missing repo: " + repo["dir"])
        continue
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_WALK]
        if "SKILL.md" not in filenames:
            continue
        rel = os.path.relpath(dirpath, root)
        parts = [] if rel == "." else rel.split(os.sep)
        if repo["roots"] and (not parts or parts[0] not in repo["roots"]):
            continue
        fname, fdesc = read_front(os.path.join(dirpath, "SKILL.md"))
        name = parts[-1] if parts else (fname or repo["dir"])
        name = re.sub(r"[^a-z0-9-]", "-", name.lower()).strip("-")
        if not name or name in SKIP_NAMES:
            continue
        if repo["allow"] != "*" and name not in repo["allow"]:
            continue
        if name in taken:
            dupes.append(name + " (" + repo["dir"] + " -> kept " + taken[name] + ")")
            dirnames[:] = []
            continue
        cat = NAME2CAT.get(name)
        if not cat and repo["dir"] == "superpowers-skills" and len(parts) > 1 and parts[-2] != "skills":
            cat = parts[-2]
        if not cat:
            cat = repo["cat"]
        dest = os.path.join(skills_root, cat, name)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copytree(dirpath, dest, ignore=IGNORE)
        taken[name] = repo["dir"]
        if fname and fname != name:
            issues.append("frontmatter name mismatch: " + name + " != " + fname)
        records.append({"name": name, "category": cat, "description": fdesc or "",
                        "source_repo": repo["dir"], "source_url": repo["url"],
                        "license": repo["license"],
                        "source_path": rel.replace("\\", "/"),
                        "path": "skills/" + cat + "/" + name})
        dirnames[:] = []
    for lic in ("LICENSE", "LICENSE.md", "LICENSE.txt", "THIRD_PARTY_NOTICES.md"):
        p = os.path.join(root, lic)
        if os.path.isfile(p):
            shutil.copyfile(p, os.path.join(DST, "licenses", repo["dir"] + "-" + lic))

records.sort(key=lambda r: (r["category"], r["name"]))
cats = {}
for r in records:
    cats.setdefault(r["category"], []).append(r)
by_repo = {}
for r in records:
    by_repo.setdefault(r["source_repo"], []).append(r["name"])

existing = []
home_skills = os.path.join(os.path.expanduser("~"), ".agents", "skills")
if os.path.isdir(home_skills):
    existing = [d for d in os.listdir(home_skills)
                if os.path.isdir(os.path.join(home_skills, d))]
collide = sorted([n for n in taken if n in set(existing)])

io.open(os.path.join(DST, "catalog.json"), "w", encoding="utf-8").write(
    json.dumps({"total": len(records), "skills": records,
                "duplicates_skipped": dupes, "issues": issues,
                "collisions_with_local_agents_skills": collide},
               ensure_ascii=False, indent=1))

CAT_TITLE = {
 "video": "Video generation & rendering",
 "media-design": "Images, audio & design",
 "web": "Web, frontend & browser automation",
 "docs": "Documents & publishing",
 "engineering": "Software engineering",
 "devops": "DevOps, cloud & reliability",
 "security": "Security",
 "data": "Data & databases",
 "debugging": "Debugging",
 "testing": "Testing",
 "collaboration": "Collaboration & workflow",
 "problem-solving": "Problem solving",
 "architecture": "Architecture",
 "research": "Research",
 "meta": "Agents, MCP & skill authoring",
 "integrations": "App integrations",
 "productivity": "Productivity",
}

rd = []
rd.append("# skills\n")
rd.append("A curated, vendored collection of **" + str(len(records)) +
          "** agent skills (`SKILL.md` format), covering everything from coding "
          "to video generation.\n")
rd.append("Every skill is copied verbatim from its upstream repository. "
          "Sources and licenses: see [ATTRIBUTION.md](ATTRIBUTION.md) and [licenses/](licenses).\n")
rd.append("## Install\n")
rd.append("```bash\n# all skills for Claude Code / compatible agents\n"
          "cp -r skills/*/*/ ~/.claude/skills/\n\n"
          "# or for agents that read .agents/skills\n"
          "cp -r skills/*/*/ ~/.agents/skills/\n\n"
          "# or per project\nmkdir -p .claude/skills && cp -r skills/*/*/ .claude/skills/\n```\n")
rd.append("A skill is just a folder with a `SKILL.md` file, so you can also copy "
          "single folders. Remotion skills can alternatively be installed with "
          "`npx remotion skills add`.\n")
rd.append("## Catalog\n")
rd.append("| Category | Skills |\n| --- | --- |\n")
for c in sorted(cats):
    rd.append("| [" + CAT_TITLE.get(c, c) + "](#" + c + ") | " + str(len(cats[c])) + " |\n")
rd.append("\n")
for c in sorted(cats):
    rd.append("### " + c + "\n\n" + CAT_TITLE.get(c, c) + "\n\n")
    rd.append("| Skill | What it does | Source |\n| --- | --- | --- |\n")
    for r in cats[c]:
        rd.append("| `" + r["name"] + "` | " + clip(r["description"], 200) +
                  " | [" + r["source_repo"] + "](" + r["source_url"] + ") |\n")
    rd.append("\n")
rd.append("## Validate\n\n```bash\npython scripts/validate_skills.py\n```\n")
if collide:
    rd.append("\n## Note\n\nThese skill names already exist in `~/.agents/skills` "
              "on the machine this repo was built on, so copying may overwrite them: " +
              ", ".join("`" + n + "`" for n in collide) + ".\n")
io.open(os.path.join(DST, "README.md"), "w", encoding="utf-8").write("".join(rd))

at = []
at.append("# Attribution\n\nThis repository redistributes skills authored by other "
          "projects. All credit goes to the upstream authors; license terms of each "
          "source apply to the copied files. License texts collected from the sources "
          "are in [licenses/](licenses).\n\n")
for repo in REPOS:
    names = by_repo.get(repo["dir"], [])
    if not names:
        continue
    at.append("## " + repo["dir"] + "\n\n- Upstream: " + repo["url"] +
              "\n- License: " + repo["license"] + "\n- Skills included (" +
              str(len(names)) + "): " + ", ".join(sorted(names)) + "\n\n")
at.append("## Not redistributed\n\n- `ComposioHQ/awesome-claude-skills` also ships 800+ "
          "auto-generated per-app integration skills under `composio-skills/`; install "
          "them from upstream if needed.\n- `VoltAgent/awesome-agent-skills` is a link "
          "list, not a skill collection.\n")
io.open(os.path.join(DST, "ATTRIBUTION.md"), "w", encoding="utf-8").write("".join(at))

io.open(os.path.join(DST, ".gitignore"), "w", encoding="utf-8").write(
    "node_modules/\n__pycache__/\n*.pyc\n.DS_Store\nThumbs.db\n.venv/\n")

print(json.dumps({"total": len(records),
                  "by_category": dict((c, len(v)) for c, v in sorted(cats.items())),
                  "by_repo": dict((k, len(v)) for k, v in sorted(by_repo.items())),
                  "duplicates_skipped": len(dupes),
                  "issues": len(issues),
                  "collisions": collide}, ensure_ascii=False))
