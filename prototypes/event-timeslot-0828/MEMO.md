# event-timeslot-0828 — 기획안 정리할 때 다룰 메모

## 커뮤니티 회원만 신청 가능
`event-input.html`의 이벤트 설정에 있는 토글(`#opt-members-row`)은 **커뮤니티 페이지 맥락에서만 노출**한다.
일반 페이지에서는 커뮤니티라는 개념이 없어 물을 값이 아니다.

- 현재 구현: `body[data-context="community"] #opt-members-row { display: flex; }` — 일반 페이지에서는 숨김
- 이 스프린트에서 프로토타입의 맥락 전환 바를 지웠기 때문에, 지금은 항상 일반 페이지로만 열려서 이 토글을 볼 수 없다
- 커뮤니티 분기 코드(`setContext`, `applyContextLayout`, `CONTEXT_DEFAULTS`)는 남겨 두었다
- 기획안에는 "커뮤니티 페이지에서 만든 이벤트에만 노출되는 설정"으로 적는다
