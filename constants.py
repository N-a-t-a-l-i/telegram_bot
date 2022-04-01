#!/usr/bin/python
# -*- coding: utf8 -*-


verbs_vars = [{'нАчал': 'correct', 'начАл': 'incorrect'},
              {'надорвалАсь': 'correct', 'надорвАлась': 'incorrect'},
              {'послАла': 'correct', 'послалА': 'incorrect'},
              {'сорИт': 'correct', 'сОрит': 'incorrect'},
              {'ворвалАсь': 'correct', 'ворвАлась': 'incorrect'},
              {'обогналА': 'correct', 'обогнАла': 'incorrect'},
              {'прибЫть': 'correct', 'прИбыть': 'incorrect'},
              {'бралАсь': 'correct', 'брАлась': 'incorrect'},
              {'взялАсь': 'correct', 'взЯлась': 'incorrect'},
              {'воссоздалА': 'correct', 'воссоздАла': 'incorrect'},
              {'клАла': 'correct', 'клалА': 'incorrect'},
              {'принялА': 'correct', 'прИняла': 'incorrect'},
              {'прИнял': 'correct', 'принЯл': 'incorrect'},
              {'занялА': 'correct', 'зАняла': 'incorrect'},
              {'жИться': 'correct', 'житьсЯ': 'incorrect'},
              {'обнялАсь': 'correct', 'обнЯлась': 'incorrect'},
              {'гналА': 'correct', 'гнАла': 'incorrect'},
              {'добралА': 'correct', 'добрАла': 'incorrect'},
              {'окружИт': 'correct', 'окрУжит': 'incorrect'},
              {'нарвалА': 'correct', 'нарвАла': 'incorrect'},
              {'отозвалА': 'correct', 'отозвАла': 'incorrect'},
              {'плодоносИть': 'correct', 'плодонОсить': 'incorrect'},
              {'ворвАться': 'correct', 'ворватьсЯ': 'incorrect'},
              {'добралАсь': 'correct', 'добрАлась': 'incorrect'},
              {'зАнял,': 'correct', 'занЯл,': 'incorrect'},
              {'налилА': 'correct', 'налИла': 'incorrect'},
              {'перезвонИть': 'correct', 'перезвОнить': 'incorrect'},
              {'воспринЯть': 'correct', 'воспрИнять': 'incorrect'},
              {'лИться': 'correct', 'литьсЯ': 'incorrect'},
              {'прИняли': 'correct', 'принЯли': 'incorrect'},
              {'баловАть': 'correct', 'бАловать': 'incorrect'},
              {'принУдить': 'correct', 'принудИть': 'incorrect'},
              {'создАть': 'correct', 'сОздать': 'incorrect'},
              {'укрепИть': 'correct', 'укрЕпить': 'incorrect'},
              {'чЕрпать': 'correct', 'черпАть': 'incorrect'},
              {'началА': 'correct', 'нАчала': 'incorrect'},
              {'взялА': 'correct', 'взЯла': 'incorrect'},
              {'насорИть': 'correct', 'насОрить': 'incorrect'},
              {'ободрИть': 'correct', 'обОдрить': 'incorrect'},
              {'исчЕрпать': 'correct', 'исчерпАть': 'incorrect'},
              {'перелилА': 'correct', 'перелИла': 'incorrect'},
              {'разбаловАть': 'correct', 'разбАловать': 'incorrect'},
              {'сорИть': 'correct', 'сОрить': 'incorrect'},
              {'дозвонЯтся': 'correct', 'дозвОнятся': 'incorrect'},
              {'премировАть': 'correct', 'премИровать': 'incorrect'},
              {'создалА': 'correct', 'создАла': 'incorrect'},
              {'укрепИт': 'correct', 'укрЕпит': 'incorrect'},
              {'нормировАть': 'correct', 'нормИровать': 'incorrect'},
              {'обзвонИт': 'correct', 'обзвОнит': 'incorrect'},
              {'полилА': 'correct', 'полИла': 'incorrect'},
              {'гналАсь': 'correct', 'гнАлась': 'incorrect'},
              {'лилАсь': 'correct', 'лИлась': 'incorrect'},
              {'баловАться': 'correct', 'бАловаться': 'incorrect'},
              {'облегчИт': 'correct', 'облЕгчит': 'incorrect'},
              {'звонИт': 'correct', 'звОнит': 'incorrect'},
              {'озлОбить': 'correct', 'озлобИть': 'incorrect'},
              {'дождалАсь': 'correct', 'дождАлась': 'incorrect'},
              {'прИбыл': 'correct', 'прибЫл': 'incorrect'},
              {'прибылА': 'correct', 'прИбыла': 'incorrect'},
              {'прИбыло': 'correct', 'прибЫло': 'incorrect'},
              {'избаловАть': 'correct', 'избАловать': 'incorrect'},
              {'отбылА': 'correct', 'отбЫла': 'incorrect'},
              {'бАловень': 'correct', 'баловЕнь': 'incorrect'},
              {'назвалАсь': 'correct', 'назвАлась': 'incorrect'},
              {'щемИть': 'correct', 'щЕмить': 'incorrect'},
              {'щЁлкать': 'correct', 'щелкАть': 'incorrect'},
              {'бралА': 'correct', 'брАла': 'incorrect'},
              {'ободрИшься': 'correct', 'обОдришься': 'incorrect'},
              {'включИт': 'correct', 'вклЮчит': 'incorrect'},
              {'формировАть': 'correct', 'формИровать': 'incorrect'},
              {'освЕдомишься': 'correct', 'осведомИшься': 'incorrect'},
              {'одолжИть': 'correct', 'одОлжить': 'incorrect'},
              {'повторИт': 'correct', 'повтОрит': 'incorrect'},
              {'позвонИшь': 'correct', 'позвОнишь': 'incorrect'},
              {'перезвонИт': 'correct', 'перезвОнит': 'incorrect'},
              {'положИл': 'correct', 'полОжил': 'incorrect'},
              {'убралА': 'correct', 'убрАла': 'incorrect'},
              {'отдалА': 'correct', 'отдАла': 'incorrect'},
              {'отозвалАсь': 'correct', 'отозвАлась': 'incorrect'},
              {'окружИть': 'correct', 'окрУжить': 'incorrect'},
              {'жилОсь': 'correct', 'жИлось': 'incorrect'},
              {'звалА,': 'correct', 'звАла,': 'incorrect'},
              {'одолжИт': 'correct', 'одОлжит': 'incorrect'},
              {'углубИть': 'correct',  'углУбить': 'incorrect'},
              {'позвалА': 'correct', 'позвАла': 'incorrect'},
              {'насорИт': 'correct', 'насОрит': 'incorrect'},
              {'вручИть': 'correct', 'врУчить': 'incorrect'},
              {'зАняли': 'correct', 'занЯли': 'incorrect'},
              {'щемИт': 'correct', 'щЕмит': 'incorrect'},
              {'опОшлить': 'correct', 'опошлИть': 'incorrect'},
              {'закУпорить': 'correct', 'закупОрить': 'incorrect'},
              {'позвонИт': 'correct', 'позвОнит': 'incorrect'},
              {'рвалА': 'correct', 'рвАла': 'incorrect'},
              {'лгалА': 'correct', 'лгАла': 'incorrect'},
              {'нАчали': 'correct', 'начАли': 'incorrect'},
              {'ждалА': 'correct', 'ждАла': 'incorrect'},
              {'опломбировАть': 'correct', 'опломбИровать': 'incorrect'},
              {'положИть': 'correct', 'полОжить': 'incorrect'},
              {'наделИт': 'correct', 'надЕлит': 'incorrect'},
              {'понялА': 'correct', 'понЯла': 'incorrect'},
              {'накренИться': 'correct', 'накрЕниться': 'incorrect'},
              {'оклЕить': 'correct', 'оклеИть': 'incorrect'},
              {'ободралА': 'correct', 'ободрАла': 'incorrect'},
              {'отозвАться': 'correct', 'отозватьсЯ': 'incorrect'},
              {'влИться': 'correct', 'влитьсЯ': 'incorrect'},
              {'крАлась': 'correct', 'кралАсь': 'incorrect'},
              {'наделИть': 'correct', 'надЕлить': 'incorrect'},
              {'зАняло': 'correct', 'занялО': 'incorrect'},
              {'сортировАть': 'correct', 'сортИровать': 'incorrect'},
              {'звонИм': 'correct', 'звОним': 'incorrect'},
              {'ободрИться': 'correct', 'обОдриться': 'incorrect'},
              {'обострИть': 'correct',  'обОстрить': 'incorrect'},
              {'дозвонИтся,': 'correct', 'дозвОнится,': 'incorrect'},
              {'включИшь,': 'correct', 'вклЮчишь,': 'incorrect'},
              {'вручИт': 'correct', 'врУчит': 'incorrect'},
              {'принЯть': 'correct', 'прИнять': 'incorrect'},
              {'навралА': 'correct', 'наврАла': 'incorrect'},
              {'воспринялА': 'correct', 'воспрИняла': 'incorrect'},
              {'понЯть': 'correct', 'пОнять': 'incorrect'},
              {'отозвАть': 'correct', 'отОзвать': 'incorrect'},
              {'звонИшь': 'correct', 'звОнишь': 'incorrect'},
              {'облилАсь': 'correct', 'облИлась': 'incorrect'},
              {'сверлИть': 'correct', 'свЕрлить': 'incorrect'},
              {'включИм': 'correct', 'вклЮчим': 'incorrect'},
              {'позвонИть': 'correct', 'позвОнить': 'incorrect'},
              {'заперлАсь': 'correct', 'зАперлась': 'incorrect'},
              {'облегчИть': 'correct', 'облЕгчить': 'incorrect'},
              {'сорвалА': 'correct', 'сорвАла': 'incorrect'},
              {'сверлИт': 'correct', 'свЕрлит': 'incorrect'},
              {'сверлИшь': 'correct', 'свЕрлишь': 'incorrect'},
              {'откУпорил': 'correct', 'откупОрил': 'incorrect'},
              {'освЕдомиться': 'correct', 'осведомИться': 'incorrect'},
              {'дозвонИться': 'correct',  'дозвОниться': 'incorrect'},
              {'накренИтся': 'correct', 'накрЕнится': 'incorrect'},
              {'влилАсь': 'correct', 'влИлась': 'incorrect'},
              {'откУпорить': 'correct', 'откупОрить': 'incorrect'},
              {'включИть': 'correct', 'вклЮчить': 'incorrect'},
              {'лилА': 'correct', 'лИла': 'incorrect'},
              {'снялА': 'correct', 'снЯла': 'incorrect'},
              {'убыстрИть': 'correct', 'убЫстрить': 'incorrect'},
              {'дозИровать': 'correct', 'дозировАть': 'incorrect'},
              {'заперлА': 'correct', 'зАперла': 'incorrect'}]

nouns_vars = [{'бАнты': 'correct', 'бантЫ': 'incorrect'},
              {'крАны': 'correct', 'кранЫ': 'incorrect'},
              {'новостЕй': 'correct', 'нОвостей': 'incorrect'},
              {'водопровОд': 'correct', 'водопрОвод': 'incorrect'},
              {'каталОг': 'correct', 'катАлог': 'incorrect'},
              {'аэропОрты': 'correct', 'аэропортЫ': 'incorrect'},
              {'киломЕтр': 'correct', 'килОметр': 'incorrect'},
              {'докумЕнт': 'correct', 'докУмент': 'incorrect'},
              {'мЕстностей': 'correct', 'местностЕй': 'incorrect'},
              {'бОроду': 'correct', 'бородУ': 'incorrect'},
              {'дефИс': 'correct', 'дЕфис': 'incorrect'},
              {'знАчимость': 'correct', 'значИмость': 'incorrect'},
              {'Иксы': 'correct', 'иксЫ': 'incorrect'},
              {'лыжнЯ': 'correct', 'лЫжня': 'incorrect'},
              {'вероисповЕдание': 'correct', 'вероисповедАние': 'incorrect'},
              {'мусоропровОд': 'correct', 'мусоропрОвод': 'incorrect'},
              {'еретИк': 'correct', 'ерЕтик': 'incorrect'},
              {'газопровОд': 'correct', 'газопрОвод': 'incorrect'},
              {'кремнЯ': 'correct', 'крЕмня': 'incorrect'},
              {'чЕлюстей': 'correct', 'челюстЕй': 'incorrect'},
              {'пОчестей': 'correct', 'почестЕй': 'incorrect'},
              {'децимЕтр': 'correct', 'децИметр': 'incorrect'},
              {'сантимЕтр': 'correct', 'сантИметр': 'incorrect'},
              {'кремЕнь': 'correct', 'крЕмень': 'incorrect'},
              {'кОнусов': 'correct', 'конусОв': 'incorrect'},
              {'исповЕдать': 'correct', 'исповедАть': 'incorrect'},
              {'некролОг': 'correct', 'некрОлог': 'incorrect'},
              {'намЕрение': 'correct', 'намерЕние': 'incorrect'},
              {'корЫсть': 'correct', 'кОрысть': 'incorrect'},
              {'монолОг': 'correct', 'монОлог': 'incorrect'},
              {'диспансЕр': 'correct', 'диспАнсер': 'incorrect'},
              {'жалюзИ': 'correct', 'жАлюзи': 'incorrect'},
              {'нефтепровОд': 'correct', 'нефтепрОвод': 'incorrect'},
              {'миллимЕтр': 'correct', 'миллИметр': 'incorrect'},
              {'диалОг': 'correct', 'диАлог': 'incorrect'},
              {'квартАл': 'correct', 'квАртал': 'incorrect'},
              {'знАчимый': 'correct', 'значИмый': 'incorrect'},
              {'бухгАлтеров': 'correct', 'бухгалтерОв': 'incorrect'},
              {'договорЁнность': 'correct', 'договОренность': 'incorrect'},
              {'граждАнство': 'correct', 'грАжданство': 'incorrect'},
              {'лЕкторов': 'correct', 'лекторОв': 'incorrect'},
              {'досУг': 'correct', 'дОсуг': 'incorrect'}]

adjectives_vars = [{'красИвейший': 'correct', 'красивЕйший': 'incorrect'},
                   {'кУхонный': 'correct', 'кухОнный': 'incorrect'},
                   {'болтлИва': 'correct', 'болтливА': 'incorrect'},
                   {'оптОвый': 'correct', 'Оптовый': 'incorrect'},
                   {'ловкА': 'correct', 'лОвка': 'incorrect'},
                   {'мозаИчный': 'correct', 'мозАичный': 'incorrect'},
                   {'смазлИва': 'correct', 'смАзлива': 'incorrect'},
                   {'прожОрлива': 'correct', 'прожорлИва': 'incorrect'},
                   {'слИвовый': 'correct', 'сливОвый': 'incorrect'},
                   {'знАчимый': 'correct', 'значИмый': 'incorrect'},
                   {'красИвее': 'correct', 'красивЕе': 'incorrect'},
                   {'прозорлИва': 'correct', 'прозОрлива': 'incorrect'},
                   {'суетлИва': 'correct', 'суЕтлива': 'incorrect'},
                   {'вернА': 'correct', 'вЕрна': 'incorrect'}]

adverbs_vars = [{'донЕльзя': 'correct', 'дОнельзя': 'incorrect'},
                {'красИвее': 'correct', 'красивЕе': 'incorrect'},
                {'дОнизу': 'correct', 'донИзу': 'incorrect'},
                {'навЕрх': 'correct', 'нАверх': 'incorrect'},
                {'зАгодя': 'correct', 'загодЯ': 'incorrect'},
                {'зАтемно': 'correct', 'затемнО': 'incorrect'},
                {'завИдно': 'correct', 'зАвидно': 'incorrect'},
                {'вОвремя': 'correct', 'воврЕмя': 'incorrect'},
                {'надОлго': 'correct', 'нАдолго': 'incorrect'},
                {'добелА': 'correct', 'дОбела': 'incorrect'},
                {'ненадОлго': 'correct', 'ненАдолго': 'incorrect'},
                {'зАсветло': 'correct', 'засвЕтло': 'incorrect'},
                {'дОсуха': 'correct', 'досУха': 'incorrect'},
                {'дОверху': 'correct', 'довЕрху': 'incorrect'}]

participles_vars = [{'нАжитый': 'correct', 'нажИтый': 'incorrect'},
                    {'низведЁнный': 'correct', 'низвЕденный': 'incorrect'},
                    {'снятА': 'correct', 'снЯта': 'incorrect'},
                    {'нажИвший': 'correct', 'нАживший': 'incorrect'},
                    {'прИнятый': 'correct', 'принЯтый': 'incorrect'},
                    {'обострЁнный': 'correct', 'обОстренный': 'incorrect'},
                    {'определЁнный': 'correct', 'опредЕленный': 'incorrect'},
                    {'зАнятый': 'correct', 'занЯтый': 'incorrect'},
                    {'включЁнный': 'correct', 'вклЮченный': 'incorrect'},
                    {'заселенА': 'correct', 'засЕлена': 'incorrect'},
                    {'сОгнутый': 'correct', 'согнУтый': 'incorrect'},
                    {'кровоточАщий': 'correct', 'кровотОчащий': 'incorrect'},
                    {'балОванный': 'correct', 'бАлованный': 'incorrect'},
                    {'зАпертый': 'correct', 'запЕртый': 'incorrect'},
                    {'поделЁнный': 'correct', 'подЕленный': 'incorrect'},
                    {'ободрЁн': 'correct', 'обОдрен': 'incorrect'},
                    {'занятА': 'correct', 'зАнята': 'incorrect'},
                    {'довезЁнный': 'correct', 'довЕзенный': 'incorrect'},
                    {'нАчатый': 'correct', 'начАтый': 'incorrect'},
                    {'ободрЁнный': 'correct', 'обОдренный': 'incorrect'},
                    {'отключЁнный': 'correct', 'отклЮченный': 'incorrect'},
                    {'налитА': 'correct', 'налИта': 'incorrect'},
                    {'зАгнутый': 'correct', 'загнУтый': 'incorrect'},
                    {'заселЁнный': 'correct', 'засЕленный': 'incorrect'},
                    {'нажитА': 'correct', 'нажИта': 'incorrect'},
                    {'избалОванный': 'correct', 'избАлованный': 'incorrect'},
                    {'низведЁн,': 'correct', 'низвЕден,': 'incorrect'},
                    {'нанЯвшийся': 'correct', 'нАнявшийся': 'incorrect'},
                    {'прожИвший': 'correct', 'прОживший': 'incorrect'},
                    {'приручЁнный': 'correct', 'прирУченный': 'incorrect'},
                    {'кормЯщий': 'correct', 'кОрмящий': 'incorrect'},
                    {'повторЁнный': 'correct', 'повтОренный': 'incorrect'},
                    {'понЯвший': 'correct', 'пОнявший': 'incorrect'},
                    {'налИвший': 'correct', 'нАливший': 'incorrect'},
                    {'включЁн,': 'correct', 'вклЮчен,': 'incorrect'},
                    {'молЯщий': 'correct', 'мОлящий': 'incorrect'},
                    {'запертА': 'correct', 'зАперта': 'incorrect'},
                    {'начАвший': 'correct', 'нАчавший': 'incorrect'},
                    {'ободренА': 'correct', 'обОдрена': 'incorrect'}]

gerunds_vars = [{'балУясь': 'correct', 'бАлуясь': 'incorrect'},
                {'поднЯв': 'correct', 'пОдняв': 'incorrect'},
                {'начАв': 'correct', 'нАчав': 'incorrect'},
                {'отдАв': 'correct', 'Отдав': 'incorrect'},
                {'закУпорив': 'correct', 'закупОрив': 'incorrect'},
                {'начАвшись': 'correct', 'нАчавшись': 'incorrect'},
                {'понЯв': 'correct', 'пОняв': 'incorrect'},
                {'прибЫв': 'correct', 'прИбыв': 'incorrect'}]


verbs_results = {'нАчал': [0, 0], 'надорвалАсь': [0, 0], 'послАла': [0, 0], 'сорИт': [0, 0], 'ворвалАсь': [0, 0], 'обогналА': [0, 0], 'прибЫть': [0, 0], 'бралАсь': [0, 0], 'взялАсь': [0, 0], 'воссоздалА': [0, 0], 'клАла': [0, 0], 'принялА': [0, 0], 'прИнял': [0, 0], 'занялА': [0, 0], 'жИться': [0, 0], 'обнялАсь': [0, 0], 'гналА': [0, 0], 'добралА': [0, 0], 'окружИт': [0, 0], 'нарвалА': [0, 0], 'отозвалА': [0, 0], 'плодоносИть': [0, 0], 'ворвАться': [0, 0], 'добралАсь': [0, 0], 'зАнял,': [0, 0], 'налилА': [0, 0], 'перезвонИть': [0, 0], 'воспринЯть': [0, 0], 'лИться': [0, 0], 'прИняли': [0, 0], 'баловАть': [0, 0], 'принУдить': [0, 0], 'создАть': [0, 0], 'укрепИть': [0, 0], 'чЕрпать': [0, 0], 'началА': [0, 0], 'взялА': [0, 0], 'насорИть': [0, 0], 'ободрИть': [0, 0], 'исчЕрпать': [0, 0], 'перелилА': [0, 0], 'разбаловАть': [0, 0], 'сорИть': [0, 0], 'дозвонЯтся': [0, 0], 'премировАть': [0, 0], 'создалА': [0, 0], 'укрепИт': [0, 0], 'нормировАть': [0, 0], 'обзвонИт': [0, 0], 'полилА': [0, 0], 'гналАсь': [0, 0], 'лилАсь': [0, 0], 'баловАться': [0, 0], 'облегчИт': [0, 0], 'звонИт': [0, 0], 'озлОбить': [0, 0], 'дождалАсь': [0, 0], 'прИбыл': [0, 0], 'прибылА': [0, 0], 'прИбыло': [0, 0], 'избаловАть': [0, 0], 'отбылА': [0, 0], 'бАловень': [0, 0], 'назвалАсь': [0, 0], 'щемИть': [0, 0], 'щЁлкать': [0, 0], 'бралА': [0, 0], 'ободрИшься': [0, 0], 'включИт': [0, 0], 'формировАть': [0, 0], 'освЕдомишься': [0, 0], 'одолжИть': [0, 0], 'повторИт': [0, 0], 'позвонИшь': [0, 0], 'перезвонИт': [0, 0], 'положИл': [0, 0], 'убралА': [0, 0], 'отдалА': [0, 0], 'отозвалАсь': [0, 0], 'окружИть': [0, 0], 'жилОсь': [0, 0], 'звалА,': [0, 0], 'одолжИт': [0, 0], 'углубИть': [0, 0], 'позвалА': [0, 0], 'насорИт': [0, 0], 'вручИть': [0, 0], 'зАняли': [0, 0], 'щемИт': [0, 0], 'опОшлить': [0, 0], 'закУпорить': [0, 0], 'позвонИт': [0, 0], 'рвалА': [0, 0], 'лгалА': [0, 0], 'нАчали': [0, 0], 'ждалА': [0, 0], 'опломбировАть': [0, 0], 'положИть': [0, 0], 'наделИт': [0, 0], 'понялА': [0, 0], 'накренИться': [0, 0], 'оклЕить': [0, 0], 'ободралА': [0, 0], 'отозвАться': [0, 0], 'влИться': [0, 0], 'крАлась': [0, 0], 'наделИть': [0, 0], 'зАняло': [0, 0], 'сортировАть': [0, 0], 'звонИм': [0, 0], 'ободрИться': [0, 0], 'обострИть': [0, 0], 'дозвонИтся,': [0, 0], 'включИшь,': [0, 0], 'вручИт': [0, 0], 'принЯть': [0, 0], 'навралА': [0, 0], 'воспринялА': [0, 0], 'понЯть': [0, 0], 'отозвАть': [0, 0], 'звонИшь': [0, 0], 'облилАсь': [0, 0], 'сверлИть': [0, 0], 'включИм': [0, 0], 'позвонИть': [0, 0], 'заперлАсь': [0, 0], 'облегчИть': [0, 0], 'сорвалА': [0, 0], 'сверлИт': [0, 0], 'сверлИшь': [0, 0], 'откУпорил': [0, 0], 'освЕдомиться': [0, 0], 'дозвонИться': [0, 0], 'накренИтся': [0, 0], 'влилАсь': [0, 0], 'откУпорить': [0, 0], 'включИть': [0, 0], 'лилА': [0, 0], 'снялА': [0, 0], 'убыстрИть': [0, 0], 'дозИровать': [0, 0], 'заперлА': [0, 0]}
nouns_results = {'бАнты': [0, 0], 'крАны': [0, 0], 'новостЕй': [0, 0], 'водопровОд': [0, 0], 'каталОг': [0, 0], 'аэропОрты': [0, 0], 'киломЕтр': [0, 0], 'докумЕнт': [0, 0], 'мЕстностей': [0, 0], 'бОроду': [0, 0], 'дефИс': [0, 0], 'знАчимость': [0, 0], 'Иксы': [0, 0], 'лыжнЯ': [0, 0], 'вероисповЕдание': [0, 0], 'мусоропровОд': [0, 0], 'еретИк': [0, 0], 'газопровОд': [0, 0], 'кремнЯ': [0, 0], 'чЕлюстей': [0, 0], 'пОчестей': [0, 0], 'децимЕтр': [0, 0], 'сантимЕтр': [0, 0], 'кремЕнь': [0, 0], 'кОнусов': [0, 0], 'исповЕдать': [0, 0], 'некролОг': [0, 0], 'намЕрение': [0, 0], 'корЫсть': [0, 0], 'монолОг': [0, 0], 'диспансЕр': [0, 0], 'жалюзИ': [0, 0], 'нефтепровОд': [0, 0], 'миллимЕтр': [0, 0], 'диалОг': [0, 0], 'квартАл': [0, 0], 'знАчимый': [0, 0], 'бухгАлтеров': [0, 0], 'договорЁнность': [0, 0], 'граждАнство': [0, 0], 'лЕкторов': [0, 0], 'досУг': [0, 0]}
adjectives_results = {'красИвейший': [0, 0], 'кУхонный': [0, 0], 'болтлИва': [0, 0], 'оптОвый': [0, 0], 'ловкА': [0, 0], 'мозаИчный': [0, 0], 'смазлИва': [0, 0], 'прожОрлива': [0, 0], 'слИвовый': [0, 0], 'знАчимый': [0, 0], 'красИвее': [0, 0], 'прозорлИва': [0, 0], 'суетлИва': [0, 0], 'вернА': [0, 0]}
participles_results = {'нАжитый': [0, 0], 'низведЁнный': [0, 0], 'снятА': [0, 0], 'нажИвший': [0, 0], 'прИнятый': [0, 0], 'обострЁнный': [0, 0], 'определЁнный': [0, 0], 'зАнятый': [0, 0], 'включЁнный': [0, 0], 'заселенА': [0, 0], 'сОгнутый': [0, 0], 'кровоточАщий': [0, 0], 'балОванный': [0, 0], 'зАпертый': [0, 0], 'поделЁнный': [0, 0], 'ободрЁн': [0, 0], 'занятА': [0, 0], 'довезЁнный': [0, 0], 'нАчатый': [0, 0], 'ободрЁнный': [0, 0], 'отключЁнный': [0, 0], 'налитА': [0, 0], 'зАгнутый': [0, 0], 'заселЁнный': [0, 0], 'нажитА': [0, 0], 'избалОванный': [0, 0], 'низведЁн,': [0, 0], 'нанЯвшийся': [0, 0], 'прожИвший': [0, 0], 'приручЁнный': [0, 0], 'кормЯщий': [0, 0], 'повторЁнный': [0, 0], 'понЯвший': [0, 0], 'налИвший': [0, 0], 'включЁн,': [0, 0], 'молЯщий': [0, 0], 'запертА': [0, 0], 'начАвший': [0, 0], 'ободренА': [0, 0]}
gerunds_results = {'балУясь': [0, 0], 'поднЯв': [0, 0], 'начАв': [0, 0], 'отдАв': [0, 0], 'закУпорив': [0, 0], 'начАвшись': [0, 0], 'понЯв': [0, 0], 'прибЫв': [0, 0]}
adverbs_results = {'донЕльзя': [0, 0], 'красИвее': [0, 0], 'дОнизу': [0, 0], 'навЕрх': [0, 0], 'зАгодя': [0, 0], 'зАтемно': [0, 0], 'завИдно': [0, 0], 'вОвремя': [0, 0], 'надОлго': [0, 0], 'добелА': [0, 0], 'ненадОлго': [0, 0], 'зАсветло': [0, 0], 'дОсуха': [0, 0], 'дОверху': [0, 0]}

all_vars = {
    'nouns': [nouns_vars, nouns_results, 'Существительные'],
    'adjectives': [adjectives_vars, adjectives_results, 'Прилагательные'],
    'verbs': [verbs_vars, verbs_results, 'Глаголы'],
    'participles': [participles_vars, participles_results, 'Причастия'],
    'gerunds': [gerunds_vars, gerunds_results, 'Деепричастия'],
    'adverbs': [adverbs_vars, adverbs_results, 'Наречия']
}



