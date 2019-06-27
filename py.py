#Work with Python 3.7.3
import asyncio, discord, datetime, logging, random, traceback, time, os, openpyxl, json
import sys, bs4, urllib, urlopen, youtube_dl, urllib.request
from discord.ext import commands
from discord import Member
from selenium import webdriver
from urllib.request import urlopen, Request

app = discord.Client()

countG = 0
players = {}
queues= {}
musiclist=[]
mCount=1
searchYoutube={}
searchYoutubeHref={}

def check_queue(id):
    if queues[id]!=[]:
        player = queues[id].pop(0)
        players[id] = player
        del musiclist[0]
        player.start()
        
@app.event
async def on_ready():
    print('Logged in as')
    print(app.user.name)
    print(app.user.id)
    print('===============')
    game = discord.Game("배돌이에게 !안녕이라  인사해보렴")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.event
async def on_message(message):

    if message.content.startswith("!안녕"):
        await message.channel.send("안녕?")
    if message.content.startswith("!도와줘"):
        await message.channel.send("***명령어 목록***")
        await message.channel.send("============")
        await message.channel.send("**안녕? 난 뉴 배돌이라고 해. 너희들과 대화를 나눠보고 싶어.")
        await message.channel.send("============")
        await message.channel.send("**!도와줘 = 배돌이가 명령어 목록창을 보여줍니다. ")
        await message.channel.send("**!컴퓨터는? = 똑똑한 배돌이가 제일 믿음직한 업체를 선별해 드립니다!")
        await message.channel.send("**!커뮤니티 웹사이트 추천 = 배돌이가 커뮤니티 웹사이트 TOP 3를 선별하여 리스트를 보여줍니다.")
        await message.channel.send("============")
        await message.channel.send("**!볼 만한 유튜버 추천 = 배돌이가 괜찮은 유튜버를 엄격히 선별하여 정확히 3명을 추천 합니다.")
        await message.channel.send("**!모바일 게임 추천 = 배돌이가 모바일 게임을 TOP 3로 분류하여 정확히 3개의 게임들을 추천 합니다.")
        await message.channel.send("**!자기소개 = 배돌이가 자기 소개를 해줍니다.")
        await message.channel.send("============")
        await message.channel.send("**!PC 게임 추천 = 배돌이가 엄선된 정보를 가지고 정확히 3개의 게임을 추천 합니다.")
        await message.channel.send("**!패치노트 = 배돌이 프로젝트의 패치노트가 궁금하신분들 위해 준비했습니다.")
    if message.content.startswith("!컴퓨터는?"):
        await message.channel.send("컴맹들을 위한 천국, 컴퓨존이지!")
    if message.content.startswith("!커뮤니티 웹사이트 추천"):
        await message.channel.send("***TOP 3***")
        await message.channel.send("1위는 네덕 급식들이 판치는 네이버 카페 입니다!")
        await message.channel.send("2위는 대한민국에서 현존하는 제일 큰 커뮤니티인 디시인사이드 입니다!")
        await message.channel.send("3위는 대한민국에서 다소 부정적인 인식을 가지고 있는 게임 커뮤니티, 인벤 입니다!")
        await message.channel.send("위 리스트에 올라온 커뮤니티 웹사이트들은 그나마 클-린한 웹사이트만을 엄격히 선별하여 골랐습니다.")
    if message.content.startswith("!볼 만한 유튜버 추천"):
        await message.channel.send("1위는 배틀그라운드 스트리머 및 유튜버이신 군림보님 입니다")
        await message.channel.send("2위는 종합게임 스트리머 및 유튜버이신 김재원님 입니다")
        await message.channel.send("3위는 iT 관련 제품들을 리뷰해주시거나 그 관련 기능들을 자세히 설명해주시는 유튜버 잇섭님 입니다")
    if message.content.startswith("!모바일 게임 추천"):
        await message.channel.send("***TOP 3***")
        await message.channel.send("1위는 클래시 오브 클랜 입니다")
        await message.channel.send("2위는 이제 모바일에서도 배틀그라운드!, 배틀그라운드 모바일 입니다")
        await message.channel.send("3위는 없습니다;;")
    if message.content.startswith("!자기소개"):
        await message.channel.send("안녕? 난 배돌이란다.")
        await message.channel.send("너희들이 디스코드 서버를 잘 이용할 수 있도록 ")
        await message.channel.send("뒤에서 도와주는 디스코드 PUBG MOBILE GLOBAL 서버 한정 어시스턴트야.")
        await message.channel.send("내가 주 업무를 맡는 시간대는 주로 금요일부터 일요일 였으나 2019년 6월 27일 드디어 월요일부터 일요일까지 업무를 맡을 수 있게되었어..")
        await message.channel.send("그런데, 그것도 나의 보스가 호스팅을 끊어버린다면 제대로 할수가 없게 되지....")
        await message.channel.send("============")
        await message.channel.send("============")
        await message.channel.send("============")
        await message.channel.send("자, 이제 이 정도면 됐지?")
    if message.content.startswith("!PC 게임 추천"):
        await message.channel.send("***TOP 3***")
        await message.channel.send("1위는 새로운 영웅은 언제나 환영이야~, 오버워치 입니다.")
        await message.channel.send("2위는 이겼닭! 오늘 저녁은 치킨이닭!, 배틀그라운드 입니다.")
        await message.channel.send("3위는 소환사의 협곡에 오신 것을 환영합니다. , 리그 오브 레전드 입니다.")
    if message.content.startswith("!패치노트"):
        await message.channel.send("*2019년 01월 배돌이 프로젝트 개발 시작!")
        await message.channel.send("*2019년 06월 01일 갑작스런 사태로 컴퓨터에 저장해놓은 프로젝트 파일이 사라짐.")
        await message.channel.send("*2019년 06월 02일부터 배돌이 프로젝트 기반의 뉴 배돌이 베타 0.0.1을 개발 시작!")
        await message.channel.send("*0.0.2 : 명령어 목록 작성, 일부 에러 구문 수정! ")
        await message.channel.send("*0.0.3 : 일부 에러 구문 수정, 일부 명령어 추가! ")
        await message.channel.send("*0.0.4 : 2019년 06월 27일 목요일, 배돌이봇 호스팅 시작! ")
        
    if message.content.startswith("!들어와"):
        channel = message.author.voice.voice_channel
        server = message.server
        voice_client = app.voice_app_in(server)
        print("들어와")
        print(voice_app)
        print("들어와")
        if voice_app== None:
            await app.send_message(message.channel, '*봇이 서버에 접속했습니다.') 
            await app.join_voice_channel(channel)
        else:
            await app.send_message(message.channel, '* ERROR 404 :: 봇이 이미 들어와있는 상태입니다.) 

    if message.content.startswith("!나가"):
            server = message.server
            voice_app = app.voice_app_in(server)
            print("나가")
            print(voice_app)
            print("나가")
            if voice_app == None:
                await app.send_message(message.channel,'봇이 음성채널에 접속하지 않았습니다.') 
                pass
            else:
                await app.send_message(message.channel, '*봇이 서버를 떠났습니다.') 
                await voice_app.disconnect()

    if message.content.startswith("!재생"):

        server = message.server
        voice_app = client.voice_app_in(server)
        msg1 = message.content.split(" ")
        url = msg1[1]
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
        print(player.is_playing())
        players[server.id] = player
        await app.send_message(message.channel, embed=discord.Embed(description="노래를 재생하겠습니다."))
        print(player.is_playing())
        player.start()

    if message.content.startswith("!일시정지"):
        id = message.server.id
        await app.send_message(message.channel, embed=discord.Embed(description="노래를 일시정지 합니다."))
        players[id].pause()

    if message.content.startswith("!다시재생"):
        id = message.server.id
        await app.send_message(message.channel, embed=discord.Embed(description="노래를 다시 재생하겠습니다."))
        players[id].resume()

    if message.content.startswith("!멈춰"):
        id = message.server.id
        await app.send_message(message.channel, embed=discord.Embed(description="노래를 완전히 멈추겠습니다."))
        players[id].stop()
        print(players[id].is_playing())

    if message.content.startswith('!예약'):
        msg1 = message.content.split(" ")
        url = msg1[1]
        server = message.server
        voice_app = app.voice_client_in(server)
        player = await voice_app.create_ytdl_player(url, after=lambda: check_queue(server.id))
        print(player)

        if server.id in queues:
            queues[server.id].append(player)
            print('if 1 '+str(queues[server.id])) #queues배열 확인
        else:
            queues[server.id] = [player] #딕셔너리 쌍 추가
            print('else 1' + str(queues[server.id]))#queues배열 확인
        await app.send_message(message.channel,'예약 완료\n')
        musiclist.append(url) #대기목록 링크


    if message.content.startswith('!대기목록'):

        server = message.server
        msg1 = message.content.split(" ")
        mList = msg1[1]
        num = 0
        bSize = len(musiclist)

        if mList =='보기':
            embed = discord.Embed(
                title='대기중인 곡 들',
                description='대기중.....',
                colour=discord.Colour.blue()
            )
            for i in musiclist:
                print('예약리스트 : ' + i)
                embed.add_field(name='대기중인 곡', value=i, inline=False)
            await app.send_message(message.channel, embed=embed)

        if mList =='취소':
            while num<bSize:
                del musiclist[0]
                num = num+1

            del queues[server.id]
            await app.send_message(message.channel,'현재 예약중인 음악의 목록들을 전부 취소합니다.')

        #if message.content.startswith('!'):
        
@app.event
async def my_background_task():
    await app.wait_until_ready()
    channel = discord.Object(id="585087748952817665")
    while not app.is_closed:
        await app.message.channel.send( "용병님들! 요즘 배틀그라운드 모바일을 너무 멀리하시는 것 같아요 ㅠㅜ")
        await app.message.channel.send( "공부도 좋지만 가끔은 이러고 노는게 더 정신건강에 좋답니다 ㅎㅎ")
        await app.message.channel.send( "빨리 접속하세요!!")
        await asyncio.sleep(60*60*24) 

@app.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신것을 환영합니다., {0.mention} 님'
    channel = member.server.get_channel("585087748952817665")
    await app.message.channel.send( fmt.format(member, member.server))
 
@app.event
async def on_member_remove(member):
    channel = member.server.get_channel("585087748952817665")
    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
    await app.message.channel.send( fmt.format(member, member.server))

@app.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신걸 환영합니다, {0.mention} 님'
    channel = member.server.get_channel("585087748952817665")
    await app.message.channel.send(fmt.format(member, member.server))
    await app.message.send(member, "안녕? 난 뉴 배돌이야.")
    await app.message.send(member, "뭐 궁금한 점이 있으면 나한테 물어봐.")
    await app.message.send(member, "내가 알려줄 수 있는 범위 안에서 최선을 다해 알려줄테니까.")
    await app.message.send(member, "아 참! 우리 서버에 들어온 것을 환영해~")


accross_token = os.environ["BOT_TOKEN"]
app.loop.create_task(my_background_task())
app.run(accross_token)
