def test1(a,b,c,*d,**e):
    print("A:",a,"B:",b,"C:",c,"D:",list(d),"E:",e)

test1(1,2,3,4,5)
test1(1,2,5,"Def",500,100,4,A="Dharti",B="Vishal")
