#Work with Python 3.7.3
import asyncio, discord, datetime, logging, random, traceback, time, os
from discord.ext import commands

app = discord.Client()


@app.event
async def on_ready():
    print('로그인 중 입니다 ..!')
    print(app.user.name)
    print(app.user.id)
    print('===============')
    game = discord.Game("배돌이에게 !도와줘라고 도움을 요청해보렴!")
    await app.change_presence(status=discord.Status.online, activity=game)
    
@app.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신것을 환영합니다., {0.mention} 님'
    channel = member.server.get_channel("585087748952817665")
    await app.message.channel.send( fmt.format(member, member.server))
    await app.message.channel.send(member, "안녕? 난 뉴 배돌이야.")
    await app.message.channel.send(member, "뭐 궁금한 점이 있으면 나한테 물어봐.")
    await app.message.channel.send(member, "내가 알려줄 수 있는 범위 안에서 최선을 다해 알려줄테니까.")
    await app.message.channel.send(member, "아 참! 우리 서버에 들어온 것을 환영해~")
 
@app.event
async def on_member_remove(member):
    channel = member.server.get_channel("585087748952817665")
    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
    await app.message.channel.send( fmt.format(member, member.server))
          
@app.event
async def my_background_task():
    await app.wait_until_ready()
    channel = discord.Object(id="585087748952817665")
    while not app.is_closed:
        await app.message.channel.send( "배틀그라운드 모바일을 멀리하지마세요, 공부를 멀리하세요.")
        await asyncio.sleep(60*60*24) 

        
@app.event
async def on_message(message):

    if message.content.startswith("!도와줘"):
        embed = discord.Embed(title="  ", description=" *안녕? 난 뉴 배돌이라고 해. 너희들과 대화를 나눠보고 싶어. ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 명령어 목록 ", description=" ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !안녕 ", description=" 배돌이가 인사를 해줍니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !도와줘 ", description=" 배돌이가 명령어 목록을 불러옵니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !컴퓨터는? ", description=" 배돌이가 믿음직한 컴퓨터 업체를 선별해드립니다 (광고 X) ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !커뮤니티 웹사이트 추천 ", description=" 배돌이가 괜찮은 커뮤니티 사이트 3개를 추천해줍니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !볼 만한 유튜버 추천 ", description=" 배돌이가 괜찮은 유튜버 3명을 추천해줍니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !모바일 게임 추천 ", description=" 배돌이가 현재 흥행하는 모바일 게임 3개를 추천해줍니다 (광고 X)", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !자기소개 ", description=" 배돌이가 자기소개를 해줍니다", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !PC 게임 추천 ", description=" 배돌이가 현재 흥행하는 PC 게임 3개를 추천해줍니다", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !언어 ", description=" 배돌이가 무슨 언어를 기반으로 개발되어지고 있는지 알려줍니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !패치노트 ", description=" 배돌이가 자신의 패치노트를 불러옵니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *명령어 목록은 계속 업데이팅 중 입니다. ", description="  ", color=0xff0000)
        await message.channel.send( embed=embed)
        
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕? ")      
    if message.content.startswith("!컴퓨터는?"):
        embed = discord.Embed(title=" 컴퓨존 ", description=" 일반인들을 위한 천국, 컴퓨존입니다.. ", color=0x0000ff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 컴마왕에서 구매하실 분들은 대게 이런 분들 입니다. ", description=" 스트리머, 유튜버, 프로게이머, ;;; 방구석 엠창 인생 사는 히키코모리 백수", color=0x0000ff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 컴마왕은 부품값도 시중에 유통되고 있는 부품들보다 더 올려서 판매합니다. ", description=" 전형적인 장사꾼들입니다. 일반인들은 이걸 알리가 없죠... ", color=0x0000ff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" it 정보에는 초짜에 해당하시는 분들은 컴퓨존으로 가세요. ", description=" 일반인들을 위한 곳은 거기밖에 없습니다. ", color=0x0000ff)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!커뮤니티 웹사이트 추천"):
        embed = discord.Embed(title=" ***TOP 3*** ", description="  ", color=0x0000ff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 1위 ", description=" *네덕 급식들이 판치는 네이버 카페 입니다! ", color=0x0000ff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 2위 ", description=" *정신병자들도 엄청 많이 판치면서 정상인들도 엄청 많이 소속되어있는 현존하는 대형 커뮤니티 중 가장 정상적인 범주에 속하는 디시인사이드 입니다. ", color=0x0000ff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 3위 ", description=" *대한민국에서 가장 사회적으로 히키코모리 취급을 받는 한남 한녀새끼들이 많이 소속되어있는 대형 게임 커뮤니티, 인벤 입니다! ", color=0x0000ff)
        await message.channel.send(embed=embed)

    if message.content.startswith("!볼 만한 유튜버 추천"):
        embed = discord.Embed(title=" ***TOP 3*** ", description="  ", color=0x997722)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 1위 ", description=" *오버워치, 배틀그라운드 스트리머 및 유튜버이신 군림보님 입니다 ", color=0x997722)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 2위 ", description=" *iT 관련 제품들을 리뷰해주시거나 그 관련 기능들을 자세히 설명및 추천해주시는 유튜버 잇섭님 입니다 ", color=0x997722)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 3위 ", description=" *오버워치 스트리머 및 유튜브에서 종합게임 스트리머로 전향하신 스트리머 및 유튜버이신 김재원님 입니다 ", color=0x997722)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!모바일 게임 추천"):
        embed = discord.Embed(title=" ***TOP 3*** ", description="  ", color=0x997722)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 1위 ", description=" *전투는 계속된다! 클래시 오브 클랜 입니다 ", color=0x997722)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 2위 ", description=" *이제 모바일에서도 배틀그라운드!, 배틀그라운드 모바일 입니다 ", color=0x997722)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 3위 ", description=" *비공식 모바일 리그오브레전드!, 펜타스톰 입니다;; ", color=0x997722)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!자기소개"):
        embed = discord.Embed(title=" 안녕? 난 뉴 배돌이야. ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 너희들이 디스코드 서버를 잘 이용할 수 있도록  ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 도와주는 디스코드 PUBG MOBILE GLOBAL 서버 한정 어시스턴트야. ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="그런데 말이야... ", description="", color=0x997722)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="난 나에 대해서 말하는 것을 별로 좋아하지 않아.. ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="이정도면 됐지?", description="", color=0x227799)
        await message.channel.send(embed=embed)

    if message.content.startswith("!PC 게임 추천"):
        embed = discord.Embed(title=" ***TOP 3*** ", description="  ", color=0x997722)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 1위 ", description=" *새로운 영웅은 언제나 환영이야~, 오버워치 입니다.. ", color=0x997722)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 2위 ", description=" *이겼닭! 오늘 저녁은 치킨이닭!, 배틀그라운드 입니다.. ", color=0x997722)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 3위 ", description=" *소환사의 협곡에 오신 것을 환영합니다. , 리그 오브 레전드 입니다.. ", color=0x997722)
        await message.channel.send(embed=embed)

    if message.content.startswith("!패치노트"):
        embed = discord.Embed(title="*2018년 12월 ", description=" 배돌이 프로젝트 구상 및 개발 시작! ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="*2019년 06월 01일 ", description=" 갑작스런 사태로 컴퓨터에 저장해놓은 프로젝트 파일이 사라짐. ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="*2019년 06월 02일 ", description=" 배돌이 프로젝트 기반의 뉴 배돌이 베타 0.0.1을 개발 시작! ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.2  ", description=" 명령어 목록 작성, 일부 에러 구문 수정! ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.3 ", description=" 일부 에러 구문 수정, 일부 명령어 추가! ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.4 ", description=" 2019년 06월 27일 목요일, 배돌이봇 호스팅 시작! ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.5 ", description=" 2019년 06월 29일 토요일, 배돌이 명령어 목록 Ui 일부 수정 및 업데이트! ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.6 ", description=" 2019년 06월 29일 토요일, 일부 Ui 수정!", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" ", description=" ***패치노트는 계속 업데이트 할 예정입니다 ^00^ ", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" ", description=" ***재밌는 기능들이 여러분들을 기다리고 있으니 기대하셔도 좋습니다 ^00^ ", color=0x00fefe)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!공지"):
        embed = discord.Embed(title=" 공지사항 ", description=" ", color=0xffaaaa)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" ", description=" 배틀그라운드 모바일을 멀리하지 마세요... ", color=0xffaaaa)
        await message.channel.send(embed=embed)  
        embed = discord.Embed(title="  ", description=" 다른 게임과 학업을 멀리하셔야 합니다... ", color=0xffaaaa)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="  ", description=" 당신들은 스트레스 받으면서 살기에는 너무 아깝고 귀한 존재에요... ", color=0xffaaaa)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 2019.06.29.토.23:29 ", description=" ", color=0xffaaaa)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!기반언어"):
        embed = discord.Embed(title=" 안녕? 난 배돌이야. ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="지금부터 내가 무슨 언어를 기반으로 개발되어지고 있는지 알려줄께. ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 우선 나는 PYTHON3으로 개발되고 있어. ", description=" ", color=0xffaaaa)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 하지만, 오직 파이썬으로만 이 모든 아이디어들을 구현하려면 너무 힘들어", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 게다가 구문자체가 가독성이 현저하게 떨어지기도 하지... ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" ㅠㅜ 이럴줄 알았으면 개발자한테 JAVA도 가르쳐볼걸 그랬어 ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        
      
        

        


accross_token = os.environ["BOT_TOKEN"]
app.loop.create_task(my_background_task())
app.run(accross_token)
