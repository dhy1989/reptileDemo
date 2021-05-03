import requests
import subprocess

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}


def send_request(url):
    response = requests.get(url=url, headers=headers)
    return response


def merge_data(video_name):
    print('视频合成开始:', video_name)
    # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4
    command = f'ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental E:/output.mp4'
    subprocess.Popen(command,shell=True)
    print('视频合成结束:', video_name)


audio_url = 'https://v9-xg-web-s.ixigua.com/14a35e9641c0619d6c25ca10f4bec0b3/60460661/video/tos/cn/tos-cn-vd-0026/0276904094d44a25b27970271145ecc9/media-audio-und-mp4a/?a=1768&br=0&bt=0&cd=0%7C0%7C0&ch=0&cr=0&cs=0&cv=1&dr=0&ds=&er=0&l=2021030817592401014406101901014EA6&lr=default&mime_type=video_mp4'
video_url = 'https://v9-xg-web-s.ixigua.com/382192da39bc44ba59e3b813b3948cc7/60460661/video/tos/cn/tos-cn-vd-0026/0276904094d44a25b27970271145ecc9/media-video-avc1/?a=1768&br=1920&bt=480&cd=0%7C0%7C0&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=0&l=2021030817592401014406101901014EA6&lr=default&mime_type=video_mp4';
#
# audio_data = send_request(audio_url).content
# video_data = send_request(video_url).content
name = '八段锦';
# with open(name + '.mp3', mode='wb') as f:
#     f.write(audio_data)
#     print('正在保存音频数据')
# with open(name + '.mp4', mode='wb') as f:
#     f.write(video_data)
#     print('正在保存视频数据')
merge_data(name)
