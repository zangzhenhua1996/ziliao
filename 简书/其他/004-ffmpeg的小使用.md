python调用cmd命令进行ffmpeg的分辨率转换
```python
import os
os.popen(r"ffmpeg -i 2.webm -strict -2 -vf scale=-1:1440 5.mp4 ", "r")
```

```python
1
[4K] GIRL CRUSH BOMI   '걸크러쉬 보미' 아트코리아 Star Show 190131 @ 직캠 fancam by IBIZA [2160p][video+audio]
2
[4K] 걸크러쉬 보미 (GIRL CRUSH BOMI) 성인식 & Bubble Pop 보미쇼 190214 @ 직캠 fancam by IBIZA [2160p][video+audio]
3
[4K] 걸크러쉬 '보미( Girl Crush BOMI) - 엉덩이' 아트코리아 Star Show 190131 @ 직캠  fancam by IBIZA [2160p][video+audio]
4
[4K] 걸크러쉬 보미(Girl Crush BOMI)  190706 @직캠 fancam vy IBIZA [2160p][video+audio]
5
[모바일용] [4K 60P] 20190510다이아 (DIA) 주은 - '우와' 세로 직캠 (KBS 미디어센터 심석홀 팬사인회) [2160p][video+audio]
6
[모바일용] [4K 60P] 20190512 다이아 (DIA) 주은 - 왠지 (Somehow) 세로 직캠 (일지아트홀 팬사인회) [2160p][video+audio]
7
180510 - 걸크러쉬 (Girl Crush) - 보미 - Crazy in love (REMIX) - 뉴타TV TheK호텔 직캠 [4320p][video+audio]
8
180715 나뮤 경리 솔로앨범 기념 팬싸인회 직캠(포토타임, 추첨이벤트, 끝인사 등) [4320p][video+audio]
9
190214 걸크러쉬(Girl Crush) (보미) 포토타임 + 커버공연 [4K][직캠] by pharkil [2160p][video+audio]
10
190414 다이아 팬사인회 WOOWA 우와 권은채 4K 직캠 by 스티치 [2160p][video+audio]
11
190530 걸크러쉬(GIRL CRUSH) 보미 - Memories @보미쇼 아이돌보쇼 제9회 4K 60P 직캠 Fancam by LIKEY [2160p][video+audio]
12
190706 [For Mobile] 다이아(DIA) - 우와(Woowa) ...은채 직캠(Eunchae fancam) @DMZ평화이음콘서트 (철원) [2160p][video+audio]
13
Excuse Me_ 네 얼마든지 실례해주세요! 팡예 느님 [2160p][video+audio]
14
걸크러쉬(Girl Crush) Bomi (Bubble Pop & Siren) _ 보미쇼12회 MC공연 _ 4KFC 07.06.2019 [2160p][video+audio]
15
걸크러쉬(Girl Crush) Bomi (Photo Time 2) _ 보미쇼11회 MC공연 _ 4KFC 06.27.2019 [2160p][video+audio]
16
걸크러쉬(Girl Crush) Bomi (떨려요) _ 보미쇼11회 MC공연 _ 4KFC 06.27.2019 [2160p][video+audio]
17

걸크러쉬(Girl Crush) 보미(Bomi) 24 hours _ 보미쇼2회 아이돌보쇼 MC공연 _ 4KFC 01.17.2019 [2160p][video+audio]

18
걸크러쉬(Girl Crush) 보미(Bomi) Cover Dance _  보미쇼4회 아이돌보쇼 MC공연 _ 4KFC 02.14.2019 [2160p][video+audio]
19
걸크러쉬(Girl Crush) 보미(Bomi) Joker & No More(넘어) _ 아트코리아쇼 MC공연 _ 4KFC 01.04.2019 [2160p][video+audio]
20
걸크러쉬(Girl Crush) 보미(Bomi) Photo Time(2) _  보미쇼3회 아이돌보쇼 MC공연 _ 4KFC 01.31.2019 [2160p][video+audio]
21
걸크러쉬(Girl Crush) 보미(Bomi) 넘어(No More) _ 보미쇼3회 아이돌보쇼 MC공연 _ 4KFC 01.31.2019 [2160p][video+audio]
22
다이아(DIA) (주은) 우와 @ 평화이음 토요콘서트 [철원][190706][4K][직캠] by pharkil [2160p][video+audio]

23
비글램(B.GLAM) (잇슈) 따라해봐 @ 평화이음 토요콘서트 [철원][190706][4K][직캠] by pharkil [2160p][video+audio]
```
