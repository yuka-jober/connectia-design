# Connectia 디자인 시스템 규칙

## 핵심 규칙 (YOU MUST)
- 모든 스타일은 `tokens.css`의 토큰과 `components.css`의 클래스를 **먼저 사용**한다.
- raw 값(hex, px, rgba, 임의 font-size 등) **하드코딩 금지**. 항상 토큰 변수 / 유틸 클래스를 참조한다.
- 필요한 스타일이 없으면 일회성으로 만들지 말고, `tokens.css`에 토큰을 추가하거나 `components.css`에 클래스를 확장한다.
- 색은 semantic 토큰(`--color-*`)만 사용. `--palette-*`는 토큰 정의용이므로 컴포넌트에서 직접 쓰지 않는다.
- 여백(padding·margin·gap)은 **4의 배수**(8 / 12 / 16 / 20 / 24…)로만 쓴다. 임의의 px 값(13px, 17px 등) 금지.
- **`components.css`나 `tokens.css`에 클래스/토큰을 추가하거나 변경하면, 아래 "사용 가능한 토큰/컴포넌트" 목록도 같은 작업에서 반드시 함께 갱신한다.**

## 문구 (YOU MUST)
- **설명용 작은 글씨를 임의로 넣지 않는다.** 라벨·항목 아래 붙는 보조 설명, 힌트, 안내 문구(`ⓘ …`, `~에게 먼저 가요`, `~하는 데 써요` 같은 것)는 **기본이 "넣지 않음"이다.**
- 그 문구가 없으면 사용자가 **실제로 잘못 조작하거나 결과를 예측할 수 없는 경우**에만 필요하다고 보고, 그때는 **넣기 전에 사용자에게 허가를 받는다.** 임의로 추가 금지.
- 화면은 라벨과 컴포넌트만으로 읽히게 만든다. 설명을 덧붙여야 이해되는 UI라면 **문구를 붙이지 말고 구조를 고친다.**
- 기존 화면을 수정할 때 이미 있던 보조 설명을 새로 늘리지 않는다. 지우는 것은 자유.

## 모임 카드 제목 (YOU MUST)
- **기대돼요 카드(곧 만나요 섹션)의 제목은 무조건 한 줄.** 사진과 오른쪽 글 블록의 상하 정렬이 깨지면 안 되므로, 길면 말줄임(`text-overflow: ellipsis`)으로 자른다. 줄바꿈 금지.
- **그 밖의 모임 카드(모든 모임·지난 모임 등)는 자연 줄바꿈에 맡긴다.** 쉼표 기준으로 강제 개행하지 않는다 — 첫 줄이 짧게 남아 어색해진다.

## 아이콘
- **Lucide** 라이브러리만 사용. CDN: `<script src="https://unpkg.com/lucide@latest"></script>`
- 사용법: `<i data-lucide="icon-name"></i>` 삽입 후 `lucide.createIcons()` 호출
- 아이콘 크기/색은 CSS로 제어 (`width`, `height`, `stroke` 또는 `color`)

## 파일
- `tokens.css` — 단일 진실 공급원. **반드시 먼저 로드.**
- `components.css` — tokens.css에 의존. 그다음 로드.

## 폴더 구조 (승격 흐름)
- `screens/` — 화면별 확정본. 직접 수정 금지(승격으로만 교체). 승격이 늦어 최신이 아닐 수 있으므로, **수정 작업은 `review/`·`prototypes/`·`screens/` 중 그 화면의 가장 최근 파일에서 출발.**
- `review/` — QA 통과 후 팀 승인 대기.
- `prototypes/` — 작업 폴더(`<주제>-MMDD/`). 기존 폴더는 아카이브 — 수정 금지.
- `assets/` — 공용 에셋. 새 에셋도 여기에 (프로토타입 폴더에 복사 금지).
- CSS/에셋 상대 경로: `screens/`·`review/`는 `../tokens.css`·`../assets/`, `prototypes/<폴더>/`는 `../../tokens.css`·`../../assets/`.
- 서비스·화면 파악은 `PRODUCT.md`, 화면↔파일 매핑은 `SCREENS.md` 참조. **화면을 `screens/`에 반영하면 두 문서도 같은 작업에서 갱신.**
- 디자인 작업 요청 시 `/design-team` 스킬 사용 (기획→승인→디자이너→QA 파이프라인).

## 사용 가능한 토큰 (tokens.css)
- **색상(semantic):** `--color-primary / -dark / -light / -subtle`, `--color-brand-gradient / -banner-gradient`, `--color-bg / -surface / -surface-sub / -surface-strong / -surface-glass / -surface-veil / -surface-dark / -card`, `--color-text / -sub / -muted / -faint`, `--color-border / -border-subtle / -input`, `--color-destructive / -destructive-subtle / -success / -success-dark / -success-subtle / -warning / -warning-dark / -warning-subtle / -star / -star-empty`, `--color-on-primary / -on-primary-sub / -on-primary-faint`, `--color-scrim / -scrim-strong / -scrim-heavy`, `--color-page-mist / -page-cream / -page-blush / -page-lilac / -page-sky / -page-mint` (프로필 페이지 배경 프리셋 — mist는 board.html과 같은 기본 배경, 나머지는 파스텔), `--color-chat-apricot / -chat-blossom / -chat-plum / -chat-ocean / -chat-forest` (대화하기 버튼 색상 프리셋 — 배경 프리셋과 1:1로 짝지은 깊은 색. mist 자리는 그라데이션), `--color-kakao / -on-kakao` (카카오 로그인 버튼 — 브랜드 가이드상 색 고정), `--color-apple / -on-apple` (Apple 로그인 버튼 — 가이드상 검정 고정), `--color-facebook / -on-facebook` (페이스북 공유 버튼 — 브랜드 파랑 고정), `--color-linkedin / -on-linkedin` (링크드인 공유 버튼 — 브랜드 파랑 고정), `--color-coral / -on-coral` (다홍 — 알림 신청 등 눈에 띄는 보조 강조), `--color-fellows / -fellows-dark / -fellows-light / -fellows-subtle / -on-fellows` (펠로우즈 공식 모임 전용 올리브 그린 — 로고색 기준. 앱 기본색은 primary 유지), `--color-mark-chocolate / -peach / -amber / -olive` (캠퍼스 선배 카드 문장 강조 형광펜 — 카드마다 돌아가며 씀), `--color-campus / -campus-dark / -campus-weak / -campus-subtle / -campus-lime / -campus-arrow / -campus-arrow-off / -on-campus` (펠로우즈 캠퍼스 화면 전용 초록), `--color-line-warm / -text-warm-sub / -text-warm-faint / -card-stack` (카드형 프로필 템플릿의 따뜻한 중립색 — 행 구분선, 보조 글자, 날짜, 명함 아래 비치는 종이)
- **타이포(유틸 클래스):** `.text-display .text-title .text-heading .text-body-lg .text-body .text-label .text-caption .text-badge .text-link .text-metric .text-nav` (title-sm 18px는 유틸 없이 `var(--fs-title-sm)`·`--lh-title-sm`·`--ls-title-sm` 토큰만 사용. hero 44px도 유틸 없이 `--fs-hero`·`--lh-hero`·`--ls-hero` — 랜딩 히어로 대형 제목(PC) 전용. 캠퍼스 화면은 `--fs-lead`(17) · `--fs-title-lg`(22) · `--fs-headline`(24) 토큰만, 각각 짝 맞는 `--lh-*`·`--ls-*`)
- **글꼴:** `--font-base`(Pretendard) · `--font-serif`(Noto Serif KR — 브런치풍 에디토리얼 제목. 쓰는 화면에서 Google Fonts 로드)
- **자간 추가:** `--ls-wide`(1px) — 영문 대문자 장식 문구(리본·마퀴 등) 트래킹 · `--ls-namecard`(0.14em) · `--ls-namecard-sub`(0.06em) — 명함 위 이름·직함
- **radius:** `--r-xs/sm/md/lg/xl/full` · `--r-tile`(12px, SNS 타일) · `--r-section`(26px, 카드형 프로필 섹션 카드) · **shadow:** `--shadow-1`~`--shadow-4`, `--shadow-lift`(명함 카드가 배경 사진 위로 떠 보이게) · **motion:** `--motion-fast/standard/slow`, `--ease-enter/exit/standard`
- **폼 컨트롤:** `--input-h`(input·select 높이) · `--input-h-lg`(큰 입력 높이, 56px) · `--input-px`(좌우 여백) · `--textarea-py` · `--textarea-h`(최소 높이). 인풋 배경은 흰색(`--color-surface`)
- **블러:** `--blur-fill`(포스터 썸네일 배경 레이어, 24px) · `--blur-dim`(편집 중 나머지 요소를 뒤로 물릴 때, 2px) · `--blur-veil`(화면 전체를 흐리고 그 위에 문구를 띄울 때, 16px)

## 사용 가능한 컴포넌트 (components.css)
모두 클래스 조합 방식. **새로 만들기 전에 여기 있는지 먼저 확인한다.**
- **Button:** `.btn` + 크기 `.btn-xs/sm/md/lg/xl` + `.btn-block .btn-pill` + 스타일 `.btn-fill-primary/dark/danger/success/gradient/kakao/apple/light/fellows/campus`(light = 색이 깔린 면·사진 위 흰 버튼, fellows = 펠로우즈 올리브 그린, campus = 펠로우즈 캠퍼스 초록), `.btn-weak-primary/dark/danger/fellows/campus`, `.btn-line-dark` / `.btn-line-light`(사진·어두운 면 위 흰 테두리) + 로딩 `.is-loading`(카카오 버튼 위에선 스피너가 글자색)
- **IconButton:** `.icon-btn` + `.icon-btn-sm/lg` + 원형 `.icon-btn-pill` + `.icon-btn-clear/fill/border` + 진한 채움 `.icon-btn-fill-primary`(보내기 등) + 소셜 공유 `.icon-btn-fill-kakao` / `.icon-btn-fill-linkedin`(브랜드 색 고정)
- **BrandLogo:** `.brand-logo` + `.brand-logo-kakao` / `.brand-logo-linkedin`(심볼만 — 각각 `.icon-btn-fill-kakao` / `-linkedin` 원형 버튼 안에 넣어 씀) / `.brand-logo-facebook`(원형 로고 그대로) — assets의 공식 로고를 브랜드 색으로 찍는다. 소셜 로고는 Lucide 대신 이걸 쓴다
- **Label:** `.label`, 필수표시 `.label-required`
- **Input:** `.input` (+ `.is-error`, 크게 `.input-lg`), 에러문구 `.input-error-msg`
- **TextArea:** `.textarea` (+ `.textarea-auto` 자동높이, `.is-error`, 크게 `.textarea-lg`)
- **Checkbox:** `.checkbox` / **Radio:** `.radio` / **Toggle(Switch):** `.toggle` (+ `.toggle-sm` 소형)
- **Select:** `.select`
- **Menu(Dropdown):** `.menu .menu-header .menu-item` (+ `.is-selected .is-danger`)
- **Badge:** `.badge` + `.badge-sm/md/lg` + `.badge-fill-*` (primary/dark/danger/neutral) / `.badge-weak-*` (primary/dark/danger/neutral/success/warning/fellows — fellows는 펠로우즈 공식 모임 포인트용) / 사진 위 `.badge-glass` `.badge-glass-danger`
- **Bottom Sheet:** `.bottom-sheet-overlay .bottom-sheet .bottom-sheet-handle` (+ `.is-open`)
- **Toast:** `.toast-container .toast` (+ 액션 붙일 때 `.toast-with-action` + `.toast-action`) + 크게 `.toast-lg` + 결과 색 `.toast-success` / `.toast-warning` / `.toast-neutral` + 안쪽 보조 텍스트 `.toast-sub`
- **Dialog/Modal:** `.dialog-overlay .dialog .dialog-title .dialog-desc .dialog-actions` (닫을 땐 `.dialog-overlay`에 `hidden` 속성)
- **Avatar:** `.avatar` + `.avatar-xs/sm/md/lg/xl/2xl` + `.avatar-rounded` — 사진 없는 사람도 `.avatar`만 쓴다(기본 실루엣 이미지가 배경으로 깔림). `.avatar-blank` 아이콘·이름 이니셜로 대체 금지. 아바타에 커스텀 클래스를 붙일 땐 `background`로 기본 이미지를 덮어쓰지 않게 주의
- **Divider:** `.divider-text` — 가운데 텍스트가 들어가는 구분선(좌우 가로선 자동)
- **SuggestChip:** `.suggest-chip` (+ `.suggest-chip-sm` 소형, 고른 상태 `.is-selected` = 무채색 채움) — AI 추천 답·빠른 요청처럼 **눌러야 하는 칩에만** 쓰는 알약. 상태·분류 표시용으로 쓰지 않는다

## ✅ 좋은 예 / ❌ 나쁜 예
- ❌ `<button style="background:#6b6be1; height:40px">` — 하드코딩
- ✅ `<button class="btn btn-md btn-fill-primary">`
- ❌ `style="color:#767985; font-size:12px"`
- ✅ `class="text-caption"` (또는 `style="color:var(--color-text-muted)"`)
- ❌ `<span class="label">대표자</span><span class="field-desc">팀원 중 한 명을 대표자로 체크해요 · 안내는 대표자에게 먼저 가요</span>` — 허가 없이 붙인 설명 문구
- ✅ `<span class="label">대표자</span>` — 라벨만. 설명이 꼭 필요하면 먼저 사용자에게 확인한다
