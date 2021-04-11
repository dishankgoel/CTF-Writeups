from binascii import unhexlify
from decimal import *
import decimal

e = 0x10001

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b%a, a)
        return (g, x - (b//a)*y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if(g != 1):
        return -1
    return x%m

def solve_rsa(factors, c):

    ds = []
    for i in range(len(factors)):
        ds.append(modinv(e, factors[i] - 1))

    m = factors[0]
    ts = []
    for i in range(1, len(factors)):
        ts.append(modinv(m, factors[i]))
        m = m*factors[i]
    xs = []
    for i in range(len(factors)):
        xs.append(pow((c%factors[i]), ds[i], factors[i]))

    x = xs[0]
    m = factors[0]

    for i in range(1, len(factors)):
        x += m*((xs[i] - x % factors[i]) * (ts[i - 1] % factors[i]))
        m = m*factors[i]
    
    print("[*] flag: {}".format(unhexlify(hex(x%m)[2:])))


# n = 25992347861099219061069221843214518860756327486173319027118759091795941826930677
# c = 23026963612553138453994241341858545669161954498018923158210487520942937328899463
# factors = [3757160792909754673945392226295475594863, 6918082374901313855125397665325977135579]

# solve_rsa(n, factors, c)

# n = 13269353506569762322866448443179444023604712744966341096534397703952746262066379915270
# c = 1190180964733245137384972297461802113210633791027492695067903719077825144431176576299
# factors = [2, 3, 5, 7, 11, 13, 17, 3757160792909754673945392226295475594863, 6918082374901313855125397665325977135579]

# solve_rsa(n, factors, c)

n = 750663646847528873168937831391907810647591913965562495296199585082759057318274521553757550724463451891668175905206221877858317290777877060166997790624527965837837993129383290402509996587556406778482067347232022225466937668396768390983554357611376057823852179263682649072729435912583278183812954787442057976301035654942470184201720410477691326653029842426252391647509934740335989269071438620690320401576861478427178128804784352142271832603194431176323445880836139
# n = Decimal(n)
pq = 80970512687406090889060992576336286518763523653333428346066206717567693624044162491796922556346210471950404967161997779545603412053582932354160368128117099634532601019309976159157713252768640669410333127578132624183514430252557952811102781031315190048386214745340936679285725364013916829276058253922234988379
r = 9270827390528364910655381211348387322489850037696558436748157342122315986076548828640373264134873757332529116344630163645837117897238251300148523115459441
# pq = Decimal(pq)
c = 221975957171552618997196127189899209276336291387640550554967727731818563960555600691881715668156105819191779108737770660990397331961689607338541452069797368288215716485835439777459317512238532636172979397173548812054679237802827275184091619620252887678664409116710340000218841023351238456144820005968602870644031701303645229364391309952172259686888808938835775360009896210855708140351244441167461823250549764537506364091367096196182191704433664638829177854628679
# factors = [, ]