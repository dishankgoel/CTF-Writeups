n=253533314669417388586475074652152461877
g=2

m1 = 166846743424922762697043843288602130766

F = IntegerModRing(n)

a = discrete_log(F(m1), F(g))

print(a)