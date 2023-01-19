# 포켓몬 연구소

##### 프로젝트 기간 : 프로젝트 기간 20221031 ~ 20221105

##### 팀명: 포켓몬 연구소

<a href="https://github.com/wxxk/Django_pair6/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=wxxk/Django_pair6" />
</a>

##### 팀장 : 1기 1회차 이상욱 @wxxk

##### 팀원 : 1기 2회차 이우열 @w00ye0l

##### 팀원 : 1기 3회차 이상훈 @danny7128

### 코드실행

---

![bandicam-2022-11-07-15-15-46-683](README.assets/bandicam-2022-11-07-15-15-46-683.gif)

### 목차

| 내용                          |
| ----------------------------- |
| [코드실행](#코드실행)         |
| [프로젝트소개](#프로젝트소개) |
| [코드구현](#코드구현)         |


### 프로젝트소개

---

- #### 목적

  > 상품 정보 및 후기 공유 커뮤니티 서비스
  >
  > - CRUD 구현
  > - Staticfiles 활용 정적 파일(이미지, CSS, JS) 다루기
  > - Django Auth 활용 회원 관리(회원가입 / 회원조회 / 로그인 / 로그아웃)
  > - Media 활용 동적 파일 다루기
  > - 모델간 1 : N / M : N 관계 매핑

* #### 개발 환경

  > 언어 : HTML, CSS, Python, JavaScript
  >
  > 프레임워크 : Django

### 코드구현

---

> ### 1. 회원가입
>
> > 앱 App
> >
> > 앱 이름 : accounts
> >
> > 모델 Model
> >
> > 모델 이름 : User
>
> - Django **AbstractUser** 모델 상속
>
> **폼 Form**
>
> - Django 내장 회원가입 폼 UserCreationForm을 상속 받아서 CustomUserCreationForm 작성
> - 해당 폼은 아래 필드만 출력
>   - username
>   - first_name
>   - last_name
>   - password1
>   - password2
>   - email
>   - image
>
> **기능 View**
>
> - 회원가입
>
>   - `POST` http://127.0.0.1:8000/accounts/signup/
>
>   - CustomUserCreationForm을 활용해서 회원가입 구현
>
> **화면 Template**
>
> - 회원가입 페이지
>
>   - `GET` http://127.0.0.1:8000/accounts/signup/
>
>   - 회원가입 폼
>
> ---
>
> ### 2. 로그인
>
> **폼 Form**
>
> - 로그인
>   - Django 내장 로그인 폼 **AuthenticationForm 활용**
>
> **기능 View**
>
> - 로그인
>
>   - `POST` http://127.0.0.1:8000/accounts/login/
>
>   - **AuthenticationForm**를 활용해서 로그인 구현
>
> **화면 Template**
>
> - 로그인 페이지
>
>   - `GET` http://127.0.0.1:8000/accounts/login/
>
>   - 로그인 폼
>
>   - 회원가입 페이지 이동 버튼
>
> ---
>
> ### 3. 회원 정보 조회
>
> **기능 View**
>
> - 회원 정보 조회
>   - `GET` http://127.0.0.1:8000/accounts/<int:pk>/profile/
>
> **화면 Template**
>
> - 회원 조회 페이지(프로필 페이지)
>
>   - `GET` http://127.0.0.1:8000/accounts/<int:pk>/profile/
>
>   - 작성한 글 버튼
>   - 작성한 댓글 버튼
>   - 정보 수정
>   - 회원 탈퇴
>
> ---
>
> ### 4. 회원 정보 수정
>
> **폼 Form**
>
> - 회원 정보 수정
> - Django 내장 회원 수정 폼 UserChangeForm을 상속 받아서 **CustomUserChangeForm** 작성
> - 해당 폼은 아래 필드만 출력
>   - last_name
>   - first_name
>   - email
>   - image
>
> **기능 View**
>
> 회원 정보 수정
>
> - `POST` http://127.0.0.1:8000/accounts/update/
>
> **화면 Template**
>
> 회원 정보 수정 페이지
>
> - `GET` http://127.0.0.1:8000/accounts/update/
> - 비밀번호 변경 버튼
> - 정보 수정 버튼
>
> ---
>
> ### 5. 비밀번호 변경
>
> **폼 Form**
>
> - 회원 정보 수정
>
> - 해당 폼은 아래 필드만 출력
>   - password
>   - new_password1
>   - new_password2
>
> **기능 View**
>
> 회원 정보 수정
>
> - `POST` http://127.0.0.1:8000/accounts/update/
>
> **화면 Template**
>
> 회원 정보 수정 페이지
>
> - `GET` http://127.0.0.1:8000/accounts/update/
>
> - 비밀번호 변경 버튼
>
> ---
>
> ### 6. 로그아웃
>
> **기능 View**
>
> - 로그아웃
>
>   - **AuthenticationForm**를 활용해서 로그아웃 구현
>
>   - `POST` http://127.0.0.1:8000/accounts/logout/
>
> ---
>
> ### 7. 팔로우
>
> ##### 기능 view
>
> 팔로우 & 팔로우 취소
>
> - `POST` http://127.0.0.1:8000/accounts/<int:user_pk>/follow/
> - 로그인한 유저만 팔로우 기능을 사용
>
> ##### 화면 Template
>
> 회원 정보 페이지(프로필 페이지)
>
> - `GET` http://127.0.0.1:8000/accounts/<int:user_pk>/profile/
>
> - 팔로워 수 / 팔로잉 수
>
> - 다른 회원의 프로필 페이지
>
>   - 스스로 팔로우 불가능
>
>   - 로그인한 유저만 기능 사용
>
>   - 로그인 상태 / 팔로우 상태에 따라 다르게 표현
>
> ---
>
> ### 8. 계정탈퇴
>
> ##### 기능 view
>
> - `POST` http://127.0.0.1:8000/accounts/delete\
> - 회원 탈퇴 시 로그아웃
>
> ##### 화면 Template
>
> - Modal을 이용해 회원 탈퇴 확인
>
>   - 탈퇴 / 아니오 버튼
>
> ---
>
> ### 8. 네비게이션바
>
> **화면 Template**
>
> - **네비게이션바**
>
>   - 스토어 페이지 이동 버튼
>   - 카드연구소 페이지 이동 버튼
>   - 놀이방법 페이지 이동 버튼
>   - 마이페이지 이동 버튼
>   - 로그아웃 버튼
>   - 로그인 상태에 따라 다른 화면 출력
>     1. 로그인 상태
>        - 마이페이지를 클릭하면 회원 정보 조회(사용자) 페이지로 이동
>        - 로그아웃 버튼
>     2. 비 로그인 상태
>        - 로그인 페이지 이동 버튼
>        - 회원가입 페이지 이동 버튼
>
> ### FOOTER
>
> ##### 화면 Template
>
> - 팀원
> - 깃허브 주소
> - 참고 사이트
>
> ### MAIN 페이지
>
> ##### 화면 Template
>
> - 비디오 재생
> - 로그인 페이지 이동 버튼
> - 스토어 페이지 이동 버튼
> - 비디오 정지 버튼
>
> ---
>
> ### 9. 판매글 생성
>
> **앱 App**
>
> 앱 이름 : store
>
> 모델 Model
>
> 모델 이름 : Store
>
> - 모델 필드
>
>   | 이름       | 역할          | 필드       | 속성              |
>   | ---------- | ------------- | ---------- | ----------------- |
>   | title      | 포켓몬 이름   | Char       |                   |
>   | content    | 리뷰 내용     | Text       |                   |
>   | created_at | 리뷰 생성시간 | DateTime   | auto_now_add=True |
>   | updated_at | 리뷰 수정시간 | DateTime   | auto_now = True   |
>   | image      | 이미지        | Image      |                   |
>   | buysell    | 구매/판매     | Boolean    |                   |
>   | cost       | 가드 가격     | Integer    |                   |
>   | user       | 유저 pk       | ForeignKey |                   |
>   | like_user  | 관심          | ManyToMany |                   |
>   | type       | 포켓몬 타입   | Char       |                   |
>
> **기능 View**
>
> 데이터 생성
>
> - `POST` http://127.0.0.1:8000/reviews/create/
>
> **화면 Template**
>
> **리뷰 작성 페이지**
>
> - `GET` http://127.0.0.1:8000/reviews/create/
> - 리뷰 작성 폼
>
> ---
>
> ### 10. 카드 목록 조회
>
> **기능 View**
>
> - 데이터 목록 조회
>   - `POST` http://127.0.0.1:8000/store/<str:type>/<int:num>/type/
> - 카드 가격에 따라 분류(가격 낮은순으로 5개만 출력)
>
> **화면 Template**
>
> - 리뷰 **목록 페이지**
>
>   - 카드 타입 이미지 출력
>
>   - 타입 출력
>
>   - `GET` http://127.0.0.1:8000/store/<str:type>/<int:num>/type/
>
>   - 구매/판매 목록 출력
>
>   - 구매/판매 버튼을 클릭하면 해당 카드의 정보 페이지로 이동
>
>   - 글 쓰기 버튼
>
> ---
>
> ### 11. 카드 정보 조회
>
> **기능 View**
>
> - 데이터 정보 조회
>   - `GET` http://127.0.0.1:8000/store/<int:pk>/detail/
> - 게시글에 작성된 댓글 목록 조회
>
>   - `GET` http://127.0.0.1:8000/store/<int:pk>/detail/
>   - 해당 게시글(store_pk)의 댓글 목록 조회
>
> - 댓글 생성
>
>   - `GET` http://127.0.0.1:8000/store/<int:pk>/comment/create/
>   - 비동기 처리
>
> - 댓글 삭제
>   - `GET` http://127.0.0.1:8000/store/<int:store_pk>/<comment_pk>/delete/
>
> **화면 Template**
>
> - **게시물 정보 페이지**
>
>   - `GET` http://127.0.0.1:8000/store/<int:pk>/detail/
>
>   - 댓글 작성 폼
>
>   - 댓글 목록
>
>     - 댓글 내용
>     - 삭제 버튼
>
> ---
>
> ### 12. 게시글 정보 수정
>
> **기능 View**
>
> - 데이터 수정
>   - `POST` http://127.0.0.1:8000/store/<int:pk>/update/
>
> **화면 Template**
>
> - **리뷰 수정 페이지**
>
>   - `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/
>
> - 리뷰 수정 폼
>
> ---
>
> ### 13. 게시글 삭제
>
> **기능 View**
>
> - 데이터 삭제
>   - `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/delete/
>
> ---
>
> ### 14. 관심
>
> **기능 View**
>
> - 좋아요 생성
>   - `POST` http://127.0.0.1:8000/store/<int:pk>/detail/
>   - 로그인한 유저만 좋아요 가능
>
> **화면 Template**
>
> - **게시글 정보 페이지**
>   - `GET` http://127.0.0.1:8000/store/<int:pk>/detail/
>   - 관심 버튼
>     - 해당 글이 받은 좋아요 수를 표시
>     - 로그인 상태와 좋아요 상태에 따라 다르게 표현
>
> ---
>
> ### 15. 포켓몬 연구소
>
> **앱 App**
>
> 앱 이름 : community
>
> 모델 Model
>
> 모델 이름 : CustomCard
>
> - 모델 필드
>
>   | 이름      | 역할             | 필드 | 속성 |
>   | --------- | ---------------- | ---- | ---- |
>   | supertype | 포켓몬 카드 구분 | Text |      |
>   | types     | 포켓몬 타입 구분 | Text |      |
>   | name      | 포켓몬 이름      | Text |      |
>   | image     | 포켓몬 이미지    | Text |      |
>
> **기능 View**
>
> 데이터 생성
>
> - `POST` http://127.0.0.1:8000/community/
> - 랜덤으로 카드 6장 받기
> - 선수들 덱
>
> **화면 Template**
>
> **리뷰 작성 페이지**
>
> - `GET` http://127.0.0.1:8000/community/
> - 행운의 포켓몬 6장
> - 선수들의 덱 레시피
>
> ---
>
> ### 16. 놀이방법
>
> **화면 Template**
>
> **리뷰 작성 페이지**
>
> - `GET` http://127.0.0.1:8000/community/rule/
> - 카드 놀이방법 영상

---
