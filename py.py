#Work with Python 3.7.3
import asyncio, discord, datetime, logging, random, traceback, time, os
from discord.ext import commands

app = discord.Client()

token = "NTM4MzE2NTIzNTcyNDI4ODAz.XPKR5w.P3AB2-rn6DnFqIoDkzFrAwUqOQg"

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
    if message.content.startswith("!컴퓨터는?"):
        await message.channel.send("컴맹들을 위한 천국, 컴퓨존이지!")
    if message.content.startswith("!커뮤니티 웹사이트 추천"):
        await message.channel.send("***TOP 3***")
        await message.channel.send("1위는 디시인사이드 입니다!")
        await message.channel.send("2위는 Superopennet 입니다!")
        await message.channel.send("3위는 대한민국에서 다소 부정적인 인식을 가지고 있는 게임 커뮤니티, 인벤 입니다!")
        await message.channel.send("위 리스트에 올라온 커뮤니티 웹사이트들은 그나마 클-린한 웹사이트만을 엄격히 선별하여 골랐습니다.")
    if message.content.startswith("!볼 만한 유튜버 추천"):
        await message.channel.send("1위는 배틀그라운드 스트리머 및 유튜버이신 군림보님 입니다")
        await message.channel.send("2위는 종합게임 스트리머 및 유튜버이신 김재원님 입니다")
        await message.channel.send("3위는 iT 관련 제품들을 리뷰해주시거나 그 관련 기능들을 자세히 설명해주시는 유튜버 잇섭님 입니다")
    if message.content.startswith("!모바일 게임 추천"):
        await message.channel.send("***TOP 3***")
        await message.channel.send("1위는 배틀그라운드 모바일 입니다")
        await message.channel.send("2위는 하루종일 이라도 게임 할 수 있어!, 마블 퓨처파이트 입니다.")
        await message.channel.send("3위는 펜타스톰 입니다")
    if message.content.startswith("!자기소개"):
        await message.channel.send("안녕? 난 배돌이란다.")
        await message.channel.send("너희들이 디스코드 서버를 잘 이용할 수 있도록 ")
        await message.channel.send("뒤에서 도와주는 디스코드 PUBG モバイル 서버 한정 어시스턴트야.")
        await message.channel.send("내가 주 업무를 맡는 시간대는 주로 금요일부터 일요일 까지란다.")
        await message.channel.send("그런데, 그것도 나의 보스가 허락하지 않는다면 수행하지도 못해..")
        await message.channel.send("============")
        await message.channel.send("============")
        await message.channel.send("============")
        await message.channel.send("자, 이제 이 정도면 됐지?")
    if message.content.startswith("!PC 게임 추천"):
        await message.channel.send("***TOP 3***")
        await message.channel.send("1위는 새로운 영웅은 언제나 환영이야~, 오버워치 입니다.")
        await message.channel.send("2위는 이겼닭! 오늘 저녁은 치킨이닭!, 배틀그라운드 입니다.")
        await message.channel.send("3위는 소환사의 협곡에 오신 것을 환영합니다. , 리그 오브 레전드 입니다.")

@app.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신것을 환영합니다., {0.mention} 님'
    channel = member.server.get_channel("채널 아이디")
    await message.channel.send(channel, fmt.format(member, member.server))
 
@app.event
async def on_member_remove(member):
    channel = member.server.get_channel("채널 아이디")
    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
    await app.message.channel.send(channel, fmt.format(member, member.server))

@app.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신걸 환영합니다, {0.mention} 님'
    channel = member.server.get_channel("채널 아이디")
    await app.message.channel.send(channel, fmt.format(member, member.server))
    await app.message.channel.send(member, "안녕? 난 뉴 배돌이야.")
    await app.message.channel.send(member, "뭐 궁금한 점이 있으면 나한테 물어봐.")
    await app.message.channel.send(member, "내가 알려줄 수 있는 범위 안에서 최선을 다해 알려줄테니까.")
    await app.message.channel.send(member, "아 참! 우리 서버에 들어온 것을 환영해~")


accross_token = os.environ["BOT_TOKEN"]
app.run(accross_token)
