import webbrowser, time

total_breaks = 3
break_count = 0

print("This program started on ", time.ctime())
for i in range(total_breaks):
  time.sleep(5)
  webbrowser.open("https://www.youtube.com/watch?v=W9P_qUnMaFg&list=RDW9P_qUnMaFg&start_radio=1")
  break_count += 1
  print("That is your break number: ", break_count)