def egcd(a, b):
    u, u1 = 1, 0
    v, v1 = 0, 1
    while b:
        q = a // b
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, a - q * b
    return a, u, v


def phi(p, q):
    return (p - 1) * (q - 1)


def get_d(p, n, e):
    q = n / p
    phi_v = phi(p, q)
    _gcd, d, _2 = egcd(e, phi_v)
    if d < 0:
        d += phi_v
    return d


def modular_sqrt(a, p):
    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.
        Solve the congruence of the form:
            x^2 = a (mod p)
        And returns x. Note that p - x is also a root.
        0 is returned is no square root exists for
        these a and p.
        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) / 4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow(a, (s + 1) / 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x
        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a, p):
    ls = pow(a, (p - 1) / 2, p)
    return -1 if ls == p - 1 else ls


class Rabin(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q

    def encrypt(self, m):
        return (m * m) % self.n

    def decrypt(self, c):
        try:
            gcd, yp, yq = egcd(self.p, self.q)
            mp = modular_sqrt(c, self.p)
            mq = modular_sqrt(c, self.q)
            assert yp * self.p + yq * self.q == 1
            assert (mp * mp) % self.p == c % self.p
            assert (mq * mq) % self.q == c % self.q
            r1 = (yp * self.p * mq + yq * self.q * mp) % self.n
            s1 = (yp * self.p * mq - yq * self.q * mp) % self.n
            r2 = self.n - r1
            s2 = self.n - s1
            return r1, s1, r2, s2
        except AssertionError:
            return []


n = 13556367081494065533476185708052653650756116075497136964825256182323930781072918245303929895120229605377517477182809443617030479949598692462954497748267489366554639632203605797434909988930580464482991493490377285383757714349425078829885400599265075448201222436077932825811408335304285298245301112338803949663031883419786986992363510642570302767604979688646061409123282967257402153812860100070540841199154936998324836394864967886769189671397457822566714054353034842069294532910048853933953319371547850367318591745968259237416038486437192536936533142364791877766292382405008879194930806902924482101123017766420392923337
p = 108625855303776649594296217762606721187040584561417095690198042179830062402629658962879350820293908057921799564638749647771368411506723288839177992685299661714871016652680397728777113391224594324895682408827010145323030026082761062500181476560183634668138131801648343275565223565977246710777427583719180083291
q = n // p
e = 1440
e_p = e//160
ct = 4293606144359418817736495518573956045055950439046955515371898146152322502185230451389572608386931924257325505819171116011649046442643872945953560994241654388422410626170474919026755694736722826526735721078136605822710062385234124626978157043892554030381907741335072033672799019807449664770833149118405216955508166023135740085638364296590030244412603570120626455502803633568769117033633691251863952272305904666711949672819104143350385792786745943339525077987002410804383449669449479498326161988207955152893663022347871373738691699497135077946326510254675142300512375907387958624047470418647049735737979399600182827754
d = get_d(p, n, e_p)

rabin = Rabin(p, q)
partially_decoded_ct = [ct]
for i in range(5):
    new_partially_decoded_ct = []
    for ct_p in partially_decoded_ct:
        new_ct_p = rabin.decrypt(ct_p)
        new_partially_decoded_ct.extend(list(new_ct_p))
    partially_decoded_ct = set(new_partially_decoded_ct)

potential_plaintext = []
for potential_rsa_ct in partially_decoded_ct:
    pt = pow(potential_rsa_ct, d, n)
    potential_plaintext.append(pt)
print(potential_plaintext)
