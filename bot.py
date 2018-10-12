import yaml
import time

from twython import Twython, TwythonError

config = yaml.safe_load(open("config.yml"))
twitter = Twython(config['APP_KEY'],
                  config['APP_SECRET'],
                  config['OAUTH_TOKEN'],
                  config['OAUTH_TOKEN_SECRET'])

try:
  with open('liners.txt', 'r+') as tweetfile:
    buff = tweetfile.readlines()

  for line in buff[:]:
    line = line.strip(r'\n')

    if len(line) <= 140 and len(line) > 0:
      print('Sending tweet.')

      twitter.update_status(status = line)

      with open('liners.txt', 'w') as tweetfile:
        tweetfile.writelines(buff)

      time.sleep(60)

    else:
      with open ('liners.txt', 'w') as tweetfile:
        buff.remove(line)
        tweetfile.writelines(buff)

      print("Skipped line - char len violation")
      continue

  print('Out of lines')

except TwythonError as e:
  print(e)