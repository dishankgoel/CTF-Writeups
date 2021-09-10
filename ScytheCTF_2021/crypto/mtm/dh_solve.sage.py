

# This file was *autogenerated* from the file dh_solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_253533314669417388586475074652152461877 = Integer(253533314669417388586475074652152461877); _sage_const_2 = Integer(2); _sage_const_166846743424922762697043843288602130766 = Integer(166846743424922762697043843288602130766)
n=_sage_const_253533314669417388586475074652152461877 
g=_sage_const_2 

m1 = _sage_const_166846743424922762697043843288602130766 

F = IntegerModRing(n)

a = discrete_log(F(m1), F(g))

print(a)

