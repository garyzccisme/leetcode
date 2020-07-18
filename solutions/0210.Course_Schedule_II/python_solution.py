class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # 0: unlearned, 1: learning, 2: learned
        self.course_status = [0] * numCourses

        self.adv_dict = collections.defaultdict(list)
        for adv, base in prerequisites:
            self.adv_dict[base].append(adv)

        self.schedule = []
        self.is_cycle = False
        for course in range(numCourses):
            self.search(course)
            if self.is_cycle: return []
        return self.schedule[::-1]

    def search(self, course):

        if self.is_cycle or self.course_status[course] == 2:
            return
        if self.course_status[course] == 1:
            self.is_cycle = True
            return

        self.course_status[course] = 1
        for adv in self.adv_dict[course]:
            self.search(adv)
        self.schedule.append(course)
        self.course_status[course] = 2
