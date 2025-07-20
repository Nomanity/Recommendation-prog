

jobs = set()

class Job:
    
    attribute_names = ('Аналитическое мышление', 'Креативность', 'Технические навыки',
                           'Навыки межличностного общения', 'Менеджмент')
    

    def __init__(self, job, attr):
        if len(attr) != 5:
            raise AttributeError('Должно быть ровно 5 аргументов')
        self.job = job
        self.analytical = attr[0]
        self.creative = attr[1]
        self.technical = attr[2]
        self.interpersonal = attr[3]
        self.management = attr[4]
        self.attributes = (self.analytical, self.creative, self.technical, self.interpersonal, self.management)
        Job.add_to_jobs_set(self)
    

    def __str__(self):
        return self.job


    def add_to_jobs_set(self):
        jobs.add(self)


    def print_attributes(self):
        for item in zip(Job.attribute_names, self.attributes):
            print (item[0], item[1], sep=': ')




it_specialist = Job('IT-специалист', (10, 7, 10, 5, 3))
engineer = Job('Инженер', (8, 6, 10, 3, 4))
psychologist = Job('Психолог', (9, 8, 7, 10, 7))
remote_tutor = Job('Онлайн-учитель', (5, 7, 7, 9, 7))
physician = Job('Врач', (9, 4, 10, 9, 9))
worker = Job('Рабочий', (3, 3, 8, 2, 1))
marketer = Job('Маркетолог', (10, 7, 3, 6, 9))
baker = Job('Пекарь', (5, 6, 8, 3, 2))
designer = Job('Дизайнер', (5, 10, 8, 10, 5))


jobs_gen = (i for i in jobs)

def job_scores_gen():
    for job in jobs:
        yield (job.job, job.attributes)

scores_gen = job_scores_gen()