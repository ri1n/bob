#########
hook = []
hook.append("Hoo-ooh, ooh-ooh")
hook.append("Hoo-ooh, hoo")


chorus = []
chorus.append("Stay in the middle")
chorus.append("Like you a little, don't want no riddle")
chorus.append("말해줘, say it back, oh, say it, ditto")
chorus.append("아침은 너무 멀어, so say it, ditto")
chorus.append("I don't want to")
chorus.append("Walk in this 미로")
chorus.append("다 아는 건 아니어도 바라던 대로")
chorus.append("말해줘, say it back, oh, say it, ditto")
chorus.append("I want you so, want you, so say it, ditto")


choruspart2 = []
choruspart2.append("다 아는 건 아니어도 바라던 대로")
choruspart2.append("말해줘, say it back, oh, say it, ditto")
choruspart2.append("I want you so, want you, so say it, ditto")


prechorus = []

prechorus.append("I got no time to lose")
prechorus.append("내 길었던 하루, 난 보고 싶어")
prechorus.append("Ra-ta-ta-ta, 울린 심장 (Ra-ta-ta-ta)")
prechorus.append("I got nothing to lose")
prechorus.append("널 좋아한다고, ooh-woah, ooh-woah, ooh-woah, ooh")
prechorus.append("Ra-ta-ta-ta, 울린 심장 (Ra-ta-ta-ta)")
prechorus.append("But I don't want to")

prechorustwo = []

prechorustwo.append("I got nothing to lose")
prechorustwo.append("널 좋아한다고, ooh-woah, ooh-woah,")
prechorustwo.append("ooh-woah, ooh")
prechorustwo.append("Ra-ta-ta-ta, 울린 심장 (Ra-ta-ta-ta)")
prechorustwo.append("But I don't want to")


verse1 = []

verse1.append("훌쩍 커버렸어")
verse1.append("함께한 기억처럼")
verse1.append("널 보는 내 마음은")
verse1.append("어느새 여름 지나 가을")
verse1.append("기다렸지 all this time")
verse1.append("Do you want somebody?")
verse1.append("Like I want somebody?")
verse1.append("날 보고 웃었지만")
verse1.append("Do you think about me now, yeah?")
verse1.append("All the time, yeah, all the time")

verse2 = []

verse2.append("Not just anybody")
verse2.append("너를 상상했지")
verse2.append("항상 닿아있던")
verse2.append("처음 느낌 그대로 난")
verse2.append("기다렸지 all this time")

singers = []
singers.append("[Intro: Hyein]")
singers.append("[Outro: Hyein]")
singers.append("[Chorus: Hanni]")
singers.append("[Chorus: Haerin, Minji]")
singers.append("[Chorus: Hanni, Minji]")
singers.append("[Verse 2: Danielle]")
singers.append("[Pre-Chorus: Hyein, Haerin]")
singers.append("[Pre-Chorus: Hyein, Hanni]")
singers.append("[Verse 1: Haerin, Danielle]")



##############################

print("DITTO, NEWJEANS")
print("")

print(singers[0])
for line in hook:
    print(line)

print("")
print(singers[2])
for line in chorus[:4]:
    print(line)

print("")
print(singers[-1])
for line in verse1:
    print(line)

print("")
print(singers[-2])
for line in prechorus:
    print(line)

print("")
print(singers[3])
for line in chorus:
    print(line)

#verse 2
print("")
print(singers[-4])
for line in verse2:
    print(line)

print("")
print(singers[-3])
for line in prechorustwo:
    print(line)

print("")
print(singers[4])
for line in chorus[:6]:
    print(line)
for line in choruspart2:
    print(line)

print("")
print(singers[1])
for line in hook:
    print(line)