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
    fmt = '{1.name} 서버에 온 것을 진심으로 환영합니다 {0.mention} 님'
    channel = member.server.get_channel("585087748952817665")
    await app.message.channel.send( fmt.format(member, member.server))
    await app.message.channel.send(member, "안녕? 난 뉴 배돌이야.")
    await app.message.channel.send(member, "뭐 궁금한 점이 있으면 나한테 물어봐.")
    await app.message.channel.send(member, "내가 알려줄 수 있는 범위 안에서 최선을 다해 알려줄테니까.")
    await app.message.channel.send(member, "아 참! 우리 서버에 들어온 것을 환영해~")
 
@app.event
async def on_member_remove(member):
    channel = member.server.get_channel("585087748952817665")
    fmt = '{0.mention} 님이 서버를 떠나셨습니다'
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
        embed = discord.Embed(title="  ", description=" 안녕? 난 뉴 배돌이야. 너희들과 대화를 나눠보고 싶어.", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 명령어 목록 ", description=" ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !안녕 ", description=" 배돌이가 인사를 해줍니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !도와줘 ", description=" 배돌이가 명령어 목록을 불러옵니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !컴퓨터는? ", description=" 배돌이가 믿음직한 컴퓨터 업체들을 선별해드립니다 (광고 X) ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !커뮤니티 웹사이트 추천 ", description=" 배돌이가 괜찮은 커뮤니티 사이트를 추천해줍니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !볼 만한 유튜버 추천 ", description=" 배돌이가 괜찮은 유튜버를 추천해줍니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !모바일 게임 추천 ", description=" 배돌이가 현재 흥행하는 모바일 게임을 추천해줍니다 (광고 X)", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !자기소개 ", description=" 배돌이가 자기소개를 해줍니다", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !PC 게임 추천 ", description=" 배돌이가 현재 흥행하는 PC 게임을 추천해줍니다", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !언어 ", description=" 배돌이가 무슨 언어를 기반으로 개발되어지고 있는지 알려줍니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !오늘 내 생일이야 ", description=" 배돌이가 생일을 축하해줍니다", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !랜덤주사위 ", description=" 배돌이가 랜덤으로 주사위를 굴려줍니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !오늘뭐할까 ", description=" 배돌이에게 오늘 하루 할 일을 정해달라고 물어보세요!", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !내쪽지 ", description=" 배돌이가 그동안 너에게 쪽지를 보내왔다는 사실을 알고 있니? ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" !패치노트 ", description=" 배돌이가 자신의 패치노트를 불러옵니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *명령어 목록은 계속 업데이팅 중 입니다. ", description="  ", color=0xff0000)
        await message.channel.send( embed=embed)
        
    if message.content.startswith("!안녕"):
        msg = "{0.author.mention} 안녕?? 반가워, 그동안 잘 지냈니.".format(message)
        await message.channel.send( msg)
        
    if message.content.startswith("!컴퓨터는?"):
        randomNum = random.randrange(1, 4)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="혹시 너 it 관련 정보도 부족하고, 조립 및 A/S가 두렵니? 그렇다면, 컴퓨존을 추천해줄께", color=0x00ff00))
            await message.channel.send(embed=discord.Embed(title="컴퓨존은 1991년 노인호 대표와 김태선 대표가 '태인시스템'이라는 회사를 설립하고 출발한 기점으로", color=0x00ff00))
            await message.channel.send(embed=discord.Embed(title="1999년 '컴퓨존'으로 상호를 변경하고 아직까지 그 명성을 이어나가고 있는 컴퓨터 및 각종 전자기기 판매 업체야.", color=0x00ff00))
            await message.channel.send(embed=discord.Embed(title="국내 컴퓨터 조립 업계 1위라고 불릴 만큼 국내 컴퓨터 판매 쇼핑몰 업계중에 규모가 가장 크고, 독보적인 지위를 차지하고 있지.", color=0x00ff00))
            await message.channel.send(embed=discord.Embed(title="하지만 근무환경이나 A/S 등 여러 방면에서 전현직 직원들의 평은 대단히 좋지 않더라. 뭐 완벽한 회사는 없잖아..?", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="컴퓨터에 대한 정보가 부족한데, 컴퓨터는 사고 싶다고? 그러면 다나와를 추천해줄께.", color=0x0000ff))
            await message.channel.send(embed=discord.Embed(title="2000년부터 온라인 가격비교 서비스를 제공하는 대한민국의 사이트. (주)다나와에서 운영하고 있지.", color=0x0000ff))
            await message.channel.send(embed=discord.Embed(title="가장 많은 업체들이 참여한 규모의 경제를 이룬 상태이기 때문에 ", color=0x0000ff))
            await message.channel.send(embed=discord.Embed(title="가격 비교가 실 구매시에 상당히 정확하며, 특히 현재 시장에서 인지도가 높은 상품들을 비교하기 좋아.", color=0x0000ff))
            await message.channel.send(embed=discord.Embed(title="전자제품, 특히 컴퓨터 부품을 기반으로 성장한 사이트이다보니 검색필터가 상당히 자세하고 정확하다는 장점이 매우 크지.", color=0x0000ff))
        
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="컴마왕은 추천하고 싶지가 않네...", color=0xff0000))
            await message.channel.send(embed=discord.Embed(title="단순히 컴퓨터에 대한 지식이 없고, 그냥 비싼게 최고라고 생각하면 여기서 알아보는게 정확하단다...", color=0xff0000))
            await message.channel.send(embed=discord.Embed(title="가서 주변 컴잘알들에게 물어보렴, 컴마왕 어떻게 생각하냐고.", color=0xff0000))
            await message.channel.send(embed=discord.Embed(title="참고로 듣보잡 업체들 특징이 뭔지 아니? 스트리머 및 유튜버들에게 광고를 부탁한다는 점이야. ", color=0xff0000))
            
    if message.content.startswith("!커뮤니티 웹사이트 추천"):
        randomNum = random.randrange(1, 4)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="네이버 카페는 어떠니", color=0x0000ff))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="디시인사이드는 어때??", color=0x0000ff))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="인벤은 해볼 생각 없어?", color=0x0000ff))

    if message.content.startswith("!볼 만한 유튜버 추천"):
        randomNum = random.randrange(1, 11)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="배틀그라운드, 오버워치 스트리머 및 유튜버이신 군림보님은 어떠니", color=0xff0000))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="종합게임 스트리머 및 유튜버이신 김재원님은 괜찮지 않니?", color=0xff0000))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="IT 제품들을 리뷰 및 설명해주시는 잇섭님은 볼 생각 들지 않니?", color=0xff0000))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="보겸은 어떠니?", color=0xff0000))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="배틀그라운드 스트리머 및 유튜버인 김블루는 어때?", color=0xff0000))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="하이톤의 목소리가 매력이신 배틀그라운드 스트리머 및 유튜버인 연다는??", color=0xff0000))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="항상 재밌는 카톡썰들을 보여주시는 오늘의카톡은??", color=0xff0000))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="데이터베이스 오류! 명령어를 다시 입력하세요,,,", color=0xfefe00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="죄송해요,, 이해를 하지 못했어요, 다시 명령어를 입력해주시겠어요...?", color=0xfefe00))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="영화 리뷰어이신 홍시네마님은?", color=0xff0000))
        
    if message.content.startswith("!모바일 게임 추천"):
        randomNum = random.randrange(1, 6)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="클래시 오브 클랜은 어떠니?", color=0x0000ff))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="배틀그라운드 모바일은 어때??", color=0x0000ff))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="펜타스톰은 해볼 생각 없어?", color=0x0000ff))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="마인크래프트 해보지 그래? ㅋㅋㅋ", color=0x0000ff))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="마블 퓨처 파이트 해봐, 추억의 게임이잖니", color=0x0000ff))
        
    if message.content.startswith("!자기소개"):
        embed = discord.Embed(title=" 안녕, 난 뉴 배돌이야.  ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 너희들이 디스코드 서버를 잘 이용할 수 있도록  ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 도와주는 디스코드 서버 한정 어시스턴트야. ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 내 이름의 뜻은 ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" [제 2의 배돌이 프로젝트] 의 줄인말이야 ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" [ (제 2의) 배돌이 프로젝트] 는 전세계 배틀그라운드, 배틀그라운드 모바일 유저들을 위한 프로젝트 였지, 지금은 아니지만. ", description="", color=0x227799)
        await message.channel.send(embed=embed)
        msg = "널 또 보길 바랄께, 나중에 보자. {0.author.mention} ".format(message)
        await message.channel.send( msg)
        
    if message.content.startswith("!PC 게임 추천"):
        randomNum = random.randrange(1, 10)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="배틀그라운드는 어떠니", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="오버워치는 어때??", color=0x00ff00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="리그 오브 레전드는 해볼 생각 없어?", color=0x00ff00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="월드 오브 탱크는?", color=0x00ff00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="히어로즈 오브 더 스톰은 해볼 생각 없어?", color=0x00ff00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="서든어택은???", color=0x00ff00))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="마인크래프트는 어떠니?", color=0x00ff00))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="피파 온라인 4는 꽤 재밌어보이던데.", color=0x00ff00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="GTA5도 한번 시작해봐, 꽤 재밌어.", color=0x00ff00))

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
        embed = discord.Embed(title=" *0.0.7 ", description=" 2019년 06월 30일 일요일, 생일 축하 기능과 랜덤주사위 기능 업데이트!", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.8 ", description=" 2019년 07월 05일 금요일, 이제 배돌이에게 조언을 받아보실 수 있습니다. 지금 당장 체험해보세요.", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.0.9 ", description=" 2019년 07월 05일 금요일, 일부 Ui 수정!", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" *0.1.0 ", description=" 2019년 07월 05일 금요일, 이제 배돌이가 너희에게 하고싶은 말들을 보내줄 수 있단다!", color=0x00fefe)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" ", description=" ***패치노트는 계속 업데이트 할 예정입니다 ^00^ ", color=0x00fefe)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!내쪽지"):
        await message.channel.send(embed=discord.Embed(title="배돌이가 너희에게 보낸 쪽지들이야. 무작위로 확인할 수 있어", color=0xfefefe))
        randomNum = random.randrange(1, 4)
        if randomNum==1:
            await message.channel.send("@everyone")
            await message.channel.send(embed=discord.Embed(title="배틀그라운드 모바일을 접속해야되.", color=0xffaaaa))
            await message.channel.send(embed=discord.Embed(title="어차피 삶은 영원하지 않아.", color=0xffaaaa))
            await message.channel.send(embed=discord.Embed(title="지금 당장 접속하지 않으면", color=0xffaaaa))
            await message.channel.send(embed=discord.Embed(title="큰코다칠줄 알아라.", color=0xffaaaa))
        if randomNum==2:
            await message.channel.send("@everyone")
            await message.channel.send(embed=discord.Embed(title="가서 영화라도 한편 보고 와.", color=0xaaaaff))
            await message.channel.send(embed=discord.Embed(title="가끔은 이런 일탈도 나쁘지 않지.", color=0xaaaaff))
        if randomNum==3:
            await message.channel.send("@everyone")
            await message.channel.send(embed=discord.Embed(title="오늘 하루는 잘 보냈니. 죽은건 아니지?", color=0xaaffaa))
        
    if message.content.startswith("!언어"):
        embed = discord.Embed(title="안녕? 난 뉴 배돌이야. ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="지금부터 내가 무슨 언어를 기반으로 개발되어지고 있는지 알려줄께. ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 우선 나는 PYTHON3으로 개발되고 있어. ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 기본적인 기능들을 구현하기에는 적합한 언어지. 우선 내 개발자는 전문가가 아니거든.", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" PYTHON 은 1991년 프로그래머인 귀도 반 로섬(Guido van Rossum)이 발표한 고급 프로그래밍 언어로, ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed) 
        embed = discord.Embed(title=" 플랫폼 독립적이며 인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 대화형 언어로 많이 알려져 있어.", description=" ", color=0xaaaaff)                      
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 특히, 파이썬이라는 이름은 귀도가 좋아하는 코미디 〈Monty Python's Flying Circus〉에서 따온 것이야.", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 재미있는 사실은 1989년 크리스마스 주에, 연구실이 닫혀있어서 그저 심심해서 만든 작품이 파이썬이라는게 .. ", description=" ", color=0xaaaaff)
        await message.channel.send(embed=embed)
      
    if message.content.startswith('!오늘 내 생일이야'):
        msg = "{0.author.mention} 생일 축하해 !!".format(message) #그냥 자축 기능. 개발자가 외로운 솔로라 만들어본 기능.
        await message.channel.send( msg)
        
    if message.content.startswith("!랜덤주사위"):
        randomNum = random.randrange(1, 7) 
        print(randomNum)
        if randomNum == 1:
            await message.channel.send( embed=discord.Embed(description=':game_die: '+ ':one:',color=0xfefe00))
        if randomNum == 2:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':two:',color=0xfefe00))
        if randomNum ==3:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':three:',color=0xfefe00))
        if randomNum ==4:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':four:',color=0xfefe00))
        if randomNum ==5:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':five:',color=0xfefe00))
        if randomNum ==6:
            await message.channel.send( embed=discord.Embed(description=':game_die: ' + ':six: ',color=0xfefe00))
        
    if message.content.startswith('!오늘뭐할까'):
        randomNum = random.randrange(1, 16)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="그냥 아무것도 하지않는게 더 났지 않을까?", color=0xfe00fe))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="그냥 잠이나 충분히 자는게 더 나을듯 해", color=0xfe00fe))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="공부하는 것도 나쁘지 않을거야", color=0xfe00fe))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="영화 한편보는 건 어때?", color=0xfe00fe))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="신책하는 것도 나쁘지 않을텐데, 가벼운 산책은 머리를 맑게 해줘.", color=0xfe00fe))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="미쳤니? 이 날씨에?! 그냥 집에서 게임이나 하는게 현명한 선택이야.", color=0xfe00fe))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="부모님한테 효도라도 해볼 생각은 없니? 안마라도 해드려.", color=0xfe00fe))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="하나님한테 기도드려봐. 해결될거야.", color=0xfe00fe))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="정말 한가하다.. 너 시간 많나보다? 기억해. 너는 한낱 인간이고, 삶은 영원하지 않다고.", color=0xfe00fe))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="솔직히 말해봐. 너 지금 모태솔로지?", color=0xfe00fe))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="문화생활이라도 즐겨봐. 너 그러다 병나. 여기다 물어볼 정도면 넌 심각해", color=0xfe00fe))
        if randomNum==12:
            await message.channel.send(embed=discord.Embed(title="넌 좋아하는 취미가 뭐니? 좋아하는 취미를 즐기면서 지금 이 시간을 즐겨.", color=0xfe00fe))
        if randomNum==13:
            await message.channel.send(embed=discord.Embed(title="너 정말 모태솔로 아닌거 확실해? 커플들은 보통 여기서 물어보지 않는단다;;", color=0xfe00fe))
        if randomNum==14:
            await message.channel.send(embed=discord.Embed(title="데이터베이스 오류! 치명적인 오류 발생!! 다시 명령어를 입력하세요...", color=0xff0000))
        if randomNum==15:
            await message.channel.send(embed=discord.Embed(title="헬스장이라도 가봐. 건강은 자기자신이 챙기는거다.?!", color=0xfe00fe))
            
    
   

accross_token = os.environ["BOT_TOKEN"]
app.loop.create_task(my_background_task())
app.run(accross_token)
