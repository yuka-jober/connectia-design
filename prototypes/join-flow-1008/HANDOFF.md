# [개발 전달] 커뮤니티 가입 흐름 · 관리자 모드 개편

이벤트를 신청한 사람이 모임 회원이 되고 회원 메뉴에 들어가기까지를 하나의 흐름으로 이었고,
운영자가 회원·방문자에게 보이는 화면을 직접 확인할 수 있게 정리했어요. 10/8 팀 리뷰에서 이대로 진행하기로 했어요.

## 먼저 보기

| 순서 | 무엇 | 링크 |
|---|---|---|
| 1 | 한눈에 보기 (시나리오 영상 17개) | https://connectia-design.vercel.app/prototypes/join-flow-1008/overview.html |
| 2 | 기획 상세 (화면별 사양·문구·확인할 장면) | [기획 문서](https://github.com/yuka-jober/connectia-design/blob/profile-head-block-0911/docs/specs/2026-10-08-%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0-%EA%B0%80%EC%9E%85%ED%9D%90%EB%A6%84-%EA%B4%80%EB%A6%AC%EC%9E%90%EB%AA%A8%EB%93%9C.md) |
| 3 | 직접 눌러보기 · 가입 흐름 | https://connectia-design.vercel.app/review/join-flow.html |
| 4 | 직접 눌러보기 · 커뮤니티 운영자 | https://connectia-design.vercel.app/review/community-mode-owner.html |

가입 흐름 프로토타입은 PC로 열면 오른쪽 패널에서 상황(이미 회원, 승인 대기, 거절 등)과 승인 방식을 바꾸거나 자동 재생할 수 있어요.
커뮤니티 운영자 화면은 상단 [관리] 버튼으로 관리자 모드에 들어가요.

## GitHub 폴더

| 폴더 | 내용 |
|---|---|
| [prototypes/join-flow-1008](https://github.com/yuka-jober/connectia-design/tree/profile-head-block-0911/prototypes/join-flow-1008) | 가입 흐름 프로토타입, 시나리오 영상(`videos/`), 시나리오 경로(`SCENARIOS.md`), 이 문서 |
| [prototypes/community-admin-mode-1008](https://github.com/yuka-jober/connectia-design/tree/profile-head-block-0911/prototypes/community-admin-mode-1008) | 커뮤니티 운영자 프로토타입, 시나리오 영상(`videos/`) |
| [review/](https://github.com/yuka-jober/connectia-design/tree/profile-head-block-0911/review) | 승인본 `join-flow.html`, `community-mode-owner.html` |
| [docs/specs/](https://github.com/yuka-jober/connectia-design/tree/profile-head-block-0911/docs/specs) | 기획 문서 |
| [tokens.css](https://github.com/yuka-jober/connectia-design/blob/profile-head-block-0911/tokens.css) · [components.css](https://github.com/yuka-jober/connectia-design/blob/profile-head-block-0911/components.css) | 디자인 토큰·컴포넌트 (이번 작업에서 변경 없음) |

## 크게 바뀌는 점

1. **가입하지 않은 사람도 회원 메뉴를 봐요.** 홈·멤버·게시판·행사 탭이 모두 보이고, 멤버·게시판 내용만 일부 가려요. 가려진 걸 누르면 로그인하지 않았으면 로그인 창, 로그인했지만 회원이 아니면 가입 모달이 떠요.
2. **이벤트 신청이 곧 가입 입구예요.** 신청 완료 직후 "회원으로도 가입할까요?" 모달이 뜨고, 행사 때 입력한 이름·전화번호가 가입 폼에 채워져요.
3. **가입 상태가 어디서나 같아요.** 가입 전 / 승인 대기 / 회원 / 거절을 이벤트 페이지, 모임 페이지, 가입한 커뮤니티가 똑같이 보여주고 새로고침해도 유지돼요.
4. **운영자도 기본은 회원 화면이에요.** [관리]를 눌러야 관리자 모드에 들어가고, 관리자 모드에서 [방문자로 보기]로 가입 전 사람의 화면도 볼 수 있어요.
5. **공개 설정이 하나로 줄었어요.** 항목별 공개 범위와 멤버별 항목 토글을 없앴어요. 전화번호·이메일만 운영자가 보고, 본인이 "연락처를 멤버에게 공개"를 켜면 멤버에게도 보여요.
6. **운영자가 미리 등록한 멤버에 '인증 전' 뱃지가 붙어요.**
7. **회원만 신청할 수 있는 행사가 생겨요.** 회원이 아닌 사람이 [신청하기]를 누르면 "회원만 신청할 수 있어요 · 경륜재에 가입할까요?"가 뜨고, 가입하면 이어서 신청할 수 있어요.

## 먼저 고쳐야 할 동작 (지금 서비스)

디자인을 바꿔도 아래가 그대로면 사용자는 똑같이 헤매요.

1. 새로고침하면 '가입 대기'가 사라지고 [가입하기]로 돌아가요
2. 신청 직후 이벤트 페이지가 그대로라 같은 이벤트를 두 번 신청할 수 있어요
3. 가입한 커뮤니티에 승인 대기 모임이 안 보여요

## 확인할 장면

기획 문서 7장에 18개 장면(가입 흐름 J1~J11, 관리자 모드 A1~A7)과 영상 번호를 정리해 두었어요. QA 기준으로 써 주세요.

궁금한 점은 디자인 담당에게 물어봐 주세요.
