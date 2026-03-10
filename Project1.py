import matplotlib.pyplot as plt



days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
study_hours = [2,3,4,3,5,6,4]
marks = [60,65,70,68,75,80,72]



plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.plot(days, study_hours, marker = "o", color = "Blue")
plt.title("Daily Study Hours")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.grid(True)


plt.subplot(2,2,2)
plt.bar(days, marks, color = "green")
plt.title("Marks Scored During Week")
plt.xlabel("Days")
plt.ylabel("Marks")



plt.subplot(2,2,3)
plt.scatter(study_hours, marks , color = "red")
plt.title("Study Hours Vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)



plt.subplot(2,2,4)
plt.hist(study_hours, bins = 5, color = "purple", edgecolor = "black")
plt.title("Study Hours Distribution")
plt.xlabel("Hours")
plt.ylabel("Frequency")



plt.suptitle("Student Study Performance Analysis", fontsize = 16)
plt.tight_layout()
plt.savefig("Study_analysis_project.png")
plt.show()