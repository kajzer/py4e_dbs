import urllib.request

def read_text():
  fhandle = open("movie_quotes.txt")
  contents = fhandle.read()
  # print(contents)
  fhandle.close()
  check_profanity(contents)

def check_profanity(text_to_check):
  full_url = "http://www.wdylike.appspot.com/?q=" + urllib.parse.quote_plus(text_to_check)
  with urllib.request.urlopen(full_url) as url:
    output = url.read()

  response = output.decode('ascii')
  if "true" in response:
    print("Profanity Alert")
  elif "false" in response:
    print("This document is clean")
  else:
    print("Could not scan the file")

if __name__ == "__main__":
  read_text()