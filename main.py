# python3

def parallel_processing(n_threads, m_jobs, job_times):
    output = []
    time_stamp = [0] * n_threads

    for i in range(m_jobs):
        next_thread = 0
        for j in range(1, n_threads):
            if time_stamp[j] < time_stamp[next_thread]:
                next_thread = j
            elif time_stamp[j] == time_stamp[next_thread] and j < next_thread:
                next_thread = j

        output.append((next_thread, time_stamp[next_thread]))
        time_stamp[next_thread] += job_times[i]



    return output




def main():
    n_threads, m_jobs = map(int, input().split())
    job_times = list(map(int, input().split()))

    result = parallel_processing(n_threads, m_jobs, job_times)

    for thread, start_time in result:
        print(thread, start_time)




if __name__ == "__main__":
    main()
