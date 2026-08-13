# Connectia 디자인 시스템 규칙

## 핵심 규칙 (YOU MUST)
- 모든 스타일은 `tokens.css`의 토큰과 `components.css`의 클래스를 **먼저 사용**한다.
- raw 값(hex, px, rgba, 임의 font-size 등) **하드코딩 금지**. 항상 토큰 변수 / 유틸 클래스를 참조한다.
- 필요한 스타일이 없으면 일회성으로 만들지 말고, `tokens.css`에 토큰을 추가하거나 `components.css`에 클래스를 확장한다.
- 색은 semantic 토큰(`--color-*`)만 사용. `--palette-*`는 토큰 정의용이므로 컴포넌트에서 직접 쓰지 않는다.
- 여백(padding·margin·gap)은 **4의 배수**(8 / 12 / 16 / 20 / 24…)로만 쓴다. 임의의 px 값(13px, 17px 등) 금지.
- **`components.css`나 `tokens.css`에 클래스/토큰을 추가하거나 변경하면, 아래 "사용 가능한 토큰/컴포넌트" 목록도 같은 작업에서 반드시 함께 갱신한다.**

## 아이콘
- **Lucide** 라이브러리만 사용. CDN: `<script src="https://unpkg.com/lucide@latest"></script>`
- 사용법: `<i data-lucide="icon-name"></i>` 삽입 후 `lucide.createIcons()` 호출
- 아이콘 크기/색은 CSS로 제어 (`width`, `height`, `stroke` 또는 `color`)

## 파일
- `tokens.css` — 단일 진실 공급원. **반드시 먼저 로드.**
- `components.css` — tokens.css에 의존. 그다음 로드.

## 폴더 구조 (승격 흐름)
- `screens/` — **화면별 확정본 = 실서비스 반영 기준.** 수정 작업은 항상 여기서 출발. 직접 수정 금지(승격으로만 교체).
- `review/` — QA 통과 후 팀 승인 대기.
- `prototypes/` — 작업 폴더(`<주제>-MMDD/`). 기존 폴더는 아카이브 — 수정 금지.
- `assets/` — 공용 에셋. 새 에셋도 여기에 (프로토타입 폴더에 복사 금지).
- CSS/에셋 상대 경로: `screens/`·`review/`는 `../tokens.css`·`../assets/`, `prototypes/<폴더>/`는 `../../tokens.css`·`../../assets/`.
- 서비스·화면 파악은 `PRODUCT.md`, 화면↔파일 매핑은 `SCREENS.md` 참조. **화면을 `screens/`에 반영하면 두 문서도 같은 작업에서 갱신.**
- 디자인 작업 요청 시 `/design-team` 스킬 사용 (기획→승인→디자이너→QA 파이프라인).

## 사용 가능한 토큰 (tokens.css)
- **색상(semantic):** `--color-primary / -dark / -light / -subtle`, `--color-brand-gradient / -banner-gradient`, `--color-bg / -surface / -surface-sub / -surface-glass / -card`, `--color-text / -sub / -muted`, `--color-border / -input`, `--color-destructive / -destructive-subtle / -success / -star / -star-empty`, `--color-on-primary / -on-primary-sub / -on-primary-faint`, `--color-scrim`
- **타이포(유틸 클래스):** `.text-display .text-title .text-heading .text-body-lg .text-body .text-label .text-caption .text-badge .text-link .text-metric .text-nav` (title-sm 18px는 유틸 없이 `var(--fs-title-sm)`·`--lh-title-sm`·`--ls-title-sm` 토큰만 사용)
- **radius:** `--r-xs/sm/md/lg/xl/full` · **shadow:** `--shadow-1`~`--shadow-4` · **motion:** `--motion-fast/standard/slow`, `--ease-enter/exit/standard`

## 사용 가능한 컴포넌트 (components.css)
모두 클래스 조합 방식. **새로 만들기 전에 여기 있는지 먼저 확인한다.**
- **Button:** `.btn` + 크기 `.btn-sm/md/lg/xl` + `.btn-block .btn-pill` + 스타일 `.btn-fill-primary/dark/danger/gradient`, `.btn-weak-primary/dark/danger`, `.btn-line-dark` + 로딩 `.is-loading`
- **IconButton:** `.icon-btn` + `.icon-btn-sm/lg` + `.icon-btn-clear/fill/border`
- **Label:** `.label`, 필수표시 `.label-required`
- **Input:** `.input` (+ `.is-error`), 에러문구 `.input-error-msg`
- **TextArea:** `.textarea` (+ `.textarea-auto` 자동높이, `.is-error`)
- **Checkbox:** `.checkbox` / **Radio:** `.radio` / **Toggle(Switch):** `.toggle` (+ `.toggle-sm` 소형)
- **Select:** `.select`
- **Menu(Dropdown):** `.menu .menu-header .menu-item` (+ `.is-selected .is-danger`)
- **Badge:** `.badge` + `.badge-sm/md/lg` + `.badge-fill-*` / `.badge-weak-*` (primary/dark/danger/neutral)
- **Bottom Sheet:** `.bottom-sheet-overlay .bottom-sheet .bottom-sheet-handle` (+ `.is-open`)
- **Toast:** `.toast-container .toast`
- **Dialog/Modal:** `.dialog-overlay .dialog .dialog-title .dialog-desc .dialog-actions`
- **Avatar:** `.avatar` + `.avatar-xs/sm/md/lg/xl` + `.avatar-rounded`

## ✅ 좋은 예 / ❌ 나쁜 예
- ❌ `<button style="background:#6b6be1; height:40px">` — 하드코딩
- ✅ `<button class="btn btn-md btn-fill-primary">`
- ❌ `style="color:#767985; font-size:12px"`
- ✅ `class="text-caption"` (또는 `style="color:var(--color-text-muted)"`)
