# Case Study — ShopFlow PM Tools

A realistic example of how a product manager applied vibe coding skills from the workshop to real PM work.

---

## Context

Alex is a product manager at ShopFlow, a Series B e-commerce platform that helps small retailers manage inventory, process orders, and track sales. The team has 3 PMs, 12 engineers, and ships on 2-week sprint cycles.

Every quarter, Alex faces the same problem: evaluating 6-10 feature ideas for the roadmap with no consistent framework. Some features get prioritized because the loudest stakeholder pushed for them. Others get killed because nobody championed them. The process felt arbitrary.

Alex had tried spreadsheets, but the criteria changed every quarter, the formulas broke, and nobody trusted the output enough to use it in planning meetings.

---

## The Workshop

Alex attended the vibe coding workshop with zero coding experience. The only tools installed beforehand were a Claude.ai account and a Replit account — both free.

### What Alex Built During the Workshop (60 minutes)

**Loop 1 (10 min):** Pasted Prompt #1 into Claude. Got a working Decision Framework tool. Copied it to Replit. Ran it. Scored a test feature. It worked.

**Loop 2 (15 min):** Pasted Prompt #2. Added input labels and ASCII bar charts. The bar charts were misaligned on the first try — Alex pasted the output back into Claude and said "The bars aren't aligned. Fix the alignment." Second version worked.

**Loop 3 (10 min):** Chose Prompt #3A (Decision Log). Added file persistence so evaluations are saved to `decision_log.txt`. The first version overwrote the file instead of appending — Alex caught this because only the last evaluation appeared in the file. Said "Use append mode, not write mode." Fixed.

**Total workshop time:** 35 minutes of building, 25 minutes of orientation and reflection.

---

## After the Workshop — Customization (30 minutes)

Back at the desk, Alex customized the tool for ShopFlow's actual prioritization criteria:

```
Replace the scoring criteria with ShopFlow's framework:
1. Customer Impact: How many customers affected? (1-10)
2. Revenue Potential: Will this drive upgrades or reduce churn? (1-10)
3. Engineering Cost: How many sprint points? (1-10, higher = more expensive)
4. Strategic Fit: Does this align with our Q2 OKRs? (1-10)

New formula:
Score = (CustomerImpact×2 + RevenuePotential×1.5 + StrategicFit×1) / EngineeringCost × 10

Keep the same output format, bar charts, and decision log.
```

Two prompts, 15 minutes, and the tool was customized for ShopFlow.

---

## The Outcome

### Q2 Planning (Week 1)

Alex evaluated all 8 candidate features in a single 20-minute session:

| Rank | Feature | Score | Decision |
|---|---|---|---|
| 1 | Bulk inventory import via CSV | 42.5 | Strong Go |
| 2 | Real-time low stock alerts | 38.7 | Strong Go |
| 3 | Multi-warehouse support | 22.1 | Strong Go |
| 4 | Customer-facing order tracking | 18.3 | Strong Go |
| 5 | Advanced reporting dashboard | 14.2 | Maybe |
| 6 | API v2 with webhooks | 12.8 | Maybe |
| 7 | White-label storefront | 8.5 | No Go |
| 8 | Cryptocurrency payments | 3.2 | No Go |

Alex brought the decision log and ranked table to the planning meeting. The conversation was different this time — instead of debating opinions, the team discussed criteria weights and whether the scores felt right. Two features were re-evaluated with different assumptions. The final priority list was decided in 30 minutes instead of the usual 2 hours.

### What Changed

- **Saved 3 hours per planning cycle.** The old process was a 2-hour meeting with a 1-hour spreadsheet prep. Now it is 20 minutes of scoring and a 30-minute discussion.
- **Engineering trusted the process more.** Having explicit criteria and weights made the prioritization feel rigorous, not political.
- **Decisions were documented.** The decision log created an audit trail — when someone asked "why did we build X instead of Y?", Alex could pull up the scores and criteria.
- **The tool got shared.** Two other PMs on the team started using it. One customized the criteria for their product area.

---

## What Alex Built Next

### Week 2: Feature Prioritizer (RICE Calculator)

For features that made it past the initial scoring, Alex built a RICE calculator to do a second-pass analysis with more detailed effort estimates. Used the Build 02 prompt with ShopFlow-specific Reach numbers.

### Week 3: Feedback Analyzer

ShopFlow had 400+ pieces of feedback from customer support tickets sitting in a text file. Alex built the sentiment analyzer from Build 06 and added ShopFlow-specific keywords (inventory, shipping, dashboard, sync, import). Found that 60% of negative feedback mentioned "sync" — which informed the decision to prioritize real-time sync improvements.

### Month 2: Cohort Retention Tool (Capstone)

Alex exported user data from ShopFlow's analytics tool and built a cohort retention analyzer as a capstone project. It runs every two weeks before the product review and produces a formatted report that gets pasted into the team Slack channel.

---

## What Did Not Work Initially

**The scoring thresholds were too easy to pass.** With the x10 multiplier in the formula, almost everything scored above 15 ("Strong Go"). Alex adjusted the thresholds: Strong Go > 30, Maybe 15-30, No Go < 15. This spread the scores out and made the tool more discriminating.

**The first version crashed on non-numeric input.** Alex typed "high" instead of a number and the tool threw a `ValueError`. The fix: "Add input validation. If the user types something that isn't a number between 1 and 10, show an error message and ask again."

**It took 3 tries to get the output format right.** The first version was too sparse (just numbers). The second version was too cluttered (every detail on screen at once). The third version — with the summary box at the top and details below — was right. Alex learned that showing the AI an example of the desired output is faster than describing it in words.

**Ties in scoring were confusing.** Two features scored 18.3. Alex added: "When features have the same score, break ties by showing the one with higher Customer Impact first."

---

## Lessons

1. **The prompts are product specs.** Alex realized that writing a prompt is the same skill as writing a feature ticket — inputs, logic, output, edge cases. The skill transferred directly.

2. **Start simple, iterate fast.** The first version was ugly and had bugs. By the third prompt, it was polished and useful. Trying to get everything right on the first try would have taken longer.

3. **The tool is a conversation starter, not a decision maker.** The scores did not replace judgment — they structured the conversation. The team still debated and overrode scores when they had context the tool did not capture.

4. **Customize early.** The generic workshop tool was useful for learning, but the real value came from customizing the criteria and formula for ShopFlow's specific context.

5. **Share the output, not the code.** Nobody on Alex's team looked at the Python script. They looked at the ranked table and the decision log. The code was a means to an end.
