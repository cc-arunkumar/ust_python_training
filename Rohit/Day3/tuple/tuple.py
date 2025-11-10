changeable = (1, 2, 3, 4, 5, 6)
ans = list(changeable)
for x in range(len(ans)):
    ans[x] = ans[x]*3


finalAns = tuple(ans)
print(finalAns)

# for x in range(len(ans)):
    # if changeable[x]==3 :
    #     for y in range(len(ans)):
    #         if changeable[y]==4:
    #             print("both numbers are present")
    #             print(True)
if 3 in changeable and 4 in changeable:
    print(True)
