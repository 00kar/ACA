class Solution:
    def findingUsersActiveMinutes(self, logs, k):
        answer = []
        users = {}
        for log in logs:
            if log[0] not in users:
                users[log[0]] = []
        for log in logs:
            if log[1] not in users[log[0]]:
                users[log[0]].append(log[1])
        for key, value in users.items():
        	users.update({key: len(value)})
        for j in range(1,k+1):
        	count = 0
        	for i in users.values():
        	    if j == i:
        	        count += 1
        	answer.append(count)
        return answer

j = Solution()
logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
print(j.findingUsersActiveMinutes(logs, k))