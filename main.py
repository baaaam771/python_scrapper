from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_pages = extract_indeed_pages()

extract_indeed_jobs(last_indeed_pages)

print(indeed_jobs)

# print(max_indeed_pages)
