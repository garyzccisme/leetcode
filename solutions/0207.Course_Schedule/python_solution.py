# DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 0: unlearned, 1: learning, 2: learned
        self.course_status = [0] * numCourses

        # Use dict to store all advanced courses
        self.adv_dict = collections.defaultdict(list)
        for adv, base in prerequisites:
            self.adv_dict[base].append(adv)

        for course in range(numCourses):
            if not self.dfs(course): return False
        return True

    def dfs(self, course):
        if self.course_status[course] == 2:
            return True
        if self.course_status[course] == 1:
            return False

        # Start to learn this course
        self.course_status[course] = 1
        for adv in self.adv_dict[course]:
            if not self.dfs(adv): return False

        # Mark the course as learned
        self.course_status[course] = 2
        return True

# BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        base_dict = collections.defaultdict(set) # Store base courses for advanced course
        adv_dict = collections.defaultdict(set) # Store advanced courses for base course
        for adv, base in prerequisites:
            base_dict[adv].add(base)
            adv_dict[base].add(adv)

        # Start to learn basest courses
        schedule = collections.deque(
            [course for course in range(numCourses) if course not in base_dict]
        )

        learn_count = 0
        while schedule:
            course = schedule.popleft()
            learn_count += 1
            for adv in adv_dict[course]:
                base_dict[adv].remove(course)
                if not base_dict[adv]:
                    schedule.append(adv)

        # If learned course number = total number, then it's valid
        return learn_count == numCourses