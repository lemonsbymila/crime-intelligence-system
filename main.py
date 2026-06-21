print("===================================")
print("   CRIME INTELLIGENCE REPORT")
print("===================================")

case_id = input("Case ID: ")
analyst = input("Analyst Name: ")
location = input("Incident Location: ")
incident = input("Incident Type: ")
risk_level = input("Risk Level (Low / Medium / High): ")

print("\n===================================")
print("        FINAL REPORT")
print("===================================")

print("Case ID:", case_id)
print("Analyst:", analyst)
print("Location:", location)
print("Incident Type:", incident)
print("Risk Level:", risk_level)
file = open("case_report.txt", "a")

file.write("\n============================\n")
file.write("CRIME INTELLIGENCE REPORT\n")
file.write("============================\n")

file.write("Case ID: " + case_id + "\n")
file.write("Analyst: " + analyst + "\n")
file.write("Location: " + location + "\n")
file.write("Incident Type: " + incident + "\n")
file.write("Risk Level: " + risk_level + "\n")
file.write("============================\n")

file.close()
