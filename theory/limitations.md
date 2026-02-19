# Limitations and Boundaries

Vibe coding is powerful for certain use cases and inappropriate for others. This document draws the line clearly so you know when to use it and when to involve your engineering team.

---

## What Vibe Coding Is Good For

| Use Case | Why It Works |
|---|---|
| **Personal PM tools** | You are the only user. If it breaks, you fix it. No other users are affected. |
| **Internal team utilities** | Small audience, low stakes. A formatting glitch is annoying, not a crisis. |
| **Prototypes and proof-of-concepts** | The goal is to demonstrate an idea, not build a production system. |
| **Data analysis scripts** | One-off analysis of a specific dataset. Run it once, get the answer, move on. |
| **Learning and exploration** | Building tools teaches you about the domain (retention, pricing, statistics). |
| **Workshop and training** | Controlled environment. The tools are exercises, not deliverables. |

The common thread: the blast radius is small. If something goes wrong, the impact is limited to you or your immediate team.

---

## What Vibe Coding Is Not Good For

| Use Case | Why It Does Not Work |
|---|---|
| **Customer-facing features** | No tests, no code review, no security audit. Bugs affect real users. |
| **Anything handling sensitive data** | AI-generated code may not follow security best practices. PII, payment data, and health data need engineering oversight. |
| **Systems that need to scale** | A script that works for 100 rows may break at 100,000. Performance optimization requires engineering. |
| **Code that other developers maintain** | AI-generated code is not designed for team collaboration. It lacks the structure, conventions, and test coverage that teams need. |
| **Anything with regulatory requirements** | HIPAA, SOC 2, GDPR, PCI — compliance requires verified, audited code. |
| **Long-lived production systems** | Tools that need to run reliably for months or years need monitoring, error handling, and maintenance plans. |

The common thread: when other people depend on the code working correctly, reliably, and securely — engineering is required.

---

## The Boundary

Here is a simple decision framework (appropriately meta for this workshop):

```
Is this tool for...

  Just me or my team?
    └─ Yes → Vibe code it
    └─ No, it's customer-facing → Stop. Involve engineering.

  Does it handle sensitive data?
    └─ No → Vibe code it
    └─ Yes → Stop. Involve engineering.

  Does it need to run reliably every day?
    └─ No, it's a one-off or occasional use → Vibe code it
    └─ Yes → Stop. Involve engineering.

  Am I using this to explore an idea or make a decision?
    └─ Yes → Vibe code it
    └─ No, I'm building a permanent system → Stop. Involve engineering.
```

**The gray zone:** Sometimes you build a quick prototype that works so well your team wants to adopt it permanently. This is a good outcome — it means you validated the idea. At that point, hand the prototype and the requirements to engineering. The prototype is a spec, not a deliverable.

---

## Specific Limitations of AI-Generated Code

### No guarantees of correctness

AI-generated code looks right but may have subtle bugs. The model assembles code from patterns — it does not verify mathematical correctness, check for edge cases, or reason about boundary conditions. Always test with known inputs.

**Example from the workshop:** The Decision Framework scoring formula uses Python operator precedence. `(a + b) / c * 10` is parsed as `((a + b) / c) * 10`, which is correct. But if the parentheses were slightly different — `(a + b) / (c * 10)` — the results would be very different. The model might generate either version depending on how the prompt is phrased.

### No tests

AI-generated code does not come with automated tests. If you change one part, there is no safety net to catch if another part broke. For personal tools, you test manually by running the tool. For anything more, tests are needed.

### No error handling for unexpected scenarios

The AI adds basic input validation when asked, but it does not anticipate all the ways things can go wrong: missing files, network errors, corrupt data, out-of-memory conditions. For a personal tool, a crash is fine — you restart and fix it. For a system others depend on, robust error handling is critical.

### No security review

AI-generated code may:
- Read files without checking paths (path traversal)
- Write to disk without checking permissions
- Format strings with user input without sanitizing them
- Handle data in memory without clearing it

For personal tools, these are non-issues. For anything handling sensitive data or exposed to other users, these are vulnerabilities.

### No performance optimization

A script that processes 50 rows of CSV data works fine. The same script on 500,000 rows may take hours or crash. AI-generated code optimizes for readability, not performance. For large datasets, engineering is needed.

---

## How to Talk About This at Work

### "Is this real software?"

Yes — it runs, takes input, produces output, and does useful work. But it is prototype-quality software, not production-quality. Think of it as a working draft, not a published document.

### "Can we ship this to customers?"

Not directly. It needs engineering review, test coverage, security audit, and production hardening first. What you can ship: the validated concept, the requirements it embodies, and a working prototype that demonstrates the idea.

### "Should PMs be writing code?"

PMs are not writing code. They are writing product specs in a format that AI can execute. The code is a byproduct, not the point. The point is that PMs can now explore ideas, validate assumptions, and build internal tools without waiting in the engineering queue.

### "Does this replace developers?"

No. It replaces the *waiting* that happens when a PM has an idea for a simple tool and the engineering team has higher-priority work. The PM builds the prototype; the engineering team builds the production version if the idea proves valuable.

### "What about code quality?"

AI-generated code is inconsistent in quality. Sometimes it is clean and well-structured. Sometimes it has redundancies, poor naming, or subtle bugs. For personal tools, this is acceptable — you are the only user, and you can fix issues as they arise. For team-shared code, quality matters more and engineering review is needed.

---

## A Responsible Approach

1. **Build for yourself first.** Use vibe coding for tools that only you use. Learn the patterns, build confidence, and understand the limitations firsthand.

2. **Share the output, not the code.** When you build a feature prioritization tool and rank your backlog, share the ranked list with your team — not the Python script. The value is in the analysis, not the implementation.

3. **Treat prototypes as prototypes.** If your prototype proves the idea, celebrate that — and then hand it to engineering for proper implementation. The prototype served its purpose.

4. **Be transparent about how you built it.** When sharing results from a vibe-coded tool, say so. "I built a quick scoring tool to rank these features. Here are the criteria and weights I used." Transparency builds trust.

5. **Know your company's AI policy.** Some organizations have policies about using AI assistants, especially regarding proprietary data in prompts. Check with your team before pasting company-specific data into Claude or ChatGPT.

6. **Keep learning.** The more you understand about how code works — even at a surface level — the better your prompts become and the more confidently you can evaluate the output. You do not need to become a developer, but reading code fluency is a multiplier.

---

## Summary

| Do | Do Not |
|---|---|
| Build personal and internal tools | Ship AI-generated code to production |
| Use it for prototyping ideas | Use it with sensitive user data |
| Share the results and analysis | Share unreviewed code for others to maintain |
| Validate concepts quickly | Skip engineering review for anything customer-facing |
| Learn from the generated code | Assume the code is correct without testing |
| Be transparent about how you built it | Imply that vibe-coded tools are production-ready |
