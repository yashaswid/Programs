def secondLargest()
    li=[-1,-2,-4]
    pre=-100
    next=-100
    for i in range(li)
        if li[i]>next:
            next=li[i]
        elif