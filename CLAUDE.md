# 프로젝트 규칙
- 언어: Python 3.11, 외부 라이브러리 금지(pytest 제외)
- 테스트: `python -m pytest -q` 가 통과해야 PR 가능
- 새 기능에는 반드시 테스트를 함께 추가
- 잘못된 인덱스는 IndexError 대신 한글 메시지의 ValueError로 처리
- 커밋 메시지: `feat:`, `fix:`, `test:` 접두사 사용
