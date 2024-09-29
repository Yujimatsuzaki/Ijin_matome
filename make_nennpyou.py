import re
with open("wiki.txt","r") as f:
    lines=f.readlines()

with open("birth.txt","r") as f:
    birth=f.read()
    birth_sikyo = re.findall(r'\d{4}', birth)
umare=int(birth_sikyo[0])
sikyo=-1 if len(birth_sikyo)==1 else int(birth_sikyo[1])

nennpyou_dict={i:[] for i in range(200)}
for line in lines:
    line=line.replace("\n","")
    result = re.findall(r'\d{3,4}年', line)
    for result_ in result:
        if -1<int(result_[:-1])-umare<200:
            nennpyou_dict[int(result_[:-1])-umare].append(line)
if sikyo>0:
    nennpyou_dict[sikyo-umare].append("死去")

for i in range(200):
    nennpyou_dict[i]="".join(nennpyou_dict[i])
ans="\n".join(nennpyou_dict.values())

print(ans)

with open("ans.txt","w") as f:
    f.write(ans)