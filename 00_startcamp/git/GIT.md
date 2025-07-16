# GIT bash

## Git이란
분산 버전 관리
- 변화를 기록하고 추적하는 것

## 중앙 vs 분산
- 중앙 서버에 저장된 버전을 가져와서 사용하고 업로드 : 원본이 여러개라 문제 발생 가능성

- 버전을 여러 개의 복제된 저장소에 저장 및 관리 : 버전 정보를 .git폴더에 저장

## Git의 영역

1. Working Directory : 현재 작업중인 영역 
- 실제 작업 중인 파일들이 위치하는 영역

2. Staging area : 기록 예상
- 작업으로 변경된 파일 중, 다음 저번에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 **중간** 영역

3. Repository
- 버전 이력과 파일들이 영구적으로 저장되는 영역, 버전과 변경 이력이 기록됨

## git 사용법

1. git init
2. git add 파일
3. git status
- staging area에 무엇이 있는지와 상태
- 현재 추적중인 파일과 추적파일의 변동사항 등을 가르쳐줌
4. git commit -m "내용"
- 버전 만들기
- 그 전에 유저를 등록해야함.
- git config --global user.email or name

5. git log
- commit 내역 열람 가능

git은 로컬의 파일의 모든 변경사항을 감시하고 있음

## master slave의 어두운 이야기

6. git remote add origin 주소
- 원격 저장소 추가하는 명령어
- git remote-v : 현재 원격 레포지토리 확인


7. git push -u origin master
- 원격 저장소에 commit한 내용 푸시




