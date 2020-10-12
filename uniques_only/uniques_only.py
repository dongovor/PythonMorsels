def uniques_only(in_iter):
    tmp_set = set()
    for item in in_iter:
        if item not in tmp_set:
            yield item
            tmp_set.add(item)


nums = iter([1, 2, 3])
output = uniques_only(nums)
print(output)