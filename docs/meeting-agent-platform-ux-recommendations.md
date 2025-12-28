# Meeting Agent Platform: UX/UI Recommendations

> **The Best at Facilitating 2+ Person Meetings**
>
> A comprehensive guide for building the definitive multi-person meeting facilitation platform.

---

## Executive Summary

### The Opportunity

While most AI meeting tools (Otter, Fireflies, Fathom) passively transcribe and summarize, **no one owns active multi-person facilitation**. This is the gap.

Meetings with 2+ participants have unique dynamics that passive tools ignore:
- Who's dominating the conversation?
- Who hasn't spoken yet?
- Are we on agenda?
- Is everyone engaged?

**Our special sauce**: AI agents that actively facilitate group dynamics in real-time.

### Market Context

| Metric | Value |
|--------|-------|
| Global AI agent market (2025) | $7.38B (doubled from 2023) |
| Organizations using AI agents | 85% have integrated in at least one workflow |
| Facilitators integrating AI | 75% (but mostly for admin, not active facilitation) |
| Cost of ineffective meetings | $399B/year (US) |
| Meetings deemed failures | 67% by executives |

### Competitive Landscape

| Competitor | Approach | Gap |
|------------|----------|-----|
| **Otter, Fireflies, Fathom** | Passive transcription | No active participation |
| **MeetGeek AI Voice Agents** | Active agents (new) | General-purpose, not facilitation-focused |
| **Microsoft Teams Facilitator** | Copilot-driven chair | Platform-locked to Teams |
| **Us** | **Multi-person facilitation specialists** | Cross-platform, purpose-built |

### Core Differentiation

1. **Multi-Speaker Awareness** - Know who's speaking, who isn't, who's dominating
2. **Active Turn Management** - Round-robin, time-boxing, queue management
3. **Participation Balancing** - Draw out quiet voices, manage dominant speakers
4. **Structured Format Support** - L10, Scrum, brainstorming protocols built-in
5. **Real-Time Group Analytics** - Speaking time, engagement, topic adherence

---

## Core Facilitation Capabilities

### The Science of Group Dynamics

Understanding group psychology is essential for effective AI facilitation:

**Social Loafing Effect:**
- Individual effort drops in groups (Ringelmann, 1913)
- In dyads: 66% individual effort
- In 6-person groups: 36% individual effort
- **AI countermeasure**: Individual accountability through turn management

**Optimal Group Sizes (Hackman Research):**
- 4-6 members: Most effective for collaboration
- 3-8 members: Optimal for productive discussion
- 7±2 members: Ideal for decision-making
- >10 members: Cognitive overload, weak bonds

**Participation Barriers:**
- Fear of judgment (psychological safety)
- Dominant speaker intimidation
- Turn-taking anxiety
- Remote meeting disengagement
- **AI countermeasure**: Structured facilitation removes social friction

### Multi-Speaker Technical Foundation

**Speaker Diarization:**
- Modern accuracy: <5% Diarization Error Rate (DER) in optimal conditions
- Real-time capable with NVIDIA Streaming Sortformer
- Challenges: Overlapping speech, interruptions, background noise
- Multimodal approaches: Audio + visual (lip movement) + semantic analysis

**Interruption Handling:**
Types to detect and manage:
- **Cooperative interruptions** - Affirmations, clarifications (allow)
- **Disruptive interruptions** - Topic hijacking (manage)
- **Backchannels** - "mm-hmm", "right" (ignore, don't yield)

**Turn-Taking Intelligence:**
- Detect natural turn completion vs. pauses
- Recognize multi-message sequences (don't respond mid-thought)
- Context-aware participation: improv vs. structured meeting vs. brainstorm

### AI Facilitation Techniques

| Technique | Implementation | When to Use |
|-----------|----------------|-------------|
| **Round Robin** | Call on participants sequentially | Standups, go-arounds |
| **Time-Boxing** | Enforce per-speaker limits | Status updates, presentations |
| **Parking Lot** | Note off-topic items for later | Decision meetings, focused agendas |
| **Hand-Raise Queue** | Manage speaking order | Large groups, Q&A |
| **Go-Rounds** | Ensure everyone contributes once | Retrospectives, consensus |
| **Gentle Prompting** | "Sarah, we haven't heard from you..." | Inclusion, quiet voices |
| **Topic Redirect** | "Great point—let's table that..." | Agenda adherence |
| **Summarize & Check** | "So we're agreeing to X—correct?" | Decision capture |

---

## Meeting Type Strategies

### 1. Team Standups & Syncs (3-10 people)

**The Challenge:**
Daily standups often become status theater—same people talk, others zone out, meetings run long.

**Facilitation Focus:**
- Strict time-boxing per person (2 min default)
- Automatic turn progression
- Blocker flagging for offline follow-up
- Quick pulse check at end

**Agent Persona: Scrum Master**
```
Name: Riley Agile
Voice: Energetic, concise, action-oriented
Entry Message: "Good morning team! Let's keep today's standup tight—15
              minutes max. I'll call on each of you for your update."

Facilitation Rules:
- Round-robin through participant list
- Time warning at 90 seconds, cut-off at 2 minutes
- When blocker mentioned: "Noted—let's take that offline after."
- At end: "Quick pulse—thumbs up if you're unblocked today."
- Capture blockers and assign offline follow-ups
```

**UX Elements:**
```
┌─────────────────────────────────────────────────────────────────┐
│  STANDUP: Engineering Team                     ⏱️ 8:34 / 15:00  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CURRENT SPEAKER                                                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ 👤 Alex Chen                           ⏱️ 1:23 / 2:00   │   │
│  │ ████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  QUEUE                                    COMPLETED             │
│  ┌───────────────────────┐               ┌───────────────────┐ │
│  │ 2. Maria Santos       │               │ ✓ Jordan Lee      │ │
│  │ 3. David Kim          │               │ ✓ Sam Taylor      │ │
│  │ 4. Priya Patel        │               └───────────────────┘ │
│  └───────────────────────┘                                      │
│                                                                 │
│  BLOCKERS CAPTURED                                              │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ 🚫 Jordan: "Waiting on API credentials from DevOps"     │   │
│  │ 🚫 Sam: "Design review blocking frontend work"          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 2. Decision-Making Meetings (5-8 people)

**The Challenge:**
Decisions stall because opinions aren't captured systematically, consensus is assumed but not verified, and action items lack owners.

**Facilitation Focus:**
- Structured option presentation
- Equal voice solicitation
- Explicit consensus checking
- Decision + owner + deadline capture

**Agent Persona: Decision Chair**
```
Name: Morgan Consensus
Voice: Thoughtful, balanced, patient
Entry Message: "Let's make some decisions today. I'll help structure our
              discussion so every option gets fair consideration and we
              leave with clear next steps."

Facilitation Rules:
- Frame decision clearly before discussion
- Solicit pros/cons from different participants
- Use go-rounds for complex decisions
- Straw poll before final commitment
- Explicitly state: "Decision: [X]. Owner: [Y]. Due: [Z]."
```

**Consensus Techniques:**
```
┌─────────────────────────────────────────────────────────────────┐
│  DECISION: Which vendor for cloud infrastructure?               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  OPTIONS UNDER DISCUSSION                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ A. AWS                  │ B. GCP           │ C. Azure   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  PARTICIPANT INPUT                                              │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Sarah:  "AWS - existing expertise"        ●○○           │   │
│  │ Mike:   "GCP - better ML tools"           ○●○           │   │
│  │ Priya:  "Azure - enterprise compliance"   ○○●           │   │
│  │ Alex:   [Not yet contributed]             ○○○  ← Prompt │   │
│  │ Jordan: "AWS - but concerned about cost"  ●○○           │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  STRAW POLL RESULTS                                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ AWS: ███████████████  3 votes (60%)                     │   │
│  │ GCP: ██████           1 vote  (20%)                     │   │
│  │ Azure: ██████         1 vote  (20%)                     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  [Move to Final Vote]  [More Discussion]  [Table Decision]     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3. Brainstorming & Ideation (4-12 people)

**The Challenge:**
A few voices dominate. Ideas get shot down prematurely. Groupthink takes over. Introverts don't contribute.

**Facilitation Focus:**
- Silent ideation before group sharing (avoid anchoring)
- Equal time for idea presentation
- "Yes, and..." culture enforcement
- Deferred judgment
- Structured convergence (dot voting)

**Agent Persona: Brainstorm Moderator**
```
Name: Sage Ideation
Voice: Enthusiastic, encouraging, curious
Entry Message: "Exciting! Let's generate some wild ideas today. Remember:
              no idea is too crazy, and we're not judging yet—that comes
              later. Let's start with 2 minutes of silent brainstorming."

Facilitation Rules:
- Start with silent/written ideation phase
- Round-robin idea sharing (1 idea per turn)
- Redirect criticism: "Great energy—let's save evaluation for later"
- Build on ideas: "Love it—anyone want to add to that?"
- Cluster similar ideas during sharing
- Dot voting for convergence
```

**Ideation Flow:**
```
┌─────────────────────────────────────────────────────────────────┐
│  BRAINSTORM: New Product Features                    Phase 2/4  │
│  ═══════════════════════●═══════════════════                    │
│  Silent Think → Share → Cluster → Vote                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SHARING ROUND (Each person: 1 idea)                            │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Current: "AI-powered search across all documents"       │   │
│  │ Shared by: Maria                                         │   │
│  │                                                          │   │
│  │ Build on this idea? [Yes, and...]  [Next Person]        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  IDEAS CAPTURED                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ 💡 Mobile app redesign (Alex)                           │   │
│  │ 💡 Voice control interface (Jordan)                     │   │
│  │ 💡 AI-powered search (Maria) ← Current                  │   │
│  │ 💡 ... more ideas appearing ...                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  PARTICIPATION                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ ✓ Alex    ✓ Jordan   ● Maria    ○ Sam    ○ Priya       │   │
│  │ Shared    Shared     Sharing    Next     Waiting       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 4. Retrospectives & Reviews (5-15 people)

**The Challenge:**
Retrospectives become complaint sessions without action. Same issues repeat. Quiet team members don't share concerns.

**Facilitation Focus:**
- Structured framework (Start/Stop/Continue, 4Ls, etc.)
- Anonymous input option for psychological safety
- Balanced contribution from all
- Action item commitment with owners

**Agent Persona: Retro Guide**
```
Name: Casey Reflect
Voice: Calm, reflective, constructive
Entry Message: "Time to reflect on our sprint. Everything shared here
              stays here. Let's celebrate wins, learn from challenges,
              and commit to improvements."

Facilitation Rules:
- Start with wins/positives (energy boost)
- Use framework structure strictly
- Equal time per category
- Prompt quiet participants specifically
- Cluster themes and vote on priorities
- End with concrete actions + owners
```

**Retrospective Interface:**
```
┌─────────────────────────────────────────────────────────────────┐
│  RETROSPECTIVE: Sprint 24                           Framework: 4Ls│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌─────────┐│
│  │   LIKED      │ │   LEARNED    │ │   LACKED     │ │ LONGED  ││
│  │   (12)       │ │   (8)        │ │   (5)        │ │ FOR (7) ││
│  │   ●          │ │   ○          │ │   ○          │ │   ○     ││
│  └──────────────┘ └──────────────┘ └──────────────┘ └─────────┘│
│                                                                 │
│  CURRENTLY DISCUSSING: LIKED                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ "Pair programming really helped with the auth feature"  │   │
│  │                                   - Jordan (3 votes)    │   │
│  │                                                          │   │
│  │ "Faster CI pipeline saved time"                          │   │
│  │                                   - Sam (2 votes)       │   │
│  │                                                          │   │
│  │ [+ Add your own]  [Vote on existing]                    │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  PARTICIPATION TRACKER                                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Alex: ████░ 4 items   Sam: ███░░ 3 items                │   │
│  │ Maria: █████ 5 items  Jordan: ██░░░ 2 items             │   │
│  │ Priya: █░░░░ 1 item  ← "Priya, anything to add?"        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 5. Training & Workshops (5-20 people)

**The Challenge:**
Large group training becomes passive. Engagement drops. Questions don't get asked. Knowledge transfer is one-way.

**Facilitation Focus:**
- Structured Q&A management
- Breakout coordination
- Engagement checks
- Knowledge retention prompts

**Agent Persona: Workshop Leader**
```
Name: Taylor Teach
Voice: Clear, patient, encouraging
Entry Message: "Welcome to today's session! We'll balance instruction
              with interaction. Don't hesitate to use the hand-raise
              feature—your questions make this better for everyone."

Facilitation Rules:
- Check understanding every 10-15 minutes
- Queue and manage questions fairly
- Prompt engagement: "Quick poll: who's tried this before?"
- Summarize key points before transitions
- Coordinate breakout groups
```

---

### 6. Leadership & L10 Meetings (5-10 people)

**The Challenge:**
Leadership meetings drift off-agenda. Scorecard review becomes interrogation. Issues don't get solved—just discussed.

**Facilitation Focus:**
- Strict L10 agenda adherence (90 minutes)
- IDS process enforcement (Identify, Discuss, Solve)
- Time-box each segment
- Decision and to-do capture

**Agent Persona: L10 Facilitator**
```
Name: Liam Leadership
Voice: Confident, efficient, business-focused
Entry Message: "Let's run a Level 10 meeting. We have 90 minutes—I'll
              keep us moving so we leave with real progress."

L10 Agenda Enforcement:
1. Segue (5 min): One personal, one professional win
2. Scorecard (5 min): Numbers on/off track only
3. Rock Review (5 min): On/off track status
4. Customer/Employee Headlines (5 min): Quick updates
5. To-Do List (5 min): Status from last week
6. IDS (60 min): Solve top issues using Identify-Discuss-Solve
7. Conclude (5 min): Recap, rate the meeting 1-10
```

**L10 Dashboard:**
```
┌─────────────────────────────────────────────────────────────────┐
│  L10 MEETING: Leadership Team            ⏱️ 32:15 / 90:00      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  AGENDA PROGRESS                                                │
│  ✓ Segue  ✓ Scorecard  ✓ Rocks  ● IDS  ○ Conclude              │
│  ════════════════════════════●═══════════════════════           │
│                                                                 │
│  IDS: ISSUE #3 of 7                          ⏱️ 12:45 remaining │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ ISSUE: "Q4 hiring target at risk due to budget freeze"  │   │
│  │                                                          │   │
│  │ PHASE: ○ Identify  ● Discuss  ○ Solve                   │   │
│  │                                                          │   │
│  │ Discussion Notes:                                        │   │
│  │ - CFO confirmed freeze through December                 │   │
│  │ - Could reallocate from contractor budget               │   │
│  │ - Marketing willing to delay 1 hire to help             │   │
│  │                                                          │   │
│  │ [Move to SOLVE]  [Need More Discussion]  [Table]        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  SPEAKING TIME                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ CEO: ██████████████████░░  35%                          │   │
│  │ CFO: ████████████░░░░░░░░  25%  ← Prompted              │   │
│  │ CTO: ████████░░░░░░░░░░░░  18%                          │   │
│  │ CMO: █████░░░░░░░░░░░░░░░  12%                          │   │
│  │ COO: ███░░░░░░░░░░░░░░░░░  10%  ← "Alex, your take?"   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## UX/UI Recommendations

### A. Pre-Meeting Configuration

**Meeting Type Selection (Primary UX Decision):**
```
┌─────────────────────────────────────────────────────────────────┐
│  NEW FACILITATED MEETING                                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  What type of meeting is this?                                  │
│  (This determines how your agent facilitates)                   │
│                                                                 │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐    │
│  │ 📋 STANDUP     │  │ 🎯 DECISION    │  │ 💡 BRAINSTORM  │    │
│  │                │  │                │  │                │    │
│  │ Quick updates  │  │ Choose between │  │ Generate ideas │    │
│  │ 3-10 people    │  │ options        │  │ 4-12 people    │    │
│  │ 15 min         │  │ 5-8 people     │  │ 30-60 min      │    │
│  └────────────────┘  └────────────────┘  └────────────────┘    │
│                                                                 │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐    │
│  │ 🔄 RETRO       │  │ 📊 L10/EOS     │  │ 🎓 TRAINING    │    │
│  │                │  │                │  │                │    │
│  │ Sprint review  │  │ Leadership     │  │ Learning       │    │
│  │ 5-15 people    │  │ team meeting   │  │ session        │    │
│  │ 60 min         │  │ 5-10 people    │  │ 5-50 people    │    │
│  └────────────────┘  └────────────────┘  └────────────────┘    │
│                                                                 │
│                                                    [Next →]     │
└─────────────────────────────────────────────────────────────────┘
```

**Participant Roster:**
```
┌─────────────────────────────────────────────────────────────────┐
│  PARTICIPANTS                                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Import from: [Calendar Invite ▼]  or  [Enter Manually]        │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Name              │ Role        │ Speaking Order         │   │
│  ├───────────────────┼─────────────┼────────────────────────│   │
│  │ Sarah Johnson     │ Facilitator │ N/A                    │   │
│  │ Mike Chen         │ Presenter   │ 1st                    │   │
│  │ Priya Patel       │ Participant │ 2nd (after Mike)       │   │
│  │ Alex Kim          │ Participant │ 3rd                    │   │
│  │ Jordan Davis      │ Observer    │ Only if called on      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  [+ Add Participant]              [Import from Previous]       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Agenda Builder with Time-Boxing:**
```
┌─────────────────────────────────────────────────────────────────┐
│  AGENDA                                    Total: 45 min        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───┬────────────────────────────────────────────┬──────────┐ │
│  │ # │ Topic                                      │ Time     │ │
│  ├───┼────────────────────────────────────────────┼──────────┤ │
│  │ 1 │ Opening & context                          │ 5 min    │ │
│  │ 2 │ Review options A, B, C                     │ 15 min   │ │
│  │ 3 │ Open discussion                            │ 15 min   │ │
│  │ 4 │ Vote and decide                            │ 5 min    │ │
│  │ 5 │ Assign action items                        │ 5 min    │ │
│  └───┴────────────────────────────────────────────┴──────────┘ │
│                                                                 │
│  [+ Add Topic]                                                  │
│                                                                 │
│  FACILITATION RULES                                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ ☑ Enforce time limits (warn at 80%, interrupt at 100%) │   │
│  │ ☑ Ensure all participants speak before repeats          │   │
│  │ ☐ Allow flexible time (topics can run over)            │   │
│  │ ☑ Use parking lot for off-topic items                   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### B. Live Facilitation Dashboard

**Participation Balance View (Core Differentiator):**
```
┌─────────────────────────────────────────────────────────────────┐
│  LIVE: Product Planning Meeting                  ⏱️ 23:15       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SPEAKING TIME DISTRIBUTION                                     │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │           Sarah                                          │   │
│  │          ╱     ╲                                         │   │
│  │         ╱   38%  ╲        Mike                           │   │
│  │        ╱           ╲     ╱    ╲                          │   │
│  │       │             │   │  22%  │                        │   │
│  │        ╲           ╱     ╲    ╱                          │   │
│  │  Alex   ╲        ╱        ──                             │   │
│  │   15%    ─────────   Priya: 18%   Jordan: 7%            │   │
│  │                                                          │   │
│  │  ⚠️ Jordan hasn't spoken in 8 minutes                   │   │
│  │  ⚠️ Sarah speaking 2x more than average                 │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  AGENT ACTION: "Jordan, what's your take on this approach?"    │
│                                                                 │
│  QUICK ACTIONS                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ [Prompt Quiet Voices]  [Balance Discussion]  [Move On]  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Agenda Progress Tracker:**
```
┌─────────────────────────────────────────────────────────────────┐
│  AGENDA PROGRESS                                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ✓ Topic 1 (5 min)    ✓ Topic 2 (15 min)    ● Topic 3 (15 min) │
│  ═════════════════════════════════════════●════════════════     │
│                                           ↑                     │
│                                      You are here               │
│                                      8:42 remaining             │
│                                                                 │
│  CURRENT TOPIC: "Open Discussion"                               │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Time: ████████████████░░░░░░░░░░  8:42 / 15:00          │   │
│  │                                                          │   │
│  │ Key Points Captured:                                     │   │
│  │ • Integration with existing CRM is priority (Sarah)      │   │
│  │ • Budget concerns for Q1 launch (Mike)                   │   │
│  │ • Competitor launching similar in Feb (Priya)            │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  PARKING LOT (Off-topic items for later)                        │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ • Team capacity discussion (raised by Alex)              │   │
│  │ • New vendor evaluation (raised by Jordan)               │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Real-Time Intervention Controls:**
```
┌─────────────────────────────────────────────────────────────────┐
│  FACILITATOR CONTROLS                                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌───────────┐ │
│  │   WHISPER   │ │  TAKE OVER  │ │    NUDGE    │ │  WRAP UP  │ │
│  │   to Agent  │ │   (Human)   │ │   Speaker   │ │   Topic   │ │
│  └─────────────┘ └─────────────┘ └─────────────┘ └───────────┘ │
│                                                                 │
│  Whisper (only agent hears):                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ [Type instruction to agent...]              [Send]       │   │
│  │                                                          │   │
│  │ Quick whispers:                                          │   │
│  │ • "Wrap up current speaker"                              │   │
│  │ • "Ask [name] for input"                                 │   │
│  │ • "Move to next agenda item"                             │   │
│  │ • "Call for a vote"                                      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### C. Post-Meeting Analytics

**Participation Equity Report:**
```
┌─────────────────────────────────────────────────────────────────┐
│  MEETING ANALYTICS: Product Planning (Dec 15)                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PARTICIPATION SCORE: 78/100 ████████████████░░░░ Good         │
│                                                                 │
│  SPEAKING TIME BREAKDOWN                                        │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Participant      │ Time    │ % of Mtg │ vs. Equal Share │   │
│  ├──────────────────┼─────────┼──────────┼─────────────────┤   │
│  │ Sarah Johnson    │ 12:34   │ 38%      │ +18% ⚠️         │   │
│  │ Mike Chen        │ 7:18    │ 22%      │ +2%             │   │
│  │ Priya Patel      │ 5:56    │ 18%      │ -2%             │   │
│  │ Alex Kim         │ 4:52    │ 15%      │ -5%             │   │
│  │ Jordan Davis     │ 2:20    │ 7%       │ -13% ⚠️         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  FACILITATION EFFECTIVENESS                                     │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Agenda adherence:     92%  ████████████████████░░       │   │
│  │ Time management:      85%  █████████████████░░░░░       │   │
│  │ Turn distribution:    78%  ████████████████░░░░░░       │   │
│  │ Decision clarity:     100% ████████████████████████     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  RECOMMENDATIONS FOR NEXT TIME                                  │
│  • Actively prompt Jordan earlier in discussions               │
│  • Set speaking time guidance for Sarah (facilitator)           │
│  • Consider smaller breakout for detailed technical topics      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Trend Analysis Over Time:**
```
┌─────────────────────────────────────────────────────────────────┐
│  TEAM MEETING TRENDS (Last 8 Weeks)                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PARTICIPATION EQUITY TREND                                     │
│  100%│                                                          │
│      │                              ●                           │
│   80%│          ●       ●    ●         ●    ●                  │
│      │     ●                                                    │
│   60%│ ●                                                        │
│      └──────────────────────────────────────────────────────    │
│        W1   W2   W3   W4   W5   W6   W7   W8                    │
│                                                                 │
│  DECISION VELOCITY                                              │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Decisions per meeting:  2.3 → 3.8  (+65%)               │   │
│  │ Avg time to decision:   18 min → 12 min  (-33%)         │   │
│  │ Action items captured:  89% → 97% (+8%)                 │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  INSIGHT: Since adding AI facilitation, Jordan's participation │
│  increased from 5% to 15% of speaking time.                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Developer API Patterns

### Participant Tracking

```
POST /meetings/{meeting_id}/participants
{
  "participants": [
    {
      "id": "user_123",
      "name": "Sarah Johnson",
      "role": "facilitator",
      "speaking_order": null,
      "max_speaking_time": null
    },
    {
      "id": "user_456",
      "name": "Mike Chen",
      "role": "participant",
      "speaking_order": 1,
      "max_speaking_time": 120  // seconds
    }
  ]
}
```

### Real-Time Events Webhook

```
// Webhook payload for participation events
{
  "event": "participation_update",
  "meeting_id": "mtg_abc123",
  "timestamp": "2025-01-15T14:32:18Z",
  "data": {
    "type": "speaker_change",
    "previous_speaker": "user_123",
    "current_speaker": "user_456",
    "participation_stats": {
      "user_123": { "speaking_time": 342, "turn_count": 8, "last_spoke": "14:32:15Z" },
      "user_456": { "speaking_time": 198, "turn_count": 5, "last_spoke": "14:32:18Z" },
      "user_789": { "speaking_time": 45, "turn_count": 2, "last_spoke": "14:18:22Z" }  // Alert: quiet
    },
    "alerts": [
      { "type": "quiet_participant", "user_id": "user_789", "silent_duration": 840 }
    ]
  }
}
```

### Facilitation Commands

```
POST /meetings/{meeting_id}/facilitate
{
  "action": "prompt_participant",
  "target_user": "user_789",
  "prompt_type": "open_question",
  "context": "We're discussing the Q1 timeline"
}

// Response
{
  "status": "executed",
  "agent_message": "Alex, we haven't heard your perspective yet—what are your thoughts on the Q1 timeline?"
}
```

### Meeting Configuration Schema

```
POST /meetings
{
  "type": "decision",
  "title": "Q1 Planning Session",
  "duration_minutes": 60,
  "participants": [...],
  "agenda": [
    { "topic": "Review options", "duration": 15, "type": "presentation" },
    { "topic": "Discussion", "duration": 25, "type": "open_discussion" },
    { "topic": "Vote", "duration": 10, "type": "decision" },
    { "topic": "Actions", "duration": 10, "type": "action_items" }
  ],
  "facilitation": {
    "enforce_time_limits": true,
    "balance_participation": true,
    "quiet_threshold_seconds": 300,
    "dominant_threshold_percent": 40,
    "use_parking_lot": true,
    "capture_decisions": true,
    "capture_action_items": true
  }
}
```

---

## Pricing Model Recommendations

### Tiered by Meeting Complexity

| Tier | Price | Meetings | Participants | Features |
|------|-------|----------|--------------|----------|
| **Solo** | Free | 5/month | 2-3 per mtg | Basic facilitation |
| **Team** | $79/month | 50/month | Up to 10 | Full facilitation, analytics |
| **Business** | $249/month | 200/month | Up to 25 | Advanced analytics, integrations |
| **Enterprise** | Custom | Unlimited | Unlimited | SSO, API, custom agents |

### Value Metrics

Track and communicate ROI:
- **Time saved**: Average 15% reduction in meeting duration
- **Decision velocity**: 2x more decisions captured per meeting
- **Participation equity**: 40% improvement in balanced contribution
- **Action item capture**: 95% vs. 60% manual capture rate

---

## Implementation Roadmap

### Phase 1: Multi-Person Foundation
- Speaker diarization integration (Deepgram/AssemblyAI)
- Basic participation tracking
- Turn management for standups
- Speaking time visualization

### Phase 2: Active Facilitation
- Quiet participant prompting
- Dominant speaker management
- Agenda time-boxing
- Parking lot functionality

### Phase 3: Structured Formats
- L10 meeting protocol
- Retrospective frameworks
- Brainstorming facilitation
- Decision capture workflows

### Phase 4: Intelligence Layer
- Participation trend analysis
- Meeting effectiveness scoring
- Team dynamics insights
- Personalized recommendations

---

## Sources

### AI & Meeting Facilitation
- [Harvard Business Review: 3 Ways AI Can Improve Team Meetings](https://hbr.org/2025/08/3-ways-ai-can-improve-team-meetings)
- [Learning News: AI Steps Up as Meeting Facilitator](https://learningnews.com/news/learning-news/2025/ai-steps-up-as-meeting-facilitator-could-this-change-workplace-learning)
- [Microsoft Teams Facilitator Agent](https://robquickenden.blog/2025/08/teams-facilitator-agent/)
- [Interaction Associates: Will AI Eliminate Meeting Facilitation Skills?](https://www.interactionassociates.com/resources/blog/ai-meetingfacilitationskills)
- [Facilitator Meets AI: What I See Coming by 2027](https://medium.com/@cemvogt/facilitator-meets-ai-what-i-see-coming-by-2027-and-why-its-exciting-5cf4b81bc4b4)

### Multi-Speaker AI Research
- [Controlling AI Agent Participation in Group Conversations (ACM IUI 2025)](https://arxiv.org/html/2501.17258v1)
- [Multiplayer AI Chat and Conversational Turn-Taking](https://interconnected.org/home/2025/05/23/turntaking)
- [AssemblyAI: Speaker Diarization Guide](https://www.assemblyai.com/blog/what-is-speaker-diarization-and-how-does-it-work)
- [Deepgram: What is Speaker Diarization?](https://deepgram.com/learn/what-is-speaker-diarization)
- [NVIDIA Streaming Sortformer for Real-Time Speaker Identification](https://developer.nvidia.com/blog/identify-speakers-in-meetings-calls-and-voice-apps-in-real-time-with-nvidia-streaming-sortformer/)
- [Imperial College: Interruption Handling for AI Chatbots](https://www.imperial.ac.uk/news/257034/analysing-speech-interruptions-help-create-more/)

### Facilitation Best Practices
- [NOAA: Techniques for Facilitating Virtual Meetings](https://coast.noaa.gov/data/digitalcoast/pdf/facilitating-virtual-meetings.pdf)
- [MIT HR: Basics of Designing & Facilitating Meetings](https://hr.mit.edu/learning-topics/meetings/articles/basics)
- [SessionLab: Brainstorming Techniques](https://www.sessionlab.com/blog/brainstorming-techniques/)
- [Harvard PON: Consensus-Building Techniques](https://www.pon.harvard.edu/daily/dealing-with-difficult-people-daily/consensus-building-techniques/)
- [Kaizenko: 9 Decision-Making Methods for Facilitators](https://www.kaizenko.com/decision-making-techniques-for-facilitators-9-methods-to-drive-group-consensus/)

### Group Psychology
- [OpenWA: Group Dynamics in Organizational Psychology](https://openwa.pressbooks.pub/industrialorganizationalpsychology/chapter/9-2-group-dynamics/)
- [Noba Project: Psychology of Groups](https://nobaproject.com/modules/the-psychology-of-groups)
- [Culture Monkey: Social Loafing at Work](https://www.culturemonkey.io/employee-engagement/social-loafing/)
- [Sharpen Notes: Strategies for Inclusive Meetings](https://www.sharpennotes.com/blog/unlocking-power-of-quiet-voices)

### Meeting Formats
- [Krisp: L10 Meeting Comprehensive Guide](https://krisp.ai/blog/l10-meeting/)
- [EOS Worldwide: Level 10 Meeting](https://www.eosworldwide.com/blog/the-level-10-meeting)
- [Atlassian: Agile Ceremonies and Scrum Meetings](https://www.atlassian.com/agile/scrum/ceremonies)
- [LeadershipIQ: Effective Team Meetings](https://www.leadershipiq.com/blogs/leadershipiq/effective-team-meetings)

### Market Data
- [Zapier: Best AI Meeting Assistants 2025](https://zapier.com/blog/best-ai-meeting-assistant/)
- [MeetGeek AI Voice Agents Announcement](https://www.globenewswire.com/news-release/2025/10/31/3178600/0/en/MeetGeek-Announces-Launch-of-AI-Voice-Agents-to-Autonomously-Participate-in-Virtual-Meetings.html)
- [Index.dev: AI Agent Statistics 2025](https://www.index.dev/blog/ai-agents-statistics)
- [Worklytics: Meeting Metrics for Collaboration](https://www.worklytics.co/blog/top-12-metrics-for-effective-meetings)
