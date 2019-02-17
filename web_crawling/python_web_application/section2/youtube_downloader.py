import pytube
import os
# Python 실행하면서 별도의 프로세스를 생성(터미널 실행 및 반환값 저장)
import subprocess

messURL = input("다운로드 받을 youtube URL을 입력해주세요.")
# 다운 받을 동영상 URL 지정
yt = pytube.YouTube(messURL)
videos = yt.streams.all()

for i in range(len(videos)):
    print(i, ' , ', videos[i])

cNum = int(input("다운로드 받을 화질을 선택해주세요."))

down_dir = "C:/Users/Chris/workspace/Pyscript/Inflearn/youtube"

videos[cNum].download(down_dir) # 0th 가장 좋은 화질

checkConvert = input("youtube 영상을 mp3로 변환하시겠습니까?[y/n]")
if checkConvert == 'y':
    newFileName = input("변환 할 mp3 파일 이름을 입력해주세요(파일명.mp3).")
    oriFileName = videos[cNum].default_filename

    subprocess.call(['ffmpeg', '-i',
        os.path.join(down_dir, oriFileName),
        os.path.join(down_dir, newFileName)
    ])
    # 주의사항: ffmpeg을 환경변수로 지정하지 않았다면, 이 python 파일을 컴파일해도 해당 커맨드 명령은 실행이 안된다.
    # 따라서, 해당 python 파일을 실행 할 폴더에 함께 둬야 정상 작동한다.
    print('Finish download and converting mp3!!')
else:
    print('Finish download your favorite video!!')


print('-End of Program-')

'''
download site: http://www.filehorse.com/download-ffmpeg-64/
Convert 기능을 많이 사용하고자 한다면, ffmpeg을 환경변수로 지정해서 사용하면 편함.
자주 사용하지 않는다면, 변환 할 파일과 같은 폴더 디렉토리에 지정.
how to use: >> ffmpeg -i [video file] [new file]
'''
