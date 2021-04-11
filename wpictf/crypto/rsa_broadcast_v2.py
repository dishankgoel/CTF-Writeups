import gmpy2
gmpy2.get_context().precision = 4096
e = 3

n1 = 95118357989037539883272168746004652872958890562445814301889866663072352421703264985997800660075311645555799745426868343365321502734736006248007902409628540578635925559742217480797487130202747020211452620743021097565113059392504472785227154824117231077844444672393221838192941390309312484066647007469668558141
n2 = 98364165919251246243846667323542318022804234833677924161175733253689581393607346667895298253718184273532268982060905629399628154981918712070241451494491161470827737146176316011843738943427121602324208773653180782732999422869439588198318422451697920640563880777385577064913983202033744281727004289781821019463
n3 = 68827940939353189613090392226898155021742772897822438483545021944215812146809318686510375724064888705296373853398955093076663323001380047857809774866390083434272781362447147441422207967577323769812896038816586757242130224524828935043187315579523412439309138816335569845470021720847405857361000537204746060031

c1 = 64830446708169012766414587327568812421130434817526089146190136796461298592071238930384707543318390292451118980302805512151790248989622269362958718228298427212630272525186478627299999847489018400624400671876697708952447638990802345587381905407236935494271436960764899006430941507608152322588169896193268212007
c2 = 96907490717344346588432491603722312694208660334282964234487687654593984714144825656198180777872327279250667961465169799267405734431675111035362089729249995027326863099262522421206459400405230377631141132882997336829218810171728925087535674907455584557956801831447125486753515868079342148815961792481779375529
c3 = 43683874913011746530056103145445250281307732634045437486524605104639785469050499171640521477036470750903341523336599602288176611160637522568868391237689241446392699321910723235061180826945464649780373301028139049288881578234840739545000338202917678008269794179100732341269448362920924719338148857398181962112

ciphertexts = [
            515274042976912179894435774656907420040599503456517078488056218986662017260212389975972477279505310799399071383390618892499008790928347543017765027618590150794317674792875250152206518326158674718404382617692169589911938548819188733852354294583496715425255584973283840789780326402769751705164900106921523637157271605500111846563844641773661723255718653040958019618435501230171699432186518803652675691180548548982155426472648502704469425298466513665043628724497448475714424482446137414939511691724839553567514050622159418495196773388690852258256550787962177196383253952227153557220272199293397879908308572668952866439,
            10512934566887371506285681495672139256544177416158977932082410009242386741198073874632763611137937701329570263046854521709347241390006612379393018933295475369159148328248445221357906382527678877429535168220389698475391828837227453358681276167720605617228338487308750653165147019400915842904872988789759529121710032871148507314874152494680057046977274373381326003405301191489108322498519602528688873942243307708631394538177629868515911161222795303220989599519719169300455717641863368473309673489958952173445661451265442004625237606054046962062434813126456494957846077185121041599277143211160596207640833275850170891378,
            4122591425712279559823043898131225014447235394996958162806737555257607173149332839353292933732548212376056402900761362427837044396517072345683265668973735260384169928448531246071624967168190024583028639591981238222340513125989229227761894026521238496145716707176637113415430809586007230597253976748507442809040629281971868442704017013258355403718545489677897799000961350863824810217217745918503635905775610161826572608564207497464646323778407843991683950506484189720225535503643332574132841288909783555334280205740975729691459011043954137669831817945210956835398278009161994675851980163314376477384045294293755909874
        ]

    # N1 = get_value(MODULUS_1)
    # N2 = get_value(MODULUS_2)
    # N3 = get_value(MODULUS_3)
    # modulus = [N1, N2, N3]
modulus = [
        21939147590581954242131893557689750173730181114330873782062274456630281986233643990882568426690149971468987847436717513764939861105600249325682418749886588739440853385485272501856860578476795830603738468829294920737586209822299603185425324611481798231193950636987017718955070420091525231666894903436050998112803225822333684113551754209802262129292376015861410644289380376439390552627189657966103965089679163295591136464541998227543058082734503570960156783196006833967361311083486266118899788620317372054292861892020849652213277431575285275801196626852675579752895079650118836892859390462805733596279690076656763624249,
        26325215018784165663958487526715385161171636566916698114816183716597566424675870012796860473421390775180027083457908584461525282815469520282303059318923930531826588673345113634118988713179894971211405380241575065877886390347877768297280022387015195069836149198306647472534681286406136303674462323742151285361538383784282113898065157278366533587767199303585208673225974716800760227497569577072903884939422787710986913747191378087554442395968729847569180921093186599977266346501947184849099856506537976370069200813758143237937721729073822639191799709052936074831322440705620902220824412476988222346922869104007199777561,
        23013589835547680503802140462487647716102548445081685245087901486321520435018899614072711065158868927754813316329675676910885474767916372370942795565358071859270832973837949423193707764788999822539648518439967218163608118921979697363190728350735745938069012584523314223346479156208977445194408267152808800890485882602068876756801123087623323707553203656108124651989136578687688847505350883163751096338640206246619001851586459510648241545637475283654557530338836698680934504086346810521919864048046078444168117563048636886066060497385368685340990757248020960409380316695810483273153565980791846594355984630591111120973 
    ]
    # temp = ciphertexts
    # ciphertexts = modulus
    # modulus = temp

c1 = ciphertexts[0]
c2 = ciphertexts[1]
c3 = ciphertexts[2]

n1 = modulus[0]
n2 = modulus[1]
n3 = modulus[2]


N = n1*n2*n3
N1 = N//n1
N2 = N//n2
N3 = N//n3

u1 = gmpy2.invert(N1, n1)
u2 = gmpy2.invert(N2, n2)
u3 = gmpy2.invert(N3, n3)

M = (c1*u1*N1 + c2*u2*N2 + c3*u3*N3) % N

m = int(gmpy2.root(M,e))
# print(m)

print (hex(m)[2:-2].rstrip("L")).decode("hex")