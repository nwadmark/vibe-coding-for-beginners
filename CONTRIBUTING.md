# Contributing

We welcome contributions from PMs, facilitators, and anyone interested in making vibe coding more accessible. Whether you built a cool tool, found a typo, or have an idea for a new guide — we would love your help.

---

## Ways to Contribute

### Add a New PM Tool Example

Built a tool that other PMs would find useful? Add it to the `build/` folder.

Your submission should include:
- `README.md` — What the tool does, who it is for, and how to use it
- `prompts.md` — The prompts used to build it, with "Why this works" explanations
- `replit/main.py` — A working reference implementation
- `replit/sample-data.*` — Sample data files if the tool reads from files

Use any existing build project (e.g., `build/01-decision-framework/`) as a template for the folder structure.

### Improve Existing Documentation

Found something unclear, outdated, or missing? Documentation improvements are always welcome:
- Fix typos, grammar, or formatting
- Clarify confusing instructions
- Add troubleshooting tips based on your experience
- Update tool guides when interfaces change

### Submit a Showcase

Share what you built with the community:
1. Copy `community/showcases/TEMPLATE.md`
2. Fill in each section
3. Submit as a new file in `community/showcases/`

### Fix Bugs in Example Code

If you find a bug in any of the reference implementations (`replit/main.py` files):
- Describe the bug and how to reproduce it
- Submit a fix that does not change the tool's intended behavior
- Test with the sample data provided

### Suggest New Theory Topics

Have an idea for a theory doc that would help PMs understand vibe coding better? Open an issue describing:
- The topic
- Who it helps
- What it would cover
- Why it is not already covered by existing docs

### Translate Content

Want to make the workshop accessible in another language? We welcome translations of:
- The participant guide
- The prompts library
- The FAQ

Create a folder like `workshop/es/` (for Spanish) or `workshop/ja/` (for Japanese) and translate the key files.

### Report Issues

Found something broken or confusing? Open a GitHub issue with:
- What you expected to happen
- What actually happened
- Which file or section is affected
- Your environment (which AI tool, which code editor)

---

## How to Contribute

1. **Fork** the repository
2. **Create a branch** for your changes (`git checkout -b add-my-tool`)
3. **Make your changes** — follow the existing style and structure
4. **Test your changes** — if you added code, run it. If you edited docs, read them.
5. **Submit a pull request** with a clear description of what you changed and why

### PR Guidelines

- Keep PRs focused — one change per PR
- Follow the existing file structure and naming conventions
- Use plain English — no jargon, no assumptions about technical knowledge
- Test code examples before submitting
- Do not add dependencies unless absolutely necessary (Python built-ins preferred)

---

## Style Guide

- **Tone:** Clear, practical, encouraging. No gatekeeping.
- **Audience:** Product managers who have never coded. Do not assume technical knowledge.
- **Format:** GitHub-flavored Markdown. Use tables, headers, and code blocks for structure.
- **Line length:** No hard limit, but keep paragraphs short (3-4 sentences max).
- **Contractions:** Use them. "You don't" instead of "you do not" in guides and docs.
- **Prompts:** Always include in fenced code blocks so they are easy to copy.

---

## Code of Conduct

All contributors are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md). The short version: be welcoming, be patient, be constructive.
