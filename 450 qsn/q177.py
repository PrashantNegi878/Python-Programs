def diagonal(root):
    queue=[]
    final=[]
    queue.append(root)
    while len(queue)!=0:
        final.append(queue[0])
        # if queue[0].left:
        #     queue.append(queue[0].left)
        while queue[0].right:
            final.append(queue[0].right)
            if queue[0].left:
                queue.append(queue[0].left)
            queue[0]=queue[0].right
        if queue[0].left:
                queue.append(queue[0].left)
        queue.pop(0)
    for i in range (len(final)):
        final[i]=final[i].data
    return final