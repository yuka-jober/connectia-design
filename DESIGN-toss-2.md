# DESIGN-toss-2 — 컴포넌트 레퍼런스

> Claude Code용 컴포넌트 사용 레퍼런스. 새 UI를 만들기 전 이 문서의 컴포넌트를
> 먼저 확인하고 재사용한다. 색/배경은 raw 값 대신 `adaptive.*` 토큰을 사용한다.
> 수록 컴포넌트: **IconButton · Checkbox · Menu(Dropdown) · TextArea**

---

## IconButton

아이콘으로 작업을 실행/트리거하는 버튼. UI를 간결하게 유지할 때 사용.

### variant (형태)
| 값 | 설명 | 클릭 시 |
|---|---|---|
| `clear` (기본) | 배경 없이 아이콘만 | 배경색이 나타남 |
| `fill` | 배경이 채워진 강조 스타일 | 배경색이 사라짐 |
| `border` | 테두리가 있는 스타일 | 배경색이 나타남 |

```tsx
<IconButton src="https://static.toss.im/icons/svg/icon-search-bold-mono.svg" variant="fill" aria-label="검색하기" />
```

### 색·크기 커스텀
- `color`: 아이콘 색. **이름이 `-mono`로 끝나는 모노타입 아이콘만** 변경 가능. (예: `color={adaptive.red500}`)
- `bgColor`: 배경색(기본 `adaptive.greyOpacity100`). `fill`이면 배경색, `clear`/`border`면 눌렀을 때 배경색.
- `iconSize`: 아이콘 크기(px). 기본 `24`.

### 접근성 (필수)
`aria-label`은 **필수**. 아이콘만으로는 역할을 알 수 없으므로 동작을 명시한다.
```tsx
<IconButton src="...icon-search-bold-mono.svg" aria-label="검색하기" />
```

### Props — `IconButtonProps`
| 속성 | 기본값 | 타입 | 설명 |
|---|---|---|---|
| `aria-label` * | - | `string` | **필수.** 버튼 동작 설명 |
| `variant` | `'clear'` | `'clear' \| 'fill' \| 'border'` | 형태 |
| `src` | - | `string` | 아이콘 URL. `name`과 동시 사용 불가 |
| `name` | - | `string` | 아이콘 이름. `src`와 동시 사용 불가 |
| `color` | - | `string` | 아이콘 색(`-mono` 아이콘만) |
| `bgColor` | `adaptive.greyOpacity100` | `string` | 배경색 |
| `iconSize` | `24` | `number` | 아이콘 크기(px) |

---

## Checkbox

하나 이상의 항목 선택. 체크/미체크 상태 표현, 다중 선택 가능.

### 형태
- `<Checkbox.Circle />` — 체크 아이콘이 원으로 감싸진 형태
- `<Checkbox.Line />` — 체크 아이콘 단독 형태

### 상태 관리
```tsx
// Controlled — 외부에서 상태 관리
const [checked, setChecked] = React.useState(true);
<Checkbox.Circle checked={checked} onCheckedChange={setChecked} aria-label="이용약관 동의" />

// Uncontrolled — 내부에서 상태 관리
<Checkbox.Line defaultChecked aria-label="이용약관 동의" />
```

### 옵션
- `size`: 크기(px). 기본 `24`.
- `disabled`: 비활성화. 클릭 시 상태 변화 없이 좌우로 흔들리는 애니메이션.
- **라디오로 활용:** `inputType="radio"` + `value` + `checked` + `onChange` 조합. 여러 항목 중 하나만 선택할 때.
```tsx
<Checkbox.Circle inputType="radio" value="1" checked={sel === '1'} onChange={(e) => setSel(e.target.value)} />
```

### 접근성 (필수)
- `role="checkbox"`, `aria-checked`, `aria-disabled`는 자동 적용됨.
- `aria-label`은 **개발자가 필수로 제공**. 단, 레이블에 "체크박스"라는 단어는 넣지 않는다(스크린 리더가 이미 읽어줌).

### Props — `CheckboxProps`
| 속성 | 기본값 | 타입 | 설명 |
|---|---|---|---|
| `inputType` | `'checkbox'` | `'checkbox' \| 'radio'` | input `type` 결정 |
| `size` | `24` | `number` | 크기 |
| `checked` | - | `boolean` | 선택 상태(controlled, `onCheckedChange`와 함께) |
| `onCheckedChange` | - | `(checked: boolean) => void` | 상태 변경 콜백 |
| `defaultChecked` | - | `boolean` | 초기 선택 상태(uncontrolled) |
| `disabled` | - | `boolean` | 비활성화 |

---

## Menu (Dropdown)

여러 옵션을 나열하고 선택하게 하는 드롭다운 메뉴.

### 구성 요소
- `Menu.Dropdown` — 컨테이너. `header` prop으로 상단 제목 지정.
- `Menu.Header` — 메뉴 제목.
- `Menu.DropdownItem` — 개별 항목. `left`/`right`로 부가 요소 배치.
- `Menu.DropdownIcon` — 항목용 아이콘(보통 `right`에 전달).
- `Menu.DropdownCheckItem` — 체크박스 항목. `checked` + `onCheckedChange`.
- `Menu.Trigger` — 사용자 동작으로 메뉴 열고 닫기.

### 기본 / 아이콘 / 체크 메뉴
```tsx
<Menu.Dropdown header={<Menu.Header>편집</Menu.Header>}>
  <Menu.DropdownItem>첫 번째 메뉴</Menu.DropdownItem>
  <Menu.DropdownItem right={<Menu.DropdownIcon name="icon-setting-mono" />}>두 번째 메뉴</Menu.DropdownItem>
  <Menu.DropdownCheckItem checked={true}>세 번째 메뉴</Menu.DropdownCheckItem>
</Menu.Dropdown>
```

### Trigger로 열기
```tsx
const [open, setOpen] = React.useState(false);
<Menu.Trigger
  open={open}
  onOpen={() => setOpen(true)}
  onClose={() => setOpen(false)}
  placement="bottom"
  dropdown={<Menu.Dropdown header={<Menu.Header>항목을 선택하세요</Menu.Header>}>...</Menu.Dropdown>}
>
  <Button>클릭해보세요</Button>
</Menu.Trigger>
```
- `open`/`onOpen`/`onClose`를 모두 주면 controlled. 안 주면 uncontrolled.
- **placement:** 방향(`top`/`bottom`/`left`/`right`) + 정렬(`-start`/`-end`) 조합. 정렬 생략 시 중앙. 기본 `'bottom-start'`.

### Props
**`MenuDropdownProps`**
| 속성 | 타입 | 설명 |
|---|---|---|
| `header` | `ReactNode` | 헤더. 주로 `Menu.Header`와 사용 |

**`MenuDropdownItemProps`**
| 속성 | 타입 | 설명 |
|---|---|---|
| `left` | `ReactNode` | 왼쪽 요소(체크는 `DropdownCheckItem` 권장) |
| `right` | `ReactNode` | 오른쪽 요소(아이콘은 `DropdownIcon` 권장) |
| `children` | `ReactNode` | 항목 내용 |

**`MenuDropdownCheckItemProps`**
| 속성 | 타입 | 설명 |
|---|---|---|
| `checked` | `boolean` | 체크 상태 |
| `onCheckedChange` | `(checked: boolean) => void` | 체크 변경 콜백 |

**`MenuTriggerProps`**
| 속성 | 기본값 | 타입 | 설명 |
|---|---|---|---|
| `open` | - | `boolean` | 열림 상태(controlled, `onOpen`/`onClose` 필요) |
| `defaultOpen` | - | `boolean` | 초기 열림 상태 |
| `dropdown` | - | `ReactNode` | 열렸을 때 표시할 메뉴(`Menu.Dropdown`) |
| `children` | - | `ReactNode` | 트리거 컴포넌트 |
| `placement` | `'bottom-start'` | `top \| bottom \| left \| right` (+ `-start`/`-end`) | 열리는 위치 |
| `onOpen` | - | `() => void` | 열릴 때 콜백 |
| `onClose` | - | `() => void` | 닫힐 때 콜백 |

---

## TextArea

여러 줄 텍스트 입력(피드백, 주소, 메모 등). `TextField`를 확장 — `prefix`, `suffix`, `right`를 **제외한** TextField 속성을 가짐.

### 고정 높이 vs 자동 높이
```tsx
// 고정 높이 — 레이아웃 일관성
<TextArea variant="box" height="200px" placeholder="텍스트를 입력해보세요." help="높이가 고정된 텍스트 필드" />

// 자동 높이 — 내용에 따라 늘어남, minHeight로 최소 높이 보장
<TextArea variant="box" minHeight={100} placeholder="길게 입력하거나 엔터를 눌러보세요." help="높이가 자동으로 조절되는 텍스트 필드" />
```

### Props — `TextAreaProps` (TextField 확장)
| 속성 | 타입 | 설명 |
|---|---|---|
| `height` | `string \| number` | 고정 높이 |
| `minHeight` | `string \| number` | 최소 높이(자동 높이 모드) |

> `variant`, `placeholder`, `help` 등 나머지는 `TextField` 속성을 따름.
