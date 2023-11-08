import discord
 
TOKEN = '**'
CHANNEL_ID = '**'

class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.champion_decks = {
            '7 빌지워터 닐라': ['그레이브즈', '일라오이', '트페', '노틸러스', '미스 포춘', '닐라', '자르반','갱플랭크'],
            '7 데마시아 케일': ['뽀삐', '케일', '갈리오', '소나', '퀸', '쉔', '자르반', '피오라'],
            '8 공허 카이사': ['말자하', '초가스', '카사딘', '렉사이', '벨코즈', '카이사', '피오라', '벨베스'],
            '6 난동꾼 초가스': ['레넥톤', '밀리오', '초가스', '카시오페아', '바이', '렉사이', '세주아니', '사이온'],
            '6 학살자 모데카이저' : ['케일','키아나','니코','렉사이','퀸','모데카이저','자르반','아트록스'],
            '문제가 두배 불한당':['그레이브즈','키아나','에코','카타리나'],
            '아이오니아 애쉬':['진','애쉬','세트','카르마','나서스','닐라','쉔','자야'],
            '7 녹서스 모데카이저':['사미라','카시오페아','스웨인','다리우스','카타리나','모데카이저','아지르','사이온','아트록스'],
            '6 슈리마 아지르':['카시오페아','나피리','탈리야','소나','나서스','아지르','자르반','아트록스','크샨테']
        }

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(status=discord.Status.online, activity=discord.Game("대기중"))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content == 'ping':
            await message.channel.send('pong {0.author.mention}'.format(message))
        else:
            answer = self.get_answer(message.content)
            await message.channel.send(answer)

    def find_decks_with_champion(self, champion):
        found_decks = []
        for deck, champions in self.champion_decks.items():
            if champion in champions:
                found_decks.append(deck)
        return found_decks

    def get_answer(self, text):
        champion = text.strip()
        found_decks = self.find_decks_with_champion(champion)

        if found_decks:
            return f'{champion}의 추천 덱 : {", ".join(found_decks)}'
        else:
            return f'{champion}은(는) 망한 것 같습니다 ..'

 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents)
client.run(TOKEN)

