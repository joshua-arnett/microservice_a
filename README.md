# microservice_a

To request data from this microservice, write 1-2 dates and an NHL team code in the form "MM/DD/YYYY CODE" or "MM/DD/YYYY MM/DD/YYYY CODE" to a file named "user_input.txt". The microservice will then automatically receive this data and write all the available games in the date range in an output file named "output.txt".

Example data request:
with open("user_input", "w") as f:
  f.write("10/14/2024 10/20/2024 DET")

Example data receiving:
with open("output.txt", "r") as f:
  games = f.read()

UML sequence diagram:

<img width="826" alt="image" src="https://github.com/user-attachments/assets/27ee373c-a8cc-4900-be7e-3d0c12a506f3">
