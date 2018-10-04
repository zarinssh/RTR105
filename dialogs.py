#!/usr/bin/python
# -*- coding: utf-8 -*-


a=input("Cienijamais lietotāj, lūdzu, ievadi skaitli:")
# 3.pytonā visi input rezultatiir ar str datu tipu
#tāpēc ievaītais lieluma datu tips vēlāk ir jāpārveido

a=int(a)

print("lietotāj, tu esi ievadīji skaitli:")
aa=a * a
print("Tavs skaitlis kvadrātā ir %d"%(aa))

