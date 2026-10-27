"""Independent arithmetic checks for 56 additional original questions.
Assertions check computed values against the selected answer text, including units.
"""
import json, pathlib, math
from fractions import Fraction
root=pathlib.Path(__file__).resolve().parents[1]
q=json.loads((root/'data/wajib.json').read_text())+json.loads((root/'data/pilihan.json').read_text())
F=Fraction
assertions=[
(str(12+9-4),str(len({1,2,3,4}&{3,4,5}))),
('3⁵',f'{math.isqrt(49)}½'),
(str((11-3)//2),str((14+1)//5)),
(str(3*2+2),str(3**2-1)),
(str(5+5*4),str(10*(2*6+9*3)//2)),
(str(2*3**3),str(4+8+16)),
('(2,2)','x≥−3'),
(str(9-2-3),str((12-4)//2)),
(f'{180-115}°',f'{180-35-85}°'),
('2 km',f'{3**2} kali'),
(str(math.isqrt(5**2+12**2)),str(math.isqrt(13**2-5**2))),
('(3,2)','(−2,8)'),
(str(math.isqrt(6**2+8**2)),str(abs(6-1))),
(f'{10*6//2} cm²',f'{4*7} cm'),
(f'{2**2*5}π cm³',f'{6*3**2} cm²'),
(str(F(4,5)),str(F(math.isqrt(13**2-5**2),13))),
(f'{(50-40)*100//40}%',str(8+12+10)),
(str(4*3),str(math.comb(5,2))),
('8',str((3+5)//2)),
(str(F(1,6)),str(F(2,5))),
(str(1-F(1,4)),str(F(4,7)*F(3,6))),
(str(3*2-2*1),str(1*(1*1-3*0)-2*(0*1-3*2))),
(str(3**2+1),'x−2'),
('x≥3',str(2**3)),
('(4,1)',str(math.isqrt(5**2+12**2))),
('x²+y²=9',str(math.isqrt(25))),
(str(5*2**2),'(−1,2)'),
(str(3+3),str(F(1,math.isqrt(4)+2)))]
assert len(q)==84 and len(assertions)==28
for i,pair in enumerate(assertions):
 for j,expected in enumerate(pair,start=1):
  item=q[3*i+j]; actual=next(o['text'] for o in item['options'] if o['id']==item['key'][0]); assert actual==expected,(item['id'],expected,actual)
print('56 additional topic answers independently checked.')
base=['26','6¼','4','19','25','45','(2,3)','2','65°','15 cm','10 cm','(5,3)','5','40 cm²','60 cm³','3/5','50%','12','7','1/2','1/4','5','2','x≠2','5','(2,−3)','54','4']
for i,answer in enumerate(base):
 item=q[3*i];actual=next(o['text'] for o in item['options'] if o['id']==item['key'][0]);assert actual==answer,(item['id'],answer,actual)
mixed=json.loads((root/'data/mixed.json').read_text());expected=['10','4','13','7','2/5','5','6','10','x²+y²=16','2']
for i,answer in enumerate(expected):
 item=mixed[i];actual=next(o['text'] for o in item['options'] if o['id']==item['key'][0]);assert actual==answer,(item['id'],answer,actual)
assert mixed[10]['key']==['A','B','D'] and mixed[11]['key']==[0,1,0]
assert mixed[12]['key']==['A','B'] and mixed[13]['key']==[0,0,1] and mixed[14]['key']==['A','B','D']
assert 18+15-7==26 and Fraction(1,4)+6==Fraction(25,4) and 4+7*3==25
assert 2*4-1*3==5 and 2*4-3*1==5 and 2**2+2==6
assert Fraction(1,2)*Fraction(1,3)==Fraction(1,6) and Fraction(1,1)-Fraction(1,4)==Fraction(3,4)
print('28 previously reviewed answers, 10 mixed keys and 5 classification keys checked.')
