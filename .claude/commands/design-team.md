---
description: 디자인 팀 파이프라인 실행 (기획→승인→디자이너→QA)
argument-hint: "작업 요청 (예 - 프로필 화면 만들어줘)"
---

`design-team` 스킬을 호출해 디자인 팀 파이프라인을 시작한다.

사용자 요청: $ARGUMENTS

위 요청을 기획 입력으로 삼아 `design-team` 스킬(`.claude/skills/design-team/SKILL.md`)을 Skill 도구로 실행하고, 스킬 지침을 그대로 따른다. 요청이 비어 있으면 먼저 무엇을 만들거나 고칠지 사용자에게 물어본다.
