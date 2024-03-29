from collections import Counter

def solution(id_list, report, k):
    report = list(set(report))
    
    report_tuples = []
    
    for item in report:
        split_item = item.split(" ")
        report_tuple = (split_item[0], split_item[1])
        report_tuples.append(report_tuple)
    
    values = []
    for tuple_item in report_tuples:
        value = tuple_item[1]
        values.append(value)
    
    reported_count = Counter(values)
    
    keys_to_count = []
    for key, value in reported_count.items():
        if value >= k:
            keys_to_count.append(key)

    reported_by_users = {id: 0 for id in id_list}
    for _, reported in report_tuples:
        if reported in keys_to_count:
            reported_by_users[_] += 1

    answer = list(reported_by_users.values())
    
    return answer
