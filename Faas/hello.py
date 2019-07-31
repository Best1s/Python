def main_handler(event,context):
  print('vallue1=' + event['key1'])
  print('vallue1=' + event['key2'])
  return event['key1']
