from src.jobs import read


def get_unique_job_types(path):
    read_job = read(path)
    conjunto_job = set()
    for job in read_job:
        if job["job_type"] != "":
            conjunto_job.add(job["job_type"])
    return conjunto_job


def filter_by_job_type(jobs, job_type):
    type_job = [job for job in jobs if job_type == job["job_type"]]
    return type_job


def get_unique_industries(path):
    read_job = read(path)
    conjunto_job = set()
    for job in read_job:
        if job["industry"] != "":
            conjunto_job.add(job["industry"])
    return


def filter_by_industry(jobs, industry):
    industry_job = [job for job in jobs if industry == job["industry"]]
    return industry_job


def get_max_salary(path):
    read_job = read(path)
    salary_job = [
        int(job["max_salary"])
        for job in read_job
        if job["max_salary"].isnumeric()
    ]
    return max(salary_job)


def get_min_salary(path):
    read_job = read(path)
    salary_job = [
        int(job["min_salary"])
        for job in read_job
        if job["min_salary"].isnumeric()
    ]
    return min(salary_job)


def matches_salary_range(job, salary):
    for jobs in job:
        if "min_salary" and "max_salary" not in job or type(job[jobs]) != int:
            raise ValueError
        if job["min_salary"] > job["max_salary"] or type(salary) != int:
            raise ValueError
        if job["min_salary"] <= salary <= job["max_salary"]:
            return True
        else:
            return False


def filter_by_salary_range(jobs, salary):
    filter_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_salary.append(job)
        except ValueError:
            continue
    return filter_salary
