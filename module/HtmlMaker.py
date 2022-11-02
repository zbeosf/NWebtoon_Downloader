import os
from pathlib import Path
import chardet
from .ImageMerger import ImageMerger
from jinja2 import Template  # html 템플릿용

# 파이썬 3에서는 모든 import 문은 기본적으로 절대(absolute) import다.
# 만약 파이썬 3에서 상대 import를 사용하고 싶다면 위처럼 (.) 으로 명시적으로 표현을 해주어야 한다.
# 또한 패키지 경로의 기준은 __name__ == "__main__" 을 실행시키는 위치가 된다.
# 그러므로 해당 코드 테스트를 원하면 이 코드를 직접 실행할 것이 아닌, main.py를 실행해야 한다.
# 파이썬의 모든 import 구문은 절대 경로이다.

# ImageMerger 을 상속받아 구현


class HtmlMaker(ImageMerger):
    def __init__(self, path):
        super().__init__(path)  # 부모 생성자 호출
        self.__title = os.path.basename(path)  # 웹툰 제목

    def __read_file(self, path):
        # 파일 열어서 인코딩 확인
        rawdata = open(path, 'rb').read()
        result = chardet.detect(rawdata)
        enc = result['encoding']

        # 인코딩 맞게 열기
        f = open(path, "r", encoding=enc)
        line = f.readline()

        data = ""
        while line:
            data += line
            line = f.readline()
        f.close()
        return data

    # ImagerMerger 오버라이딩으로 구현
    # 실제 run() 이 호출해서 처리해주는 함수
    # Python __ : private, _ : protected
    def _processing(self, file_lst: list):
        try:
            rel_base_path = os.path.dirname(file_lst[0])  # 웹툰이 저장되어 있는 폴더 경로
            base_path = os.path.abspath(rel_base_path)  # 절대경로로 변환
            print("기반 경로 : ", base_path)

            # 기존에 생성한 index.html을 삭제한다.
            output_path = os.path.join(base_path, 'index.html')

            if os.path.isfile(output_path):
                os.remove(output_path)

            # html template 을 위한 데이터를 생성한다.
            episode = os.path.basename(os.path.dirname(file_lst[0]))
            episode = episode.split()[1]

            img_lst = []
            for file in file_lst:
                img_lst.append(os.path.basename(file))

            # print(img_lst)

            # template.html을 읽고, 데이터를 채운다.
            html_data = self.__read_file("./module/template.html")
            html_data = Template(html_data).render(
                title=self.__title, episode=episode, img_lst=img_lst)

            # index.html 파일을 생성한다.
            index_path = os.path.join(base_path, 'index.html')
            f = open(index_path, 'w', encoding="UTF-8")
            f.write(html_data)
            f.close()
            print(f"{index_path} 생성 완료")

        except Exception as e:
            raise e

    def make_html(self):
        self.run()  # 실제로 Processing 해주는 함수