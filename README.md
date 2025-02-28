# NWebtoon_Downloader

![image](https://user-images.githubusercontent.com/31213158/222766338-b20b22b9-909c-46df-ac24-fe2f26e71196.png)
Python으로 제작한 CLI 버전  
네이버 웹툰 초고속 다운로더 입니다.  
https://pgh268400.tistory.com/216

## 지원 기능
* 웹툰 부분, 전체 다운로드
* 성인 웹툰 다운로드
* 웹툰 받을시 고유번호 or 검색으로 다운 가능
* 다운로드 받은 웹툰 파일들 이미지 한개로 통째로 합치는 기능 (세로 병합)

## 계획중인 기능
* 다운로드 받은 웹툰 HTML 사이트로 볼 수 있게 HTML 생성해주는 기능
  - Release 엔 반영하지 않았고 소스코드 다운로드 받으셔서 직접 실행해보시면 HTML 기능은 사용해볼 수 있습니다. (Experimental)
* 완전한 CLI 명령어 인터페이스로 제작하여 GUI 지원

## 크로스 플랫폼
기본적으로 파이썬 코드로 작성되었고 별다른 GUI 없이 구현되었기에  
리눅스 환경에서도 파이썬 인터프리터만 제대로 설치되었으면 실행이 가능합니다.  
**다만 윈도우 기준으로 제작되어 일부 기능이 제대로 동작하지 않을 수 있습니다.**

```
requirement : Python >=3.9
```

```
git clone https://github.com/pgh268400/NWebtoon_Downloader.git && cd "$(basename "$_" .git)"; #clone and auto change directory
pip3 install -r requirements.txt
python3 main.py #or python main.py;
```
위 코드를 이용해서 코드를 실행해볼 수 있습니다.



## ⛔Warning
웹툰을 받고 반드시 소장용으로만 사용해주세요.  
웹툰의 경우 엄연한 저작물이기에 무단배포시 법적 처벌을 받을 수 있습니다.  
**본 프로그램은 프로그램 사용시 발생하는 법적 문제에 대해 일절 책임을 지지 않습니다. (면책 조항)**
