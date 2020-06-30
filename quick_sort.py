def quick_sort(sort_list, start_index, end_index):
    # print(sort_list)
    if start_index < end_index:
        basic, i, j = sort_list[start_index], start_index, end_index
        while i < j:
            while i < j and basic <= sort_list[j]:
                j -= 1
            while i < j and basic >= sort_list[i]:
                i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]

        sort_list[i], sort_list[start_index] = sort_list[start_index], sort_list[i]
        quick_sort(sort_list,start_index,i-1)
        quick_sort(sort_list,i+1,end_index)

l = [10,4,9,90,2,5,6,4,80,0]
quick_sort(l, 0, len(l)-1)

def quick_sort2(quick_list):
    if quick_list == []:
        return []
    else:
        first = quick_list[0]
        less = quick_sort2([l for l in quick_list[1:] if l < first])
        more = quick_sort2([m for m in quick_list[1:] if m > first])
        return less + [first] + more

l = [10,4,9,90,2,5,6,4,80,0]
print(quick_sort2(l))