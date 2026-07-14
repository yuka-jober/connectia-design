# 화면 인덱스 (SCREENS.md)

Connectia 화면별 확정본 관리 문서. **`screens/`의 파일이 실서비스 반영 기준(최신 확정본)이다.**

## 폴더 구조와 흐름

```
prototypes/   작업 폴더 — <주제>-MMDD/ 단위로 실험·버전을 쌓는 곳 (아카이브)
review/       승인 대기 — QA 통과한 결과물이 팀 OK를 기다리는 곳
screens/      확정본 — 팀 OK = 실서비스 반영 기준. 화면당 1파일, 화면 이름으로 명명
assets/       공용 에셋 — 프로토타입에서 재사용하는 이미지·로고. 새 에셋도 여기에 추가
```

**승격 흐름:** `prototypes/`에서 작업 → QA 통과 → `review/` → 팀 OK → `screens/`에 반영(교체)

**경로 규칙:** `screens/` 파일은 루트 기준 한 단계 아래이므로 `../tokens.css`, `../components.css`, `../assets/...`로 참조한다.

## 화면 목록

| 화면 | 확정본 | 원본 (작업 이력) |
|---|---|---|
| 게시판(보드) | `screens/board.html` | prototypes/board-gallery-tab-0708/board.html |
| 프로필 편집 | `screens/profile-edit.html` | prototypes/gallery-view-change-0708/profile-edit-v4.html |
| 이벤트 입력폼 | `screens/event-input.html` | prototypes/event-review-remove-0714/event-input.html |
| 이벤트 랜딩 | `screens/event-landing.html` | prototypes/event-review-remove-0714/event-landing.html |
| 이벤트 신청자 확인 | `screens/event-applicants-check.html` | prototypes/event-applicants-check-0701/index.html |
| 이벤트 소개 | `screens/event-intro.html` | prototypes/event-intro-0701/event-intro.html |
| 통계 | `screens/statistics.html` | prototypes/statistics-0611/statistics-v2.html |
| 로그인 | `screens/login.html` | prototypes/login-0707/login.html |
| 프로필 시작(온보딩) | `screens/profile-start.html` | prototypes/profile-start-0612/start-v2.html |
| 답변 플로우(채팅) | `screens/answer-flow.html` | prototypes/answer-flow-0611/chat-inline.html |
| 커뮤니티 멤버 | `screens/community-member.html` | prototypes/community-member-0630/community-member.html |
| 글쓰기 | `screens/post-write.html` | prototypes/post-write-0703/post-write.html |
| 영업 프로필 이름 | `screens/sales-profile-name.html` | prototypes/sales-profile-name-0701/sales-profile-name.html |
| 팀 단위 페이지 관리 | `screens/team-page.html` | prototypes/team-ai-page-0707/index.html |
| 내 AI 아바타 | `screens/my-ai-avatars.html` | prototypes/my-ai-avatars-0701/index.html |
| 이력서 프로필 | `screens/resume-profile.html` | prototypes/resume-profile-0610/resume-profile.html |

### 보류 (확정본 미선정)
- **카카오 공유 썸네일** — prototypes/kakao-share-thumbnail-0708/ 에서 a/b/c 시안 작업 중. 확정되면 `screens/kakao-share-thumbnail.html`로 승격.

### 제외 (일회성·미사용)
- prototypes/event-landing-derma-0624/ — 특정 고객용 일회성 작업.
- 이벤트 상세, 이벤트 참여자 목록, 프로필 버튼, 명함 앱, 명함(프로필 랜딩) — 확정본에서 제외 (2026-07-08, 미사용 판단). 원본은 prototypes/·handoff/에 그대로 있음.

## 공용 에셋 (assets/)

| 파일 | 용도 |
|---|---|
| `profile.svg` | 프로필 아바타 (기존 6개 폴더 중복분 통합) |
| `profile.png` | 프로필 사진 |
| `logo.svg` | Connectia 로고 (event-detail 계열) |
| `logo-start.svg` | Connectia 로고 (온보딩 계열, 내용 다름) |
| `logo-company.png` | 예시 회사 로고 (커넥트생명) |
| `banner-board.png` | 보드 상단 배너 |
| `banner-gsdd.png` / `avatar-gsdd.png` | 데모 커뮤니티(강남세브란스) 배너·아바타 |
| `eye_banner.png` / `eye_banner2.png` | 안과 이벤트 배너 |
| `thumbnail_1~3.png` | 이벤트 카드 썸네일 |
| `event_thumbnail.png` | 이벤트 대표 썸네일 |
| `event_thumbnail_image/` | 이벤트 썸네일 템플릿 16종 (업종별) |
| `profile-cs/sales/service/fan.png` | 온보딩 서비스 유형별 예시 이미지 |

## 유지 규칙

1. `prototypes/`, `handoff/`의 기존 파일은 수정하지 않는다 (아카이브).
2. 수정 작업은 항상 `screens/`의 확정본을 복사해 `prototypes/<주제>-MMDD/`에서 시작한다.
3. 새 확정본을 `screens/`에 반영할 때 이 문서의 표도 함께 갱신한다.
4. 에셋은 `assets/`에서 참조하고, 새 에셋이 생기면 `assets/`에 추가한다 (프로토타입 폴더에 복사하지 않는다).
