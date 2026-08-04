# Brightspace Interactive Design Skill Suite

40 specialist skills and one orchestrator for designing D2L Brightspace courses with Claude. Describe what you need in plain language. The orchestrator classifies the request, checks prerequisites, flags conflicts, and routes you to the specialist that handles it.

**Author:** Kumar Chandrasekhar, PhD, Mount Royal University, Calgary, Alberta, Canada
**License:** CC BY-NC 4.0

## How it works

The suite is built like a general contractor and a crew. You describe the course design job once to the orchestrator. It knows the order of operations, catches dependencies such as setting up gradebook structure before any assessment, and calls the right specialist skill for each task. Each specialist knows its own domain and produces Brightspace-ready output. You only ever call the orchestrator.

## The skills

Seven categories, 40 specialists, plus the orchestrator that routes between them.

| Category | Count | Skills |
|---|---|---|
| Inception | 4 | course-outline-builder, learning-outcomes-generator, course-calendar-builder, program-alignment-mapper |
| Planning | 4 | redesign-planner, gradebook-planner, release-condition-planner, competency-mapper |
| Content | 11 | html-builder, slide-converter, pdf-transformer, dual-format-builder, glossary-builder, case-study-builder, reading-list-builder, video-script-writer, course-video-pipeline, google-flow-video-pipeline, notebooklm-video-builder |
| Assessment | 9 | quiz-generator, assignment-generator, discussion-generator, rubric-builder, survey-generator, group-project-setup, self-assessment-generator, exam-wrapper-builder, google-peer-eval |
| Quality | 4 | accessibility-auditor, course-copy-auditor, content-currency-auditor, student-experience-preview |
| Communication | 3 | announcement-writer, email-template-builder, intelligent-agent-builder |
| Management | 5 | checklist-builder, lti-integration-guide, end-of-term-workflow, course-analytics-guide, session-debrief |

## Requirements

- A paid Claude plan. Projects are not available on the free tier.
- Code execution and file creation enabled in Settings.

## Install

Setup takes about ten minutes. Steps 1 to 3 are account-level and done once. Steps 4 and 5 are per course.

1. In Settings > Capabilities, turn on Code execution and file creation.
2. Download this repository with Code > Download ZIP, then unzip it. Each subfolder is one skill and contains a single SKILL.md.
3. Upload each skill under Settings > Capabilities > Skills > Customize. Toggle each one on after upload. Upload `brightspace-orchestrator` last so it is easy to find.
4. Create a Claude Project for your course. Use one Project per course.
5. Open a chat inside the Project, type `/`, choose `brightspace-orchestrator`, and describe your course design need. Paste the Project instructions block it generates into Edit Project Instructions.

Claude Code users can place the skill folders in `.claude/skills/` on a local drive instead of uploading through Settings. Projects are a claude.ai feature and are not available in Claude Code.

## Using the suite

Call `/brightspace-orchestrator` once at the start of a session. It routes to the specialist skills as needed. You do not invoke the specialists directly.

## Packaging skills individually (optional)

If you need each skill as its own ZIP for distribution, run one of these from inside the unzipped repository folder.

macOS and Linux:
```bash
for dir in */; do zip -r "${dir%/}.zip" "$dir"; done
```

Windows PowerShell:
```powershell
Get-ChildItem -Directory | ForEach-Object { Compress-Archive -Path $_.FullName -DestinationPath "$($_.Name).zip" }
```

## Privacy and copyright

Use the suite for course design, not for student records. Do not paste student names, identifiers, or grades into a session. Two skills, `google-flow-video-pipeline` and `notebooklm-video-builder`, send content to Google services, and NotebookLM builds video from the sources you upload, so use only materials you have the rights to.

## Support

Report a problem or request a feature on the repository Issues page. Include which skill triggered the problem, what you asked for, and what happened instead.

## License

Licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). See [LICENSE](LICENSE). The Python scripts in `course-video-pipeline/scripts/` are licensed separately under the MIT License; see that folder's `LICENSE.md`.

Attribution: Brightspace Interactive Design Skill Suite by Kumar Chandrasekhar, PhD. Licensed under CC BY-NC 4.0.

## The series

This suite accompanies a three-part series on AI-assisted course design in Brightspace, published on the D2L community blog. <!-- Add blog post links here at publication. -->
