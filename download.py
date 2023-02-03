import requests


def fire(page):
    url = 'https://api-tinyvideo-web.yy.com/home/tinyvideosv2'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    for _ in range(page+1):
        response = requests.get(url=url, headers=headers)
        data = response.json()

        data_list = data['data']['data']
        # print(data_list)

        for d in data_list:
            video_title = str(d['yyNum']) + '.mp4'
            video_url = d['resurl']

            video_content = requests.get(
                url=video_url, headers=headers).content
            # 地址：更改自己存放视频位置
            with open('C:/Users/95484/Desktop/demo/YouTube/' + video_title, mode='wb') as f:
                f.write(video_content)
                print('保存完成:', video_title)


if __name__ == '__main__':
    fire(10)
