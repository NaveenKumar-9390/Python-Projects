class Job:
    def __init__(self, id, cpu, mem):
        self.id = id
        self.cpu = cpu
        self.mem = mem
        self.node = None

    def __str__(self):
        return f"Job {self.id}: CPU={self.cpu}, Memory={self.mem}, Node={self.node}"


class Node:
    def __init__(self, id, cpu, mem):
        self.id = id
        self.total_cpu = cpu
        self.total_mem = mem
        self.available_cpu = cpu
        self.available_mem = mem
        self.jobs = []

    def can_fit(self, job):
        return (self.available_cpu >= job.cpu and
                self.available_mem >= job.mem)

    def assign(self, job):
        if self.can_fit(job):
            self.jobs.append(job)
            self.available_cpu -= job.cpu
            self.available_mem -= job.mem
            job.node = self.id
            return True
        return False

    def remove(self, job):
        if job in self.jobs:
            self.jobs.remove(job)
            self.available_cpu += job.cpu
            self.available_mem += job.mem
            job.node = None
            return True
        return False

    def __str__(self):
        jobs_str = ', '.join([str(job) for job in self.jobs])
        return f"Node {self.id}: CPU={self.available_cpu}/{self.total_cpu}, Memory={self.available_mem}/{self.total_mem}, Jobs={jobs_str}"


class Scheduler:
    def __init__(self):
        self.nodes = []
        self.pending_jobs = []

    def add_node(self, node):
        self.nodes.append(node)

    def schedule(self, job):
        # First Fit strategy
        for node in self.nodes:
            if node.can_fit(job):
                node.assign(job)
                print(f"Job {job.id} scheduled on Node {node.id}")
                return True
        self.pending_jobs.append(job)
        print(f"Job {job.id} pending - no available resources")
        return False

    def best_fit(self, job):
        best_node = None
        min_waste = float('inf')
        for node in self.nodes:
            if node.can_fit(job):
                waste = (node.available_cpu - job.cpu) + (node.available_mem - job.mem)
                if waste < min_waste:
                    min_waste = waste
                    best_node = node
        if best_node:
            best_node.assign(job)
            print(f"Job {job.id} scheduled on Node {best_node.id} (best fit)")
            return True
        self.pending_jobs.append(job)
        print(f"Job {job.id} pending - no available resources")
        return False

    def display_status(self):
        print("\nCluster Status:")
        for node in self.nodes:
            print(f"\n{node}")
        if self.pending_jobs:
            print(f"\nPending Jobs: {[job.id for job in self.pending_jobs]}")


# Test the Kubernetes-like Task Scheduler
print("Kubernetes-like Task Scheduler Simulator")
print("="*50)

scheduler = Scheduler()

print("\nAdding nodes to cluster:")
node1 = Node("node-1", cpu=10, mem=16)
print(f"Added Node {node1.id}: {node1}")
scheduler.add_node(node1)

node2 = Node("node-2", cpu=8, mem=12)
print(f"Added Node {node2.id}: {node2}")
scheduler.add_node(node2)

node3 = Node("node-3", cpu=12, mem=20)
print(f"Added Node {node3.id}: {node3}")
scheduler.add_node(node3)

print("\n" + "="*50)
print("\nScheduling jobs (First Fit):")

job1 = Job("job-1", cpu=3, mem=4)
print(f"\nJob {job1.id}: {job1}")
scheduler.schedule(job1)

job2 = Job("job-2", cpu=5, mem=8)
print(f"\nJob {job2.id}: {job2}")
scheduler.schedule(job2)

job3 = Job("job-3", cpu=2, mem=3)
print(f"\nJob {job3.id}: {job3}")
scheduler.schedule(job3)

scheduler.display_status()

print("\n" + "="*50)
print("\nScheduling more jobs:")

job4 = Job("job-4", cpu=6, mem=10)
print(f"\nJob {job4.id}: {job4}")
scheduler.schedule(job4)

job5 = Job("job-5", cpu=4, mem=6)
print(f"\nJob {job5.id}: {job5}")
scheduler.schedule(job5)

scheduler.display_status()