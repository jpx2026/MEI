# DevOps and Version Control Systems (VCS)

These notes explain the class topics in a learning order: the problem DevOps addresses, its guiding ideas, and the practices that put them into action. Examples use an online shop throughout.

Explanations and examples expand the original notes. Section 9 contains supporting technical background; it is not a claim that every topic was covered in class.

## Reading map

1. What is DevOps, and why do we need it?
2. Lean: why improve the whole process?
3. Agile and DevOps: how do they relate?
4. Scrum and Kanban: how do we organize work?
5. The Three Ways: how do we improve delivery?
6. The Five Ideals: what conditions help people do good work?
7. CALMS: what areas should we examine?
8. Practices: how do these ideas work in real situations?
9. Technical background: Git, environments, pipelines, CI/CD, and monitoring.
10. How to implement DevOps: a practical starting sequence.
11. DevOps best practices: meaning, application, and common mistakes.
12. DevOps challenges: what makes improvement difficult.
13. One example connecting the ideas.
14. Revision questions with explanations.

## 1. What is DevOps?

**DevOps** combines development (Dev) and operations (Ops). It is a culture and a set of practices that help people build, deliver, and operate useful, reliable software together.

The goal is to deliver value to customers frequently and reliably, learn from feedback, and improve continuously. **Value** means a useful outcome for the customer, such as being able to complete an online purchase successfully.

DevOps involves people, processes, and tools. A **process** describes how work is done; tools can automate parts of it. Installing a tool alone does not create collaboration or shared responsibility.

### Development and operations

| Area | Typical responsibilities | Example in an online shop |
| --- | --- | --- |
| Development | Create features, fix bugs, and maintain software. | Write the code for a new checkout page. |
| Operations | Run and monitor software and infrastructure, manage deployments, and respond to incidents. | Keep the shop running and investigate failed payments. |

**Infrastructure** means the resources software needs, such as servers, networks, and databases. **Production** is the environment where the real service runs for users. An **incident** disrupts or degrades the service.

- **Performance:** how quickly and efficiently the system works. Example: how long checkout takes to load.
- **Reliability:** whether the system consistently performs its intended function. Example: whether valid orders are processed correctly.
- **Availability:** whether the service is accessible and usable when needed. Example: whether customers can access checkout.

These concerns overlap. A reachable checkout page can still process orders incorrectly, so availability alone does not guarantee reliability.

### Why do silos cause problems?

A **silo** is a group that works in isolation, with limited communication and shared responsibility.

Traditionally, developers might be rewarded for delivering features, while operations might be rewarded for stability. These incentives can conflict: developers want to introduce changes, while operations worries that changes may cause failures.

Example: developers hand over a large update without explaining its configuration. Operations then has to discover how to run it under pressure. This can cause delays, risky releases, and slow feedback.

Separate teams do not automatically cause these problems; isolated work and conflicting goals do. DevOps encourages shared responsibility, including after software reaches production.

## 2. Lean principles

**Lean** focuses on delivering customer value while reducing waste and improving how work moves through a process.

Waste can include waiting for approvals, repeating manual tasks, fixing avoidable mistakes, or building features nobody needs.

- **Small batches:** make smaller changes more frequently, so they are easier to review, test, and investigate if something fails.
- **Fewer unnecessary handoffs:** avoid passing work between groups without the information needed to continue it.
- **Improve the whole process:** faster coding provides little benefit if every change then waits weeks for testing.
- **Continuous improvement:** regularly examine how work happens and make improvements.

Example: automating a repetitive test reduces manual effort and the time developers wait for results.

### Why can doing less at once help us deliver more?

Starting a task does not deliver its value; finishing it does. If five checkout changes are half-finished, customers may benefit from none of them. Finishing one useful change creates an opportunity to test it and receive feedback.

A **bottleneck** is a step that restricts the flow of the whole process. If developers complete ten changes a week but reviewers can review only four, unfinished work accumulates before review. Making developers code faster increases that queue.

This is why Lean looks at the whole journey. Helping review catch up can improve delivery more than starting more code. Small batches still need useful boundaries: splitting work into meaningless fragments creates extra coordination without customer benefit.

## 3. Agile and DevOps

**Agile** is an approach guided by values and principles about collaboration, working software, responding to change, and learning through frequent delivery.

**Iterative** means revisiting and improving something using feedback. **Incremental** means adding usable pieces over time. A team can use both: first deliver a basic checkout, then improve it and add payment options.

Why work this way? At the start, we do not know every customer need or technical difficulty. Smaller increments let us test assumptions before investing months in a mistaken plan. This still requires planning; the plan changes as evidence improves. See the [Agile Manifesto principles](https://agilemanifesto.org/principles).

| Question | Agile emphasis | DevOps emphasis |
| --- | --- | --- |
| What are we trying to improve? | Adapting work to deliver useful software and respond to feedback. | Collaboration and the ability to build, deliver, run, and improve software reliably. |
| What might we change? | Priorities, collaboration, feedback frequency, and ways of developing software. | Shared ownership, testing, deployment, infrastructure, and production feedback. |
| What do they share? | Customer value, collaboration, frequent delivery, and continuous improvement. | The same concerns, including strong attention to operation of the live service. |

These are overlapping emphases, not strict boundaries. Agile already values delivery and technical excellence; DevOps also concerns people and customer outcomes.

**Example:** a shop team adapts its checkout design every two weeks using customer feedback. That supports Agile thinking. If each update then waits two months for a difficult manual deployment, customers still wait. Improving delivery and involving operations throughout the work helps close that gap.

Scrum is one framework that can support Agile work. DevOps does not require Scrum, and using Scrum alone does not guarantee DevOps practices.

## 4. Organizing work: Scrum and Kanban

Both help teams organize and improve work. They can support DevOps practices.

| Concept | Scrum | Kanban |
| --- | --- | --- |
| Structure | Work toward goals in fixed-length Sprints of one month or less. | Optimize the flow of work through a defined workflow. |
| Planning and adaptation | Use Sprint Planning, a Daily Scrum, a Sprint Review, and a Sprint Retrospective. | Pull new work when there is capacity; improve flow using feedback and measurements. |
| Responsibilities | Defines Product Owner, Scrum Master, and Developers accountabilities. | Does not prescribe these accountabilities. |
| Work control | Select work supporting a Sprint Goal and adapt the plan as learning occurs. | Explicitly control work in progress (WIP). |

A **backlog** is a list of work that may be needed. A **Sprint** is a short cycle for pursuing a goal and producing usable work. A **retrospective** is a discussion about improving how the team works.

A Kanban board might show `To do → In progress → Review → Done`. **WIP** means work started but not finished. Limiting it helps a team finish work before starting too much more. A board alone is not a complete Kanban system.

Scrum and Kanban can be combined. Teams using Scrum can release usable work before a Sprint ends.

Sources: [The Scrum Guide](https://scrumguides.org/scrum-guide.html) and [The Kanban Guide](https://kanbanguides.org/the-kanban-guide/).

### Why do these approaches organize work differently?

Scrum provides a regular rhythm for choosing a goal, inspecting results, and adapting. That helps people coordinate under uncertainty. The Sprint Goal gives direction; it does not mean every initial task must stay unchanged.

Kanban makes queues and capacity visible. If the review column is full, the team can help finish reviews instead of adding more work to the queue. Limiting WIP also reduces the number of tasks people must repeatedly switch between.

In Scrum, the **Product Owner** is accountable for maximizing product value and managing the Product Backlog effectively. The **Scrum Master** helps establish Scrum and improve team effectiveness. **Developers** create a usable result each Sprint; the term includes the skills needed to create it, not only coding.

The **Daily Scrum** helps Developers inspect progress toward the Sprint Goal and adapt their plan. The **Sprint Review** examines the product outcome with stakeholders; the **Retrospective** examines how the team worked.

A common misunderstanding is that the board or meetings create improvement automatically. They help only when people use what they reveal to change decisions. See the [Scrum Guide](https://scrumguides.org/scrum-guide.html) and [Kanban Guide](https://kanbanguides.org/the-kanban-guide/).

## 5. The Three Ways of DevOps

The Three Ways connect **flow**, **feedback**, and **continual experimentation and learning**. Experimentation and learning belong together in the Third Way.

### First Way: Flow

Improve how work moves through the whole system toward the customer. Use shared goals, smaller batches, and fewer delays.

```text
Business need → Development → Testing → Operations / delivery → Customer value
```

This is a simplified picture of work, not a requirement for separate teams. Development helps implement business needs; operations helps run the service for customers.

**Value stream mapping** means mapping the steps and waiting times between an idea and its delivery to find delays. **Test automation** means running checks automatically to give repeatable results sooner.

### Second Way: Feedback

Send information about results back to the people who can act on it. Shorter feedback loops help teams detect problems and adjust sooner.

```text
Make a change → Test or observe the result → Learn → Adjust the change
```

Feedback comes from tests, production monitoring, and customer conversations. It should happen throughout development and operation.

### Third Way: Continual experimentation and learning

Create a culture where people test ideas, practise, learn from failures, and improve the system. Learning also improves flow and feedback; these activities reinforce one another.

Source: [Gene Kim — The Three Ways](https://itrevolution.com/articles/the-three-ways-principles-underpinning-devops/).

### Why do we need all three?

Consider an illustrative checkout change:

- **Flow:** a small change reaches testing quickly instead of waiting behind a large batch.
- **Feedback:** a payment test reports a failure while the developer still remembers the change.
- **Learning:** the team notices that the same mistake has happened twice and improves the design or checks.

Fast flow without useful feedback can spread mistakes quickly. Feedback without time to act on it produces reports but little improvement. Learning should change how future work happens.

## 6. The Five Ideals

The Five Ideals in Gene Kim's *The Unicorn Project* describe conditions that support effective work. They complement the Three Ways. The names are listed in the publisher's [Five Ideals poster](https://itrevolution.com/wp-content/uploads/2019/11/5-Ideals-poster-c.pdf).

### 1. Locality and Simplicity

**Meaning:** make work understandable and reduce unnecessary dependencies between components and teams. Locality means a change can often be understood, tested, and made within a limited area.

**Why:** every required coordination step can add waiting and misunderstanding. Changes spread across many connected components are harder to reason about.

**Example:** changing checkout wording should not require editing five unrelated services and coordinating five release schedules.

Locality does not mean teams ignore each other. They still need clear agreements about how their components interact. Simplicity means reducing unnecessary complexity while preserving required behaviour. See the author's discussion in [The Idealcast](https://itrevolution.com/podcast/the-idealcast-episode-1/).

### 2. Focus, Flow, and Joy

**Meaning:** create conditions where people can concentrate, make progress, and find satisfaction in useful work.

**Why:** after an interruption, a developer must reconstruct what they were doing. Frequent interruptions and blocked tasks consume attention that could have gone into understanding and solving problems.

**Example:** a rotating support role handles incoming questions while others have protected focus time. Urgent incidents still receive attention.

Here, flow includes the experience of sustained concentration; in the First Way, the emphasis is work moving through the delivery system. These ideas support each other. See [The Idealcast](https://itrevolution.com/podcast/the-idealcast-episode-1/).

### 3. Improvement of Daily Work

**Meaning:** reserve capacity to improve how work is performed, as part of doing the work.

**Why:** a recurring difficulty consumes time on every repetition. Fixing its cause can help many future tasks.

**Example:** imagine a setup problem costs 20 minutes each day. Over 15 working days, that is five hours. A two-hour fix could repay its effort during that period, assuming it removes the problem.

**Technical debt** is a design or implementation compromise that increases the effort of future changes. It can be deliberate, but allowing it to accumulate can make ordinary work progressively harder.

### 4. Psychological Safety

**Meaning:** people can ask questions, admit uncertainty, raise concerns, and report mistakes without fear of humiliation or unfair punishment.

**Why:** if speaking up feels dangerous, warnings stay hidden. Hidden problems cannot be investigated early, and others lose the opportunity to learn.

**Example:** a student or junior developer notices that a test was skipped. They should be able to ask about it, even if a senior colleague approved the change.

Safety supports honest discussion and accountability; it does not remove quality expectations.

### 5. Customer Focus

**Meaning:** judge work by its contribution to customer outcomes.

**Why:** an internal activity can look productive without making the product more useful. A team needs to check whether its effort solves a real problem.

**Example:** adding ten checkout options may count as feature output, but simplifying a confusing payment step may help more customers finish buying.

Infrastructure and maintenance can also serve customers indirectly by improving reliability or enabling future changes. Customer focus does not mean building only visible features.

The third, fourth, and fifth ideals are introduced in the publisher's [excerpt from The Unicorn Project](https://itrevolution.com/wp-content/uploads/2022/06/TUP_Excerpt_Final.pdf). The shop examples and numerical illustration above are learning examples.

## 7. The CALMS framework

**CALMS** identifies five areas to examine when improving DevOps. The M usually means **Measurement**: metrics are the individual quantities used in measurement.

| Area | Meaning and reason |
| --- | --- |
| **Culture** | Build trust and shared responsibility so problems receive cooperation instead of being passed between teams. |
| **Automation** | Make repeatable tasks executable by tools to reduce manual effort and variation. |
| **Lean** | Reduce waste and improve the whole flow so local activity produces customer value sooner. |
| **Measurement** | Gather evidence to check whether changes actually improve results. |
| **Sharing** | Share knowledge, feedback, and responsibility so learning reaches beyond one person or team. |

Source: [Atlassian's CALMS explanation](https://www.atlassian.com/devops/frameworks/calms-framework).

### An example of applying CALMS

For our imaginary shop, developers and operators agree to investigate failed purchases together. They automate a repeated checkout check, reduce time waiting for review, compare failed-purchase rates before and after the change, and document what they learned.

Automating a wrong check simply repeats the wrong check faster. Collecting numbers without a question can distract from the problem. For example, counting commits tells us how many commits exist; it does not tell us whether checkout became easier to use.

### How do the frameworks fit together?

This table is a study aid, not an official one-to-one mapping.

| Model | Useful question to ask |
| --- | --- |
| Three Ways | How can work move better, feedback arrive sooner, and learning improve future work? |
| Five Ideals | What technical and human conditions make good work possible? |
| CALMS | Are we considering culture, automation, Lean, measurement, and sharing together? |

One action can serve several models. Improving a slow test helps flow, improves daily work, and contributes to automation. The overlap is expected.

## 8. Practices: feedback, experimentation, and learning

### Shared goals

Development and operations agree on outcomes they both care about. For our shop, a shared goal could be successful, fast purchases. Counting features alone would miss whether customers can actually use them.

### A/B testing

An **A/B test** compares two variants with different groups of users, usually assigned randomly, to evaluate a specific outcome.

Example: show two checkout layouts and compare the proportion of customers who complete a purchase. A small difference does not automatically prove that one layout is better; the experiment needs enough evidence.

### Feature flags (toggles)

A **feature flag** is a configuration switch that enables or disables a feature without requiring a new code deployment for each switch.

Example: deploy the new checkout code but enable it only for staff first, then a small group of customers. A flag can support an A/B test, control access, or stop exposing a problematic feature.

Disabling a flag does not necessarily undo effects that already happened, such as database changes.

### Continuous customer contact

Collect feedback regularly through conversations, usability sessions, support reports, or other channels. This helps check whether the team is solving the right problem.

Example: customers explain that checkout is confusing, even though technical monitoring shows it is fast.

### Chaos engineering

**Chaos engineering** uses controlled experiments to check how a system behaves under failures. Start with an expectation, introduce a specific disruption, observe the result, and limit the impact with clear stopping conditions.

Example: in a controlled environment, stop one of several application instances and check whether the others continue serving requests. The aim is to discover weaknesses before an unexpected failure exposes them.

Source: [Principles of Chaos Engineering](https://principlesofchaos.org/).

### 20% time and hackathons

- **20% time:** an example of setting aside a portion of working time for exploration, learning, or improvements outside immediate delivery tasks. The percentage is not a DevOps requirement.
- **Hackathon:** a focused event where people collaborate to explore an idea or build a prototype. A prototype may need more work before it is suitable for production.

Both create opportunities to experiment, but learning should also happen during everyday work.

### Blameless culture and blameless postmortems

A **blameless culture** encourages people to report mistakes openly so the team can understand and improve the conditions that contributed to them.

A **postmortem** is a review after an incident. It records what happened, the impact, contributing factors, what helped recovery, and follow-up actions.

Example: after a deployment causes an outage, investigate why tests missed the problem and how deployment controls can improve. Assign owners to improvements. Blamelessness still includes responsibility for taking action.

### Why choose one practice rather than another?

| Practice | Problem it helps answer | Why it helps / practical limit |
| --- | --- | --- |
| A/B testing | Which variant changes a user outcome? | A fair comparison helps separate a variant's effect from other differences. It needs a clear measure and sufficient evidence. |
| Feature flags | Who should receive the feature, and when? | Separating exposure from deployment allows gradual release. Old flags add code paths to maintain and should be reviewed for removal. |
| Customer contact | Why are users struggling? | Conversations can explain motivations that numbers alone do not reveal. One person's opinion may not represent everyone. |
| Chaos engineering | Will the system cope with a specific failure? | A controlled disruption tests assumptions about recovery. The result applies to the conditions tested; impact must be bounded. |
| Learning time and hackathons | How can we explore ideas beyond immediate tasks? | Protected time makes exploration possible. Useful findings still need evaluation and follow-through. |
| Blameless postmortems | How did the system allow an incident, and what should change? | Looking beyond individual error reveals missing checks, confusing tools, or incentives. Actions need owners and follow-up. |

For example, blaming someone for choosing the wrong server does not explain why two servers were easily confused, why review missed it, or why recovery was slow. Those questions reveal changes that can protect the next person too.

## 9. Technical background: from a change to a running service

### Version Control Systems (VCS) and Git

A **VCS** records changes to files over time. It helps people collaborate, review history, compare versions, and recover earlier work.

**Git** is a distributed VCS: a normal clone contains a local repository and its history. **GitHub** is a service that hosts Git repositories and provides collaboration features.

- **Repository:** the stored project history and associated version-control data.
- **Commit:** a recorded snapshot of staged changes, with a message describing the change.
- **Branch:** a movable reference used to maintain a line of development.
- **Merge:** combine development histories, resolving conflicting changes when necessary.
- **Remote:** a named reference to another repository, often hosted online.

Version control makes code and configuration changes traceable and allows changes to trigger pipelines. See [Git commands and everyday workflow](git.md) for practical commands.

### Environments, deployment, and release

- **Development environment:** where developers build and try changes.
- **Test or staging environment:** where the team checks changes before production; staging aims to resemble production.
- **Production environment:** where the real service runs for users.
- **Deployment:** put a version of the software into an environment.
- **Release:** make a feature or version available to its intended users.

Deployment and release can happen at different times. A feature flag can keep a deployed feature hidden until the team enables it.

### What is a pipeline?

A **pipeline** is an ordered set of steps that takes a software change through checks and delivery tasks. Many steps are automated; some may require human approval.

```text
Code change → Build → Automated tests → Deploy to staging → Checks → Deploy to production
```

**Build** means preparing code into something that can run or be distributed. An **artifact** is a resulting output, such as an application package. Automated tests check expected behaviour, but passing tests cannot prove that software has no bugs.

Example: a checkout change triggers a build and tests. If a required payment test fails, the pipeline stops before production deployment.

### CI/CD

| Term | Meaning |
| --- | --- |
| Continuous integration (CI) | Developers integrate small changes frequently into shared code, supported by automated builds and tests. |
| Continuous delivery | Keep validated software ready to deploy; production deployment may require a deliberate decision or approval. |
| Continuous deployment | Automatically deploy changes that pass the required pipeline checks to production. |

**CD** can mean either continuous delivery or continuous deployment, so check which meaning is intended. Continuous does not mean releasing unfinished work every second.

### Monitoring and feedback

**Monitoring** collects and checks information about the running system.

- **Metrics:** numerical measurements, such as response time or failed requests.
- **Logs:** recorded events, such as an error during payment processing.
- **Alerts:** notifications when a condition needs attention.

Example: monitoring detects more failed checkouts after a deployment. The team investigates and may disable the feature or roll back. A **rollback** returns to an earlier version or state where feasible; data changes can make this more complicated.

### Infrastructure as Code (IaC)

**Infrastructure as Code** means defining and managing infrastructure using machine-readable files. These files can be versioned, reviewed, and applied with automation.

Example: record server configuration in files so the team can recreate environments consistently, rather than relying on remembered manual steps.

### Why do these technical practices belong together?

| Practice | Why it matters |
| --- | --- |
| Version control | A recorded history lets the team inspect what changed and connect failures to changes. A commit records a state; it does not certify that state is correct. |
| Frequent integration | Combining changes sooner reveals incompatible assumptions while the changes are still relatively small. A CI service alone cannot compensate for rarely integrating work. |
| Automated tests | Repeat checks quickly after changes. Their usefulness depends on which behaviours they cover and whether failures are meaningful. |
| Staging | Find problems before real users encounter them. Differences in data, traffic, and configuration mean staging cannot predict every production failure. |
| Pipelines | Make delivery steps repeatable and visible, reducing reliance on memory. Keep checks maintained as the software changes. |
| Infrastructure as Code | Review and reproduce configuration more consistently. An incorrect configuration can also be repeated, so review and validation still matter. |
| Monitoring | Real traffic and dependencies can behave differently from test conditions. Production evidence closes the feedback loop. |

Continuous delivery is useful even when production release needs a business decision. It reduces the technical work remaining once that decision is made. Continuous deployment goes further by automating that decision path for changes that meet the required checks; it depends on confidence in validation, monitoring, and recovery.

## 10. How to implement DevOps

**Implementation** means introducing the working agreements, processes, and technical capabilities that turn DevOps principles into everyday behaviour. **Best practices** are habits that help those processes work reliably over time.

The sequence below is a learning guide, not a universal checklist. Start with one application, learn from the results, and adapt. Several activities can overlap.

### Step 1: Choose a problem and define success

Talk with the people who build, run, support, and use the product. Choose a concrete problem, such as unreliable checkout releases.

Record a **baseline**: the current situation before making improvements. For an illustrative shop, deployments might take two hours and require six manual steps. These are example values, not industry targets.

**Why first?** You need to distinguish an improvement from simply installing a new tool. Decide what should become better and what must remain acceptable, such as purchase success and team workload.

**Result:** a shared problem statement, baseline, and success criteria.

### Step 2: Map the work and agree on responsibilities

Follow a real change from request to production. Record active work, waiting, handoffs, and repeated failures. This applies value stream mapping from the First Way.

Identify who reviews changes, maintains tests, manages deployment access, and responds to incidents. Shared responsibility still needs named owners.

**Why?** A delay may come from waiting for a decision rather than slow code. Clear ownership also prevents everybody assuming somebody else is handling a failure.

**Result:** a simple workflow with visible bottlenecks and responsibilities.

### Step 3: Make the project reproducible

Put code, tests, scripts, and non-secret configuration in Git. Document how to obtain the project, install dependencies, build it, and run checks.

A **dependency** is a library or other component the application relies on. Record the versions needed so two people do not accidentally test different combinations.

**Why?** If the application only works on one laptop, automating deployment is difficult. First make the process understandable and repeatable.

**Result:** a teammate can prepare the project from its documented files without relying on undocumented local changes.

### Step 4: Build a small, useful CI pipeline

Automate the build and a few meaningful checks. Run them on proposed changes and the integrated code. Keep changes small and integrate frequently.

**Why?** Running tests on an isolated change is useful, but the combined code also needs validation. If two changes work separately and fail together, integration feedback exposes that disagreement.

A **pipeline runner** is the machine or execution environment that performs the configured jobs. The configuration describes what it should run; the runner does the work.

**Result:** a failed required check produces visible feedback and prevents that pipeline run from progressing. The team investigates rather than routinely bypassing it. See [DORA's CI guidance](https://dora.dev/capabilities/continuous-integration/).

### Step 5: Introduce repeatable deployment

Document deployment, simplify it, and automate it. Deploy to a test or staging environment first. Where applicable, promote the same built artifact to production, supplying the appropriate environment configuration separately.

**Why?** Rebuilding separately for production can introduce differences from what was tested. Reusing the artifact reduces this uncertainty, although configuration and real traffic still differ.

A **smoke test** is a short check that essential functionality works after deployment. It might verify that the shop starts and can reach its database.

**Result:** a recorded application version can be deployed through a repeatable process and checked afterward. This follows [DORA's deployment automation guidance](https://dora.dev/capabilities/deployment-automation/).

### Step 6: Prepare operation and recovery before exposing users

Assign support responsibility, collect essential logs and measurements, and prepare a runbook. Practise recovery in a suitable test environment.

Decide what happens if the release fails: disable a flagged feature, restore a compatible earlier version, or deliver a corrective change. **Roll forward** means fixing the problem with a newer version. Consider data compatibility before choosing a recovery method.

**Why?** The cost of failure depends partly on how quickly the team detects and handles it. A deployment button without recovery knowledge leaves an important part of delivery unfinished.

**Result:** the team knows how to detect a problem, who will act, and which recovery procedure is appropriate.

### Step 7: Release a small change and inspect the outcome

Initially, the team may explicitly approve production deployment. Continuous deployment can follow when automatic checks and operational controls are sufficient for that application.

Check both technical signals and customer behaviour after release. An illustrative success check is whether customers can still complete purchases without an increase in errors.

**Why?** A completed pipeline shows that its configured steps succeeded. It does not by itself establish that users received value.

**Result:** evidence about the change in real use, feeding the next decision.

### Step 8: Improve the next constraint and expand gradually

Compare results with the baseline. Review incidents and delays with the team, choose one concrete improvement, and assign an owner.

For example, if deployment is now quick but review waits three days, improving review is likely more useful than shaving another second off deployment.

**Why?** Improving one step can expose the next bottleneck. DevOps adoption continues as the product and organization change.

**Result:** an ongoing cycle of measured improvements. Share a successful approach with other teams while adapting it to their needs.

### How the implementation connects to the earlier frameworks

| Implementation activity | Connection to the notes |
| --- | --- |
| Define customer outcomes and shared ownership | Customer Focus; CALMS Culture and Sharing. |
| Map waiting, limit unfinished work, integrate smaller changes | Lean and the First Way: Flow. |
| Run checks and observe production | The Second Way: Feedback; CALMS Measurement. |
| Review incidents and improve scripts or procedures | The Third Way: Learning; Improvement of Daily Work. |

### A first project exercise

Use a small application and demonstrate one complete cycle:

1. Make a small change with a clear expected behaviour.
2. Record it in Git and have it reviewed if working with a partner.
3. Run an automated build and relevant tests.
4. Deploy the result to a test environment and check it.
5. Inspect logs or measurements, then practise recovery.
6. Record what was difficult and improve one part of the process.

The exercise combines delivery and learning. It does not require a large cloud platform or a particular vendor's tools.

## 11. DevOps best practices

These practices put the earlier principles into action. Apply them to a specific problem and check the result; adopting more tools or practices is not itself the goal.

### Involve stakeholders throughout the work

A **stakeholder** is someone affected by the product or able to influence its success: customers, developers, operations, support, product managers, or security specialists.

**Why:** each group sees different needs and constraints. Discovering these only after implementation can force the team to redo work. Early involvement helps reveal assumptions before they become expensive decisions.

**Example:** before changing checkout, ask support about common complaints and operations about busy shopping periods. Their answers may change both the design and the release timing.

Involvement does not mean everyone approves every commit. Agree on who contributes knowledge and who makes which decisions, so collaboration does not create an unnecessary queue.

**How to apply:** before implementation, agree on **acceptance criteria**: observable conditions that establish whether the requested behaviour is satisfied. For example, “a declined payment shows a clear message and does not create a confirmed order.” Review the result with relevant stakeholders.

**Common mistake:** inviting stakeholders only for the final demonstration, when changing the design is more expensive.

### Automate testing, builds, and environment setup

An **automated build** prepares the application using a repeatable script. Automated tests check behaviour. Automated environment setup prepares the resources and configuration needed to run those checks or the application.

**Why:** manual instructions can be skipped or interpreted differently. Repeatable steps make results easier to compare and reduce dependence on one person's memory.

**Example:** the shop's pipeline builds the application and tests a successful purchase and a declined payment. A failed required check blocks progression and gives the team feedback.

Keep dependency versions and setup instructions controlled so another machine can reproduce the process. Automation still needs maintenance: an incorrect test can pass repeatedly, and a **flaky test** can sometimes fail without a relevant code change. Unreliable feedback weakens trust in the pipeline.

These practices support the capabilities described in [DORA's continuous delivery guidance](https://dora.dev/capabilities/continuous-delivery/).

**How to apply:** select checks that catch meaningful failures at different levels.

| Check | What it examines | Shop example |
| --- | --- | --- |
| Unit test | A small piece of logic in isolation. | The calculation of an order total. |
| Integration test | Whether connected components work together. | Saving and retrieving an order from a test database. |
| End-to-end test | A complete path through the application. | Adding a product to the basket and completing a test purchase. |
| Exploratory testing | A person investigates behaviour and unexpected cases. | Trying confusing inputs or unusual navigation sequences. |

Run fast, focused checks early and broader checks where needed. An end-to-end test involves more moving parts, so a failure can take more effort to diagnose. Human exploration remains useful for questions the automated suite does not ask. See [DORA's test automation guidance](https://dora.dev/capabilities/test-automation/).

**Common mistake:** judging quality only by the number of tests or the percentage of code executed by them. A test must check a meaningful result to provide useful evidence.

### Integrate configuration and change management

**Configuration management** keeps track of the settings and resources that determine how a system runs. **Change management** controls how proposed changes are reviewed, checked, introduced, and recorded. Integrating them means treating related code, configuration, and infrastructure changes as a coordinated change.

**Why:** identical application code can behave differently with different settings. Reviewing only the code can miss a configuration change that breaks the service.

**Example:** a checkout update expects a new configuration setting. Its change record should identify the setting, the compatible application version, validation steps, and the recovery plan. Otherwise, the application might deploy successfully but fail when someone tries to pay.

Store non-secret configuration and deployment scripts in version control. Keep passwords and tokens in a suitable secret-management system. **Configuration drift** occurs when an environment diverges from its intended configuration, often after an unrecorded manual edit.

Review and automation make changes traceable; they do not require every change to wait for a large approval meeting. Choose controls appropriate to the change's impact. See [DORA's version control guidance](https://dora.dev/capabilities/version-control/).

**How to apply:** put the change description, related configuration, validation evidence, and recovery notes together for review. Record which version is running in each environment.

A **pull request** or **merge request** proposes changes for review before integration. The platform's review record helps people understand the purpose and checks, while Git records the resulting history.

**Common mistake:** fixing production manually and leaving the recorded configuration unchanged. The next automated deployment may undo the fix or reproduce the original failure.

### Integrate frequently and deploy with appropriate checks

CI combines changes frequently and validates them. Continuous deployment automatically sends changes that pass the required checks to production. Section 9 explains how continuous delivery differs.

**Why:** postponing integration allows incompatible changes to accumulate. Checking smaller combinations sooner makes failures easier to connect to their causes.

**Example:** two developers change the payment interface. Integrating early exposes a disagreement about the required fields before both build more features on incompatible assumptions.

When integration fails, restoring a healthy shared version should take priority. Automatic production deployment is useful when validation and recovery are adequate; it is not a universal requirement for DevOps. See [DORA's continuous integration guidance](https://dora.dev/capabilities/continuous-integration/).

**How to apply:** use short-lived changes, run checks before and after integration, and investigate failures promptly. A **required check** is a condition that the workflow must satisfy before it may proceed; repository and deployment rules need to enforce that condition.

**Common mistake:** assuming a green result on an old commit also validates code added afterward. Checks need to correspond to the version being integrated or deployed.

### Keep software deliverable and support it after release

Continuous delivery keeps software ready for deployment. **Product support** includes helping users, diagnosing defects, responding to incidents, and feeding findings into future work.

**Why:** a successful deployment only confirms part of the journey. Users may encounter problems that tests did not cover, and their needs can change. The team needs to learn from actual use.

**Example:** support reports that customers cannot understand a payment failure message. The team reproduces the problem, improves the message, adds a relevant check, and delivers the correction.

Agree who receives reports, who investigates, and how urgent incidents reach the right people. Shared ownership works best with clear responsibilities and enough capacity to fulfil them.

**How to apply:** provide a clear support channel, record reports, and distinguish urgent service incidents from ordinary enhancement requests. When fixing a defect, add a useful regression test where feasible.

A **regression** is behaviour that used to work but stops working after a change. A regression test helps detect a recurrence.

**Common mistake:** treating the first release as the end of responsibility, or expecting one person to handle every incident without backup.

### Monitor the application and automate useful dashboards

A **dashboard** presents selected measurements together. Automating it means collecting and updating the data without someone manually rebuilding a report each time.

**Why:** shared, timely information helps people notice changes and discuss the same evidence. However, a dashboard only helps if its measurements answer useful questions.

**Example:** show checkout response time, payment error rate, and successful purchases. A server can be running while purchases fail, so machine health alone does not establish that customers are being served.

Use alerts for conditions requiring action, with a clear owner. A dashboard supports investigation; an alert prompts attention. Too many low-value alerts cause **alert fatigue**, where people become less responsive to notifications. See [DORA's monitoring and observability guidance](https://dora.dev/capabilities/monitoring-and-observability/).

**How to apply:** choose a small set of measurements tied to user experience, annotate deployments on the dashboard, and connect actionable alerts to a runbook and responsible person. Test that the notification actually reaches them.

**Common mistake:** collecting many graphs without defining what decisions they should support. Deployment timing can help an investigation, but correlation alone does not prove that the deployment caused the problem.

### How to choose tools for these practices

Choose a tool after identifying the job it must perform. For example, version control records changes, a CI service runs checks, and a monitoring system gathers operational evidence. One product may cover several jobs.

Start with capabilities the team can understand and maintain. Adding another service means managing access, configuration, updates, and failures in the connections between tools. A small working process is easier to learn from than a large collection of partly configured products.

### What does good implementation look like?

The team can explain how a change moves from an idea to a running service, inspect evidence from checks, identify the deployed version, respond to problems, and improve the process together. The system remains understandable enough that it does not depend on one person's memory.

## 12. DevOps challenges

These are common obstacles to applying the practices above. The examples expand the challenges heading in the class notes; they are not a confirmed list from the lecture.

### Cultural resistance and conflicting incentives

People may reasonably hesitate if a change threatens their responsibilities or exposes them to blame. If one group is rewarded for speed and another for avoiding all change, asking them to collaborate does not fix the incentive conflict.

**Response:** agree on shared outcomes and demonstrate improvement through a small trial. For the shop, track whether customers can complete purchases reliably, alongside delivery progress. Psychological safety helps people explain what is actually blocking them.

### Skills gaps, unclear ownership, and limited capacity

Automated delivery involves development, testing, infrastructure, and operational skills. Renaming a team does not instantly create that knowledge. Giving developers support duties without training or time can overload them.

**Response:** pair people with complementary skills, document recurring tasks, and define escalation paths. A **runbook** is a practical guide for handling a known operational task or problem. Reserve time for learning and improvement as well as feature work.

### Tightly connected systems and team dependencies

**Coupling** means that one component depends on another. In a tightly coupled system, a small change can require coordinated updates across many components or teams. That adds waiting and increases the number of interactions to test.

**Example:** the shop cannot update checkout until accounts and inventory deploy matching changes.

**Response:** improve boundaries and compatibility incrementally. This does not automatically require microservices; the useful outcome is being able to change, test, and deliver with fewer unnecessary dependencies. See [DORA's guidance on loosely coupled teams](https://dora.dev/capabilities/loosely-coupled-teams/).

### Fragile automation and too many disconnected tools

Pipelines can become slow, unreliable, or difficult to understand. Adding more tools creates additional connections and settings to maintain. When checks are noisy, people may start ignoring them.

**Response:** address the most important failure or delay first, assign maintenance responsibility, and simplify duplicated steps. For example, repair a flaky payment test before treating its result as a reliable deployment gate.

### Environment differences and difficult data changes

Staging may have less traffic or different data from production. Database changes can also make recovery harder: restoring old application code does not recreate deleted data or undo all transactions.

**Response:** keep configuration controlled, test representative cases, and plan application and data compatibility together. For example, introduce a new database field while the old application can still operate, then migrate usage in stages. Backups need a workable restoration procedure; merely having a backup does not demonstrate successful recovery.

### Security and access in automated delivery

A pipeline may have permission to modify production. A mistake or compromised credential can therefore affect many users quickly. Adding checks only at the end can also produce late rework.

**Response:** review relevant risks early, control credentials, and give automation only the permissions it needs. Preserve records of changes. The reason for these controls is to make repeated delivery dependable as well as fast.

### Misleading measurements and short-term pressure

Counting deployments alone can encourage trivial releases; demanding features at all times can leave recurring problems unfixed. Both can make activity look successful while the service deteriorates.

**Response:** interpret delivery measures alongside failures, recovery, customer outcomes, and team workload. Prioritize an improvement when it removes a repeated obstacle. In the shop example, fixing recurring payment errors may create more value than another optional checkout feature.

## 13. One example connecting the ideas

Suppose customers abandon the shop at the payment step.

1. **Understand the need:** customer conversations suggest that an error message is confusing. Customer focus prevents us from assuming that more features are the answer.
2. **Choose a small improvement:** plan a clearer message instead of redesigning checkout immediately. This tests an assumption with less investment.
3. **Make the work visible:** track the change on the team's board. If review is blocked, help finish review before starting several more changes.
4. **Record and check the code:** commit the change to Git and integrate it. The pipeline builds the application and runs payment tests.
5. **Control exposure:** deploy the code with a feature flag, then enable it for a small group when ready.
6. **Learn from results:** check errors and customer outcomes. A properly designed A/B test could compare the old and new messages.
7. **Respond when needed:** disable the feature if it causes a problem, while investigating any effects that already occurred.
8. **Improve future work:** document findings and fix gaps in tests or procedures. If an incident occurred, review it without blame and assign improvement actions.

This example illustrates how culture, product decisions, work organization, and technical tools contribute to one customer outcome.

## 14. Revision questions with explanations

Try answering each question before reading its answer.

### Why does DevOps need shared goals?

If developers are rewarded only for shipping features and operators only for avoiding changes, each group can meet its own target while customers wait. Shared outcomes make cooperation useful to both.

### Why can small changes reduce risk?

They usually contain fewer interacting changes to review and diagnose. They also make feedback easier to connect to a cause. Small size helps, but does not replace testing or careful handling of data changes.

### Why is faster feedback valuable?

The team can correct an assumption before more work depends on it. Recent changes are also easier to remember and investigate.

### Why limit work in progress instead of keeping everyone busy?

Keeping everyone busy can create more unfinished work at a bottleneck. Limiting WIP encourages finishing and unblocking work so value reaches users.

### Why do psychological safety and blameless postmortems support reliability?

People are more likely to report concerns and describe mistakes honestly. That information helps the team improve the conditions that allowed failure.

### Why do Agile and DevOps complement each other?

Adapting the product is more useful when changes can reach users reliably, and reliable delivery is more useful when the team is delivering something customers need.

### Why is measurement more than collecting metrics?

Measurement should answer a question. After changing checkout, we need evidence about successful purchases and errors, not just a larger number of commits.

### Why are deployment and release different?

Code can be installed in production while its feature remains disabled. This lets a team decide separately when and to whom it becomes available.

### Why can speed and reliability improve together?

Smaller changes, earlier checks, repeatable delivery, and effective recovery can reduce delays and failures together. Skipping checks to appear faster does not provide the same benefit.

### How are the Three Ways, Five Ideals, and CALMS different?

They provide complementary views: improvement of delivery and learning, conditions for effective work, and areas to examine when adopting DevOps. They are not consecutive stages to complete once.


### Why involve stakeholders before implementation?

They reveal different requirements and constraints. Finding a missing requirement early lets the team adapt before more work depends on an incorrect assumption.

### Why manage configuration alongside code?

The running behaviour depends on both. A code review cannot detect an incompatible setting if that setting is changed separately without a record.

### Why does product support belong in DevOps?

Value is experienced during real use. Support brings problems and unmet needs back into development, completing the feedback loop after deployment.

### Why can a dashboard show healthy servers while customers cannot buy?

Server health measures only part of the system. Payment dependencies, application errors, or confusing behaviour may prevent purchases. Include measurements of the user journey.

### Why can adopting DevOps initially require extra time?

People need to learn, build reliable automation, and remove existing obstacles. Those investments aim to reduce repeated effort later; buying tools alone does not create that improvement.

### Why should we establish a baseline before adopting new tools?

Without knowing the original delays, failures, and customer outcomes, we cannot tell whether the change improved the situation. A baseline makes comparison possible.

### Why test the combined code as well as an individual change?

Two changes can each work alone but rely on conflicting assumptions. Integration checks examine the combination that the team will actually deliver.

### Why deploy the same artifact that was tested?

A separate build may introduce different dependencies or outputs. Reusing the artifact reduces that source of uncertainty; environment configuration still needs validation.

### Why prepare recovery before the first production release?

When an incident occurs, customers are already affected. A practised procedure and clear responsibilities reduce the amount the team must figure out under pressure.

### What is the difference between implementation and best practices?

Implementation establishes the team's working process and capabilities. Best practices guide how those capabilities are used and maintained during everyday work.
