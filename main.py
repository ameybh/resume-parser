from resume_parser import resumeparse

# return object with parsed data
# change path to pdf file relative to main.py
data = resumeparse.read_file("./test/resume.pdf")
# print(data)
print(data.name, data.email)
