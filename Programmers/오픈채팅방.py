def solution(record):
    answer = []
    names = dict()
    recs = [reco.split() for reco in record]
    for rec in recs:
        if rec[0] == 'Enter' or rec[0] == 'Change':
            names[rec[1]] = rec[2]
    for rec in recs:
        if rec[0] == 'Enter':
            answer.append(names[rec[1]]+ "님이 들어왔습니다.")
        elif rec[0] == 'Leave':
            answer.append(names[rec[1]]+ "님이 나갔습니다.")
    
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))